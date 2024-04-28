#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
"""
To form a business question that requires a drill-up operation and to generate the
corresponding SQL, we should consider a scenario where detailed data is aggregated
to a higher level of summarization. Given your database schema, one possible question might be:

"What is the total sales volume for each region?"

This question requires drilling up from more specific data points (like sales by city or state)
to a more general level (sales by region). The drill-up will aggregate sales data from possibly
finer geographical units to their encompassing regions.
"""

query = """
SELECT Regions.name AS Region, SUM(Invoice.total_sales) AS Total_Sales
FROM Invoice
JOIN States ON Invoice.state_id = States.id
JOIN Regions ON States.region_name = Regions.name
GROUP BY Regions.name;


"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
result.close()
