import requests
import json


def test_get_headers_json():
    url = "http://127.0.0.1:5000/app/v1/todo"

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # convert dict to json by json.dumps() for body data.
    resp = requests.get(url)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200

# print response full body as text
    print(resp.text)