# 📊 Stock Market Dashboard with Power BI & Python

This project is a fully functional stock market analytics dashboard built using **Power BI**, combined with **Python automation** to fetch stock data from Yahoo Finance via the `yfinance` library. It is designed to showcase financial data storytelling, key technical indicators, and interactive visuals.

---

## 🚀 Features

✅ Visualize historical and real-time stock data  
✅ KPI Cards: Open, Close, Volume, % Change, SMA  
✅ Line chart for price trends  
✅ Volume bar chart  
✅ Date slicers and filters  
✅ Python script to pull live data  
✅ Ready-to-customize Power BI `.pbix` file  
✅ Ideal for resume, LinkedIn, and quant/data finance portfolios  

---

## 🧰 Tools & Technologies

- **Power BI** (Visualization & DAX)
- **Python** (Data fetching with `yfinance`)
- **CSV** (Data storage)
- **DAX** (for KPIs and calculations)

---

## 🧮 Technical Metrics

- **% Change Formula**: `(Close - Open) / Open * 100`
- **Simple Moving Average (SMA)**: 5-day average of closing prices
- **Volume Alerts**: Conditional formatting for high-volume days

---

## 📂 Project Structure

powerbi-stock-dashboard/
├── stock_dashboard.pbix # Power BI Dashboard File
├── data/
│ └── reliance_stock_data.csv # Sample Stock Data (Historical)
├── fetch_data.py # Python script for live data
├── dashboard_preview.png # Screenshot of the dashboard
└── README.md # Project documentation

---

## 🐍 Python Script

```python
import yfinance as yf

symbol = "RELIANCE.NS"
df = yf.download(symbol, start="2024-01-01", end="2025-01-01")
df.to_csv("data/reliance_stock_data.csv")
print("✅ Data saved to CSV.")
