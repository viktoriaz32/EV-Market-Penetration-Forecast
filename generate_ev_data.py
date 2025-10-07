# EV Data Generation with Pandas and Numpy

import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Create monthly dates for 2021–2024
dates_hist = pd.date_range("2021-01-01", "2024-12-01", freq="MS")
months_hist = len(dates_hist)
t_hist = np.arange(1, months_hist + 1)

# Seasonality pattern (index for months)
season_factors = [0.92, 0.94, 1.00, 1.05, 1.07, 0.95, 0.85, 0.87, 0.92, 1.08, 1.20, 1.25]
seasonality = np.array([season_factors[(i - 1) % 12] for i in t_hist])

# Simulate adoption & drivers
base_sales = 300 + (t_hist * 12)                           # growth trend
noise = np.random.normal(1.0, 0.08, months_hist)           # monthly noise
sales_hist = (base_sales * seasonality * noise).round().astype(int)

marketing_spend_hist = (np.random.normal(30000, 5000, months_hist) 
                        + t_hist * 200).round(0).astype(int)

price_eur_hist = (40000 - (t_hist * 40) 
                  + np.random.normal(0, 500, months_hist)).round(0).astype(int)

rebate_eur_hist = np.zeros(months_hist, dtype=int)
rebate_eur_hist[(t_hist >= 12) & (t_hist <= 24)] = 2000   # rebate window 2021–2022
rebate_eur_hist[(t_hist >= 36) & (t_hist <= 42)] = 2500   # second rebate window 2024

competitor_flag_hist = np.where(t_hist >= 30, 1, 0).astype(int)
fast_chargers_hist = np.linspace(300, 1800, months_hist).round().astype(int)

# Combine into DataFrame
hist_df = pd.DataFrame({
    "date": dates_hist,
    "new_adopters": sales_hist,
    "price_eur": price_eur_hist,
    "rebate_eur": rebate_eur_hist,
    "marketing_spend_eur": marketing_spend_hist,
    "competitor_flag": competitor_flag_hist,
    "fast_chargers": fast_chargers_hist,
})

hist_df.to_csv("ev_data.csv", index=False)
