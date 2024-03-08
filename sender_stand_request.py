import data
import configuration
import requests


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def update_token():
    new_token = post_new_user(data.user_body)
    data_token = new_token.json()
    return data_token["authToken"]


def post_new_client_kit(kit_body):
    new_token = update_token()
    data.headers["Authorization"] = f"Bearer {new_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.headers)
