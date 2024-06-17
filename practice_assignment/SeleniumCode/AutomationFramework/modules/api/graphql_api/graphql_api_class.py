#from base.api_base import APIMethods
import json

from base.api_base import *
from .graphql_api_test_data import *


class GraphqlAPI(APIMethods):

    def get_user_list(self, user_url):
        print("URL :", user_url)
        response = self.get_method(url=user_url)
        return response

    def create_new_phone_entry(self, url, phone_details):
        payload = json.dumps(phone_details)
        headers = {
        'Content-Type': 'application/json'
    }
        response = self.post_method(url, headers=headers, payload=payload)
        return response

    def get_user_entry_with_authentication(self, url):
        access_token = "a6541a8634555f42ce8274740ac1859640bed540ff30a9f96aa90e5513bdfdb7"
        headers = {'Authorization': f"Bearer {access_token}"}
        response = self.get_method(url=url, headers=headers)
        return response



