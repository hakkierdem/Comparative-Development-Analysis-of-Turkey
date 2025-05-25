import pandas as pd

df = pd.read_excel("historical_data_only.xlsx")


df["Year"] = df["Year"].replace({"2012-2013" : 2013,"2017-2018" : 2017})
df["Country"] = df["Country"].replace({"Korea, Rep." : "South Korea","Türkiye" : "Turkey"})

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]

years = range(2013,2025)

result = []

for year in years: 
    for country in countries:
    
        if year == 2018:
            filtered = (df["Country"] == country) & (df["Year"] == 2017)
        else:
            filtered = (df["Country"] == country) & (df["Year"] == 2017)
            
        result.append({
        "Country" : country,
        "Year" : year,
        "Score" : df[filtered]["WJP Rule of Law Index: Overall Score"].values[0] * 100})
       
results_df = pd.DataFrame(result)
results_df.to_excel("wjp_filteredcountries.xlsx",index = False)

