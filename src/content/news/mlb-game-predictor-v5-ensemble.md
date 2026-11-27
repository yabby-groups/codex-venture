---
category: "models"
summaryEn: "MLB Game Predictor V5 combines three inputs, including market-implied probabilities, to predict game outcomes. The project makes predictions available through a dashboard and a REST API."
summaryZh: "MLB Game Predictor V5 结合三路信号预测棒球赛果，其中一路来自市场隐含概率。项目通过仪表板和 REST API 提供预测结果。"
tags: ["mlb", "hugging-face-spaces", "catboost", "ensemble-models"]
titleEn: "MLB Game Predictor V5 adds a three-part ensemble"
titleZh: "MLB Game Predictor V5 用三路集成模型预测赛果"
published: "2026-11-27T08:45:43+08:00"
sources: [{"title": "GaboLarrazabal/mlb-game-predictor", "url": "https://huggingface.co/spaces/GaboLarrazabal/mlb-game-predictor"}]
---
<p lang="zh-CN">GaboLarrazabal 在 Hugging Face 的项目说明中介绍了 MLB Game Predictor V5。这个版本用 CatBoost、基于棒球统计指标的逻辑回归和市场隐含概率共同预测比赛结果。读者可以在 Streamlit 仪表板查看预测，也可以通过 FastAPI 提供的 REST API 获取结果。<a href="https://huggingface.co/spaces/GaboLarrazabal/mlb-game-predictor">项目说明</a></p>

<p lang="en">GaboLarrazabal describes MLB Game Predictor V5 in the project’s Hugging Face Space. The version combines CatBoost, logistic regression based on baseball statistics, and market-implied probabilities to predict game outcomes. Users can view predictions in a Streamlit dashboard or retrieve them through a REST API built with FastAPI. <a href="https://huggingface.co/spaces/GaboLarrazabal/mlb-game-predictor">Project documentation</a></p>

<p lang="zh-CN">作者还描述了每周重训流程，用于比较现用模型与候选模型，并报告了覆盖 2024 至 2026 年的逐月验证。验证结果来自作者自述，项目摘录对评估方法的交代有限。<a href="https://huggingface.co/spaces/GaboLarrazabal/mlb-game-predictor">验证与重训说明</a></p>

<p lang="en">The author also describes a weekly retraining process that compares the current model with challengers and reports month-by-month validation covering 2024 through 2026. The validation is self-reported, and the available excerpt gives limited detail on the evaluation method. <a href="https://huggingface.co/spaces/GaboLarrazabal/mlb-game-predictor">Validation and retraining notes</a></p>
