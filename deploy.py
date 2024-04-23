#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
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
session.add_all([Retailers(name=row['Retailer'])
                 for index, row in retailers_df.iterrows()])
session.add_all([Products(name=row['Product'], price=row['Price per Unit'])
                    for index, row in products_df.iterrows()])
session.add_all([Regions(name=row['Region'])
                    for index, row in regions_df.iterrows()])
session.add_all([States(name=row['State'], region_name=row['Region'])
                    for index, row in states_df.iterrows()])

session.commit()
