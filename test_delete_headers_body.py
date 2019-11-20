import requests
import json


def test_delete_headers_body_json():
    url = "http://127.0.0.1:5000/app/v1/todo"

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {"title": "sample"}

    # convert dict to json by json.dumps() for body data.
    resp = requests.delete(url, data=json.dumps(payload), headers=headers)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200

    # print response full body as text
    print(resp.text)