from dotenv import load_dotenv
import json
import os
import urllib3
from urllib3 import HTTPResponse

from api.http_verbs import HttpVerbs

load_dotenv()

base_url = os.environ["FAA_BASE_URL"]
http = urllib3.PoolManager()

def _full_url(path: str) -> str:
    return f"{base_url}/{path}"

def get(path: str) -> HTTPResponse:
    return http.request(
        HttpVerbs.GET.value,
        _full_url(path),
        headers={
            "Content-Type": "application/json"
        }
    )

def post(path: str, body: str) -> HTTPResponse:
    return http.request(
        HttpVerbs.POST.value,
        _full_url(path),
        body=body
    )
