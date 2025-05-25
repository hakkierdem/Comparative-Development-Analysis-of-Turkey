import pandas as pd

edu_df = pd.read_csv("overall_edu_score.csv")
cult_df = pd.read_csv("overall_cultural_score.csv")
freedom_df = pd.read_csv("overall_freedom_score.csv")
sci_df = pd.read_csv("overall_scientific_contribution_score.csv")
ethic_df = pd.read_excel("overall_socialmorality_score.xlsx")

years = range(2006,2025)
countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]

result = []

def calculateOverallScore(edu,cult,freedom,sci,ethic):
    
    return 0.2 * edu + 0.2 * cult + 0.2 * freedom + 0.2 * sci + 0.2 * ethic

for country in countries:
    for year in years :
        
        filtered_edu = (edu_df["Country"] == country) & (edu_df["Year"] == year)
        filtered_cult = (cult_df["Country"] == country) & (cult_df["Year"] == year)
        filtered_freedom = (freedom_df["Country"] == country) & (freedom_df["Year"] == year)
        filtered_sci = (sci_df["Country"] == country) & (sci_df["Year"] == year)
        filtered_ethic = (ethic_df["Country"] == country) & (ethic_df["Year"] == year)
        
        edu_data = edu_df[filtered_edu]["Score"].values[0]
        cult_data = cult_df[filtered_cult]["Score"].values[0]
        freedom_data = freedom_df[filtered_freedom]["Score"].values[0]
        sci_data = sci_df[filtered_sci]["Score"].values[0]
        ethic_data = ethic_df[filtered_ethic]["Score"].values[0]
        
        result.append({
        "Country" : country,
        "Year" : year,
        "Score" : calculateOverallScore(edu_data,cult_data,freedom_data,sci_data,ethic_data)})
        
results_df = pd.DataFrame(result)

results_df.to_csv("overall_score.csv",index = False)
