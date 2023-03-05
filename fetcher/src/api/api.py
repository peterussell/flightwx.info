from dotenv import load_dotenv
import os
import requests
from requests import Response

load_dotenv()

base_url = os.environ["FAA_BASE_URL"]
chunk_size = 2**16    # 64kb


def get(path: str) -> Response:
    return requests.get(_full_url(path), verify=False)


def download_file(url: str, file_path: str) -> None:
    """
    Downloads the file at URL and saves to file_path
    """
    with requests.get(url, stream=True) as req:
        req.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in req.iter_content(chunk_size):
                f.write(chunk)


def _full_url(path: str) -> str:
    return f"{base_url}/{path}"
