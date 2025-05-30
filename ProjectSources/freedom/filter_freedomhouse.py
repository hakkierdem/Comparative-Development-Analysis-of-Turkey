import pandas as pd

df = pd.read_excel("All_data_FIW_2013-2024.xlsx",sheet_name = "FIW13-25")


filtered_df = df[["Country/Territory","Edition","Total"]]
filtered_df.to_excel("freedom_house.xlsx",index = False)
