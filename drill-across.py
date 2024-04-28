#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

"""
"Compare the total sales and units sold of each product across different regions for the current year."

This question involves analyzing data across the dimensions of
products and regions while focusing on the measures of total sales
and units sold. It is suitable for a drill-across operation because
it requires comparing aggregated data from different categories within
the same level of aggregation (across different regions).
"""
query = """
SELECT 
    p.name AS Product_Name, 
    r.name AS Region, 
    SUM(i.total_sales) AS Total_Sales, 
    SUM(i.units_sold) AS Units_Sold
FROM 
    invoice i
JOIN 
    products p ON i.product_id = p.id
JOIN 
    regions r ON i.region_id = r.id
WHERE 
    strftime('%Y', i.date) = '2020'  -- Assuming the current year is 2023
GROUP BY 
    p.name, r.name
ORDER BY 
    p.name, r.name;

"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
