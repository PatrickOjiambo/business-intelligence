#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine("sqlite:///adidas.db", echo=True)
# # Load spreadsheet
# xl = pd.ExcelFile("adidas.xlsx")
# #Load a sheet as a dataframe

# df = xl.parse("Data Sales Adidas")
# #Write data to a csv file
# df.to_csv("adidas.csv", index=False)
with engine.connect() as connection:
    pass
print("True")
