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
        # invoice dataframe
        # Invoice dataframe
        invoice_df = self.df[
            [
                "Invoice ID",
                "Customer type",
                "Tax 5%",
                "Quantity",
                "Date",
                "Payment",
                "cogs",
                "gross margin percentage",
                "gross income",
                "Rating",
            ]
        ]
        fact_df = self.df.drop_duplicates(subset=["Invoice ID"])
        self.session.add_all([Branch(name=branch) for branch in branch_df["Branch"]])
        self.session.add_all(
            [
                Product(name=row["Product line"], price=row["Unit price"])
                for index, row in product_df.iterrows()
            ]
        )
        self.session.add_all([City(name=city) for city in city_df["City"]])
        self.session.add_all(
            [
                Invoice(
                    invoice_id=row["Invoice ID"],
                    customer_type=row["Customer type"],
                    tax=row["Tax 5%"],
                    quantity=row["Quantity"],
                    date=row["Date"],
                    payment=row["Payment"],
                    cost_of_goods=row["cogs"],
                    gross_margin_percentage=row["gross margin percentage"],
                    gross_income=row["gross income"],
                    rating=row["Rating"],
                )
                for index, row in invoice_df.iterrows()
            ]
        )
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwwWWWWWWWWW")
        self.session.add_all(
            FactTable(
                invoice_id=row["Invoice ID"],
                branch_id=session.query(Branch.id)
                .filter(Branch.name == row["Branch"])
                .first()[0],
                product_id=session.query(Product.id)
                .filter(Product.name == row["Product line"])
                .first()[0],
                city_id=session.query(City.id)
                .filter(City.name == row["City"])
                .first()[0],
            )
            for index, row in fact_df.iterrows()
        )

        self.session.commit()


populate = Populate()
session = populate.session
populate.populate_database()
