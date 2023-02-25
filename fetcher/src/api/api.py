from dotenv import load_dotenv
import os
import requests
from requests import Response

load_dotenv()

base_url = os.environ["FAA_BASE_URL"]
chunk_size = 2**16    # 64kb


def get(path: str) -> Response:
    return requests.get(_full_url(path), verify=False)


# tmp - dummy fn for testing
# def download_file(url: str, path: str, fs: Filesystem) -> None:
#     print(f"api.download_file called. URL: {url}, path: {path}")

# tmp - uncomment when we *actually* want to download files
def download_file(url: str, filename: str) -> None:
    """
    Downloads the file at URL and saves it to filename
    """
    with requests.get(url, stream=True) as req:
        req.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size):
                f.write(chunk)


def _full_url(path: str) -> str:
    return f"{base_url}/{path}"
