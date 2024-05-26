from google_auth_oauthlib.flow import InstalledAppFlow
from langchain_community.document_loaders import (
    GoogleApiClient,
)
from pathlib import Path

CREDENTIALS_PATH = Path(".credentials/credentials.json")
TOKEN_PATH = Path(".credentials/token.json")


def __write_google_api_client_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/youtube.readonly"],
    )

    creds = flow.run_local_server(port=0)

    with open(TOKEN_PATH, "w") as token_file:
        token_file.write(creds.to_json())


def get_google_api_client():
    # Check if the token file exists
    if not TOKEN_PATH.exists():
        __write_google_api_client_token()

    google_api_client = GoogleApiClient(
        credentials_path=CREDENTIALS_PATH,
        token_path=TOKEN_PATH,
    )

    return google_api_client
