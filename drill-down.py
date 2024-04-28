#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

"""How do the sales totals for a particular product break down by city within a specific state during a certain year?
This question requires drilling down from state level to city level for detailed analysis of sales performance of a specific product over a period (in this case, a year).
"""
#I'll assume you want to analyze sales for a product with a specific ID in the state of "California" during the year "2020".
query = """
SELECT
    c.name AS City_Name,
    SUM(i.total_sales) AS Total_Sales,
    COUNT(i.id) AS Number_of_Invoices
FROM
    invoice i
    JOIN city c ON i.city_id = c.id
    JOIN states s ON i.state_id = s.id
    JOIN products p ON i.product_id = p.id
WHERE
    p.id = 1
    AND s.name = 'California'
    AND strftime('%Y', i.date) = '2020'
GROUP BY
    c.name
ORDER BY
    Total_Sales DESC;

"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
