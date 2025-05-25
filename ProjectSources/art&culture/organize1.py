import pandas as pd


df = pd.read_csv("global_cultural_trends.csv")


for col in ['concert', 'cinema', 'museum', 'book', 'theater']:
    df[col] = pd.to_numeric(df[col], errors='coerce')


print("Eksik veri sayısı:\n", df.isnull().sum())


df = df.fillna(0)


df['Overall_Score'] = df[['concert', 'cinema', 'museum', 'book', 'theater']].mean(axis=1)


df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
yearly_scores = df.groupby(['Country', 'Year'])['Overall_Score'].mean().reset_index()


yearly_scores.to_csv("yearly_cultural_scores_clean.csv", index=False)
print("İşlem başarılı!")
