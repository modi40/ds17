import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City', 'Cairo'],
    'Population': [37400000, 30290000, 27050000, 22040000, 21780000, 20900000],
    'GDP': [2000, 370, 680, 250, 260, 140],
    'Literacy_Rate': [99.0, 88.7, 96.8, 95.4, 98.6, 85.0]
}

df = pd.DataFrame(data)

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

plt.figure(figsize=(10, 6))
labels = [f"{city}\n{pop//1000000}M" for city, pop in zip(df['City'], df['Population'])]
squarify.plot(sizes=df['Population'], label=labels, color=colors, alpha=0.8)
plt.title("Treemap of City-wise Population Distribution")
plt.axis('off')
plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Population'] / 1e6, df['GDP'], df['Literacy_Rate'], c=colors, s=150, edgecolors='black')

for i, txt in enumerate(df['City']):
    ax.text(df['Population'][i] / 1e6, df['GDP'][i], df['Literacy_Rate'][i], txt)

ax.set_xlabel("Population (Millions)")
ax.set_ylabel("GDP (Billion USD)")
ax.set_zlabel("Literacy Rate (%)")
ax.set_title("3D Scatter Plot: Population, GDP, and Literacy Rate")
plt.tight_layout()
plt.show()
