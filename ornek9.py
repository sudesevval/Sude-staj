import sqlite3
from fastapi import FastAPI, HTTPException, Query
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()
class Movie(BaseModel):
    year: int
    title: str
@app.get("/movies", response_model=list[dict])
async def get_movies(year: int = Query(None, description="Filter movies by year")):
    if year is not None:
        cursor.execute("SELECT year, title FROM movie WHERE year = ? ORDER BY year", (year,))
    else:
        cursor.execute("SELECT year, title FROM movie ORDER BY year")

    movies = cursor.fetchall()
    movie_list = [{"year": title, "title": year} for year, title in movies]
    return movie_list

@app.post("/movies", response_model=Movie)
async def create_movie(movie: Movie):
    # Extract year and title from the request body
    year = movie.year
    title = movie.title

    # Execute SQL query to insert the new movie record
    cursor.execute("INSERT INTO movie (year, title) VALUES (?, ?)", (year, title))
    conn.commit()

    # Return the created movie as the response
    return {"year": year, "title": title}