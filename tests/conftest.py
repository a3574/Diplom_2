import pytest
from objects.client import Client
from objects.order import Order
from objects.ingredient import Ingredient
import helpers as h

@pytest.fixture()
def get_client_data():
    client_name = h.get_random_name()
    client_email = h.get_random_email()
    client_password = h.get_random_password()
    client = Client(name=client_name, email=client_email, password=client_password)
    client_register_response = client.register()
    yield {'register_response': client_register_response, 'client': client}
    access_token = client_register_response.json()['accessToken']
    client.delete_info(access_token).json()
