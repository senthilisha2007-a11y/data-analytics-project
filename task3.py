import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# Top 10 Authors
top_authors = df["Author"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_authors.plot(kind="bar")

plt.title("Top 10 Authors")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_authors_chart.png")

plt.show()

print("Visualization Completed Successfully!")