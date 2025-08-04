import pandas as pd

df = pd.read_csv("data/BFS_Share_Price.csv", parse_dates=["Date"], date_format="%Y-%m-%d")


def get_price_stats(start: str, end: str) -> str:
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end)
    sel = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    if sel.empty:
        return "No data found for the selected range."
    
    hi = sel["Close"].max()
    lo = sel["Close"].min()
    avg = sel["Close"].mean()
    return f"From {start} to {end}:\nHigh: ₹{hi:.2f}\nLow: ₹{lo:.2f}\nAverage: ₹{avg:.2f}"
