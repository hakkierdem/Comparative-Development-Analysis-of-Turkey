import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("overall_score.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]

colors = plt.cm.tab20.colors  
color_map = {country: colors[i % len(colors)] for i, country in enumerate(countries)}

plt.figure(figsize=(12, 7))

for country in countries:
    data = df[df["Country"] == country]
    plt.plot(data["Year"], data["Score"], label=country,
             color=color_map[country], linewidth=2, marker='o')

plt.title("Overall Education Score Over Time by Country", fontsize=15)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Education Score (0-100)", fontsize=12)
plt.xticks([2005, 2010, 2015, 2020, 2025])
plt.grid(True, alpha=0.3)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9)
plt.tight_layout()
plt.show()

