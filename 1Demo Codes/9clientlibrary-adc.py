from google.cloud import bigquery

#query a public dataset available in BigQuery
query = """
SELECT
  year,
  COUNT(1) as num_babies
FROM
  publicdata.samples.natality
WHERE
  year > 2000
GROUP BY
  year
"""

#no credentials provided so will use ADC
client = bigquery.Client()

print(client.query(query).to_dataframe())