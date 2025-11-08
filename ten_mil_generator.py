import pandas as pd
import numpy as np

df = pd.read_csv("large_order_data_2024.csv")
df = df.sort_values(by=["order_no", "sku"], ascending=[True, True])

mock = []

for i in range(1,11):
  temp_df = df.copy()
  temp_df["order_no"] = temp_df["order_no"] + str(i)
  temp_df["amount"] = temp_df["amount"] + np.random.randint(1000)
  temp_df["customer_no"] = temp_df["customer_no"] + str(i)
  temp_df["quantity"] = np.random.randint(1,5)
  temp_df["transaction_datetime"] = pd.to_datetime(temp_df["transaction_datetime"]) + pd.to_timedelta(np.random.randint(-10,10), unit="d")
  mock.append(temp_df)

result_df = pd.concat(mock)

result_df.to_csv("mock_data_10mil.csv", index=False)

