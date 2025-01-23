import argparse
from typing import List

from google.cloud import storage    


def create_client() -> storage.Client:
    """
    Construct a client object for the Storage API using the
    application default credentials.

    Returns:
        Storage API client object.
    """
    # Construct the service object for interacting with the Cloud Storage API -
    # the 'storage' service, at version 'v1'.
    # Authentication is provided by application default credentials.
    # When running locally, these are available after running
    # `gcloud auth application-default login`. When running on Compute
    # Engine, these are available from the environment.
    return storage.Client()


def list_buckets(client: storage.Client, project_id: str) -> List[storage.Bucket]:
    """
    Retrieve bucket list of a project using provided client object.


    Args:
        client: Storage API client object.
        project_id: name of the project to list buckets from.

    Returns:
        List of Buckets found in the project.
    """
    buckets = client.list_buckets()
    return list(buckets)


def main(project_id: str) -> None:
    client = create_client()
    buckets = list_buckets(client, project_id)
    print(buckets)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project_id", help="Your Google Cloud Project ID.")

    args = parser.parse_args()

    main(args.project_id)