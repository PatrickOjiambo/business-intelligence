#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
#Analyze sales for Amazon
query = """
SELECT r.name, SUM(CAST(i.total_sales AS FLOAT)) as total_sales
FROM invoice i
JOIN retailers r ON i.retailer_id = r.id
GROUP BY r.name
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
#Analyze sales for Amazon
result.close()
