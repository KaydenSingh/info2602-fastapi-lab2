from fastapi import FastAPI
from .database import create_db_and_tables
app = FastAPI()


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/yo')
def hi():
    return 'try to get another page loaded'