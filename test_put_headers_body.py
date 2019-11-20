import requests
import json


def test_put_headers_body_json():
    url = "http://127.0.0.1:5000/app/v1/todo"

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {"title": "sample", "done": "True"}

    # convert dict to json by json.dumps() for body data.
    resp = requests.put(url, data=json.dumps(payload), headers=headers)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201

    # print response full body as text
    print(resp.text)