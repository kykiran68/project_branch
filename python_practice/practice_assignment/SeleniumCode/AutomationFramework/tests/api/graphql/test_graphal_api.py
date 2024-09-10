import pytest
from modules.api.graphql_api.graphql_api_class import GraphqlAPI
from base.api_base import *
from modules.api.graphql_api.graphql_api_test_data import *


class TestGraphqlAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gq = GraphqlAPI()

    def test_verify_user_list(self):
        response = self.gq.get_user_list(user_url=users_url)
        print(response.text)
        assert response.status_code == 200
        assert len(response.json()) == 10

    def test_mobiles(self):
        url = "https://api.restful-api.dev/objects"
        response = self.gq.get_method(url)
        print(response.text)

    def test_create_mobile_entry(self):
        response = self.gq.create_new_phone_entry(url=create_phone_entry_url, phone_details=phone_details)
        assert response.status_code == 200
        assert response.json()['name'] == phone_details['name']

    def test_get_user_details_with_authentication(self):
        response = self.gq.get_user_entry_with_authentication(url=auth_user_url)
        assert response.status_code == 200


