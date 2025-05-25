import pandas as pd

df = pd.read_excel("scimagojr_allcountries.xlsx")

def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min()) * 100
    
df["Citations per document"]=min_max_normalize(df["Citations per document"])
df["H index"]=min_max_normalize(df["H index"])
df["Citable documents"]=min_max_normalize(df["Citable documents"])
df["Citations"] =min_max_normalize(df["Citations"])
df["Self-citations"]=min_max_normalize(df["Self-citations"])

df.to_excel("all_countries_normalization.xlsx",index = False)




