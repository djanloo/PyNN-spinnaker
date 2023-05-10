import nmpi
import hbp_service_client
client = nmpi.Client(
                    username="djanloo", password="ebra_in_758", 
                    # token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJfNkZVSHFaSDNIRmVhS0pEZDhXcUx6LWFlZ3kzYXFodVNJZ1RXaTA1U2k0In0.eyJleHAiOjE2ODQzMzkyODcsImlhdCI6MTY4MzczNDQ4NywiYXV0aF90aW1lIjoxNjgzNzM0MzQ0LCJqdGkiOiI5NzJkOTY0ZS0wOGQ5LTQwNjMtYmNiOC00NTIxM2ZkMGZlZGIiLCJpc3MiOiJodHRwczovL2lhbS5lYnJhaW5zLmV1L2F1dGgvcmVhbG1zL2hicCIsImF1ZCI6WyJqdXB5dGVyaHViLWpzYyIsInh3aWtpIiwidGVhbSIsImdyb3VwIl0sInN1YiI6IjBmYTk0YWM0LWU0YWEtNDAzOS05YTY0LTI4ODk1ZDk5ZDEyZCIsInR5cCI6IkJlYXJlciIsImF6cCI6Imp1cHl0ZXJodWIiLCJzZXNzaW9uX3N0YXRlIjoiNjMyNTlmYWQtN2IyMC00MjE2LWI3OWMtMjY3MDA2MDkzOGI3IiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL2p1cHl0ZXJodWIuYXBwcy5qc2MuaGJwLmV1LyIsImh0dHBzOi8vbGFiLmVicmFpbnMuZXUvIiwiaHR0cHM6Ly9sYWIuanNjLmVicmFpbnMuZXUvIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyJdfSwic2NvcGUiOiJjb2xsYWIuZHJpdmUgcHJvZmlsZSBvZmZsaW5lX2FjY2VzcyBjbGIud2lraS53cml0ZSBlbWFpbCByb2xlcyBvcGVuaWQgZ3JvdXAgY2xiLndpa2kucmVhZCB0ZWFtIiwic2lkIjoiNjMyNTlmYWQtN2IyMC00MjE2LWI3OWMtMjY3MDA2MDkzOGI3IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJHaWFubHVjYSBCZWN1enppIiwibWl0cmVpZC1zdWIiOiI4MzU1NTQ3NjcxOTY0NDg5IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZGphbmxvbyIsImdpdmVuX25hbWUiOiJHaWFubHVjYSIsImZhbWlseV9uYW1lIjoiQmVjdXp6aSIsImVtYWlsIjoiZy5iZWN1enppMUBzdHVkZW50aS51bmlwaS5pdCJ9.T0STb_v7OXrr7LgF3gP1x14US5pkpCjPZ7R853uw5TTWm_GW1rrU45Oc5nXrYi8wOJ8RGacPESBYIlgYcyQ5XNbJedXe0_oZEnOgTjOk_fZEkAGbz2xNX_BSAQAlrtRyv_woIVrmeth4eITNtJCpGr57gKP1CcWRd8_RBucHaQCv7XtdBVlgK8KKZ2trJUWfdoOhyHykVpu0Q2hTSWcDMcqJxgOY4oixgP6bUJGCKJiB19oCidasldcjMtELfXBRHQHxnLoYnFVV5DrOjGYxmO3RM4PUDUXTh2dmNT9NLJkQeg0rY3wjJ0tepVdancwvGAlJoW4VFFJWdzvS6m2Cqw",
                    
                     )
# print(client.auth)
# print(client.job_server)
# print(client.user_info)

# exit()
import os 
import time
import ebrains_drive
from ebrains_drive.client import DriveApiClient

collab_id = "nmc-test-djanloo"

print("Using the repository ",collab_id," for quotas. Starting the job at",time.ctime())
job = client.submit_job(source='base.py',
                        platform=nmpi.SPINNAKER,
                        collab_id=collab_id,
                        command="run.py",
                        wait=True)
print(job["log"])

filenames = client.download_data(job, local_dir=os.getcwd())
print("Fetched the files",filenames)
image_filenames = [name for name in filenames if name.endswith(".png")]
print(image_filenames)