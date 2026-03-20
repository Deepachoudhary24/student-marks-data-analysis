import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("netflix_titles.csv")

print(data.head())
print(data.info())
print(data.shape)
print(data.columns)
print(data["type"].value_counts())
print("......Graphical Representation......")
type_counts = data["type"].value_counts()

plt.bar(type_counts.index, type_counts.values)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("movies_vs_tvshows.png")
plt.show()

print("......Top 10 Countries with Most Content......")
print(data["country"].value_counts().head(10))

print("......Graphical Representation......")
print(data["country"].value_counts().head(10))
plt.bar(data["country"].value_counts().head(10).index, data["country"].value_counts().head(10).values)
plt.title("Top 10 Countries with Most Content on Netflix")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("top_countries.png")
plt.show()

print()
print(data["release_year"].value_counts().head(10))
print("......Graphical Representation......")
year_counts = data["release_year"].value_counts().sort_index()

plt.plot(year_counts.index, year_counts.values)

plt.title("Netflix Content Release Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.savefig("content_growth.png")
plt.show()