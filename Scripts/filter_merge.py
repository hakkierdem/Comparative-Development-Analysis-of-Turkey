import pandas as pd

df05 = pd.read_csv("CPI2005_Results.csv") #country /score /rank
df06 = pd.read_csv("CPI2006_Results.csv") #country /score /rank
df07 = pd.read_csv("CPI2007_Results.csv") #country /score /rank
df08 = pd.read_csv("CPI2008_Results.csv") #country /score /rank
df09 = pd.read_csv("CPI2009_Results.csv") #country /score /rank
df10 = pd.read_csv("CPI2010_Results.csv") #country /score /rank
df11 = pd.read_csv("CPI2011_Results.csv") #country /score /rank
df12 = pd.read_excel("CPI2012_Results.xlsx",sheet_name ="CPI 2012") #Country/Territory /CPI 2012 Score /Country Rank
df13 = pd.read_excel("CPI2013_Results.xlsx") #Country/Territory /CPI 2013 Score /Country Rank
df14 = pd.read_excel("CPI2014_Results.xlsx",sheet_name = "CPI 2014") #Country/Territory /CPI 2014 /Country Rank
df15 = pd.read_excel("CPI2015_Results.xlsx",sheet_name = "CPI 2015") #Country/Territory /CPI 2015 Score /Country Rank
df16 = pd.read_excel("CPI2016_Results.xlsx",sheet_name = "CPI 2015-2016") #Country /CPI2016 /CPI2016 Rank
df17 = pd.read_excel("CPI2017_Results.xlsx",sheet_name = "CPI 2017") #Country /CPI Score 2017 /Rank
df18 = pd.read_excel("CPI2018_Results.xlsx",sheet_name = "CPI2018") #Country /CPI Score 2018 /Rank
df19 = pd.read_excel("CPI2019_Results.xlsx",sheet_name = "CPI2019") #Country /CPI score 2019 /Rank
df20 = pd.read_excel("CPI2020_Results.xlsx",sheet_name = "CPI 2020") #Country /CPI score 2020 /Rank
df21 = pd.read_excel("CPI2021_Results.xlsx",sheet_name = "CPI 2021") #Country/Territory /CPI score 2021 /Rank
df22 = pd.read_excel("CPI2022_Results.xlsx",sheet_name = "CPI 2022 (final)") #Country/Territory /CPI score 2022 /Rank
df23 = pd.read_excel("CPI2023_Results.xlsx",sheet_name = "CPI 2023") #Country/Territory /CPI score 2023 /Rank
df24 = pd.read_excel("CPI2024_Results.xlsx",sheet_name = "CPI2024") #Country/Territory /CPI 2024 score /Rank

df_list = [df05,df06,df07]

df05["score"] = pd.to_numeric(df05["score"].str.replace(",", "."), errors="coerce")


countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","Korea (South)","Malaysia"]
countries2 = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","Korea, South","Malaysia"]
countries3 = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]

result = []

year = 2005

for df in df_list:
    for country in countries3: 
        filtered = (df["country"] == country)
        
        result.append({
        "Country" : country,
        "Score" : (df[filtered]["score"].values[0]) * 10,
        "Rank": df[filtered]["rank"].values[0],
        "Year" : year})
    
    year += 1

for country in countries2:
    filtered = (df08["country"] == country)
    
    result.append({
    "Country" : country,
    "Score" : df08[filtered]["score"].values[0] * 10,
    "Rank" : df08[filtered]["rank"].values[0],
    "Year" : 2008})

for country in countries3:
    filtered = (df09["country"] == country)
    
    result.append({
    "Country" : country,
    "Score" : df09[filtered]["score"].values[0] * 10,
    "Rank" : df09[filtered]["rank"].values[0],
    "Year" : 2009})

for country in countries:
    filtered = (df10["country"] == country)
    
    result.append({
    "Country" : country,
    "Score" : df10[filtered]["score"].values[0] * 10,
    "Rank" : df10[filtered]["rank"].values[0],
    "Year" : 2010})

for country in countries:
    filtered = (df11["country"] == country)
    
    result.append({
    "Country" : country,
    "Score" : (df11[filtered]["score"].values[0]) * 10,
    "Rank" : df11[filtered]["rank"].values[0],
    "Year" : 2011})

for country in countries:
    filtered = (df12["Country / Territory"] == country)
    

    result.append({
    "Country" : country,
    "Score" : df12[filtered]["CPI 2012 Score"].values[0],
    "Rank" : df12[filtered]["Country Rank"].values[0],
    "Year" : 2012})


for country in countries:
    filtered = (df13["Country / Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df13[filtered]["CPI 2013 Score"].values[0],
    "Rank" : df13[filtered]["Country Rank"].values[0],
    "Year" : 2013})
    
for country in countries:
    filtered = (df14["Country/Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df14[filtered]["CPI 2014"].values[0],
    "Rank" : df14[filtered]["Country Rank"].values[0],
    "Year" : 2014})
    
for country in countries:
    filtered = (df15["Country/Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df15[filtered]["CPI 2015 Score"].values[0],
    "Rank" : df15[filtered]["Country Rank"].values[0],
    "Year" : 2015})

for country in countries:
    filtered = (df16["Country"] == country)
    result.append({
    "Country" : country,
    "Score" : df16[filtered]["CPI2016"].values[0],
    "Rank" : df16[filtered]["CPI 2016 Rank"].values[0],
    "Year" : 2016})



for country in countries2:
    filtered = (df17["Country"] == country)
    result.append({
    "Country" : country,
    "Score" : df17[filtered]["CPI Score 2017"].values[0],
    "Rank" : df17[filtered]["Rank "].values[0],
    "Year" : 2017})

for country in countries2:
    filtered = (df18["Country"] == country)
    result.append({
    "Country" : country,
    "Score" : df18[filtered]["CPI Score 2018"].values[0],
    "Rank" : df18[filtered]["Rank "].values[0],
    "Year" : 2018})

for country in countries2:
    filtered = (df19["Country"] == country)
    result.append({
    "Country" : country,
    "Score" : df19[filtered]["CPI score 2019"].values[0],
    "Rank" : df19[filtered]["Rank"].values[0],
    "Year" : 2019})

for country in countries2:
    filtered = (df20["Country"] == country)
    result.append({
    "Country" : country,
    "Score" : df20[filtered]["CPI score 2020"].values[0],
    "Rank" : df20[filtered]["Rank"].values[0],
    "Year" : 2020})

for country in countries2:
    filtered = (df21["Country / Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df21[filtered]["CPI score 2021"].values[0],
    "Rank" : df21[filtered]["Rank"].values[0],
    "Year" : 2021})


for country in countries2:
    filtered = (df22["Country / Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df22[filtered]["CPI score 2022"].values[0],
    "Rank" : df22[filtered]["Rank"].values[0],
    "Year" : 2022})

for country in countries2:
    filtered = (df23["Country / Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df23[filtered]["CPI score 2023"].values[0],
    "Rank" : df23[filtered]["Rank"].values[0],
    "Year" : 2023})

for country in countries2:
    filtered = (df24["Country / Territory"] == country)
    result.append({
    "Country" : country,
    "Score" : df24[filtered]["CPI 2024 score"].values[0],
    "Rank" : df24[filtered]["Rank"].values[0],
    "Year" : 2024})


results_df = pd.DataFrame(result)

results_df["Country"] = results_df["Country"].replace({
        "Korea (South)": "South Korea",
        "Korea, South": "South Korea"
    })

results_df.to_excel("cpi_general_scores.xlsx",index = False)
    
        
