#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///supermarket.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
query = """
SELECT 
    b.name as branch_name, 
    p.name as product_name, 
    SUM(i.gross_income) as total_gross_income
FROM 
    fact_table as f
JOIN 
    branch as b ON f.branch_id = b.id
JOIN 
    product as p ON f.product_id = p.id
JOIN 
    invoice as i ON f.invoice_id = i.invoice_id
GROUP BY 
    branch_name, 
    product_name
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
