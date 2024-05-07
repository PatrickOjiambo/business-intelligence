#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///supermarket.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
query = """
SELECT 
    branch.name AS branch_name, 
    product.name AS product_name, 
    SUM(invoice.gross_income) AS total_gross_income, 
    AVG(invoice.rating) AS average_rating
FROM 
    fact_table
INNER JOIN 
    branch ON fact_table.branch_id = branch.id
INNER JOIN 
    product ON fact_table.product_id = product.id
INNER JOIN 
    city ON fact_table.city_id = city.id
INNER JOIN 
    invoice ON fact_table.invoice_id = invoice.invoice_id
WHERE 
    city.name = 'Yangon'
GROUP BY 
    branch.name, 
    product.name
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
