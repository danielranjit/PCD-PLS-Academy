
import argparse

import requests


METADATA_URL = "http://metadata.google.internal/computeMetadata/v1/"
METADATA_HEADERS = {"Metadata-Flavor": "Google"}
SERVICE_ACCOUNT = "default"


def get_access_token() -> str:
    """
    Retrieves access token from the metadata server.

    Returns:
        The access token.
    """
    url = f"{METADATA_URL}instance/service-accounts/{SERVICE_ACCOUNT}/token"

    # Request an access token from the metadata server.
    r = requests.get(url, headers=METADATA_HEADERS)
    r.raise_for_status()

    # Extract the access token from the response.
    access_token = r.json()["access_token"]

    return access_token


def list_buckets(project_id: str, access_token: str) -> dict:
    """
    Calls Storage API to retrieve a list of buckets.

    Args:
        project_id: name of the project to list buckets from.
        access_token: access token to authenticate with.

    Returns:
        Response from the API.
    """
    url = "https://www.googleapis.com/storage/v1/b"
    params = {"project": project_id}
    headers = {"Authorization": f"Bearer {access_token}"}

    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()

    return r.json()


def main(project_id: str) -> None:
    """
    Retrieves access token from metadata server and uses it to list
    buckets in a project.

    Args:
        project_id: name of the project to list buckets from.
    """
    access_token = get_access_token()
    buckets = list_buckets(project_id, access_token)
    print(buckets)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project_id", help="Your Google Cloud project ID.")

    args = parser.parse_args()

    main(args.project_id)