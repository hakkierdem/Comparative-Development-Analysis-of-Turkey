import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("overall_edu_score.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]


colors = plt.cm.tab20.colors  

color_map = {country: colors[i % len(colors)] for i, country in enumerate(countries)}

xticks_years = [2005, 2010, 2015, 2020, 2025]

fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(16, 10), sharex=True, sharey=True)
axs = axs.flatten()

for i, country in enumerate(countries):
    data = df[df["Country"] == country]
    axs[i].plot(data["Year"], data["Score"], color=color_map[country], marker='o')
    axs[i].set_title(country)
    axs[i].grid(True)
    axs[i].set_xticks(xticks_years)


if len(countries) < len(axs):
    fig.delaxes(axs[len(countries)])

plt.tight_layout()
plt.suptitle("Overall Education Score Over Time", fontsize=16, y=1.02)
plt.xlabel("Year")
plt.ylabel("Overall Education Score (0-100)")
plt.show()

