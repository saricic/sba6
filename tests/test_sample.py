import pytest
@pytest.fixture
def sample_data():
 return {"name": "Alice", "age": 30}
def test_sample_data(sample_data):
 assert sample_data["name"] == "Alice"
 assert sample_data["age"] == 30

 @pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
 def test_add_param(a, b, expected):
  assert add(a, b) == e

  name: Python
  Test
  Automation
  on:
  push:
  branches:
  - main
  pull_request:

 jobs:
 test:
 runs - on: ubuntu - latest
 steps:
 - name: Checkout
 repository
 uses: actions / checkout @ v3
 - name: Set
 up
 Python
 uses: actions / setup - python @ v4
 with:
  python - version: "3.10"
 - name: Install
 dependencies
 run: pip
 install
 pytest
 - name: Run
 tests
 run: pytest