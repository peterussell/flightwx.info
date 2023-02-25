from dotenv import load_dotenv
import os
import urllib3
from urllib3 import HTTPResponse

from api.http_verbs import HttpVerbs
from filesystem.filesystem import Filesystem

load_dotenv()

base_url = os.environ["FAA_BASE_URL"]
http = urllib3.PoolManager()
chunk_size = 2**16    # 64kb

def _full_url(path: str) -> str:
    return f"{base_url}/{path}"

def get(path: str) -> HTTPResponse:
    # TODO: WORKING HERE - getting an SSL cert error (mabye related to python 3.10 update?)
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

# tmp - dummy fn for testing
def download_file(url: str, path: str, fs: Filesystem) -> None:
    print(f"api.download_file called. URL: {url}, path: {path}")

# tmp - uncomment when we *actually* want to download files
# def download_file(url: str, path: str, fs: Filesystem) -> HTTPResponse:
#     res: HTTPResponse = http.request(
#         HttpVerbs.GET.value,
#         url,
#         preload_content=False
#     )

#     with open(path, 'wb') as out:
#         for data in res.read(chunk_size):
#             out.write(data)

#     res.release_conn()
