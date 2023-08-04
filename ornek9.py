
import sqlite3
from fastapi import FastAPI, Query

app = FastAPI()

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()

# "/movies" endpointini oluştur
@app.get("/movies")
async def get_movies(year: int = Query(None, description="Filter movies by year")):
    if year is not None:
        cursor.execute("SELECT year, title FROM movie WHERE year = ? ORDER BY year", (year,))
    else:
        cursor.execute("SELECT year, title FROM movie ORDER BY year")
    movies = cursor.fetchall()
    movie_list = [{"year": row[0], "title": row[1]} for row in movies]
    return {"movies": movie_list}