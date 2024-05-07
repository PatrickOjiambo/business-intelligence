#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///supermarket.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

query = """
SELECT 
    invoice.invoice_id, 
    invoice.customer_type, 
    invoice.tax, 
    invoice.quantity, 
    invoice.date, 
    invoice.payment, 
    invoice.cost_of_goods, 
    invoice.gross_margin_percentage, 
    invoice.gross_income, 
    invoice.rating
FROM 
    fact_table
INNER JOIN 
    invoice ON fact_table.invoice_id = invoice.invoice_id
INNER JOIN 
    product ON fact_table.product_id = product.id
INNER JOIN 
    branch ON fact_table.branch_id = branch.id
WHERE 
    product.name = 'Food and beverages' AND 
    branch.name = 'C'
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
