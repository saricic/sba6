import pytest
@pytest.fixture
def car_data():
 return {"car": "mercedes", "model": 2003}
def test_sample_data(car_data):
 assert car_data["car"] == "mercedes"
 assert car_data["age"] == 2003

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),      # 2 * 3 = 6
    (5, 0, 0),       # 5 * 0 = 0
    (-4, 3, -12),    # -4 * 3 = -12
    (2.5, 4, 10.0),  # 2.5 * 4 = 10.0
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
  
