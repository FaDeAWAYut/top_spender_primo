import pandas as pd

df = pd.read_csv("mock_data_10mil.csv")

df["month"] = pd.to_datetime(df["transaction_datetime"]).dt.month

spending = df.groupby(["month", "customer_no"])["amount"].sum().reset_index(name="amount spent in this month")

spending["rank_this_month"] = spending.groupby("month")["amount spent in this month"].rank(method="dense", ascending=False)

spending = spending.sort_values(by=["month","rank_this_month"], ascending=[True,True])

top_spenders = spending[spending["rank_this_month"] < 11]

top_spenders.to_csv("top_10_spenders.csv", index=False)