from app import app
import unittest
import json


TEST_JWT_HEADER = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": "foiclientfe"
}

TEST_JWT_CLAIMS = {
    "iss": "http://keycloak.aottech.com:8080/auth/realms/codechallenge",
    "sub": "3559e79c-7115-41c1-bb26-1a3dc54bbf5e",
    "firstname": "Test",
    "lastname": "User",
    "realm_access": {
        "roles": [
            "librarian"
        ]
    },
    "preferred_username": "user"
}


def factory_auth_header(jwt, claims):
    """Produce JWT tokens for use in tests."""
    return {'Authorization': 'Bearer ' + jwt.create_jwt(claims=claims, header=TEST_JWT_HEADER)}



class FlaskTestCase(unittest.TestCase):
    REQUEST_OBJECT = {
        'name': 'unit test1',
        'description': 'Unit test the post request status',
        'status': 'submitted',
        'createdby': 'unittest user',
        'updated': False
    }

    def test_ping(self):
        client = app.test_client(self)
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_secure(self):
        client = app.test_client(self)        
        response = client.get('requests/test')
        self.assertEqual(response.status_code, 200)    
    def test_ping_text(self):
        client = app.test_client(self)
        response = client.get('/ping')
        self.assertTrue(b'pong' in response.data)
    def test_get_requests(self):
        client = app.test_client(self)
        response = client.get('/requests/all')
        self.assertEqual(response.status_code, 200)
    def test_get_requests_text(self):
        client = app.test_client(self)
        response = client.get('/requests/all')
        self.assertTrue(b'test' in response.data)
    def test_post_requests(self):
        client = app.test_client(self)        
        response = client.post('/requests/add',json=FlaskTestCase.REQUEST_OBJECT)
        self.assertEqual(response.status_code, 200)
    def test_post_requests_text(self):
        client = app.test_client(self)
        data = {'name': 'unit test2', 'description': 'Unit test the POST request text', 'status': 'submitted', 'createdby': 'unittest user', 'updated': False}
        response = client.post('/requests/add', json=data)
        self.assertTrue(b'true' in response.data)
    def test_update_requests(self):
        client = app.test_client(self)
        data = {'name': 'unit test3', 'description': 'Unit test the PUT request text', 'status': 'submitted', 'createdby': 'unittest user', 'updated': False}
        response = client.put('/requests/10', json=data)
        self.assertEqual(response.status_code, 200)
    def test_delete_requests(self):
        client = app.test_client(self)        
        response = client.delete('/requests/12')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()