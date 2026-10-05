# UKCS Oil Production Analysis and Baseline Forecasting

**Level 1 — Foundational Python Data-Science Project**

An end-to-end portfolio project using public North Sea Transition Authority production data to prepare a monthly Schiehallion oil series, evaluate three transparent forecasting approaches on a held-out year, and export reproducible evidence.

> Core finding: on the unseen 2025 test period, the simple last-value baseline outperformed both seasonal-naive forecasting and linear regression. The project reports that result honestly instead of treating model complexity as proof of quality.
## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom  

Built as an independent professional portfolio project to apply my petroleum
and reservoir engineering experience to energy-data problems using Python,
SQL and machine learning. I reviewed the engineering assumptions, analytical
workflow, results and limitations.

© 2026 Khaldoun Shaker. All rights reserved.
## Project question

To what extent can historical monthly UKCS production data be prepared, analysed and used to develop a baseline model for forecasting reported oil production while clearly communicating data limitations, model error and uncertainty?

## Data and validation

- Official context: NSTA Petroleum Production Reporting System (PPRS)
- Local extract: 21,479 rows covering January 2021–December 2025
- Analytical series: 60 consecutive Schiehallion observations
- Reported operator: BP EXPLORATION
- Target: monthly oil production volume in m³
- Quality controls: schema, continuity, duplicate, missing-value, positivity, and operator checks

See [DATA_SOURCE.md](DATA_SOURCE.md) for attribution and scope.

## Evaluation

| Model | MAE (m³) | RMSE (m³) | MAPE | MAE rank |
|---|---:|---:|---:|---:|
| Last value | 41,112.50 | 55,043.95 | 21.28% | 1 |
| Linear trend | 66,384.93 | 70,562.52 | 27.17% | 2 |
| Seasonal naive | 72,404.92 | 81,374.14 | 29.07% | 3 |

Training uses January 2021–December 2024. Testing uses January–December 2025. No row shuffling is used.

![Out-of-sample prediction comparison](outputs/charts/02_test_predictions_comparison.png)

## Repository structure

```text
.
├── data/
│   ├── raw/                         # Reproducible NSTA source extract
│   └── processed/                   # Validated Schiehallion series
├── docs/                            # Methodology and bilingual report
├── models/                          # Saved model and readable parameters
├── outputs/
│   ├── charts/                      # Three portfolio-ready visualisations
│   └── tables/                      # Profile, metrics, predictions, scenarios
├── src/                             # Preparation, modelling, orchestration
├── tests/                           # Automated data and model tests
├── run_project.py                   # One-command workflow
└── requirements.txt
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_project.py
python -m unittest discover -s tests -v
```

Expected headline result: `Best test model by MAE: last_value`.

## Key outputs

- `data/processed/schiehallion_monthly_oil_2021_2025.csv`
- `outputs/tables/model_metrics.csv`
- `outputs/tables/test_predictions_2025.csv`
- `outputs/tables/forecast_scenarios_2026.csv`
- `models/linear_trend_model.joblib`
- `models/model_parameters.json`

## Limitations

This is a transparent educational baseline, not a reservoir-engineering, reserves, investment, safety, or production-planning model. It omits shutdowns, maintenance, well activity, pressure, weather, prices, and interventions. See [MODEL_CARD.md](MODEL_CARD.md).

---

## الملخص العربي

هذا هو **المشروع الثاني — المستوى الأول (التأسيسي)**. يستخدم بيانات إنتاج شهرية حقيقية منشورة من NSTA لتحليل إنتاج النفط في حقل Schiehallion وبناء ثلاثة نماذج أولية ومقارنتها على سنة 2025 التي لم تدخل في التدريب.

النتيجة الأساسية هي أن نموذج «آخر قيمة» كان أدق من الانحدار الخطي والنموذج الموسمي البسيط. احتفظنا بهذه النتيجة لأنها تبين التقييم الصحيح وتمنع المبالغة في قدرات النموذج.

لتشغيل المشروع: ثبّت المكتبات من `requirements.txt` ثم شغّل `python run_project.py`، وبعدها الاختبارات. التفاصيل الثنائية اللغة موجودة في `docs/PROJECT_REPORT_AR_EN.md`.

