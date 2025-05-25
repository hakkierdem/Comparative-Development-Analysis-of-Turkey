import pandas as pd
import numpy as np

# Verileri yükle
rsf_score = pd.read_csv("edit_scores.csv")
freedomhouse_score = pd.read_csv("filtered_freedom.csv")

# Sütun isimlerini düzelt
rsf_score.columns = rsf_score.columns.str.strip()
freedomhouse_score.columns = freedomhouse_score.columns.str.strip()

# Year sütunlarını normalize et
rsf_score["Year"] = rsf_score["Year (N)"].astype(str).str.extract(r"(\d{4})")[0].astype(int)
freedomhouse_score["Year"] = freedomhouse_score["Year"].astype(int)

# ISO → ülke adı dönüşümü
countriesISO = ["TUR","DEU","JPN","BRA","POL","GBR","JOR","CAN","SWE","KOR","MYS"]
countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Jordan","Canada","Sweden","South Korea","Malaysia"]
iso_to_country = dict(zip(countriesISO, countries))

rsf_score["Country"] = rsf_score["ISO"].map(iso_to_country)

# Sütun isimlerini değiştir
rsf_score.rename(columns={"Score N": "RSFScore"}, inplace=True)
freedomhouse_score.rename(columns={"Score": "FreedomScore"}, inplace=True)

# Birleştir
merged = pd.merge(rsf_score[["Country", "Year", "RSFScore"]],
                  freedomhouse_score[["Country", "Year", "FreedomScore"]],
                  on=["Country", "Year"],
                  how="outer")

# Overall skor hesapla
def calculate(row):
    if pd.isna(row["FreedomScore"]):
        return row["RSFScore"]
    else:
        return 0.4 * row["RSFScore"] + 0.6 * row["FreedomScore"]

merged["OverallScore"] = merged.apply(calculate, axis=1)

# Sonuçları kaydet
merged[["Country", "Year", "OverallScore"]].sort_values(by=["Country", "Year"]).to_csv("overall_freedom_score1.csv", index=False)

