import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors, db
from auth.auth import requires_auth, AuthError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def home():
        return 'App is running'

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):

        try:
            selection = Actors.query.order_by(Actors.id).all()
            total_actors = len(selection)

            return jsonify({
                'success': True,
                "actors": [actor.format() for actor in selection],
                "total": total_actors
            }), 200
        except Exception:
            abort(404)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        try:
            selection = Actors.query.get(actor_id)
            selection.delete()
        except Exception:
            abort(404)

        return jsonify({
            "success": True,
            "deleted": selection.id,
        }), 200

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        body = request.get_json()

        actorName = body.get('name', None)
        actorAge = body.get('age', None)
        actorGender = body.get('gender', None)

        try:
            newActor = Actors(
                name=actorName,
                age=actorAge,
                gender=actorGender
            )

            newActor.insert()
        except Exception:
            abort(422)

        return jsonify({
            "success": True,
            "created": newActor.id
        }), 200

    @app.route("/actors/<int:actor_id>", methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        body = request.get_json()

        try:
            actor = Actors.query.get(actor_id)

            actor.name = body.get('name', actor.name)
            actor.age = body.get('age', actor.age)
            actor.gender = body.get('gender', actor.gender)

            actor.update()
        except Exception:
            abort(404)

        return jsonify({
            "success": True,
            "actor": actor.format()
        }), 200

    @app.route("/movies")
    @requires_auth('get:movies')
    def get_movies(payload):

        try:
            selection = Movies.query.order_by(Movies.id).all()
            total_movies = len(selection)
        except Exception:
            abort(404)

        return jsonify({
            'success': True,
            "movies": [movie.format() for movie in selection],
            "total": total_movies
        }), 200

    @app.route("/movies/<int:movie_id>", methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):

        try:
            selection = Movies.query.get(movie_id)
            selection.delete()
        except Exception:
            abort(404)

        return jsonify({
            "success": True,
            "deleted": selection.id,
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        body = request.get_json()

        movieTitle = body.get('title', None)
        movieRelease = body.get('release_date', None)

        try:
            newMovie = Movies(
                title=movieTitle,
                release_date=movieRelease
            )

            newMovie.insert()
        except Exception:
            abort(422)

        return jsonify({
            "success": True,
            "created": newMovie.id
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        body = request.get_json()

        try:
            selection = Movies.query.get(movie_id)

            selection.title = body.get('title', selection.title)
            selection.release_date = body.get(
                'release_date', selection.release_date)

            selection.update()
        except:
            abort(404)

        return jsonify({
            "success": True,
            "movie": selection.format()
        }), 200

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'nor found'
        }), 404

    @app.errorhandler(422)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable entity'
        }), 422

    '''
    error handler for AuthError 
    '''
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=8080, debug=True)
