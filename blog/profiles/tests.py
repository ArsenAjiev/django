from django.test import TestCase, Client

# Create your tests here.

class ProfilesTestCase(TestCase):
    def test_get_requests(self):
        client = Client()

        response = client.get("/profiles/?query=test")
        self.assertEqual(response.status_code, 200)

        response = client.post("/profiles/", {"first_name": "First", "last_name": "Last"})
        self.assertEqual(response.status_code, 200)


