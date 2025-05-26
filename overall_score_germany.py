import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("overall_score.csv")

countries = [ "Germany", "Japan", "Brazil", "Poland",
             "United Kingdom", "Canada", "Jordan", "Sweden", "South Korea", "Malaysia"]

colors = plt.cm.tab10.colors


for i, country in enumerate(countries):
    country_data = df[df["Country"] == country]

    plt.figure(figsize=(10, 6))
    plt.plot(country_data["Year"], country_data["Score"],
             color=colors[i], linewidth=3, marker='o', markersize=8, label=country)

    plt.title(f"{country} - Overall Score Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Overall Score (0-100)", fontsize=12)
    plt.xticks([2005, 2010, 2015, 2020, 2025])
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.show()
