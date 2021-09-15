import pytest
from rest_framework import status

from rest_framework.test import APIClient


@pytest.mark.django_db
class TestNotessApi:
    def setup_method(self):
        self.client = APIClient()

    def test_notes_api(self):
        response = self.client.get("/api/notes/")
        assert response.status_code == status.HTTP_200_OK