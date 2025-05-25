import pandas as pd

df = pd.read_excel("filteredmerged_rd_scores.xlsx")


df = df.sort_values(by=["Country Name", "Year"])


df["R&D_Expenditure"] = df.groupby("Country Name")["R&D_Expenditure"].transform(
    lambda group: group.interpolate(method='linear', limit_direction='both')
)

df.to_excel("interpolation_rd_scores.xlsx",index = False)
