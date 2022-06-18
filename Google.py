import pickle
from googleapiclient.discovery import build
import datetime

TOKEN_PICKLE = 'token.pickle'


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    with open(TOKEN_PICKLE, 'rb') as token:
        cred = pickle.load(token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
    except:
        DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred, discoveryServiceUrl=DISCOVERY_SERVICE_URL)
    
    return service


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt
