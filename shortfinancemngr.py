# mini_data_analysis.py
"""
Simple, clean, fully working data-analysis template.
Includes:
- synthetic data
- cleaning
- groupby, pivot, rolling
- t-test
- shows and saves a graph
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(0)

# -------------------------------------------------
# 1) CREATE SMALL SYNTHETIC DATASETS
# -------------------------------------------------

dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
sales = pd.DataFrame({
    'date': np.tile(dates, 2),
    'region': np.repeat(['North', 'South'], len(dates)),
    'product': np.random.choice(['A', 'B'], size=2*len(dates))
})

sales['units'] = np.random.poisson(10, len(sales))
sales['price'] = sales['product'].map({'A': 100, 'B': 70})
sales['revenue'] = sales['units'] * sales['price']

customers = pd.DataFrame({
    'customer_id': range(1,201),
    'age': np.random.randint(18,70,200),
    'monthly_spend': np.round(np.random.gamma(2,30,200), 2),
    'churn': np.random.binomial(1, 0.12, 200)
})

sensors = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='H'),
    'sensor_id': np.random.choice([f's{i}' for i in range(1,21)], 100),
    'reading': np.random.normal(50, 5, 100)
})

# -------------------------------------------------
# 2) CLEANING
# -------------------------------------------------

sales = sales[sales['units'] >= 0]
customers = customers[(customers.age >= 15) & (customers.age <= 100)]
sensors['reading'] = sensors['reading'].fillna(method='ffill')

# -------------------------------------------------
# 3) ANALYSIS
# -------------------------------------------------

# Daily revenue summary
daily = sales.groupby('date', as_index=False).agg(
    total_revenue=('revenue','sum'),
    total_units=('units','sum')
)

# Pivot + rolling
pivot = sales.pivot_table(index='date', columns='region', values='revenue', aggfunc='sum').fillna(0)
rolling7 = pivot.rolling(7).mean().add_suffix('_7davg').reset_index()

# Simple customer spend summary
spend_by_churn = customers.groupby('churn').monthly_spend.agg(['count','mean','std']).reset_index()

# Sensor summary
sensor_summary = sensors.groupby('sensor_id').reading.agg(['count','mean','std']).reset_index().sort_values('mean', ascending=False)

# -------------------------------------------------
# 4) HYPOTHESIS TEST
# -------------------------------------------------

churned = customers.loc[customers.churn == 1, 'monthly_spend']
retained = customers.loc[customers.churn == 0, 'monthly_spend']

tstat, pvalue = stats.ttest_ind(churned, retained, equal_var=False)

# -------------------------------------------------
# 5) PLOT (SHOW + SAVE)
# -------------------------------------------------

plt.figure(figsize=(8,3))
plt.plot(daily['date'], daily['total_revenue'], marker='o')
plt.title('Total Daily Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.tight_layout()

plt.savefig('daily_revenue.png', dpi=120)
plt.show()   # THIS MAKES THE GRAPH APPEAR

# -------------------------------------------------
# 6) OUTPUT RESULTS
# -------------------------------------------------

print("\n=== DAILY REVENUE (LAST 5) ===")
print(daily.tail().to_string(index=False))

print("\n=== CUSTOMER SPEND BY CHURN ===")
print(spend_by_churn.to_string(index=False))

print("\n=== TOP 5 SENSORS ===")
print(sensor_summary.head(5).to_string(index=False))

print("\n=== HYPOTHESIS TEST ===")
print(f"t-statistic: {tstat:.3f}, p-value: {pvalue:.4f}")

print("\nGraph displayed and saved as daily_revenue.png")
