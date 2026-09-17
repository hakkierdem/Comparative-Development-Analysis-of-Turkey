import pandas as pd

thedataset = pd.read_csv("THE World University Rankings 2016-2025.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
years = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]

filtered_data = pd.DataFrame()

for country in countries :
    for year in years :
        temp_df = thedataset[(thedataset["Country"] == country) & (thedataset["Year"] == year)][["Year","Country","Rank","Name","Overall Score"]]
        filtered_data = pd.concat([filtered_data,temp_df],ignore_index = True)
        
filtered_data.to_csv("THE_filtered_countries.csv",index = False, encoding = "utf-8-sig")
