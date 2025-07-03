# beta-drugs-var
# Beta Drugs 1‑Month Value‑at‑Risk (VaR) Project

## Objective
Estimate 21‑day (≈1 month) 95% VaR for Beta Drugs Ltd. using Monte Carlo simulation.

## Data Source
NSE CSV export.

## Method
1. Compute daily log returns from adjusted close prices  
2. Assume returns ~ Normal(μ, σ²)  
3. Simulate 10 000 future 21‑day paths  
4. VaR₉₅ = 5th percentile of cumulative returns  

## Results  
`1‑Month 95% VaR ≈ −19.04 %`

## How to run
```bash
git clone https://github.com/rahulkr-2107/beta-drugs-var.git
cd beta-drugs-var
pip install -r requirements.txt
python get_data.py
python beta_var.py
