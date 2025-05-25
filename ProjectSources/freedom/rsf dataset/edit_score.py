import pandas as pd

df = pd.read_csv("filteredmerged_allcountries.csv")

years = [str(y) for y in range(2005, 2011)]
countries = ["TUR","POL","BRA","DEU","JPN","GBR","JOR","CAN","SWE","KOR","MYS"]

df["Score N"] = df["Score N"].astype(str).str.replace(",", ".").astype(float)

result = []

for year in years:
    year_mask = (df["Year (N)"] == year)
    year_scores = df.loc[year_mask, "Score N"]
       
    original_min = year_scores.min()
    original_max = year_scores.max()
        
    df.loc[year_mask, "Score N"] = (original_min + original_max) - df.loc[year_mask, "Score N"]

    new_scores = df.loc[year_mask, "Score N"]
    new_min = new_scores.min()
    new_max = new_scores.max()
    denominator = new_max - new_min
    
    if denominator == 0:
        df.loc[year_mask, "Score N"] = 100
    else:
        df.loc[year_mask, "Score N"] = ((new_scores - new_min) / denominator) * 100

df_score = (df["Year (N)"] == "2011-12") 
df.loc[df_score,"Score N"] += 10

year_mask = (df["Year (N)"] == "2011-12")
year_scores = df.loc[year_mask, "Score N"]
    
original_min = year_scores.min()
original_max = year_scores.max()

df.loc[year_mask, "Score N"] = (original_min + original_max) - df.loc[year_mask, "Score N"]
    
new_scores = df.loc[year_mask, "Score N"]
new_min = new_scores.min()
new_max = new_scores.max()
denominator = new_max - new_min
    
if denominator == 0:
    df.loc[year_mask, "Score N"] = 100
else:
    df.loc[year_mask, "Score N"] = ((new_scores - new_min) / denominator) * 100

for year in years :
    for country in countries:
            df_score = (df["Year (N)"] == year) & (df["ISO"] == country)
            score = df.loc[df_score,"Score N"].values[0] 
            
            result.append({
            "ISO" : country,
            "Year (N)" : year,
            "Rank N" : df.loc[df_score,"Rank N"].values[0],
            "Score N" : score})
        
for country in countries:
            df_score = (df["Year (N)"] == "2011-12") & (df["ISO"] == country)
            score = df.loc[df_score,"Score N"].values[0] 
            
            result.append({
            "ISO" : country,
            "Year (N)" : "2011",
            "Rank N" : df.loc[df_score,"Rank N"].values[0],
            "Score N" : score})

years2 = [str(y) for y in range(2013,2026)]

for year in years2:
    for country in countries:
            df_score = (df["Year (N)"] == year) & (df["ISO"] == country)
            score = df.loc[df_score,"Score N"].values[0]
            
            result.append({
            "ISO" : country,
            "Year (N)" : year,
            "Rank N" : df.loc[df_score,"Rank N"].values[0],
            "Score N" : score})

results_df = pd.DataFrame(result)

results_df.to_csv("edit_scores.csv",index = False)
