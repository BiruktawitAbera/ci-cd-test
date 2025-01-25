# test_app.py
import pytest
from simple_flask_app.app import app

 # Import your Flask app

# Test the homepage route
def test_homepage():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200  # Ensure the response is OK
        assert b"Simple Flask Application" in response.data  # Check if specific content is on the page

# Test a basic addition function
def test_example():
    assert 1 + 1 == 2

# You can add more tests for other routes and functionalities here
