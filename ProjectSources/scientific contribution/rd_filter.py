import pandas as pd

df = pd.read_csv("research & development expenditure.csv")

df["Country Name"] = df["Country Name"].replace({"Turkiye" : "Turkey","Korea, Rep." : "South Korea"})


df_long = df.melt(
    id_vars=["Country Name"],  
    var_name="Year",
    value_name="R&D_Expenditure"
)



df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")


df_filtered = df_long[df_long["Year"] >= 2005]


countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
df_result = df_filtered[df_filtered["Country Name"].isin(countries)]



df_result.to_excel("filtered_rd_scores.xlsx", index=False)
