import requests


# def get_method(url):
#     headers = {}
#     payload = {}
#     print("URL :", url)
#     response = requests.request("GET", url, headers=headers, data=payload)
#     return response


class APIMethods:

    def get_method(self, url, headers=None, payload=None):
        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    def post_method(self, url, headers=None, payload=None):
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def put_method(self, url, headers=None, payload=None):
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    def patch_method(self, url, headers=None, payload=None):
        response = requests.request("PATCH", url, headers=headers, data=payload)
        return response
