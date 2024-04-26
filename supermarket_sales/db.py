#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Branch(Base):
    __tablename__ = 'branch'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Invoice(Base):
    __tablename__ = 'invoice'
    invoice_id = Column(String, primary_key=True)
    customer_type = Column(String)
    tax = Column(Float)
    quantity = Column(Integer)
    date = Column(String)
    
    payment = Column(String)
    cost_of_goods = Column(Float)
    gross_margin_percentage = Column(Float)
    gross_income = Column(Float)
    rating = Column(Float)

class FactTable(Base):
    __tablename__ = 'fact_table'
    id = Column(Integer, primary_key=True)
    branch_id = Column(Integer, ForeignKey('branch.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    city_id = Column(Integer, ForeignKey('city.id'))
    invoice_id = Column(Integer, ForeignKey('invoice.invoice_id'))

    branch = relationship('Branch', backref='fact_table')
    product = relationship('Product', backref='fact_table')
    city = relationship('City', backref='fact_table')
    invoice = relationship('Invoice', backref='fact_table')