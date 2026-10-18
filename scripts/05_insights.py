import pandas as pd

df = pd.read_csv("../output/cleaned_data.csv")
rfm = pd.read_csv("../output/rfm_segments.csv")

print("=" * 60)
print("E-COMMERCE CUSTOMER BEHAVIOUR ANALYSIS")
print("Business Insights Report")
print("=" * 60)

print("\n=== KEY METRICS ===")
print(f"Total Revenue Generated : GBP {df['TotalAmount'].sum():,.2f}")
print(f"Total Unique Customers  : {df['CustomerID'].nunique():,}")
print(f"Total Products Sold     : {df['Description'].nunique():,}")
print(f"Total Countries Reached : {df['Country'].nunique()}")
print(f"Average Order Value     : GBP {df['TotalAmount'].mean():,.2f}")

print("\n=== INSIGHT 1: REVENUE TREND ===")
monthly = df.groupby("MonthYear")["TotalAmount"].sum()
best_month = monthly.idxmax()
worst_month = monthly.idxmin()
print(f"Best month  : {best_month} with GBP {monthly.max():,.2f}")
print(f"Worst month : {worst_month} with GBP {monthly.min():,.2f}")
print("Recommendation: Stock up inventory before November.")
print("Run promotional campaigns in slow months like February.")

print("\n=== INSIGHT 2: TOP MARKET ===")
top_country = df.groupby("Country")["TotalAmount"].sum().idxmax()
top_revenue = df.groupby("Country")["TotalAmount"].sum().max()
print(f"Largest market : {top_country} with GBP {top_revenue:,.2f}")
print("Recommendation: Focus marketing budget on UK.")
print("Expand Netherlands and Germany for international growth.")

print("\n=== INSIGHT 3: BEST PRODUCTS ===")
top3 = df.groupby("Description")["TotalAmount"].sum().sort_values(ascending=False).head(3)
print("Top 3 revenue-generating products:")
for i, (p, r) in enumerate(top3.items(), 1):
    print(f"  {i}. {p[:50]} — GBP {r:,.2f}")
print("Recommendation: Keep these always in stock.")
print("Bundle these products with slower-selling items.")

print("\n=== INSIGHT 4: CUSTOMER SEGMENTS ===")
seg_counts = rfm["Segment_Name"].value_counts()
for seg, count in seg_counts.items():
    pct = (count / len(rfm)) * 100
    print(f"  {seg}: {count} customers ({pct:.1f}%)")
print("Recommendation:")
print("  Champions   : Reward with loyalty program and early access.")
print("  At Risk     : Send win-back email campaign with discount.")

print("\n=== INSIGHT 5: HIGH VALUE CUSTOMERS ===")
top_customer = rfm.sort_values("Monetary", ascending=False).iloc[0]
print(f"Top customer ID  : {int(top_customer['CustomerID'])}")
print(f"Total spending   : GBP {top_customer['Monetary']:,.2f}")
print(f"Purchase count   : {int(top_customer['Frequency'])} orders")
print("Recommendation: Assign a dedicated account manager")
print("to the top 10 customers. They drive significant revenue.")

print("\n=== INSIGHT 6: ORDER VALUE ===")
order_totals = df.groupby("InvoiceNo")["TotalAmount"].sum()
print(f"Average order value : GBP {order_totals.mean():,.2f}")
print(f"Median order value  : GBP {order_totals.median():,.2f}")
print(f"Max order value     : GBP {order_totals.max():,.2f}")
print("Recommendation: Introduce free shipping above GBP 50")
print("to increase average order value.")

print("\n" + "=" * 60)
print("SUMMARY OF RECOMMENDATIONS")
print("=" * 60)
print("1. Stock up inventory before November peak season")
print("2. Run discount campaigns in February slow season")
print("3. Focus UK market and expand Germany and Netherlands")
print("4. Keep top 3 products always in stock")
print("5. Launch loyalty program for Champion customers")
print("6. Send win-back campaign to 1067 At Risk customers")
print("7. Introduce free shipping above GBP 50 threshold")
print("8. Assign account managers to top 10 spenders")
print("=" * 60)

# Save insights
insights = [
    "Stock up inventory before November peak season",
    "Run discount campaigns in February slow season",
    "Focus UK market and expand Germany and Netherlands",
    "Keep top 3 products always in stock",
    "Launch loyalty program for Champion customers",
    "Send win-back campaign to 1067 At Risk customers",
    "Introduce free shipping above GBP 50 threshold",
    "Assign account managers to top 10 spenders"
]
pd.DataFrame(insights, columns=["Recommendation"]).to_csv(
    "../output/recommendations.csv", index=False)
print("\nRecommendations saved to ../output/recommendations.csv")
