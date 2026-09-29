#Use pytest with fixtures/mocking for at least two important behaviors.

import pytest
from unittest.mock import patch, Mock
from extract import extract_orders, ExtractConfig, ExtractError

def test_extract_orders():
    config = ExtractConfig(url = "http://fake", max_retries = 3, backoff = 2)
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = [{"order_id": 1, "customer_id": 1, "total_amount": 100, "status": "pending"}]
    with patch("requests.get", return_value = fake_response):
        orders = extract_orders(config)
        assert orders == [{"order_id": 1, "customer_id": 1, "total_amount": 100, "status": "pending"}]

def test_extract_orders_failure(): 
    config = ExtractConfig(url = "http://fake", max_retries = 3, backoff = 2)
    with patch("requests.get", side_effect = ConnectionError("bad connection")):
        with pytest.raises(ExtractError):
            extract_orders(config)

def test_extract_orders_timeout(): 
    config = ExtractConfig(url="http://fake", max_retries=3, backoff=2)
    with patch("requests.get", side_effect=TimeoutError("request timed out")):
        with pytest.raises(ExtractError):
            extract_orders(config)