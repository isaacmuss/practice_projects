import yfinance as yf
import pandas as pd
import os

# Download data for XLU from 2010 to today
xlu = yf.download("XLU", start="2010-01-01", interval="1mo")

# Keep only the Adjusted Close price
xlu = xlu[['Close']]

# Calculate monthly returns (%)
xlu['Monthly Return'] = xlu['Close'].pct_change()

# Drop the first NaN row
xlu = xlu.dropna()

# Display the result
print(xlu)

os.chdir(r'C:\Users\isaac\Downloads')
xlu.to_excel('month_xlu.xlsx')