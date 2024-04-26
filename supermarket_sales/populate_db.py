#!/usr/bin/env python
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker
from db import Base, Branch, Product, City, Invoice, FactTable


class Populate:
    """
    Class to populate db
    """

    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///supermarket.db", echo=True)
        self.df = pd.read_csv("super.csv")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def populate_database(self):
        """
        Populate the database
        """
        # branch dataframe

        branch_df = self.df[["Branch"]].drop_duplicates(subset=["Branch"])
        # Product dataframe
        product_df = self.df[["Product line", "Unit price"]].drop_duplicates(
            subset=["Product line"]
        )
        # city dataframe
        city_df = self.df[["City"]].drop_duplicates(subset=["City"])
        self.session.add_all([Branch(name=branch) for branch in branch_df["Branch"]])
        self.session.add_all(
            [
                Product(name=row["Product line"], price=row["Unit price"])
                for index, row in product_df.iterrows()
            ]
        )
        self.session.add_all([City(name=city) for city in city_df["City"]])
        self.session.commit()


populate = Populate()
session = populate.session
populate.populate_database()
