"""Sends "simulation.py" to spinnaker server, then retrieves the job results.

It is a revisitation of the script given in form of jupyter notebook in EBRAINS spinnaker lab.
"""
import nmpi
from rich import print

# Replace None with your username, password and collab_id
username = None 
password = None
collab_id = None

if username is None or password is None or collab_id is None:
    print("[red]username/password/collab_id not set yet[/red]")
    exit()

client = nmpi.Client(
                    username=username, password=password,                     
                    )

print(f"Authorization endpoint: [green]{client.authorization_endpoint}[/green]")
print("It may be necessary to grant access visiting this URL by browser [blue]once[/blue]")

import os 
import time

print("Using the repository ",collab_id," for quotas. Starting the job at",time.ctime())
job = client.submit_job(source='simulation.py',
                        platform=nmpi.SPINNAKER,
                        collab_id=collab_id,
                        command="run.py",
                        wait=True)
print(job["log"])

filenames = client.download_data(job, local_dir=os.getcwd())
print("Fetched the files",filenames)
image_filenames = [name for name in filenames if name.endswith(".png")]
print(image_filenames)