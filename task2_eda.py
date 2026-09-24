import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# 1. Data structure
print("First 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

# 2. Statistics
print("\nStatistics:")
print(df.describe())

# 3. Missing values and duplicates
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# 4. Price analysis
df["Price"] = df["Price"].str.replace("£", "").astype(float)

print("\nAverage Price:", df["Price"].mean())
print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())

# 5. Visualization
df["Price"].plot(kind="bar", title="Book Price Analysis")
plt.xlabel("Books")
plt.ylabel("Price (£)")
plt.show()
