#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///supermarket.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
query = """
SELECT product.name AS product_name, SUM(invoice.gross_income) AS total_gross_income
FROM fact_table
INNER JOIN product ON fact_table.product_id = product.id
INNER JOIN invoice ON fact_table.invoice_id = invoice.invoice_id
GROUP BY product.name
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
