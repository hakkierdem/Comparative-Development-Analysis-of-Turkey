import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("normalization_rd_scores.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]


xticks_years = [2005, 2010, 2015, 2020, 2025]

fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(16, 10), sharex=True, sharey=True)
axs = axs.flatten()

for i, country in enumerate(countries):
    data = df[df["country name"] == country]
    axs[i].plot(data["year"], data["score"],"b", marker='s',)
    axs[i].set_title(country)
    axs[i].grid(True)
    axs[i].set_xticks(xticks_years)

plt.tight_layout()
plt.suptitle("R&D Expenditure Score Over Time", fontsize=16, y=1.02)
plt.xlabel("Year")
plt.ylabel("R&D Expenditure Score (0-100)")
plt.show()

