import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Veriyi oku
df = pd.read_csv("overall_score.csv")  # Kolonlar: Country, Year, OverallScore

# Ülkeleri ve yılları ayıkla
countries = df['Country'].unique()
years = sorted(df['Year'].unique())

# Renk paleti
colors = plt.cm.get_cmap('tab20', len(countries))

# Şekil ve eksen
fig, ax = plt.subplots(figsize=(10, 6))

lines = {country: ax.plot([], [], label=country, color=colors(i))[0] for i, country in enumerate(countries)}

# Ekseni ayarla
ax.set_xlim(min(years), max(years))
ax.set_ylim(0, 100)
ax.set_title("Animated Overall Score Trend")
ax.set_xlabel("Year")
ax.set_ylabel("Score")
ax.legend(loc='upper left')

# Animasyonu başlatan fonksiyon
def init():
    for line in lines.values():
        line.set_data([], [])
    return list(lines.values())

# Frame bazlı güncelleme fonksiyonu
def update(frame):
    current_years = years[:frame+1]
    for country in countries:
        data = df[df['Country'] == country]
        years_data = data[data['Year'].isin(current_years)]['Year']
        scores = data[data['Year'].isin(current_years)]['Score']
        lines[country].set_data(years_data, scores)
    return list(lines.values())

# Animasyon oluştur
ani = animation.FuncAnimation(fig, update, frames=len(years),
                              init_func=init, blit=True, repeat=False)


ani.save("animated_trend.mp4", fps=2)

plt.tight_layout()
plt.show()

