import pandas as pd

df = pd.read_excel("2024_wjp_rule_of_law_index_HISTORICAL_DATA_FILE.xlsx",sheet_name="Historical Data")

filtered_df=df[["Country","Year","WJP Rule of Law Index: Overall Score"]]
filtered_df.to_excel("historical_data_only.xlsx", index=False)
