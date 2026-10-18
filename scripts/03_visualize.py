import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../output/cleaned_data.csv")
print("Creating visualizations...")

sns.set_style("whitegrid")

# Chart 1: Monthly Revenue Trend
monthly = df.groupby("MonthYear")["TotalAmount"].sum().reset_index()
monthly.columns = ["Month", "Revenue"]
plt.figure(figsize=(14, 6))
plt.plot(monthly["Month"], monthly["Revenue"], marker="o", color="steelblue", linewidth=2)
plt.title("Monthly Revenue Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue in GBP")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../output/chart1_monthly_revenue.png")
plt.close()
print("Chart 1 saved: Monthly Revenue Trend")

# Chart 2: Top 10 Products by Revenue
top_products = df.groupby("Description")["TotalAmount"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(14, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="Blues_r")
plt.title("Top 10 Products by Revenue", fontsize=16, fontweight="bold")
plt.xlabel("Revenue in GBP")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("../output/chart2_top_products.png")
plt.close()
print("Chart 2 saved: Top 10 Products by Revenue")

# Chart 3: Top 10 Countries by Revenue
top_countries = df.groupby("Country")["TotalAmount"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(14, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="Greens_r")
plt.title("Top 10 Countries by Revenue", fontsize=16, fontweight="bold")
plt.xlabel("Revenue in GBP")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("../output/chart3_top_countries.png")
plt.close()
print("Chart 3 saved: Top 10 Countries by Revenue")

# Chart 4: Revenue by Month
monthly_bar = df.groupby("Month")["TotalAmount"].sum()
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
plt.figure(figsize=(14, 6))
sns.barplot(x=monthly_bar.index, y=monthly_bar.values, palette="Oranges_r")
plt.title("Revenue by Month", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue in GBP")
plt.xticks(ticks=range(12), labels=months)
plt.tight_layout()
plt.savefig("../output/chart4_revenue_by_month.png")
plt.close()
print("Chart 4 saved: Revenue by Month")

# Chart 5: Top 10 Customers by Spending
top_customers = df.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=False).head(10)
top_customers.index = ["Customer " + str(int(c)) for c in top_customers.index]
plt.figure(figsize=(14, 6))
sns.barplot(x=top_customers.values, y=top_customers.index, palette="Purples_r")
plt.title("Top 10 Customers by Spending", fontsize=16, fontweight="bold")
plt.xlabel("Total Spending in GBP")
plt.ylabel("Customer")
plt.tight_layout()
plt.savefig("../output/chart5_top_customers.png")
plt.close()
print("Chart 5 saved: Top 10 Customers by Spending")

# Chart 6: Order Value Distribution
order_totals = df.groupby("InvoiceNo")["TotalAmount"].sum()
order_totals_filtered = order_totals[order_totals < 500]
plt.figure(figsize=(14, 6))
sns.histplot(order_totals_filtered, bins=50, color="coral")
plt.title("Order Value Distribution under 500 GBP", fontsize=16, fontweight="bold")
plt.xlabel("Order Value in GBP")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("../output/chart6_order_distribution.png")
plt.close()
print("Chart 6 saved: Order Value Distribution")

print("\nAll 6 charts saved to output folder!")
