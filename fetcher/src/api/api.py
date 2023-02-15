import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.environ["FAA_BASE_URL"]

def get(path: str) -> None:
    print(f"Getting path {base_url}/{path}")
