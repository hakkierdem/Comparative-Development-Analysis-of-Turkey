import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("overall_score.csv")


turkey_data = df[df["Country"] == "Turkey"]


plt.figure(figsize=(10, 6))
plt.plot(turkey_data["Year"], turkey_data["Score"], 
         color='crimson', linewidth=3, marker='o', markersize=8, label="Turkey")


plt.title("Turkey - Overall Score Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Overall Score (0-100)", fontsize=12)
plt.xticks([2005, 2010, 2015, 2020, 2025])
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

