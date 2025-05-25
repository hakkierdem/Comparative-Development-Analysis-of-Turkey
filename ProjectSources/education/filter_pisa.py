import pandas as pd

pisa = pd.read_csv("pisa_2006-2018.csv")
countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]
filtered_pisa = pisa[pisa["Country"].isin(countries)]
filtered_pisa.to_csv("filtered_countries_pisa.csv")
