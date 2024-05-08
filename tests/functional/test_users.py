from conftest import test_client, new_user
from pathlib import Path
from faker import Faker

resources = Path(__file__).parent / "resources"

fake = Faker() 

def test_post_users(new_user):
    username = fake.name()
    email = fake.email()
    password = '123'
    payload = {
        "name": username,
        "password": password,
        "email": email
    }
    response = test_client.post("/auth/signup", data=payload)
    assert response.status_code == 200
    


# def test_login(test_client):
#     username = 'jacob'
#     password = '123'
#     payload = {
#         "name": username,
#         "password": password,
#     }
#     response = test_client.post("/auth/login", data=payload)
#     assert response.status_code == 200

# def test_access_session(test_client):
#     with test_client:
#         test_client.post("/auth/login", data={"name": "dizhu"})
#         # session is still accessible
#         assert session["user_id"] == 1

#     # session is no longer accessible

# def test_signup_redirect(test_client):
#     response = test_client.get("/auth/signup")
#     # Check that there was one redirect response.
#     assert len(response.history) == 1
#     # Check that the second request was to the index page.
#     assert response.request.path == "/auth/login"


# def test_home_page(test_client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/' page is requested (GET)
#     THEN check that the response is valid
#     """
#     response = test_client.get('/')
#     assert response.status_code == 200
#     assert b"About" in response.data
#     assert b"Login" in response.data
#     assert b"Signup" in response.data
#     response = test_client.post('/')
#     assert response.status_code == 405
#     assert b"About" not in response.data


# def test_404_page(test_client):   
#     response = test_client.get('/nothing')  # 传入目标 URL
#     assert response.status_code == 404
#     assert b"Ouch, Wrong Page." in response.data


# def test_profile_page(test_client):
#     response = test_client.get('/auth/protected')
#     assert response.status_code == 401
#     assert b"Unauthorized" in response.data

# def test_logout(test_client):
#     response = test_client.get("auth/logout")
#     assert response.status_code == 401

# def test_protected(test_client):
#     response = test_client.get("/auth/protected")
#     assert response.status_code == 401