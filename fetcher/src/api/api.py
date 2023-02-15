import os
from dotenv import load_dotenv
import urllib3
import json
from urllib3 import HTTPResponse

from api.http_verbs import HttpVerbs

load_dotenv()

base_url = os.environ["FAA_BASE_URL"]
http = urllib3.PoolManager()

def _full_url(path: str) -> str:
    return f"{base_url}/{path}"

def _get_response_body(response: HTTPResponse) -> any:
    # return json.loads(response.data.decode("utf-8"))
    return response.data.decode("utf-8")

def get(path: str) -> None:
    print(f"Getting path {base_url}/{path}")
    res: HTTPResponse = http.request(HttpVerbs.GET.value, _full_url(path))

    print(f"API response status: {res.status}")
    print("Response data")
    print(_get_response_body(res))
