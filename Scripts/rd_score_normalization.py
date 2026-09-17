import pandas as pd

rd_df = pd.read_csv("complated_rd_data.csv")
allcountries_df = pd.read_excel("filtered_rd_scores_allcountries.xlsx")

# Sütun isimlerini normalize et
rd_df.columns = rd_df.columns.str.strip().str.lower()
allcountries_df.columns = allcountries_df.columns.str.strip().str.lower()

years = range(2005, 2025)
countries = ["Turkey", "Germany", "Japan", "Brazil", "Poland", "United Kingdom",
             "Canada", "Jordan", "Sweden", "South Korea", "Malaysia"]

min_scores = {}
max_scores = {}

for year in years:
    year_df = allcountries_df[allcountries_df["year"] == year]
    
    if year in [2023, 2024]:
        # 2023 ve 2024 için 2022 değerlerini kullan
        min_scores[year] = allcountries_df[allcountries_df["year"] == 2022]["r&d_expenditure"].min()
        max_scores[year] = allcountries_df[allcountries_df["year"] == 2022]["r&d_expenditure"].max()
    else:
        min_scores[year] = year_df["r&d_expenditure"].min()
        max_scores[year] = year_df["r&d_expenditure"].max()

score_list = []

for _, row in rd_df.iterrows():
    year = row["year"]
    country = row["country name"]
    value = row["r&d_expenditure"]

    if year in min_scores and country in countries:
        min_val = min_scores[year]
        max_val = max_scores[year]

        if pd.notna(value) and max_val != min_val and min_val is not None and max_val is not None:
            score = ((value - min_val) / (max_val - min_val)) * 100
        else:
            score = None
    else:
        score = None

    score_list.append(score)

rd_df["score"] = score_list

rd_df.to_csv("normalization_rd_scores.csv", index=False)

