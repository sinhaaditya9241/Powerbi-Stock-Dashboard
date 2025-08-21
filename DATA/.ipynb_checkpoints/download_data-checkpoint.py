import yfinance as yf
import os

symbol = input("Enter the stock symbol (e.g., AAPL): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
interval = input("Enter the time interval (e.g., 1d, 1h, 5m): ")

# Ensure the data directory exists
download_dir = "data"
os.makedirs(download_dir, exist_ok=True)

data = yf.download(symbol, start=start_date, end=end_date, interval=interval)

if data is not None and not data.empty:
    file_path = os.path.join(download_dir, f"{symbol}_{interval}_data.csv")
    data.to_csv(file_path)
    print(f"Data for {symbol} from {start_date} to {end_date} ({interval}) has been downloaded and saved to {file_path}")
    print("Download complete.")
else:
    print("No data was downloaded. Please check the symbol, date range, and interval.")



# Example usage:# python download_data.py
# Enter the stock symbol (e.g., AAPL): AAPL
# Enter the start date (YYYY-MM-DD): 2020-01-01
# Enter the end date (YYYY-MM-DD): 2020-12-31
# Enter the time interval (e.g., 1d, 1h, 5m): 1d
# Data for AAPL from 2020-01-01 to 2020-12-31 (1d) has been downloaded and saved to data/AAPL_1d_data.csv
 

# example of symbol:
# NIFTY50 STOCKS:
# RELIANCE
# TCS
# HDFCBANK
# INFY
# ITC
# SBIN
# BHARTIARTL
# ICICIBANK
# KOTAKBANK
# LT
# HINDUNILVR
# AXISBANK
# SUNPHARMA
# ASIANPAINT
# MARUTI
# M&M
# ULTRACEMCO
# TATAMOTORS
# TITAN
# NESTLEIND
# BAJFINANCE
# WIPRO
# POWERGRID
# NTPC
# ONGC
# HCLTECH
# BAJAJFINSV
# TATASTEEL
# GRASIM
# TECHM
# JSWSTEEL
# HDFCLIFE
# ADANIENT
# DIVISLAB
# HINDALCO
# SBILIFE
# CIPLA
# BRITANNIA
# COALINDIA
# UPL
# EICHERMOT
# DRREDDY
# HERO
# INDUSINDBK
# BAJAJAUTO
# APOLLOHOSP
# TATACONSUM
# ADANIPORTS
# BPCL
# SHREECEM

# BANKNIFTY STOCKS:
# HDFCBANK
# ICICIBANK
# KOTAKBANK
# SBIN
# AXISBANK
# INDUSINDBK
# BANDHANBNK
# FEDERALBNK
# PNB
# BANKBARODA
# IDFCFIRSTB
# RBLBANK
# UNIONBANK
# CANBK
# BANKINDIA

# NSE INDICES:
# ^NSEI
# ^NSEBANK
# ^NSEIT
# ^NSEPHARMA
# ^NSEAUTO
# ^NSEFMCG
# ^NSEMETAL
# ^NSEENERGY
# ^NSEINFRA
# ^NSEFIN
# ^NSEPSU
# ^NSEMEDIA
# ^NSECPSE
# ^NSEDEFTY
# ^NSEREALTY
# ^NSESMALLCAP
# ^NSEMIDCAP
# ^NSE500

# BSE INDICES:
# ^BSESN
# ^BANKEX
# ^BSEIT
# ^BSEPHARMA
# ^BSEAUTO
# ^BSEFMCG
# ^BSEMETAL
# ^BSEENERGY
# ^BSEINFRA
# ^BSEFIN
# ^BSEPSU
# ^BSEMEDIA
# ^BSECPSE
# ^BSEDEFTY
# ^BSEREALTY
# ^BSESMALLCAP
# ^BSEMIDCAP
# ^BSE500
