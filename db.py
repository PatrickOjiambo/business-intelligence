from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create the engine

# Create the base class for declarative models
Base = declarative_base()

# Define the Retailers table
class Retailers(Base):
    """
    Retailer table
    """
    __tablename__ = 'retailers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
class Invoice(Base):
    """
    Invoice table
    """
    __tablename__ = 'invoice'
    invoice_id = Column(Integer, primary_key=True)
    retailer_id = Column(Integer, ForeignKey('retailers.id'))
    retailer = relationship("Retailers")
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Products")
    units_sold = Column(Integer)
    date = Column(String)
    total_sales = Column(Integer)


# Define the Regions table
class Regions(Base):
    """
    Regions table
    """
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Define the States table
class States(Base):
    """
    States table
    """
    __tablename__ = 'states'
    state_id = Column(Integer, primary_key=True)
    name = Column(String)
    region_id = Column(Integer, ForeignKey('regions.id'))
    region = relationship("Regions")

# Define the City table
class City(Base):
    """
    Cities table
    """
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey('states.state_id'))
    state = relationship("States")

# Define the Products table
class Products(Base):
    """
    Products table
    """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


# Define the Facts table
class Facts(Base):
    """
    Facts table
    """
    __tablename__ = 'facts'
    id = Column(Integer, primary_key=True)
    retailer_id = Column(Integer, ForeignKey('retailers.id'))
    retailer = relationship("Retailers")
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Products")
    city_id = Column(Integer, ForeignKey('city.city_id'))
    city = relationship("City")
