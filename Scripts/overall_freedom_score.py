import pandas as pd
import numpy as np

rsf_score = pd.read_csv("edit_scores.csv")
freedomhouse_score = pd.read_csv("filtered_freedom.csv")

rsf_score.columns = rsf_score.columns.str.strip()
freedomhouse_score.columns = freedomhouse_score.columns.str.strip()

rsf_score["Year (N)"] = rsf_score["Year (N)"].astype(int)
freedomhouse_score["Year"] = freedomhouse_score["Year"].astype(int)

def calculateOverallScore(rsf,freedomhouse):

    if pd.isna(freedomhouse):
        return rsf
        
    else:
        return (0.4 * rsf + 0.6 * freedomhouse)
        
years = range(2005,2026)

countriesISO = ["TUR","DEU","JPN","BRA","POL","GBR","JOR","CAN","SWE","KOR","MYS"]
countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Jordan","Canada","Sweden","South Korea","Malaysia"]

result = []

for countryISO , country in zip(countriesISO,countries):
    for year in years :
        
        rsf_data = rsf_score[(rsf_score["ISO"] == countryISO) & (rsf_score["Year (N)"] == year)]
        rsf_data_value = rsf_data["Score N"].values[0] if not rsf_data.empty else np.nan
        
        freedomhouse_data = freedomhouse_score[(freedomhouse_score["Country"] == country) & (freedomhouse_score["Year"] == year)]
        freedomhouse_data_value = freedomhouse_data["Score"].values[0] if not freedomhouse_data.empty else np.nan
        
        overall_score = calculateOverallScore(rsf_data_value,freedomhouse_data_value)
        
        result.append({
        "Country" : country,
        "Year" : year,
        "Score" : overall_score})
        
results_df = pd.DataFrame(result)
results_df.to_csv("overall_freedom_score.csv",index = False)

        
        
    


