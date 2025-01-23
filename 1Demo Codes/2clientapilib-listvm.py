import argparse
import os
import time

import googleapiclient.discovery


def list_instances(compute, project, zone):
    """Lists all instances in the given zone for the specified project.

    Args:
        compute: The Compute Engine API client.
        project: The project ID (e.g., 'my-project').
        zone: The name of the zone (e.g., 'us-central1-a').

    Returns:
        A list of instances.
    """
    result = compute.instances().list(project=project, zone=zone).execute()
    return result.get("items")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--project", help="Your Google Cloud Project ID", required=True)
    parser.add_argument("--zone", help="Compute Engine zone to list instances in", required=True)
    args = parser.parse_args()

    service = googleapiclient.discovery.build('compute', 'v1')
    instances = list_instances(service, args.project, args.zone)

    print(f"Instances found in {args.zone}:")
    for instance in instances:
        print(f"- {instance['name']}")


if __name__ == "__main__":
    main()