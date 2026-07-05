import pandas as pd

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

print("\n===== DATASET =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== UNIQUE AUTHORS =====")
print(df["Author"].nunique())

print("\n===== TOP 10 AUTHORS =====")
print(df["Author"].value_counts().head(10))

print("\n===== TOP TAGS =====")
print(df["Tags"].value_counts().head(10))

print("\nEDA Completed Successfully!")