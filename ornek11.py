from fastapi import FastAPI, HTTPException, Query
import sqlite3
app = FastAPI()
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()
@app.get("/movies", response_model=list[dict])
async def get_movies(year: int = Query(None, description="Filmleri yıla göre filtrele")):
    if year is None:
        cursor.execute("SELECT year, title FROM movies ORDER BY year")
    else:
        cursor.execute("SELECT year, title FROM movies WHERE year = ? ORDER BY year", (year))
    movies = cursor.fetchall()
    movie_list = [{"year": year, "title": title} for year, title in movies]
    if not movie_list:
        raise HTTPException(status_code=404, detail="Belirtilen yılda film bulunamadı.")
    return movie_list