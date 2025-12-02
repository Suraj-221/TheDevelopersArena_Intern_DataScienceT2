# Mini Data Analysis, Finance manager

## Overview
This project provides a simple, clean, and fully working Python template for basic data analysis. It demonstrates core concepts such as data generation, cleaning, aggregation, statistical testing, and plotting—all in one lightweight script.

The goal is to help beginners understand the end-to-end workflow of a typical data analysis task without unnecessary complexity.

## Features
### 1. Synthetic Data Generation
The script generates three small datasets:
- **Sales data** – daily units sold, revenue, and regions.
- **Customer data** – age, monthly spend, and churn status.
- **Sensor data** – hourly sensor readings for multiple sensors.

### 2. Data Cleaning
Includes simple but essential cleaning steps:
- Removing invalid values  
- Handling missing data  
- Correcting types  

### 3. Data Analysis
Performs multiple analytical operations:
- Groupby summarization  
- Pivot table creation  
- 7-day rolling averages  
- Sensor performance summary  
- Churn-based customer analysis  

### 4. Statistical Testing
Runs a **two-sample t-test** to compare monthly spending between churned and retained customers.

### 5. Visualization
Generates and displays:
- A **daily revenue plot**

The graph is also saved as:
```
daily_revenue.png
```

### 6. Console Outputs
The script prints:
- Recent daily revenue  
- Customer spend analysis  
- Top-performing sensors  
- Hypothesis test results  

---

## Requirements
Install the required dependencies:

```bash
pip install pandas numpy matplotlib scipy
```

---

## How to Run
1. Save the main script as:
```
mini_data_analysis.py
```

2. Run it using:
```bash
python mini_data_analysis.py
```

3. Output includes:
- A displayed plot  
- A saved image (`daily_revenue.png`)  
- Clean summaries printed in the terminal  

---

## File Structure
```
mini_data_analysis.py     # main executable script
daily_revenue.png         # plot generated after running the script
README.md                 # documentation file
```

---

## Customization

| Task | How to Modify |
|------|---------------|
| Use real datasets | Replace synthetic DataFrames with `pd.read_csv()` |
| Add more plots | Add additional Matplotlib figure blocks |
| Make an interactive dashboard | Convert to Streamlit or Plotly |
| Improve performance | Use Polars or chunked processing |
| Add more statistics | Expand using scipy or statsmodels |

---

## Purpose
This template is designed as a foundational, beginner-friendly tool for:
- Students  
- Portfolio practice  
- College assignments  
- Quick prototyping  
- Learning how real data analysis works

## Author
This README.md documents the mini analysis script created for educational and demonstration purpo
