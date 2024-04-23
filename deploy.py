#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker
from db import Base, Retailers, Invoice, Regions, States, City
engine = create_engine("sqlite:///adidas.db", echo=True)
# # Load spreadsheet
# xl = pd.ExcelFile("adidas.xlsx")
# #Load a sheet as a dataframe

# df = xl.parse("Data Sales Adidas")
# #Write data to a csv file
# df.to_csv("adidas.csv", index=False)

df = pd.read_csv("adidas.csv")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

