import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../output/cleaned_data.csv")
print("Building customer segments...")

# Build RFM table
# R = Recency (how recently they bought)
# F = Frequency (how many times they bought)
# M = Monetary (how much they spent)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
latest_date = df["InvoiceDate"].max()

rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (latest_date - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("TotalAmount", "sum")
).reset_index()

print(f"RFM table built for {len(rfm)} customers")
print("\nSample RFM data:")
print(rfm.head())

print("\nRFM Statistics:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe())

# Scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])

# K-Means with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm["Segment"] = kmeans.fit_predict(rfm_scaled)

# Label segments based on characteristics
segment_summary = rfm.groupby("Segment").agg(
    Customers=("CustomerID", "count"),
    Avg_Recency=("Recency", "mean"),
    Avg_Frequency=("Frequency", "mean"),
    Avg_Monetary=("Monetary", "mean")
).reset_index()

print("\nSegment Summary:")
print(segment_summary.round(2))

# Name the segments
segment_names = {}
for idx, row in segment_summary.iterrows():
    seg = row["Segment"]
    if row["Avg_Recency"] < 50 and row["Avg_Monetary"] > 1000:
        segment_names[seg] = "Champions"
    elif row["Avg_Recency"] < 100 and row["Avg_Frequency"] > 5:
        segment_names[seg] = "Loyal Customers"
    elif row["Avg_Recency"] > 200:
        segment_names[seg] = "At Risk"
    else:
        segment_names[seg] = "Potential Loyalists"

rfm["Segment_Name"] = rfm["Segment"].map(segment_names)

print("\nCustomer Segments:")
print(rfm["Segment_Name"].value_counts())

# Chart 1: Segment Distribution
plt.figure(figsize=(10, 6))
rfm["Segment_Name"].value_counts().plot(kind="bar", color=["gold","steelblue","coral","green"])
plt.title("Customer Segment Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../output/chart7_segments.png")
plt.close()
print("Chart 7 saved: Customer Segments")

# Chart 2: RFM Scatter — Frequency vs Monetary
plt.figure(figsize=(10, 6))
colors = {"Champions": "gold", "Loyal Customers": "steelblue",
          "At Risk": "coral", "Potential Loyalists": "green"}
for segment, group in rfm.groupby("Segment_Name"):
    plt.scatter(group["Frequency"], group["Monetary"],
                label=segment, alpha=0.6, color=colors.get(segment, "gray"))
plt.title("Customer Segments: Frequency vs Monetary", fontsize=16, fontweight="bold")
plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spending (GBP)")
plt.legend()
plt.tight_layout()
plt.savefig("../output/chart8_rfm_scatter.png")
plt.close()
print("Chart 8 saved: RFM Scatter Plot")

# Save RFM data
rfm.to_csv("../output/rfm_segments.csv", index=False)
print("RFM segments saved to ../output/rfm_segments.csv")
