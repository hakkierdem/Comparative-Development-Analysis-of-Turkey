import pandas as pd

df = pd.read_excel("all_countries_normalization.xlsx")

print(df.columns)

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
years = range(2005,2025)

filtered_dfs = []

for country in countries:
    for year in years:
        mask = (df["Country"] == country) & (df["Year"] == year)
        filtered = df[mask]
        filtered_dfs.append(filtered)

filtered_df = pd.concat(filtered_dfs,ignore_index=True)

filtered_df["scientific_score"] = (
    0.4 * filtered_df["Citations per document"] +
    0.3 * filtered_df["H index"] +
    0.2 * filtered_df["Citable documents"] -
    0.1 * (filtered_df["Self-citations"] / filtered_df["Citations"])
)
print(filtered_df[["Citations per document", "H index", "Citable documents", "Self-citations"]].describe())

filtered_df.to_excel("general_score.xlsx",index = False)
