from Google import Create_Service
import pandas as pd
import os
import json

API_NAME = os.environ['API_NAME']
API_VERSION = os.environ['API_VERSION']
SCOPES = [os.environ['SCOPES']]
CLIENT_SECRET = json.loads(os.environ['CLIENT_SECRET'])
SPREADSHEET_ID = os.environ['SPREADSHEET_ID']


class GSheets:

    def __init__(self):
        self.df = pd.DataFrame()
        self.update_data(2)

    def update_data(self, start: int):

        service = Create_Service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPES)

        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            majorDimension='ROWS',
            range='Pilna Pomoc!' + f"A{start}:G{start + 30000}"
        ).execute()

        data = pd.DataFrame(result['values'])

        data.columns = ['nauczyciel', 'grupa', 'link', 'status', 'osoba', 'przedmiot', 'data']

        data['osoba'] = data['osoba'].str.strip().str.title()
        data['data'] = data['data'].str.strip()
        data['data'] = pd.to_datetime(data['data'])

        self.df = data
