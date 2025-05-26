import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("THE_filtered_countries.csv") 

# 2. Üniversite seçimi
selected_universities = ["Koç University", "Middle East Technical University", "Istanbul Technical University", "Boğaziçi University","Ankara University","Gazi University"]

# 3. Grafik çizimi
plt.figure(figsize=(12, 6))

for uni in selected_universities:
    data = df[(df["Name"] == uni) & (df["Country"] == "Turkey")]
    plt.plot(data["Year"], data["Rank"], marker="o", label=uni)

plt.gca().invert_yaxis()  
plt.title("Selected Turkish Universities - THE World Rankings Over Time")
plt.xlabel("Year")
plt.ylabel("World Rank")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

