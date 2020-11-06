import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import APP
from models import Actors, Movies, setup_db, database_path

PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndxSURuU1BILVJ4YzVvTi1oRHVfZyJ9.eyJpc3MiOiJodHRwczovL21obmQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYTMyMjYxNzA5MjA4MDA2ZWI1ZDdhYiIsImF1ZCI6ImNhc3RpbmdfYWdlbmN5IiwiaWF0IjoxNjA0Njc2MDE0LCJleHAiOjE2MDQ2ODMyMTQsImF6cCI6IjJkaHBpd09aUTFoVXlXZldhenRJdHBuNUIwZVhpYzA2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.1HsoAW4663DSrX_8I-CUC0foWrX8HljVcgidJ6KH5CGJzYuIAGqC2Y3x1KlfSvwTj7MyEg114-BP657IkmNFdfM5rptz_6XL3pX7xXcq-IASYwqlr5pfRw1Q84sLQ3VlbNYn0RcFBVMzVPHk7ZKLlwQQYMi4pOoiT33xYk7UAPURKMTeJZ_hN-hMh5Yw3pXHHcnHAczK0WrjBccc2hECnZ5gLUzw3ZPJG3ztWt2TKQ_DZqzEuTgDst9E-mNh__VrxmOJlkoEDz02gm67d9jeMF2hfmXB2Trhx1FajxStRYmaMHGbv6L7dzXlWW98RTI-YFfa183ShXAdBC6IHK7dhg'


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        APP.config['TESTING'] = True
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

    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertGreaterEqual(len(data['actors']), 0)

    def test_fail_get_actors(self):
        res = self.client().get('/actorss', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actors(self):
        res = self.client().delete('/actors/5', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)

    def test_fail_delete_actors(self):
        res = self.client().delete('/actors/4', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_actors(self):
        res = self.client().post('/actors', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_post_actors(self):
        res = self.client().post('/actors',
                                 json=self.actor
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_actors(self):
        res = self.client().patch('/actors/6', headers={
            'Authorization': 'Bearer ' + self.producer
        },
            json=self.patch_actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

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
        res = self.client().delete('/movies/3', headers={
            'Authorization': 'Bearer ' + self.producer
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 3)

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
        res = self.client().patch('/movies/4', headers={
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
