#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from db import Base, Retailers, Invoice, Regions, States, City, Products




class Deploy:
    """
    Deploy class
    """
    def __init__(self):
        self.engine = create_engine("sqlite:///adidas.db", echo=True)
        self.df = pd.read_excel("adidas.xlsx", sheet_name="Data Sales Adidas")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
    
    def populate_db(self):
        """
        This function populates the database with the data from the excel file.
        """
        # retailers dataframe
        retailers_df = self.df[['Retailer', 'Retailer ID']].drop_duplicates(subset=['Retailer'])
        #Products dataframe
        products_df = self.df[['Product', 'Price per Unit',]].drop_duplicates(subset=['Product'])
        #Regions dataframe
        regions_df = self.df[['Region']].drop_duplicates(subset=['Region'])
        #States dataframe
        states_df = self.df[['State', 'Region']].drop_duplicates(subset=['State'])
        
        #cities dataframe
        cities_df = self.df[['City', 'State']].drop_duplicates(subset=['City'])
        
        #invoice dataframe
        invoice_df = self.df[['Invoice Date', 'Product', 'Retailer', 'State', 'Region', 'City', 'Units Sold', 'Total Sales', 'Operating Profit', 'Operating Margin', 'Sales Method' ]].drop_duplicates(subset=['Invoice Date'])
        start_date = datetime.strptime('2020-01-01', '%Y-%m-%d')
        
        self.session.add_all([Retailers(name=row['Retailer'])
                         for index, row in retailers_df.iterrows()])
        self.session.add_all([Products(name=row['Product'], price=row['Price per Unit'])
                            for index, row in products_df.iterrows()])
        self.session.add_all([Regions(name=row['Region'])
                            for index, row in regions_df.iterrows()])
        self.session.add_all([States(name=row['State'], region_name=row['Region'])
                            for index, row in states_df.iterrows()])
        self.session.add_all([City(name=row['City'], state_name=row['State'])
                            for index, row in cities_df.iterrows()])
        
        self.session.add_all([Invoice(date=start_date + timedelta(days=i),
                                 retailer_id=self.session.query(Retailers.id).filter(Retailers.name == row['Retailer']).first()[0],
                                 product_id=self.session.query(Products.id).filter(Products.name == row['Product']).first()[0],
                                 region_id=self.session.query(Regions.id).filter(Regions.name == row['Region']).first()[0],
                                    state_id=self.session.query(States.id).filter(States.name == row['State']).first()[0],
                                city_id=self.session.query(City.id).filter(City.name == row['City']).first()[0],
                                 units_sold=row['Units Sold'],
                                 total_sales=row['Total Sales'],
                                 operating_profit=row['Operating Profit'],
                                 operating_margin=row['Operating Margin'],
                                 sales_method=row['Sales Method'])
                         for i, row in invoice_df.iterrows()])
        
        self.session.commit()

# Create an instance of the Deploy class
deploy = Deploy()

# Call the populate_db function to populate the database
deploy.populate_db()

# Access the session object from outside the module
session = deploy.session
