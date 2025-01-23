from google.cloud import bigquery
from google.oauth2 import service_account

# Replace with the actual path to your service account key file
SERVICE_ACCOUNT_FILE = '/home/skillupgcp2023/gcplearning2024-defaultcompute.json' 
SCOPES = ['https://www.googleapis.com/auth/bigquery'] 

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

client = bigquery.Client(project='gcplearning2024', credentials=credentials)

query = """
SELECT
  year,
  COUNT(1) as num_babies
FROM
  `publicdata.samples.natality`
WHERE
  year > 2000
GROUP BY
  year
"""

query_job = client.query(query)  # Make an API request.

results = query_job.result()  # Wait for the job to complete.

# Print the results
for row in results:
    print(f"{row.year}: {row.num_babies}")