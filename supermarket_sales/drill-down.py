#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///supermarket.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
query = """
SELECT invoice.customer_type AS customer_type, invoice.invoice_id AS invoice_id, SUM(invoice.tax) AS total_tax
FROM fact_table
INNER JOIN invoice ON fact_table.invoice_id = invoice.invoice_id
GROUP BY invoice.customer_type, invoice.invoice_id
ORDER BY invoice.customer_type, total_tax DESC;
"""

query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
