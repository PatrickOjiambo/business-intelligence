#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker
from db import Base, Retailers, Invoice, Regions, States, City, Products
engine = create_engine("sqlite:///adidas.db", echo=True)

df = pd.read_excel("adidas.xlsx", sheet_name="Data Sales Adidas")

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
# retailers dataframe
retailers_df = df[['Retailer', 'Retailer ID']].drop_duplicates(subset=['Retailer'])
#Products dataframe
products_df = df[['Product', 'Price per Unit',]].drop_duplicates(subset=['Product'])
#Regions dataframe
regions_df = df[['Region']].drop_duplicates(subset=['Region'])
#States dataframe
states_df = df[['State', 'Region']].drop_duplicates(subset=['State'])
regions_obj = {
    "Northeast": 1,
    "South":2,
    "West":3,
    "Midwest":4,
    "Southeast":5
}
#cities dataframe
cities_df = df[['City', 'State']].drop_duplicates(subset=['City'])

#invoice dataframe
invoice_df = df[['Invoice Date', 'Product', 'Retailer', 'Units Sold', 'Total Sales', 'Operating Profit', 'Operating Margin', 'Sales Method' ]].drop_duplicates(subset=['Invoice Date'])
start_date = datetime.strptime('2020-01-01', '%Y-%m-%d')

session.add_all([Retailers(name=row['Retailer'])
                 for index, row in retailers_df.iterrows()])
session.add_all([Products(name=row['Product'], price=row['Price per Unit'])
                    for index, row in products_df.iterrows()])
session.add_all([Regions(name=row['Region'])
                    for index, row in regions_df.iterrows()])
session.add_all([States(name=row['State'], region_name=row['Region'])
                    for index, row in states_df.iterrows()])
session.add_all([City(name=row['City'], state_name=row['State'])
                    for index, row in cities_df.iterrows()])
# retail = session.query(Retailers.id).filter(Retailers.name == 'Foot Locker').first()
# print("retail incoming")
# print(retail[0])
# prod = session.query(Products.id).filter(Products.name == 'Women\'s Athletic Footwear').first()
# print("prod incoming")
# print(prod[0])
session.add_all([Invoice(date=start_date + timedelta(days=i),
                         retailer_id=session.query(Retailers.id).filter(Retailers.name == row['Retailer']).first()[0],
                         product_id=session.query(Products.id).filter(Products.name == row['Product']).first()[0],
                         units_sold=row['Units Sold'],
                         total_sales=row['Total Sales'],
                         operating_profit=row['Operating Profit'],
                         operating_margin=row['Operating Margin'],
                         sales_method=row['Sales Method'])
                 for i, row in invoice_df.iterrows()])

session.commit()
