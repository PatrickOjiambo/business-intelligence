#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

"""What is the total sales and operating profit for each region and state, broken down by sales method?
"""
query = """
SELECT 
    r.name AS region,
    s.name AS state,
    SUM(CASE WHEN i.sales_method = 'In-store' THEN i.total_sales ELSE 0 END) / 1.0 AS total_sales_in_store,
    SUM(CASE WHEN i.sales_method = 'Outlet' THEN i.total_sales ELSE 0 END) / 1.0 AS total_sales_outlet,
    SUM(CASE WHEN i.sales_method = 'In-store' THEN i.operating_profit ELSE 0 END) / 1.0 AS operating_profit_in_store,
    SUM(CASE WHEN i.sales_method = 'Outlet' THEN i.operating_profit ELSE 0 END) / 1.0 AS operating_profit_outlet
FROM 
    invoice i
JOIN 
    regions r ON i.region_id = r.id
JOIN 
    states s ON i.state_id = s.id
GROUP BY 
    r.name, 
    s.name;
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
#Analyze sales for Amazon
result.close()
