from fastapi import FastAPI
import sqlite3
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()
app = FastAPI()
@app.get("/movies")
async def get_movies():
    cursor.execute("SELECT year, title FROM movie ORDER BY year")
    movies = cursor.fetchall()
    movie_list = [{"year": year, "title": title} for year, title in movies]
    return movie_list

