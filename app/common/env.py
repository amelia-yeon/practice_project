import os
from dotenv import load_dotenv

load_dotenv()




GCS_PROJECT_ID = str(os.environ.get("GCS_PROJECT_ID"))
GCS_KEY_FILE = 'sy-gcp-project.json'




















# linux path
# GCS_KEY_FILE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) + str(os.environ.get("GCS_KEY_FILE"))

# ENV = str(os.environ.get("ENV"))
# API_PORT = int(os.environ.get("API_PORT"))

