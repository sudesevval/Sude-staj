import sqlite3
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()

# Endpoint to retrieve movies
@app.get("/movies", response_model=list[dict])
async def get_movies(year: int = Query(None, description="Filter movies by year")):
    if year is not None:
        cursor.execute("SELECT year, title FROM movie WHERE year = ? ORDER BY year", (year,))
    else:
        cursor.execute("SELECT year, title FROM movie ORDER BY year")

    movies = cursor.fetchall()
    movie_list = [{"year": row[0], "title": row[1]} for row in movies]
    return movie_list

# Endpoint to create a new movie
@app.post("/movies", response_model=dict)
async def create_movie(year: int, title: str):
    # Insert the new movie record into the database
    cursor.execute("INSERT INTO movie (year, title) VALUES (?, ?)", (year, title))
    conn.commit()

    # Return the newly created movie as the response
    return {"year": year, "title": title}
