import os
from fastapi import FastAPI
x = os.getenv("SUPABASE_URL")
y = os.getenv("SUPABASE_KEY")

app = FastAPI()

@app.get("/")
def main_route():
    return {'message': 'Hello main route'}

@app.get("/health")
def health_check():
    return {'message': 'Healthy'}