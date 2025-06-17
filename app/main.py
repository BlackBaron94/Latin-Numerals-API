from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Latin Numerals API")

# Συνδέεις routes
app.include_router(router)