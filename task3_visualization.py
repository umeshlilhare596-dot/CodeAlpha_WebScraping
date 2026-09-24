import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Convert price to number
df["Price"] = df["Price"].str.replace("£", "").astype(float)

# 1. Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Book Title"], df["Price"])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.title("Book Price Visualization")
plt.tight_layout()
plt.show()

# 2. Basic insights
print("Average Price:", df["Price"].mean())
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())

print("\nData Story:")
print("The chart shows the price variation among books.")
print("This visualization helps compare book prices easily.")
