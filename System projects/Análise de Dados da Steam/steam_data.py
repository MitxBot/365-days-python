import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("steam_.csv")

print(df.head())

#Top jogos por preço

top = df.sort_values(by="price",ascending=False).head(10)

plt.bar(top["name"],top["price"])
plt.xticks(rotation=90)
plt.show()