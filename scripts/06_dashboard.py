import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="shopping_cart",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1 {
        color: #1a1a2e;
        text-align: center;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 10px;
    }
    h2 {
        color: #16213e;
        border-bottom: 3px solid #667eea;
        padding-bottom: 8px;
    }
    h3 {
        color: #0f3460;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(102,126,234,0.4);
        margin: 5px;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: white;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #e0e0e0;
        margin-top: 5px;
    }
    .insight-box {
        background: white;
        border-left: 5px solid #667eea;
        padding: 15px;
        border-radius: 10px;
        margin: 8px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        color: #1a1a2e;
        font-size: 1rem;
    }
    .section-divider {
        border: none;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 5px;
        margin: 20px 0;
    }
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
    footer {
        text-align: center;
        color: #667eea;
        font-weight: bold;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv("../output/cleaned_data.csv")
rfm = pd.read_csv("../output/rfm_segments.csv")

# === HEADER ===
st.markdown("<h1>E-Commerce Customer Behaviour Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; font-size:1.1rem;'>Analyzing 541,909 real transactions from UCI Online Retail Dataset</p>", unsafe_allow_html=True)
st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# === KPI CARDS ===
st.markdown("## Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)

metrics = [
    (col1, "Total Revenue", f"GBP {df['TotalAmount'].sum():,.0f}", "#667eea"),
    (col2, "Customers", f"{df['CustomerID'].nunique():,}", "#f093fb"),
    (col3, "Products", f"{df['Description'].nunique():,}", "#4facfe"),
    (col4, "Countries", f"{df['Country'].nunique()}", "#43e97b"),
    (col5, "Avg Order", f"GBP {df.groupby('InvoiceNo')['TotalAmount'].sum().mean():,.0f}", "#fa709a"),
]

for col, label, value, color in metrics:
    with col:
        st.markdown(f"""
        <div class='metric-card' style='background: linear-gradient(135deg, {color}, #764ba2);'>
            <div class='metric-value'>{value}</div>
            <div class='metric-label'>{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# === ROW 1: Monthly Revenue + Top Countries ===
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Monthly Revenue Trend")
    monthly = df.groupby("MonthYear")["TotalAmount"].sum().reset_index()
    monthly.columns = ["Month", "Revenue"]
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    ax.plot(monthly["Month"], monthly["Revenue"],
            marker="o", color="#667eea", linewidth=2.5,
            markerfacecolor="#764ba2", markersize=8)
    ax.fill_between(range(len(monthly)), monthly["Revenue"],
                    alpha=0.15, color="#667eea")
    ax.set_xlabel("Month", fontsize=11)
    ax.set_ylabel("Revenue (GBP)", fontsize=11)
    ax.set_xticks(range(len(monthly)))
    ax.set_xticklabels(monthly["Month"], rotation=45, ha="right", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("### Top 10 Countries by Revenue")
    top_countries = df.groupby("Country")["TotalAmount"].sum().sort_values(ascending=True).tail(10)
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    colors = plt.cm.viridis([i/10 for i in range(10)])
    ax.barh(top_countries.index, top_countries.values, color=colors)
    ax.set_xlabel("Revenue (GBP)", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# === ROW 2: Top Products + Customer Segments ===
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top 10 Products by Revenue")
    top_products = df.groupby("Description")["TotalAmount"].sum().sort_values(ascending=True).tail(10)
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    colors = plt.cm.plasma([i/10 for i in range(10)])
    ax.barh(top_products.index, top_products.values, color=colors)
    ax.set_xlabel("Revenue (GBP)", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("### Customer Segments")
    seg_counts = rfm["Segment_Name"].value_counts()
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#f8f9fa")
    colors = ["#667eea", "#fa709a"]
    wedges, texts, autotexts = ax.pie(
        seg_counts.values,
        labels=seg_counts.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
        wedgeprops=dict(edgecolor="white", linewidth=2)
    )
    for text in autotexts:
        text.set_color("white")
        text.set_fontweight("bold")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# === ROW 3: Top Customers + RFM Scatter ===
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top 10 Customers by Spending")
    top_customers = df.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=True).tail(10)
    top_customers.index = ["C-" + str(int(c)) for c in top_customers.index]
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    colors = plt.cm.cool([i/10 for i in range(10)])
    ax.barh(top_customers.index, top_customers.values, color=colors)
    ax.set_xlabel("Total Spending (GBP)", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("### RFM: Frequency vs Monetary")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    colors_map = {"Champions": "#667eea", "At Risk": "#fa709a",
                  "Loyal Customers": "#43e97b", "Potential Loyalists": "#f093fb"}
    for segment, group in rfm.groupby("Segment_Name"):
        ax.scatter(group["Frequency"], group["Monetary"],
                   label=segment, alpha=0.6,
                   color=colors_map.get(segment, "gray"), s=30)
    ax.set_xlabel("Purchase Frequency", fontsize=11)
    ax.set_ylabel("Total Spending (GBP)", fontsize=11)
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# === BUSINESS RECOMMENDATIONS ===
st.markdown("## Business Recommendations")
recommendations = [
    ("Stock up inventory before November peak season", "#667eea"),
    ("Run discount campaigns in February slow season", "#f093fb"),
    ("Focus UK market and expand Germany and Netherlands", "#4facfe"),
    ("Keep top 3 products always in stock", "#43e97b"),
    ("Launch loyalty program for Champion customers", "#fa709a"),
    ("Send win-back campaign to 1,067 At Risk customers", "#764ba2"),
    ("Introduce free shipping above GBP 50 threshold", "#667eea"),
    ("Assign account managers to top 10 spenders", "#f093fb"),
]

col1, col2 = st.columns(2)
for i, (rec, color) in enumerate(recommendations):
    if i % 2 == 0:
        with col1:
            st.markdown(f"""
            <div class='insight-box' style='border-left-color: {color};'>
                <b style='color:{color};'>{i+1}.</b> {rec}
            </div>
            """, unsafe_allow_html=True)
    else:
        with col2:
            st.markdown(f"""
            <div class='insight-box' style='border-left-color: {color};'>
                <b style='color:{color};'>{i+1}.</b> {rec}
            </div>
            """, unsafe_allow_html=True)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# === DATA TABLE ===
st.markdown("## Raw Data Preview")
st.dataframe(
    df[["InvoiceNo", "Description", "Quantity", "UnitPrice", "TotalAmount", "Country"]].head(100),
    use_container_width=True
)

# === FOOTER ===
st.markdown("""
<footer>
    Built by Pavana | E-Commerce Customer Behaviour Analysis | Python + Streamlit
</footer>
""", unsafe_allow_html=True)
