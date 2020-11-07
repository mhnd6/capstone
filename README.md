# Casting Agency API

## Full Stack Nano - Final Project (Capstone)

An API responsible for managing Casting Agency company
Wich allows them to assign actors or create movies and retrieve them
The application must:

1. Do CRUD operations on both actors and movies.
2. Allow only registered users to view actors and movies.
3. Allow only authorized roles to do certain things.

Note: The frontend isn't implemented yet make sure to test the app using curl or postman.

## Application Heroku Link

['https://capstone-mhnd.herokuapp.com/']

- Roles:
  - Casting Assistant
    - Can view actors and movies
  - Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
  - Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

## Getting started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the capstone.psql file provided:

```bash
psql capstone < capstone.psql
```

## Running the server

ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## API Reference

### Getting Started

- Base URL: At present this app doesn't have frontend. The backend app is hosted at the default, https://capstone-mhnd.herokuapp.com/.
- Authentication: This application require authentication, the tokens provided inside postman collection.

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error: 404,
    "message": "not found
}
```

The API will return four error types when request fail:

- 400: Bad Request
- 404: Not Found
- 422: Not Processable
- AuthError: Unauthorized

### Endpoints

#### GET /actors

- General:
  - Return all available actors, and success value.
- Parameters: None.
- Sample: curl -H 'Accept: application/json' -H "Authorization: Bearer \${TOKEN}" https://capstone-mhnd.herokuapp.com/actors

```
{
    "actors": [
        {
            "age": 30,
            "gender": "Male",
            "id": 1,
            "name": "salman"
        },
        {
            "age": 30,
            "gender": "Male",
            "id": 2,
            "name": "ahmed"
        }
    ],
    "success": true,
    "total": 2
}
```

#### DELETE /actors/{actor_id}

- General:
  - Delete actor by actor id, and return the deleted actor id, success value.
- Parameters:
  - actor id
- Sample: curl -H 'Accept: application/json' -H "Authorization: Bearer \${TOKEN}" https://capstone-mhnd.herokuapp.com/actors/3 -X DELETE

```
{
    "deleted": 2,
    "success": true
}
```

#### POST /actors

- General:
  - create a new actor.
- Parameters:
  - name
  - age
  - gender
- Sample: curl -d '{"name":"kiki", "age":43, "gender":"male"}' -H "Content-Type: application/json" -X POST https://capstone-mhnd.herokuapp.com/actors

```
{
    "created": 3,
    "success": true
}
```

#### PATCH /actors

- General:
  - Update an excisting actor.
- Parameters:
  - name
  - age
  - gender
- Sample: curl -d '{"name":"kiki", "age":43, "gender":"male"}' -H "Content-Type: application/json" -X POST https://capstone-mhnd.herokuapp.com/actors/2

```
{
    "actor": {
        "age": 20,
        "gender": "Male",
        "id": 3,
        "name": "chack"
    },
    "success": true
}
```

#### GET /movies

- General:
  - Return all available movies, and success value.
- Parameters: None.
- Sample: curl -H 'Accept: application/json' -H "Authorization: Bearer \${TOKEN}" https://capstone-mhnd.herokuapp.com/movies

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "2020",
            "title": "Anime"
        }
    ],
    "success": true,
    "total": 1
}
```

#### DELETE /movies/{movie_id}

- General:
  - Delete movie by movie id, and return the deleted movie id, success value.
- Parameters:
  - movie id
- Sample: curl -H 'Accept: application/json' -H "Authorization: Bearer \${TOKEN}" https://capstone-mhnd.herokuapp.com/movies/3 -X DELETE

```
{
    "deleted": 2,
    "success": true
}
```

#### POST /movies

- General:
  - create a new movie.
- Parameters:
  - title
  - releade_date
- Sample: curl -d '{"title":"kiki", "release_date":"2000"}' -H "Content-Type: application/json" -X POST https://capstone-mhnd.herokuapp.com/movies

```
{
    "created": 3,
    "success": true
}
```

#### PATCH /movies

- General:
  - Update an excisting movie.
- Parameters:
  - title
  - releade_date
- Sample: curl -d '{"title":"kiki", "release_date":"2000"}' -H "Content-Type: application/json" -X POST https://capstone-mhnd.herokuapp.com/movies/2

```
{
    "movie": {
        "id": 1,
        "release_date": "1999",
        "title": "Anime"
    },
    "success": true
}
```

## Testing

Note: If you want to test it locally please replace the DB URL with your local DB URL.

To run the tests, run

```
python test_app.py
```

Or import the postman collection file provided and run it in postman.
