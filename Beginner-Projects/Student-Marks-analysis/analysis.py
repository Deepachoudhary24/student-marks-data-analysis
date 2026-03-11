import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print(data)
print()
print(".....Calculating Total and Average Marks.....")

data["Total"] = data["Maths"] + data["Science"] + data["English"]

data["Average"] = data["Total"] / 3

print(data)

print()

print(".....Finding Topper in the class.....")
topper = data.loc[data["Average"].idxmax()]

print()
print("Class Topper:")
print(topper)

print()
print(".....Statistical Summary.....")
print(data.describe())

sorted_data = data.sort_values(by="Average", ascending=False)

print()
print(".....Students sorted by Average Marks:.....")
print(sorted_data)

top3 = sorted_data.head(3)

print()
print(".....Top 3 Students:.....")
print(top3)

print()
print(".....Highest Marks in Each Subject:.....")

print("Maths Topper:")
print(data.loc[data["Maths"].idxmax()])

print()

print("Science Topper:")
print(data.loc[data["Science"].idxmax()])

print()

print("English Topper:")
print(data.loc[data["English"].idxmax()])

# print("Bar Graph of Average Marks:")
# plt.bar(data["Name"], data["Average"])

# plt.title("Student Average Marks")

# plt.xlabel("Students")

# plt.ylabel("Average Marks")

# plt.show()

