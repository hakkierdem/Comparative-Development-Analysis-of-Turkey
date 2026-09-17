import pandas as pd

df = pd.read_excel("freedom_house.xlsx")


countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]

years = range(2013,2026)

result = []

for year in years : 
    for country in countries:
    
        score_data = df[(df["Country/Territory"] == country) & (df["Edition"] == year)]["Total"].values[0]

        result.append({
        "Country" : country,
        "Year" : year,
        "Score" : score_data })
        
result_df = pd.DataFrame(result)
result_df.to_csv("filtered_freedom.csv",index = False)
