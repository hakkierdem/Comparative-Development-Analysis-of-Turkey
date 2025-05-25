import pandas as pd

pisa_scores = pd.read_csv("pisa_intrepolation_scores.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
years = range(2006,2026)

max_score = 550
min_score = 350

def normalization(score):
    new_score = ((score - min_score) / (max_score - min_score) ) * 100
    return new_score

result = []

for country in countries :
    for year in years :  
    
        pisa_data = pisa_scores[(pisa_scores["Country"] == country ) & (pisa_scores["Year"] == year)]["Overall Score"].values[0]

        result.append({
            "Country" : country,
            "Year" : year,
            "Normalization Score" : normalization(pisa_data)
        })
        
results_df = pd.DataFrame(result)
results_df.to_csv("normalization_pisa_scores.csv",index = False)
