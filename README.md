# E-Commerce Customer Behaviour Analysis

## Project Overview
Analyzed 541,909 real e-commerce transactions from the UCI Online Retail Dataset
to uncover customer behaviour patterns, revenue trends, and business insights.

## Key Findings
- Total Revenue: GBP 8,911,407
- Total Customers: 4,338
- Total Products: 3,877
- Countries Reached: 37
- Best Month: November 2011 (GBP 1,161,817)
- Top Product: Paper Craft Little Birdie (GBP 168,469)

## Customer Segments (RFM Analysis)
- Champions: 3,271 customers (75.4%)
- At Risk: 1,067 customers (24.6%)

## Business Recommendations
1. Stock up inventory before November peak season
2. Run discount campaigns in February slow season
3. Focus UK market and expand Germany and Netherlands
4. Keep top 3 products always in stock
5. Launch loyalty program for Champion customers
6. Send win-back campaign to At Risk customers
7. Introduce free shipping above GBP 50 threshold
8. Assign account managers to top 10 spenders

## Tech Stack
- Python 3.11
- Pandas - data cleaning and exploration
- Matplotlib - data visualization
- Seaborn - statistical charts
- Scikit-learn - K-Means clustering
- Streamlit - interactive dashboard

## Scripts
- 01_load_and_clean.py - Load and clean raw data
- 02_explore.py - Exploratory data analysis
- 03_visualize.py - Generate 8 charts
- 04_segment.py - RFM customer segmentation
- 05_insights.py - Business insights and recommendations
- 06_dashboard.py - Interactive Streamlit dashboard

## How to Run
1. Install dependencies: py -3.11 -m pip install pandas matplotlib seaborn scikit-learn streamlit openpyxl
2. Download dataset to data/ folder
3. Run scripts in order: 01 to 05
4. Launch dashboard: py -3.11 -m streamlit run scripts/06_dashboard.py

## Dataset
UCI Online Retail Dataset
541,909 transactions from a UK-based online retailer
Period: December 2010 to December 2011
