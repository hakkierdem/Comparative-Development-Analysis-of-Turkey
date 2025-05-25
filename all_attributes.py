import pandas as pd

edu_df = pd.read_csv("overall_edu_score.csv")
cult_df = pd.read_csv("overall_cultural_score.csv")
freedom_df = pd.read_csv("overall_freedom_score.csv")
sci_df = pd.read_csv("overall_scientific_contribution_score.csv")
ethic_df = pd.read_excel("overall_socialmorality_score.xlsx")


edu_df = edu_df.rename(columns={"Score" : "Score Education"})
cult_df = cult_df.rename(columns={"Score" : "Score Culture"})
freedom_df = freedom_df.rename(columns={"Score" : "Score Freedom"})
sci_df = sci_df.rename(columns={"Score" : "Score Science"})
ethic_df = ethic_df.rename(columns={"Score" : "Score Ethic"})

df_list = [edu_df,cult_df,freedom_df,sci_df,ethic_df]

df_merged = edu_df.merge(cult_df,on = ["Country","Year"],how = "outer")
df_merged = df_merged.merge(freedom_df,on = ["Country","Year"],how = "outer")
df_merged = df_merged.merge(sci_df,on = ["Country","Year"],how = "outer")
df_merged = df_merged.merge(ethic_df,on = ["Country","Year"],how = "outer")

df_merged.to_csv("all_criters.csv")
