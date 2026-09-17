import pandas as pd
import numpy as np

df_cpi = pd.read_excel("cpi_general_scores.xlsx")
df_wjp = pd.read_excel("wjp_filteredcountries.xlsx")

def calculateOverallScore(cpi,wjp):

    if pd.isna(wjp):
        return cpi
        
    else:
        return 0.6 * wjp + 0.4 * cpi
        
years = range(2005,2025)
countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Jordan","Canada","Sweden","South Korea","Malaysia"]

result = []

for country in countries:
    for year in years:
        filter_cpi = df_cpi[(df_cpi["Year"] == year) & (df_cpi["Country"] == country)]
        filter_wjp = df_wjp[(df_wjp["Year"] == year) & (df_wjp["Country"] == country)]
        
        cpi_data = filter_cpi["Score"].values[0] if not filter_cpi.empty else np.nan
        wjp_data = filter_wjp["Score"].values[0] if not filter_wjp.empty else np.nan

        result.append({
        "Country" : country,
        "Year" : year,
        "Score" : calculateOverallScore(cpi_data,wjp_data)})
        
results_df = pd.DataFrame(result)

results_df.to_excel("overall_socialmorality_score.xlsx",index = False)
