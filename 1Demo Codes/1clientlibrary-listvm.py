# Snippet for List
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-compute


# [START compute_v1_generated_Instances_List_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import compute_v1


def sample_list():
    # Create a client
    client = compute_v1.InstancesClient()

    # Initialize request argument(s)
    request = compute_v1.ListInstancesRequest(
        project="545785800826",
        zone="us-central1-a",
    )

    # Make the request
    page_result = client.list(request=request)

    # Handle the response
    for response in page_result:
        print(response)

sample_list()
# [END compute_v1_generated_Instances_List_sync]