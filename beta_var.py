# file: beta_var.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns

df = pd.read_csv("BETA.csv", parse_dates=['Date'], index_col='Date')
df['Returns'] = df['Price'].pct_change().dropna()

mean_r, std_r = df['Returns'].mean(), df['Returns'].std()
num_sims, num_days = 10000, 21

simulated = []
for _ in range(num_sims):
    daily = np.random.normal(mean_r, std_r, num_days)
    simulated.append(np.prod(1+daily) - 1)

VaR95 = -np.percentile(simulated, 5)
print(f"1‑Month 95% VaR for Beta Drugs: {VaR95:.2%}")

sns.histplot(simulated, bins=100, kde=True)
plt.axvline(-VaR95, color='red', ls='--', label=f'95% VaR: {-VaR95:.2%}')
plt.title('1‑Month Monte Carlo Return Distribution – Beta Drugs')
plt.xlabel('Simulated Return'); plt.ylabel('Frequency'); plt.legend()
plt.tight_layout(); plt.savefig("beta_var_plot.png"); plt.show()
