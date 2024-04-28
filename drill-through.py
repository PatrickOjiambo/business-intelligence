#!/usr/bin/env python
from sqlalchemy import text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///adidas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

"""
"For a particular summary of sales data by retailer and region, what 
are the detailed transactions that contributed to a high operating margin?"

This question requires not just an aggregate view, but an exploration into the individual records that aggregate to understand
better what drives higher operating margins, potentially for strategic or optimization purposes.
"""

summary_query = """
SELECT retailer_id, region_id, operating_margin
FROM invoice
GROUP BY retailer_id, region_id
HAVING operating_margin > (SELECT AVG(operating_margin) FROM invoice) * 1.2;
"""
summary_result = session.execute(text(summary_query))
for row in summary_result:
    print(row)
summary_result.close()
retailer_id = 1
region_id = 1
detailed_query = f"""
SELECT i.date, r.name as retailer_name, reg.name as region_name, p.name as product_name, i.units_sold, i.total_sales, i.operating_profit, i.operating_margin
FROM invoice i
JOIN retailers r ON i.retailer_id = r.id
JOIN regions reg ON i.region_id = reg.id
JOIN products p ON i.product_id = p.id
WHERE i.retailer_id = {retailer_id} AND i.region_id = {region_id};
"""
detailed_result = session.execute(text(detailed_query))
for detail in detailed_result:
    print(detail)
detailed_result.close()


"""
The first SQL query selects retailers and regions with operating margins significantly higher than the average (in this case, more than 20% higher).
The second SQL query is the drill-through query, which should be executed after selecting a particular retailer and region from the 
results of the first query. It fetches detailed transaction data including the date, retailer name, region name, 
product name, units sold, total sales, operating profit, and operating margin for the specified retailer and region.
"""
