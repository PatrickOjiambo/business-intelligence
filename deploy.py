#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker
from db import Base, Retailers, Invoice, Regions, States, City
engine = create_engine("sqlite:///adidas.db", echo=True)

df = pd.read_excel("adidas.xlsx", sheet_name="Data Sales Adidas")

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
retailers_df = df[['Retailer', 'Retailer ID']].drop_duplicates(subset=['Retailer'])
session.add_all([Retailers(name=row['Retailer'])
                 for index, row in retailers_df.iterrows()])
session.commit()
