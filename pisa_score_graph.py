import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pisa_rankscore.csv") 
countries = df["Country"].unique()

fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(16, 10), sharex=True, sharey=True)
axs = axs.flatten()

for i, country in enumerate(countries):
    data = df[df["Country"] == country]
    axs[i].plot(data["Year"], data["Overall Score"], marker='o')
    axs[i].set_title(country)
    axs[i].grid(True)

plt.tight_layout()
plt.suptitle("PISA Scores by Country (Years)", fontsize=16, y=1.02)
plt.show()

