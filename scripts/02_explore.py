import pandas as pd

# Load cleaned data
print("Loading cleaned data...")
df = pd.read_csv("../output/cleaned_data.csv")
print(f"Rows loaded: {len(df)}")

# === BASIC STATS ===
print("\n=== BASIC STATISTICS ===")
print(f"Total transactions: {len(df)}")
print(f"Total unique customers: {df['CustomerID'].nunique()}")
print(f"Total unique products: {df['Description'].nunique()}")
print(f"Total unique countries: {df['Country'].nunique()}")
print(f"Total revenue: £{df['TotalAmount'].sum():,.2f}")
print(f"Average order value: £{df['TotalAmount'].mean():,.2f}")

# === TOP 10 PRODUCTS BY REVENUE ===
print("\n=== TOP 10 PRODUCTS BY REVENUE ===")
top_products = df.groupby("Description")["TotalAmount"].sum().sort_values(ascending=False).head(10)
for i, (product, revenue) in enumerate(top_products.items(), 1):
    print(f"{i}. {product[:50]} — £{revenue:,.2f}")

# === TOP 10 COUNTRIES BY REVENUE ===
print("\n=== TOP 10 COUNTRIES BY REVENUE ===")
top_countries = df.groupby("Country")["TotalAmount"].sum().sort_values(ascending=False).head(10)
for i, (country, revenue) in enumerate(top_countries.items(), 1):
    print(f"{i}. {country} — £{revenue:,.2f}")

# === MONTHLY REVENUE ===
print("\n=== MONTHLY REVENUE ===")
monthly = df.groupby("MonthYear")["TotalAmount"].sum()
for month, revenue in monthly.items():
    print(f"{month} — £{revenue:,.2f}")

# === TOP 10 CUSTOMERS BY SPENDING ===
print("\n=== TOP 10 CUSTOMERS BY SPENDING ===")
top_customers = df.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=False).head(10)
for i, (customer, spending) in enumerate(top_customers.items(), 1):
    print(f"{i}. Customer {int(customer)} — £{spending:,.2f}")

# === BEST SELLING PRODUCTS BY QUANTITY ===
print("\n=== TOP 10 BEST SELLING PRODUCTS BY QUANTITY ===")
top_quantity = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
for i, (product, qty) in enumerate(top_quantity.items(), 1):
    print(f"{i}. {product[:50]} — {qty:,} units")

# Save summary
summary = {
    "Total Transactions": len(df),
    "Unique Customers": df["CustomerID"].nunique(),
    "Unique Products": df["Description"].nunique(),
    "Unique Countries": df["Country"].nunique(),
    "Total Revenue": round(df["TotalAmount"].sum(), 2),
    "Average Order Value": round(df["TotalAmount"].mean(), 2)
}

summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])
summary_df.to_csv("../output/summary_stats.csv", index=False)
print("\nSummary saved to ../output/summary_stats.csv")
