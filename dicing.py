#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

"""What were the total sales for Walmart and Foot Locker 
in the states of California and New York during
the first quarter (January to March) of 2020?
"""
query = """
SELECT r.name, s.name as state, SUM(CAST(i.total_sales AS FLOAT)) as total_sales
FROM invoice i
JOIN retailers r ON i.retailer_id = r.id
JOIN states s ON i.state_id = s.id
WHERE r.name IN ('Walmart', 'Foot Locker') AND 
      s.name IN ('California', 'New York') AND
      CAST(strftime('%m', i.date) AS INTEGER) BETWEEN 1 AND 3 AND
      strftime('%Y', i.date) = '2020'
GROUP BY r.name, s.name
"""
query = text(query)
result = session.execute(query)
for row in result:
    print(row)
#Analyze sales for Amazon
result.close()
