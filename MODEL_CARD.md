# Model Card | بطاقة النموذج

## Purpose

This is a foundational portfolio model for learning reproducible time-series preparation and out-of-sample comparison. It forecasts reported monthly oil volume for one UKCS field using only time and historical oil volume.

## Models compared

1. **Last-value baseline:** every test month receives the final training observation.
2. **Seasonal-naive baseline:** every test month receives the observation from the corresponding month one year earlier.
3. **Linear trend:** ordinary least-squares regression using a sequential monthly time index.

## Validation design

- Training: January 2021–December 2024, 48 observations
- Test: January 2025–December 2025, 12 observations
- The rows are never shuffled.
- The test period is not used to fit the evaluation models.
- Primary ranking metric: mean absolute error (MAE)

## Result

The last-value baseline ranked first with MAE **41,112.50 m³**, RMSE **55,043.95 m³**, and MAPE **21.28%**. The linear trend did not beat the simple baseline. This negative finding is retained because it is the honest validation result.

## Appropriate use

- Demonstrating Python, pandas, scikit-learn, data validation, chronological testing, and reproducibility
- Establishing a benchmark for more advanced models
- Producing a transparent baseline scenario

## Inappropriate use and limitations

- Not for investment, reserves, production planning, safety, or operational decisions
- Not a decline-curve analysis or reservoir-engineering model
- No maintenance, shutdown, well, pressure, weather, price, or intervention variables are included
- Only 60 monthly observations and one field are modelled
- MAPE can be unstable near zero, although this selected series has no zero observations
- A forecast is not a promise; the 2026 output is a baseline scenario with material uncertainty

## ملخص عربي

يقارن المشروع ثلاثة نماذج أولية باستخدام فصل زمني صحيح: التدريب على 2021–2024 والاختبار على 2025. حقق نموذج «آخر قيمة» أفضل نتيجة، بينما لم يتفوق الانحدار الخطي عليه. احتفظنا بهذه النتيجة لأنها تقييم صادق. النموذج تعليمي ولا يصلح لاتخاذ قرارات تشغيلية أو استثمارية.

