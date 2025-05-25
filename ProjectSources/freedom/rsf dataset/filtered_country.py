import pandas as pd

df05 = pd.read_csv("2005.csv",sep = ";")
df06 = pd.read_csv("2006.csv",sep = ";")
df07 = pd.read_csv("2007.csv",sep = ";")
df08 = pd.read_csv("2008.csv",sep = ";")
df09 = pd.read_csv("2009.csv",sep = ";",on_bad_lines = "skip")
df10 = pd.read_csv("2010.csv",sep = ";",on_bad_lines = "skip")
df12 = pd.read_csv("2012.csv",sep = ";",on_bad_lines = "skip")
df13 = pd.read_csv("2013.csv",sep = ";",on_bad_lines = "skip")
df14 = pd.read_csv("2014.csv",sep = ";",on_bad_lines = "skip")
df15 = pd.read_csv("2015.csv",sep = ";",on_bad_lines = "skip")
df16 = pd.read_csv("2016.csv",sep = ";",on_bad_lines = "skip")
df17 = pd.read_csv("2017.csv",sep = ";",on_bad_lines = "skip")
df18 = pd.read_csv("2018.csv",sep = ";",on_bad_lines = "skip")
df19 = pd.read_csv("2019.csv",sep = ";",on_bad_lines = "skip")
df20 = pd.read_csv("2020.csv",sep = ";",on_bad_lines = "skip")
df21 = pd.read_csv("2021.csv",sep = ";",on_bad_lines = "skip")
df22 = pd.read_csv("2022.csv",sep = ";",on_bad_lines = "skip")
df23 = pd.read_csv("2023.csv",sep = ";",on_bad_lines = "skip")
df24 = pd.read_csv("2024.csv",sep = ";",on_bad_lines = "skip")
df25 = pd.read_csv("2025.csv",sep = ";",encoding = "latin1",on_bad_lines = "skip")


df_list = [df05,df06,df07,df08,df09,df10,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25]


for year, df in zip(range(2022, 2026), [df22, df23, df24]):
    df["Year (N)"] = year
    df.rename(columns = {"Score" : "Score N","Rank" : "Rank N"},inplace = True)
    
df25["Year (N)"] = 2025
df25.rename(columns = {"Score 2025" : "Score N","Rank" : "Rank N"},inplace = True)


for df in df_list:

    print(df.columns.to_list())

countries = ["TUR","POL","BRA","DEU","JPN","GBR","JOR","CAN","SWE","KOR","MYS"]

filtered_df = pd.DataFrame()


for df in df_list:

    df_data = df[["Year (N)","ISO","Rank N","Score N"]]
    filtered_df = pd.concat((filtered_df,df_data),ignore_index = True)
        

filtered_df.to_csv("filteredmerged_allcountries.csv",index = False)
