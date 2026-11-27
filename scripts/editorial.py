from article_schema import conforms

DIMENSIONS = dict(interest=25, utility=25, originality=15, depth=15, readability=10, shareability=10)
GATES = ('truth', 'evidence', 'duplication', 'rights', 'safety')
DEFAULT_THRESHOLDS = dict(publish=75, featured=85, lead=90)


def obj(**fields):
    return dict(type='object', properties=fields, required=list(fields), additionalProperties=False)


STRING = dict(type='string')
BOOLEAN = dict(type='boolean')
INTEGER = dict(type='integer')
PITCH = obj(pitches=dict(type='array', items=obj(
    id=STRING, reader=STRING, angle=STRING, payoff=STRING, evidence=STRING,
    distinction=STRING, reasonToShare=STRING,
)))
REVIEW = obj(reviews=dict(type='array', items=obj(
    slug=STRING, grounds=STRING, actionable=BOOLEAN,
    scores=obj(**dict.fromkeys(DIMENSIONS, INTEGER)),
    gates=obj(**dict.fromkeys(GATES, BOOLEAN)),
)))


def thresholds(strategy):
    values = {**DEFAULT_THRESHOLDS, **strategy.get('reader_review', {})}
    if (set(values) != set(DEFAULT_THRESHOLDS)
            or any(type(value) is not int for value in values.values())
            or not 0 < values['publish'] <= values['featured'] <= values['lead'] <= 100):
        raise ValueError('Invalid reader review thresholds')
    return values


def decisions(draft, review, strategy):
    if not conforms(review, REVIEW):
        raise ValueError('Invalid reader review')
    articles = draft['articles']
    by_slug = {article['slug']: article for article in articles}
    rows = review['reviews']
    if len(by_slug) != len(articles) or len(rows) != len(articles) or {row['slug'] for row in rows} != by_slug.keys():
        raise ValueError('Reader reviews must cover each draft exactly once')
    limits = thresholds(strategy)
    published = []
    ratings = {}
    for row in rows:
        scores = row['scores']
        if not row['grounds'].strip() or any(not 0 <= scores[key] <= cap for key, cap in DIMENSIONS.items()):
            raise ValueError('Invalid reader review scores or grounds')
        article = by_slug[row['slug']]
        score = sum(scores.values())
        if not all(row['gates'].values()) or not row['actionable'] or score < limits['publish']:
            continue
        published.append(article)
        tier = 'lead' if score >= limits['lead'] else 'featured' if score >= limits['featured'] else 'standard'
        ratings[row['slug']] = dict(score=score, tier=tier)
    return published, ratings
