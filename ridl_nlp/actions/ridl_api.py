import json
import pdb
import requests

URL = "http://localhost:4000/"
headers = {"Content-Type": "application/json"}
"""
Args:
"""

def create_account(info):
    data = {"user": info}
    sign_in_url = URL+"/api//user/signin"
    try:
        response = requests.post(sign_in_url, json=data, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
    return


if __name__ == '__main__':
    c = create_account("Test")
