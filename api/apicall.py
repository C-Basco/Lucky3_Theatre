import requests
from keys import bearer_key
import json
from queries.pool import pool
from psycopg.errors import UniqueViolation


moviesDone = []
vids = {}
imgs = {}

url = ("https://api.themoviedb.org/3/movie/now_playing?"
       "api_key=8b258828568322bcfb9205ef95a46942"
       "&page=1"
       "&language=en-US"
       "&region=US"
       "&sort_by=popularity.desc")

headers = {"accept": "application/json", "Authorization": bearer_key}

response = requests.get(url, headers=headers)
movie_data = response.json()
movies = movie_data["results"]
movie_ids = []

if moviesDone:
    moviesDone.clear()

for i in range(12):
    i += 1
    movie_info = {
        "movie_id": movies[i]["id"],
        "movie_title": movies[i]["original_title"],
        "movie_description": movies[i]["overview"],
    }

    moviesDone.append(movie_info)
    movie_ids.append(movies[i]["id"])


for id in movie_ids:
    url2 = (f"https://api.themoviedb.org/3/movie/{id}/videos""?language=en-US")
    headers = {"accept": "application/json", "Authorization": bearer_key}
    response = requests.get(url2, headers=headers)
    data = response.json()
    for vid in data["results"]:
        id2 = data["id"]
        if vid["name"] == "Official Trailer" and vid["type"] == "Trailer":
            vids[id2] = vid


for id in movie_ids:
    url3 = f"https://api.themoviedb.org/3/movie/{id}/images"

    headers = {"accept": "application/json", "Authorization": bearer_key}

    response = requests.get(url3, headers=headers)
    data = response.json()
    movie_images = data["posters"][0]
    id2 = id
    imgs[id2] = movie_images["file_path"]

for movie in moviesDone:
    if movie["movie_id"] in imgs.keys():
        movie[
            "image"
        ] = f"https://image.tmdb.org/t/p/w500{imgs[movie['movie_id']]}"
    if movie["movie_id"] in vids.keys():
        movie["trailer"] = vids[movie["movie_id"]]

    title = movie["movie_title"]
    description = movie["movie_description"]
    image = movie["image"]
    if "trailer" in movie:
        trailer = movie["trailer"]
        trailer_json = json.dumps(trailer)  # dumps for NOT NULL
    else:
        trailer = None
        trailer_json = None

    print([title, description, image, trailer_json])
    try:
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                          INSERT INTO movies(title,
                          description,
                          image,
                          trailer)
                          VALUES(%s, %s, %s, %s)
                          RETURNING id, title, description, image, trailer;
                          """,
                    [title, description, image, trailer_json],
                )
    except UniqueViolation:
        print("Movie already exists")
    except Exception as e:
        print(type(e))


upcoming_moviesDone = []
upcoming_vids = {}
upcoming_imgs = {}

upcoming_url = ("https://api.themoviedb.org/3/movie/upcoming?"
                "api_key=8b258828568322bcfb9205ef95a46942"
                "&page=1"
                "&language=en-US"
                "&region=US&sort_by=popularity.desc")
response2 = requests.get(upcoming_url, headers=headers)

upcoming_movie_data = response2.json()
upcoming_movies = upcoming_movie_data["results"]
upcoming_movie_ids = []

if upcoming_moviesDone:
    upcoming_moviesDone.clear()

for i in range(12):
    movie_info = {
        "movie_id": upcoming_movies[i]["id"],
        "movie_title": upcoming_movies[i]["original_title"],
        "movie_description": upcoming_movies[i]["overview"],
    }

    upcoming_moviesDone.append(movie_info)
    upcoming_movie_ids.append(upcoming_movies[i]["id"])


for id in upcoming_movie_ids:
    url2 = f"https://api.themoviedb.org/3/movie/{id}/videos?language=en-US"
    headers = {"accept": "application/json", "Authorization": bearer_key}
    response = requests.get(url2, headers=headers)
    data = response.json()
    for vid in data["results"]:
        id2 = data["id"]
        if vid["name"] == "Official Trailer" and vid["type"] == "Trailer":
            upcoming_vids[id2] = vid


for id in upcoming_movie_ids:
    url3 = f"https://api.themoviedb.org/3/movie/{id}/images"

    headers = {"accept": "application/json", "Authorization": bearer_key}

    response = requests.get(url3, headers=headers)
    data = response.json()
    movie_images = data["posters"][0]
    id2 = id
    upcoming_imgs[id2] = movie_images["file_path"]

for movie in upcoming_moviesDone:
    if movie["movie_id"] in upcoming_imgs.keys():
        movie[
            "image"
        ] = (f"https://image.tmdb.org/t/p/w500"
             f"{upcoming_imgs[movie['movie_id']]}")
    if movie["movie_id"] in upcoming_vids.keys():
        movie["trailer"] = upcoming_vids[movie["movie_id"]]

    title = movie["movie_title"]
    description = movie["movie_description"]
    image = movie["image"]
    if "trailer" in movie:
        trailer = movie["trailer"]
        trailer_json = json.dumps(trailer)  # dumps for NOT NULL
    else:
        trailer = None
        trailer_json = None

    print([title, description, image, trailer_json])
    try:
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                        INSERT INTO upcoming_movies
                        (title,
                        description,
                        image,
                        trailer)
                        VALUES(%s, %s, %s, %s)
                        RETURNING id, title, description, image, trailer;
                          """,
                    [title, description, image, trailer_json],
                )
    except UniqueViolation:
        print("Movie already exists")
    except Exception as e:
        print(type(e))
