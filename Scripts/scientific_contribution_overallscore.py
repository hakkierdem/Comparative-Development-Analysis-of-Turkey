import pandas as pd

scimagojr_df = pd.read_excel("general_score_scimagojr.xlsx")
rd_df = pd.read_csv("normalization_rd_scores.csv")

years = range(2005,2025)
countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]


def calculateOverallScore(scimago,rd):

    return 0.7 * scimago + 0.3 * rd

result = []



for country in countries:
    for year in years:
   
        filter_sci = (scimagojr_df["Country"] == country) & (scimagojr_df["Year"] == year)

        sci_data = scimagojr_df[filter_sci]["scientific_score"].values[0]
        
        filter_rd = (rd_df["country name"] == country) & (rd_df["year"] == year)
        rd_data = rd_df[filter_rd]["score"].values[0]
        
        result.append({
        "Country" : country,
        "Year" : year,
        "Score" : calculateOverallScore(sci_data,rd_data)})
        
results_df = pd.DataFrame(result)

results_df.to_csv("overall_scientific_contribution_score.csv",index = False)
        
