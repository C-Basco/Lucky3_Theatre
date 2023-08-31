### Log in

- Endpoint path: /token
- Endpoint method: POST

- Request shape (form):

  - username: string
  - password: string

- Response: Account information and a token
- Response shape (JSON):
  ```json
  {
    "account": {
      «key»: type»,
    },
    "token": string
  }
  ```

### Log out

- Endpoint path: /token
- Endpoint method: DELETE

- Headers:

  - Authorization: Bearer token

- Response: Always true
- Response shape (JSON):
  ```json
  true
  ```

### Get list of movies

- Endpoint path: /movies
- Endpoint method: GET
- Query parameters:

  - movie: The date to search by

- Headers:

  - Authorization: Bearer token

- Response: A list of movies
- Response shape (JSON):
  ```json
  {
      "movies": [
          {
              "movie_title": string,
              "picture_url": string,
              "description": string,
              "times": time,
              "date": date,
              "status": string,
              "trailer": third_party_api
          }
      ]
  }
  ```

### Create movie

- Endpoint path: /movies
- Endpoint method: POST

- Headers:
  <<<<<<< HEAD

  - Authorization: Bearer token

- Request body (JSON):

````json
    {
        "movie_title": string,
        "picture_url": string,
        "description": string,
        "times": time,
        "date": date,
        "status": string,
        "trailer": third_party_api
    }
    ```
=======

  - Authorization: Bearer token

- Request body (JSON):

* Request body (JSON):

  ```json
  {
      "movie": [
          {
              "movie_title": string,
              "picture_url": string,
              "description": string,
              "times": time,
              "date": date,
              "status": string,
              "trailer": third_party_api
          }
      ],
  }
  ```
>>>>>>> 22640414e282f8320363919009b28cdba74a636f

* Response: A list of movies
* Response shape (JSON):
  ```json
  {
      {
      "movie_title": string,
      "picture_url": string,
      "description": string,
      "times": time,
      "date": date,
      "status": string,
      "trailer": third_party_api
      }
  }
  ```

### Delete a movie

- Endpoint path: /movies/<int:id>
- Endpoint method: DELETE
- Query parameters:

  - movie: ID to search by

- Headers:

  - Authorization: Bearer token

- Request body (JSON):
  ```json
  {
      "movie_id": INT,
  }
  ```

### Get movie details

- Endpoint path: /movies/<int:id>
- Endpoint method: GET
- Query parameters:

  - movie: ID to search by

- Response: A list of movies
- Response shape (JSON):
  ```json
  {
      "movies": [
          {
              "movie_title": string,
              "picture_url": string,
              "description": string,
              "times": time,
              "date": date,
              "status": string,
              "trailer": third_party_api
          }
      ],
  }
  ```

### Show movie list

- Endpoint path: /movies
- Endpoint method: GET
- Query parameters:

  - movie: The date to search by

- Response: A list of movies
- Response shape (JSON):
  ```json
  {
      "movie": [
          {
              "movie_title": string,
              "picture_url": string,
              "description": string,
              "times": time,
              "date": date,
              "status": string,
              "trailer": third_party_api
          }
      ]
  }
  ```

### Show room

- Endpoint path: /rooms/<int:id>
- Endpoint method: GET
- Query parameters:

  - room: The room number

- Response: Room detail
- Response shape (JSON):
  ```json
  {
      "Room": [
          {
              "room_number": int,
              "seats": int,
              "movie": string
          }
      ],
  }
  ```

### Customer list

- Endpoint path: /customers
- Endpoint method: GET
- Query parameters:

* Response: Customer list
* Response shape (JSON):
    ```json
    {
        "Customers": [
            {
                "first_name": string,
                "last_name": string,
                "email": string
            }
        ],
    }

Done
````
