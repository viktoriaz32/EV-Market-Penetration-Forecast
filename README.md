# EV Market Penetration Forecast and Analysis

## Project Overview

This project simulates an electric vehicle (EV) adoption analysis for a hypothetical automotive market between 2021–2024, with a forecast extending to 2028.
It was designed to demonstrate advanced Excel analytics, forecasting, and dashboard design.

The analysis models how price, marketing spend, rebates, and charging infrastructure influence EV adoption over time.
It includes full time-series forecasting, scenario testing, and KPI reporting built natively in Excel.

Tools: Python, Excel

Note: All data in this project is simulated for demonstration purposes. No confidential or proprietary automotive data is used.

## Objectives

- Analyze historical EV adoption data (2021–2024)
- Identify market drivers (price, incentives, chargers, marketing)
- Forecast adoption trends for 2025–2028 using Excel’s ETS algorithm
- Simulate optimistic / pessimistic market scenarios
- Visualize results in a professional KPI dashboard

## Feature Description

| Feature                    | Description                                                                     |
| -------------------------- | ------------------------------------------------------------------------------- |
| `ETS Forecasting`       | Uses `FORECAST.ETS` to project EV adoption with 95% confidence intervals        |
| `Scenario Control Sheet` | Allows real-time adjustment of marketing, rebate, and infrastructure impacts    |
| `Correlation Analysis`  | Quantifies the relationships between adoption and market drivers                |
| `Seasonality Index`     | Identifies monthly seasonality patterns across multiple years                   |
| `KPI Dashboard`          | Summarizes performance metrics, YoY trends, and driver insights                 |
| `Visualization`          | Includes scatter plots, seasonality charts, and confidence band forecast graphs |


## Data Structure

Workbook: EV_Market_Penetration_Forecast.xlsx

| Sheet                         | Purpose                                                                     |
| ----------------------------- | --------------------------------------------------------------------------- |
| `Historical Data (2021–2024)` | Raw dataset with EV adoption, pricing, rebates, marketing, and charger data |
| `Forecast`                    | ETS forecast with confidence intervals and adjusted scenario outputs        |
| `Controls`                    | Scenario inputs for marketing, rebate, and charger factors                  |
| `Correlation`                 | Statistical relationship matrix between key variables                       |
| `Seasonality`                 | Month-level index to visualize demand fluctuations                          |
| `Dashboard`                   | Executive summary with KPIs, charts, and insights                           |

## Analytical Methods

1. Forecasting
Applied FORECAST.ETS and FORECAST.ETS.CONFINT for trend + seasonality prediction.
Confidence interval bands visualize upper/lower expected adoption ranges.

2. Correlation Analysis
Used CORREL() across historical variables to identify positive and negative drivers:

Price → negative correlation

Marketing Spend → positive correlation

Charger Density → strong positive correlation

3. Seasonality Index
Calculated average adoption per month relative to the overall mean to highlight cyclical patterns (e.g., year-end demand peaks).

4. Scenario Modeling
Composite uplift formula:
=1 + Marketing_Uplift + Rebate_Uplift + Charger_Uplift
