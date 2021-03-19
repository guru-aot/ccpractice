from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    REQUEST_OBJECT = {
        'name': 'unit test1',
        'description': 'Unit test the post request status',
        'status': 'submitted',
        'createdby': 'unittest user',
        'updated': False
    }

    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/ping')
        self.assertEqual(response.status_code, 200)
    def test_ping_text(self):
        tester = app.test_client(self)
        response = tester.get('/ping')
        self.assertTrue(b'pong' in response.data)
    def test_get_requests(self):
        tester = app.test_client(self)
        response = tester.get('/requests/all')
        self.assertEqual(response.status_code, 200)
    def test_get_requests_text(self):
        tester = app.test_client(self)
        response = tester.get('/requests/all')
        self.assertTrue(b'test' in response.data)
    def test_post_requests(self):
        tester = app.test_client(self)        
        response = tester.post('/requests/add',json=FlaskTestCase.REQUEST_OBJECT)
        self.assertEqual(response.status_code, 200)
    def test_post_requests_text(self):
        tester = app.test_client(self)
        data = {'name': 'unit test2', 'description': 'Unit test the POST request text', 'status': 'submitted', 'createdby': 'unittest user', 'updated': False}
        response = tester.post('/requests/add', json=data)
        self.assertTrue(b'true' in response.data)
    def test_update_requests(self):
        tester = app.test_client(self)
        data = {'name': 'unit test3', 'description': 'Unit test the PUT request text', 'status': 'submitted', 'createdby': 'unittest user', 'updated': False}
        response = tester.put('/requests/10', json=data)
        self.assertEqual(response.status_code, 200)
    def test_delete_requests(self):
        tester = app.test_client(self)        
        response = tester.delete('/requests/12')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()