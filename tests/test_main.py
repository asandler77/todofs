import pytest 
from main import app # Import the Flask app instance from your main file

@pytest.fixture
def client():
    # Set up the test client for the Flask app
    app.testing = True
    return app.test_client()

def test_post_api_data(client):
    # Define the data to send with the POST request
    item = {
        "item": "milk"
        }

    # Send a POST request to the endpoint with JSON data
    response = client.post('/set/item', json=item)

    # Assert the status code is 200 OK
    assert response.status_code == 200

    # Assert the response JSON contains the expected data
    # print(response)

    response_json = response.get_json()
    print("item ---", item)
    print("response ---", response_json)
    assert response_json['status'] == 'success'
    assert response_json['received_item'] == item
