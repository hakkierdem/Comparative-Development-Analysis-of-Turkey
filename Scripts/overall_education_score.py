import pandas as pd
import numpy as np

pisa_dataset = pd.read_csv("normalization_pisa_scores.csv")
the_dataset = pd.read_csv("THE_countries_overallscores.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
years = range(2006,2026)

result = []

def calculateOverallEduScore(pisa,the):
    
    if pd.isna(the):
        return pisa
    
    elif pd.isna(pisa):
        return the
        
    else:
        return 0.6 * pisa + 0.4 * the
        

for country in countries :
    for year in years :
        
        pisa_data = pisa_dataset[(pisa_dataset["Country"] == country) & (pisa_dataset["Year"] == year)]
        pisa_score = pisa_data["Normalization Score"].values[0] if not pisa_data.empty else np.nan
        
        the_data = the_dataset[(the_dataset["Country"] == country) & (the_dataset["Year"] == year)]
        the_score = the_data["Score"].values[0] if not the_data.empty else np.nan
        
        overall_edu_score = calculateOverallEduScore(pisa_score,the_score)
        
        result.append({
            "Country" : country,
            "Year" : year,
            "Score" : overall_edu_score
            })
            
results_df = pd.DataFrame(result)
results_df.to_csv("overall_edu_score.csv",index = False)
