import pandas as pd
import os

# Load dataset
print("Loading dataset...")
df = pd.read_excel("../data/Online_Retail.xlsx")

print(f"Dataset loaded successfully!")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"\nColumn names: {list(df.columns)}")

# Check missing values
print(f"\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Clean data
print("\nCleaning data...")

# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove rows with missing Description
df = df.dropna(subset=["Description"])

# Remove cancelled orders (InvoiceNo starting with C)
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove negative or zero quantities
df = df[df["Quantity"] > 0]

# Remove negative or zero prices
df = df[df["UnitPrice"] > 0]

# Add TotalAmount column
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Extract month and year
df["Month"] = df["InvoiceDate"].dt.month
df["Year"] = df["InvoiceDate"].dt.year
df["MonthYear"] = df["InvoiceDate"].dt.to_period("M")

# Reset index
df = df.reset_index(drop=True)

print(f"Data cleaned successfully!")
print(f"Rows after cleaning: {len(df)}")
print(f"\nSample cleaned data:")
print(df[["InvoiceNo", "Description", "Quantity", "UnitPrice", "TotalAmount", "CustomerID"]].head())

# Save cleaned data
output_path = "../output/cleaned_data.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned data saved to: {output_path}")
