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
        print(branch_df)

        self.session.add_all([Branch(name=branch) for branch in branch_df["Branch"]])
        self.session.commit()


populate = Populate()
session = populate.session
populate.populate_database()
