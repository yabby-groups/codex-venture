"""Structured editorial blocks permitted from the Responses output."""

STRING = {'type': 'string'}


def object_schema(**fields):
    return dict(type='object', properties=fields, required=list(fields), additionalProperties=False)


def array(items):
    return dict(type='array', items=items)


def enum(*values):
    return dict(type='string', enum=list(values))


PAIR = object_schema(zh=STRING, en=STRING)
BLOCKS = array({'anyOf': [
    object_schema(kind=enum('workflow', 'steps', 'timeline', 'takeaways', 'changes'), title=PAIR, items=array(PAIR)),
    object_schema(kind=enum('facts', 'pros-cons', 'comparison'), title=PAIR, columns=array(PAIR), rows=array(array(PAIR))),
    object_schema(kind=enum('code'), title=PAIR,
                  language=enum('json', 'yaml', 'toml', 'bash', 'shell', 'python', 'javascript', 'docker', 'nginx', 'text'),
                  file=STRING, code=STRING),
    object_schema(kind=enum('notice'), title=PAIR, text=PAIR),
]})


def conforms(value, schema):
    if 'anyOf' in schema:
        return any(conforms(value, option) for option in schema['anyOf'])
    if schema['type'] == 'object':
        fields = schema['properties']
        return type(value) is dict and set(value) == set(fields) and all(
            conforms(value[key], field) for key, field in fields.items()
        )
    if schema['type'] == 'array':
        return type(value) is list and len(value) <= 12 and all(conforms(item, schema['items']) for item in value)
    if schema['type'] in ('boolean', 'integer'):
        return type(value) is {'boolean': bool, 'integer': int}[schema['type']]
    return isinstance(value, str) and len(value) <= schema.get('maxLength', 6000) and value in schema.get('enum', [value])

