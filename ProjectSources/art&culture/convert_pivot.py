import pandas as pd


yearly_scores = pd.read_csv("yearly_cultural_scores_clean.csv")


pivot_table = yearly_scores.pivot(
    index='Country',      
    columns='Year',       
    values='Overall_Score' 
)


print(pivot_table.head())
pivot_table.to_excel("yearly_cultural_score_pivot.xlsx")
