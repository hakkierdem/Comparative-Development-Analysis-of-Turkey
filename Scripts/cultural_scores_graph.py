import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("cultural_trends_final_clean.csv") 




categories = ["book", "cinema", "concert", "museum", "theater"]


countries = df["Country"].unique()


for country in countries:
    df_country = df[df["Country"] == country]

    plt.figure(figsize=(10, 6))
    for category in categories:
        plt.plot(df_country["Year"], df_country[category], label=category, marker='o')

    plt.title(f"{country} - Cultural Interest Trends (Google Trends)")
    plt.xlabel("Year")
    plt.ylabel("Interest Level")
    plt.legend(title="Category")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

