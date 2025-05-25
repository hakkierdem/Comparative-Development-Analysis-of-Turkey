import pandas as pd

df1 = pd.read_excel("scimagojr country rank 2005.xlsx")
df2 = pd.read_excel("scimagojr country rank 2006.xlsx")
df3 = pd.read_excel("scimagojr country rank 2007.xlsx")
df4 = pd.read_excel("scimagojr country rank 2008.xlsx")
df5 = pd.read_excel("scimagojr country rank 2009.xlsx")
df6 = pd.read_excel("scimagojr country rank 2010.xlsx")
df7 = pd.read_excel("scimagojr country rank 2011.xlsx")
df8 = pd.read_excel("scimagojr country rank 2012.xlsx")
df9 = pd.read_excel("scimagojr country rank 2013.xlsx")
df10 = pd.read_excel("scimagojr country rank 2014.xlsx")
df11 = pd.read_excel("scimagojr country rank 2015.xlsx")
df12 = pd.read_excel("scimagojr country rank 2016.xlsx")
df13 = pd.read_excel("scimagojr country rank 2017.xlsx")
df14 = pd.read_excel("scimagojr country rank 2018.xlsx")
df15 = pd.read_excel("scimagojr country rank 2019.xlsx")
df16 = pd.read_excel("scimagojr country rank 2020.xlsx")
df17 = pd.read_excel("scimagojr country rank 2021.xlsx")
df18 = pd.read_excel("scimagojr country rank 2022.xlsx")
df19 = pd.read_excel("scimagojr country rank 2023.xlsx")
df20 = pd.read_excel("scimagojr country rank 2024.xlsx")

years = range(2005,2025)
df_list = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20]

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"] 

filtered_dfs = []

for df, year in zip(df_list, years):
    df["Year"] = year
    filtered = df[["Year", "Rank", "Country", "Citations per document","Citations", "H index", "Self-citations", "Citable documents"]]
    filtered_dfs.append(filtered)

filtered_df = pd.concat(filtered_dfs, ignore_index=True)
filtered_df.to_excel("scimagojr_allcountries.xlsx",index = False)
    
    
