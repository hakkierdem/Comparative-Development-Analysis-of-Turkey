import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


df = pd.read_csv("pisa_rankscore.csv")


result = pd.DataFrame()

for country in df['Country'].unique():
    country_df = df[df['Country'] == country].sort_values('Year').copy()
    

    country_df['Score'] = country_df['Score'].interpolate(method='linear')
    

    full_years = pd.DataFrame({'Year': list(range(2006, 2026))})
    country_df = pd.merge(full_years, country_df, on='Year', how='left')
    country_df['Country'] = country
     

    known = country_df[country_df['Score'].notna()]
    unknown = country_df[country_df['Score'].isna()]

    if not unknown.empty and len(known) >= 2:
        X = known['Year'].values.reshape(-1, 1)
        y = known['Score'].values
        model = LinearRegression().fit(X, y)

        preds = model.predict(unknown['Year'].values.reshape(-1, 1))
        country_df.loc[unknown.index, 'Score'] = preds

    result = pd.concat([result, country_df])


result = result.sort_values(['Country', 'Year'])
result.to_csv("pisa_interpolated_extrapolated.csv", index=False)

