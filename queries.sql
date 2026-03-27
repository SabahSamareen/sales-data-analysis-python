--Total revenue
select sum(sales) as total_sales from superstoreorders;

--total revenue by category
select category, sum(sales) as total_sales from SuperStoreOrders group by category order by total_sales desc;

--total sales by market
select market, sum(sales) as total_sales from SuperStoreOrders group by market order by total_sales desc;

--total sales by country
select country, sum(sales) as total_sales from SuperStoreOrders group by country order by total_sales desc;

--profit by caegory
select category, sum(profit) as total_profit FROM SuperStoreOrders group by category order by category DESC;

--top 5 customers
select customer_name, sum(sales) as total_Sales FROM SuperStoreOrders group by customer_name order by customer_name desc limit 5;

--average sales per ORDER
select avg(sales) as average_sales from SuperStoreOrders;

--shipping cost analysis
select product_name, shipping_cost from SuperStoreOrders group by product_name order by shipping_cost desc limit 5;

--top products by profit
select product_name, sum(profit) as total_profits FROM SuperStoreOrders group by product_name order by total_profits desc limit 5;