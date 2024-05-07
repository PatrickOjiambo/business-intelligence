#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///supermarket.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
query = """
SELECT city.name AS City, SUM(invoice.gross_income) AS Total_Gross_Income
FROM fact_table
INNER JOIN city ON fact_table.city_id = city.id
INNER JOIN invoice ON fact_table.invoice_id = invoice.invoice_id
GROUP BY city.name
"""

query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
