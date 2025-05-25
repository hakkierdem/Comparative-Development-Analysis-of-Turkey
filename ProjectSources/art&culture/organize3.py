import pandas as pd


df = pd.read_csv("global_cultural_trends.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year


melted_df = df.melt(
    id_vars=['Country', 'Year'],
    value_vars=['book', 'cinema', 'museum', 'concert', 'theater'],
    var_name='Attribute',
    value_name='Score'
)


melted_df['Score'] = pd.to_numeric(melted_df['Score'], errors='coerce')
melted_df['Score'] = melted_df['Score'].fillna(0)  


pivot_result = melted_df.pivot_table(
    index=['Country', 'Year'],
    columns='Attribute',
    values='Score',
    aggfunc='mean'
).reset_index()


pivot_result.to_csv("cultural_trends_final_clean.csv", index=False)
print(pivot_result.head())
