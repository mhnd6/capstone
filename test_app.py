import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app
from models import Actors, Movies, setup_db, database_path

PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndxSURuU1BILVJ4YzVvTi1oRHVfZyJ9.eyJpc3MiOiJodHRwczovL21obmQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYTMyMjYxNzA5MjA4MDA2ZWI1ZDdhYiIsImF1ZCI6ImNhc3RpbmdfYWdlbmN5IiwiaWF0IjoxNjA0NzQ0NzI0LCJleHAiOjE2MDQ3NTE5MjQsImF6cCI6IjJkaHBpd09aUTFoVXlXZldhenRJdHBuNUIwZVhpYzA2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.o6M8UuvifRjL94dnPI9dIgikC4989NUgue4635Qk8vaFWqfmjMSgeocJ0nxAX2jNmClaUvEqUqLFuZm9NldoTXocnORhkl4CPLxwCPCTD-77nuhRUBa00yPrdmEzr0p7D60lMrnr3dwhdlq4jbinl-vH5tKRlg1jqR3m2uuBbbjE7hllVEn6QK3-wy3tQtiaMYTEXn87qsUJ2ZNV0qqbDgPc8QzrLTuAc2ZvcaIxg9Q8GBcgW9fMgCq0VAzlKcv6aj7s12z3HMs75I5ertOLaCVe5-z0bw3IrqkCGT_knPQJyyZ3ekdunauoQx8PKWiSDl2K7UZ-YzEfQ0gloacbMA'


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        app.config['TESTING'] = True
        self.client = self.app.test_client
        self.producer = PRODUCER_TOKEN
        self.database_path = database_path

        self.actor = {
            "name": "Trump",
            "age": 20,
            "gender": "male"
        }

        self.patch_actor = {
            "name": "Loly"
        }

        self.movie = {
            "title": "Taken",
            "release_date": "2007"
        }

        self.patch_movie = {
            "title": "The hunt",
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """ get actor test """

    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertGreaterEqual(len(data['actors']), 0)

    """ fail get actors with wrong endpoint"""

    def test_fail_get_actors(self):
        res = self.client().get('/actorss', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    """ delete actor test """

    def test_delete_actors(self):
        res = self.client().delete('/actors/8', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 8)

    """ fail delete actor test with not found"""

    def test_fail_delete_actors(self):
        res = self.client().delete('/actors/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    """ post actor test """

    def test_post_actors(self):
        res = self.client().post('/actors', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    """ fail post actor with no authintication"""

    def test_fail_post_actors(self):
        res = self.client().post('/actors',
                                 json=self.actor
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    """ update actor test """

    def test_patch_actors(self):
        res = self.client().patch('/actors/6', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.patch_actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    """ fail update actor not found"""

    def test_fail_patch_actors(self):
        res = self.client().patch('/actors/5', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.patch_actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertGreaterEqual(len(data['movies']), 0)

    def test_fail_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movies(self):
        res = self.client().delete('/movies/5', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)

    def test_fail_delete_movies(self):
        res = self.client().delete('/movies/3', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_movies(self):
        res = self.client().post('/movies', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.movie
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_post_movies(self):
        res = self.client().post('/movies',
                                 json=self.movie
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movies(self):
        res = self.client().patch('/movies/1', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.patch_movie
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_patch_movies(self):
        res = self.client().patch('/movies/4',
                                  json=self.patch_movie
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
