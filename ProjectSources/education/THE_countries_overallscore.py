import pandas as pd

countries_data = pd.read_csv("THE_filtered_countries.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
years = range(2016,2026)

results = []

for country in countries :
    for year in years :            
        
        top_values = countries_data[(countries_data["Country"] == country) & (countries_data["Year"] == year)]["Overall Score"].head(5).to_list()
        top_values += [0] * (5 - len(top_values))
        
        overall_score = sum(top_values) / 5
        
        results.append({
            "Country" : country,
            "Year" : year,
            "Score" : overall_score,
            "Actual Universities" : len(countries_data[(countries_data["Country"] == country) & (countries_data["Year"] == year)]["Overall Score"].head(5))
        })
        
        '''print(countries_data[(countries_data["Country"] == country) & (countries_data["Year"] == year)][["Country","Year","Overall Score"]],top_values,overall_score)'''
        
results_df = pd.DataFrame(results)

results_df.to_csv("THE_countries_overallscores.csv",index = False)
