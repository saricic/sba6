import pytest
@pytest.fixture
def car_data():
 return {"car": "mercedes", "model": 2003}
def test_sample_data(car_data):
 assert car_data["car"] == "mercedes"
 assert car_data["age"] == 2003


  