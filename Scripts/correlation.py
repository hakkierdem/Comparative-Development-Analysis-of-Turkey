import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("all_criters.csv")

criteria = ["Score Education", "Score Culture", "Score Freedom", "Score Science", "Score Ethic"]

corr = df[criteria].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Tüm Veri Üzerinden Korelasyon Matrisi")
plt.show()


