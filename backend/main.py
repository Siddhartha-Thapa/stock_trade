from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .models import User, Stock, Transaction
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the stock trade system!"}
# Create tables in the database
Base.metadata.create_all(bind=engine)
# Add CORS middleware to allow requests from React (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React app to access backend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    user = User(Username=username, Email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

stocks = [
    {"id": 1, "name": "Stock A", "price": 100, "description": "Stock A description"},
    {"id": 2, "name": "Stock B", "price": 200, "description": "Stock B description"},
]

@app.get("/stocks/")
async def get_stocks():
    return stocks

@app.get("/stocks/{id}/")
async def get_stock_details(id: int):
    stock = next((stock for stock in stocks if stock["id"] == id), None)
    if stock is None:
        return {"error": "Stock not found"}
    return stock