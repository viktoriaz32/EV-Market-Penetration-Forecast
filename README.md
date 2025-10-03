# EV-Market-Penetration-Forecast

# Market Penetration Forecasting Simulator — EV Launch (Hungary)

**Predictive marketing analytics** app that forecasts adoption for a new compact EV in Hungary and lets you explore **what‑if** scenarios (rebate, marketing spend, competitor entry, charger rollout). Built with a classic **Bass diffusion model** and shipped as a **Streamlit** dashboard for decision-makers.

> 💡 Portfolio focus: business-first story + solid modeling + a usable tool.

---

## 🚀 Demo (what you’ll see)
- **S‑curve of cumulative adoption** and **monthly adoptions** for 36–48 months.
- **Scenario sliders**: change spend, referral/CRM, price → see the curve shift.
- **Launch events baked into the dataset**: government **rebate** (months 4–12), **heavy launch spend** (months 1–6), **competitor entry** (month 15), steady **charger growth**.
- **KPIs**: peak month, peak sales, time to 50% (T50) penetration.

---

## 🧭 Why this matters
- Entering a new market demands **timing and budget** choices. The simulator shows expected **penetration**, **peak timing**, and sensitivity to levers a marketing leader controls.
- This is **predictive**, not prescriptive: it shows what is likely to happen under your assumptions.

---

## 🧱 Tech
- **Modeling**: Bass diffusion (fit via nonlinear least squares)
- **App**: Streamlit + pandas/numpy/scipy
- **(Optional)**: Backtesting (RMSE/MAPE), uncertainty bands, Prophet/SARIMA baselines

---

## 📦 Quickstart
```bash
# 1) Install
pip install -r requirements.txt

# 2) Run the dashboard
streamlit run src/dashboard/app.py
```

**Default dataset**: If `data/processed/ev_hungary_launch.csv` exists, the app loads it automatically. Otherwise, it falls back to a small synthetic dataset.

Upload your own CSV anytime (see schema below).

---

## 🗂️ Repository structure
```
market-penetration-simulator/
├─ data/processed/ev_hungary_launch.csv   # EV launch dataset (Hungary) — default
├─ src/
│  ├─ models/bass.py                      # Bass fit + forecast
│  ├─ scenario.py                         # What‑if elasticities
│  └─ dashboard/app.py                    # Streamlit app
├─ tests/                                 # Unit tests (sample)
├─ assets/                                # Screenshots/GIFs (add yours)
└─ README.md
```

---

## 📊 Data dictionary (CSV)
Required columns (the app will compute `cum_adopters` if missing):
- `date` — month start (e.g., 2025‑01‑01)
- `new_adopters` — monthly adoptions (units)

Included **context** columns (useful for storytelling and future ML baselines):
- `price` (EUR) — promo periods lower price via rebate
- `spend_digital`, `spend_offline` (EUR) — heavier in months 1–6
- `rebate_eur` — 10% of base price during months 4–12
- `fast_chargers` — steadily increasing infrastructure
- `competitor_flag` — 1 from month 15 onward
- `dealer_count` — network build‑out

> You can upload any file with at least `date,new_adopters`.

---

## 🧪 Modeling overview
### Bass diffusion
We estimate parameters **m, p, q** from cumulative adopters:
- **m** — market size (TAM within targeting)
- **p** — innovation (media/launch push)
- **q** — imitation (word‑of‑mouth/referrals)

The app then forecasts:
- **Cumulative adoption** \(N(t)\), **monthly adoptions** \(n(t)\), and **penetration** \(N(t)/m\).

### Scenarios (what‑if)
Scenario sliders apply elasticities that map business levers → parameters:
- **Spend → p:** `p' = p * (1 + α · ΔSpend%)`
- **Referral/CRM → q:** `q' = q * (1 + β · ΔRef%)`
- **Price → m:** `m' = m * (1 − γ · ΔPrice%)`

Default elasticities are illustrative; tune to your context.

---

## 🗺️ EV‑Hungary scenario (baked into dataset)
- **Bass params (starter):** `m=20,000`, `p=0.028`, `q=0.42`, horizon 48 months.
- **Months 1–6:** heavy launch spend → *higher effective p*.
- **Months 4–12:** government rebate (≈10% price cut) → temporarily higher *m* and slight lift to *p*.
- **Month 15+:** competitor entry → modest dampening (effective p↓, q↓).
- **Chargers:** steady growth → context regressor; currently used for storytelling.

---

## 📈 KPIs & charts
- **Peak month & peak sales**
- **Time to 10/50/80%** penetration
- **Cumulative S‑curve** and **monthly adoptions**

*(Optional advanced)* Add: **rolling backtests** (RMSE/MAPE), **uncertainty bands** (delta method/bootstraps), and **model comparison** (Prophet/SARIMA).

---

## 🧩 Flowchart
```mermaid
flowchart TD
  A[Define objectives & KPIs<br/>(penetration %, time-to-50%, peak month)] --> B{Data source?}
  B -->|Upload CSV| C[Ingest & validate<br/>(schema check, dates, missing)]
  B -->|No data| D[Generate synthetic data<br/>(Bass-based + noise + seasonality)]
  C --> E[EDA & sanity checks<br/>(trends, seasonality)]
  D --> E
  E --> F[Fit Bass model on cumulative<br/>estimate m, p, q]
  F --> G[Baseline forecast<br/>(N(t), n(t), penetration)]
  F --> H[Uncertainty (optional)<br/>parameter covariance / bootstrap]
  G --> I[Backtesting (rolling)<br/>RMSE / MAPE]
  H --> I
  I --> J{Scenario inputs (what‑if)?}
  J -->|Spend| K1[Adjust p ← p * (1 + α·ΔSpend%)]
  J -->|Referral/CRM| K2[Adjust q ← q * (1 + β·ΔRef%)]
  J -->|Price| K3[Adjust m ← m * (1 − γ·ΔPrice%)]
  K1 --> L[Re‑forecast S‑curves]
  K2 --> L
  K3 --> L
  L --> M[KPIs & visuals<br/>(peak month, T50, penetration bands)]
  M --> N[Streamlit dashboard<br/>(sliders, charts, downloads)]
  N --> O[Export results<br/>CSV / PNGs]
  N --> P[README polish & repo badges]
  O --> Q[Deliverable ready]
  P --> Q
```

---

## 🎯 Positioning (for roles)
- **Marketing / Growth Analytics** — scenario analysis, peak timing, T50, spend/price levers
- **Marketing Data Science / Forecasting** — Bass fitting, (optional) backtesting & uncertainty, exogenous signals
- **PMM / GTM / Strategy** — market sizing narrative, competitor timing, exec‑friendly visuals
- **BI / RevOps / Demand Planning** — tracking vs. plan, exportable CSVs
- **Product (Growth PM / Data PM)** — end‑to‑end **data product** that supports decisions

**ATS keywords**: Bass diffusion, market penetration, time‑series forecasting, RMSE/MAPE, scenario analysis, Streamlit, Python (pandas/scipy), TAM/SAM/SOM, pricing elasticity, go‑to‑market analytics.

---

## 🛣️ Roadmap (nice‑to‑have)
- Uncertainty bands (delta method / bootstrap)
- Rolling-origin backtests & metrics table
- Model comparison (Prophet/SARIMA with exogenous regressors)
- Competitor dynamics (multi‑brand generalized Bass)
- Segmented Bass (by region/segment)

---

## 📜 License
MIT
