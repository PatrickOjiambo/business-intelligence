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
    CAST(SUM(invoice.gross_income) AS FLOAT) AS total_gross_income
FROM 
    fact_table
INNER JOIN 
    branch ON fact_table.branch_id = branch.id
INNER JOIN 
    invoice ON fact_table.invoice_id = invoice.invoice_id
GROUP BY 
    branch.name
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
