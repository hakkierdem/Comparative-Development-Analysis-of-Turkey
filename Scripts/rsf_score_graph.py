import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("rsf_scores.csv")

countries = ["TUR","POL","BRA","DEU","JPN","GBR","JOR","CAN","SWE","KOR","MYS"]

xticks_years = [2005, 2010, 2015, 2020, 2025]

df["Year (N)"] = df["Year (N)"].astype(int)

plt.figure(figsize=(14, 7))


fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(16, 10), sharex=True, sharey=True)
axs = axs.flatten()

for i, country in enumerate(countries):
    data = df[df["ISO"] == country]
    axs[i].plot(data["Year (N)"], data["Score N"],"r", marker='*',)
    axs[i].set_title(country)
    axs[i].grid(True)
    axs[i].set_xticks(xticks_years)
    
plt.tight_layout()
plt.suptitle("RSF Score Over Time", fontsize=16, y=1.02)
plt.xlabel("Year")
plt.ylabel("RSF Score (0-100)")
plt.show()

