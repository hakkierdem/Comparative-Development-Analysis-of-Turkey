import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("freedom_scores.csv")

countries = ["Turkey","Germany","Japan","Brazil","Poland","United Kingdom","Canada","Jordan","Sweden","South Korea","Malaysia"]


plt.figure(figsize=(14, 7))


fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(16, 10), sharex=True, sharey=True)
axs = axs.flatten()

for i, country in enumerate(countries):
    data = df[df["Country"] == country]
    axs[i].plot(data["Year"], data["Score"],"r", marker='o',)
    axs[i].set_title(country)
    axs[i].grid(True)

plt.tight_layout()
plt.suptitle("Freedom House Score Over Time", fontsize=16, y=1.02)
plt.xlabel("Year")
plt.ylabel("Freedom House Score (0-100)")
plt.show()

