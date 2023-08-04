import sqlite3
from fastapi import FastAPI, HTTPException, Query
from fastapi import FastAPI
app = FastAPI()
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()
@app.get("/movies", response_model=list[dict])
async def get_movies(year: int = Query(None, description="Filter movies by year")):

    cursor.execute("SELECT year, title FROM movie ORDER BY year")
    movies = cursor.fetchall()
    movie_list = [{"year": year, "title": title} for year, title in movies]
    return movie_list
