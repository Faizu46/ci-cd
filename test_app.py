from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask CI/CD App!" in response.data

