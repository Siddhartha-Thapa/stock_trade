from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+pyodbc://@LAPTOP-2P63RQCI/StockDB?driver=ODBC+Driver+17+for+SQL+Server"

# Example: 
# DATABASE_URL = "mssql+pyodbc://sa:yourpassword@localhost/StockDB?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
