from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "Users"
    UserID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50), unique=True, nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    CreatedAt = Column(DateTime, default=datetime.now)

class Stock(Base):
    __tablename__ = "Stocks"
    StockID = Column(Integer, primary_key=True, index=True)
    Symbol = Column(String(10), nullable=False)
    CompanyName = Column(String(100))
    CurrentPrice = Column(Float)
    LastUpdated = Column(DateTime, default=datetime.now)

class Transaction(Base):
    __tablename__ = "Transactions"
    TransactionID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"))
    StockID = Column(Integer, ForeignKey("Stocks.StockID"))
    TransactionType = Column(String(10))
    Quantity = Column(Integer)
    PricePerStock = Column(Float)
    TransactionDate = Column(DateTime, default=datetime.now)
