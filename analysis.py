import pandas as pd

# Load dataset
df = pd.read_csv("SuperStoreOrders.csv")

# Basic info
print(df.info())

# Data Cleaning
df.drop_duplicates(inplace=True)
df.ffill(inplace=True)

# Convert date column if present
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, format='mixed')
if 'ship_date' in df.columns:
    df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, format='mixed')

# Analysis
# Total Sales
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
print(df['sales'].dtype)
total_sales = df['sales'].sum()
print("Total Sales:", total_sales)


# Sales by Category
category_sales = df.groupby('category')['sales'].sum()
print("\nSales by Category:\n", category_sales)

# Sales by Country
country_sales = df.groupby('country')['sales'].sum()
print("\nSales by Country:\n", country_sales)

#Sales by Market
market_sales=df.groupby('market')['sales'].sum()
print('\nSales by Market:\n', market_sales)


# Top 5 Sales
top_sales = df.sort_values(by='sales', ascending=False).head()
print("\nTop 5 Sales:\n", top_sales) 


#Monthly Sales Trend
df['month'] = df['order_date'].dt.to_period('M')
monthly_sales = df.groupby('month')['sales'].sum()
print("\nMonthly Sales Trend\n",monthly_sales)
#Identify growth/decline trends
#Useful for business planning

#Top 5 Products by Sales
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(5)
print("\nTop Products\n",top_products)

#Profit Analysis
profit_category = df.groupby('category')['profit'].sum().sort_values(ascending=False)
print("\nProfit Analysis\n",profit_category)

#Loss Analysis
loss_category= profit_category[profit_category<0]
print("\nLoss Aanalysis\n",loss_category)

#Average Sales per Order
avg_sales= df['sales'].mean()
print("\nAverage Sales per Order: ",avg_sales)

#Sales vs Profit Comparison
sales_profit = df.groupby('category')[['sales', 'profit']].sum()
print("\nSales vs Profit Comparison\n",sales_profit)

#Shipping Cost Analysis
high_shipping = df.sort_values(by='shipping_cost', ascending=False).head(5)
print("\nShipping Cost Analysis\n",high_shipping[['product_name', 'shipping_cost']])