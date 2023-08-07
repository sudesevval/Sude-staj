import requests

# Define the URL of the FastAPI endpoint for creating movies
url = "http://localhost:8000/movies"

# Define the movie data to be sent in the request body
data = {
    "year": 2023,
    "title": "Barbie"
}

# Make the POST request to create a new movie record
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Movie record created successfully:")
    print(response.json())
else:
    print("Failed to create movie record. Status code:", response.status_code)
