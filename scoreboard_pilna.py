from gss import GSheets
import pandas as pd
from datetime import datetime as dt


class ScoreBoard:
    def __init__(self):
        self.gss_data = pd.DataFrame()
        self.get_gss_data()

    def get_gss_data(self):
        self.gss_data = GSheets().df

    def get_month_stats(self, month: int):
        try:
            if month < 1 or month > 12:
                raise Exception
            result = self.gss_data[self.gss_data.data.dt.month == month]
            return result['osoba'].value_counts().to_dict()
        except:
            return "Error: Invalid Month"

    def get_stats_from_date(self, date: str):
        try:
            my_date = pd.to_datetime(date)
            result = self.gss_data[self.gss_data.data.dt.date == my_date]
            return result['osoba'].value_counts().to_dict()
        except:
            return "Error: Invalid Date"

    def get_today_stats(self):
        result = self.gss_data[self.gss_data.data.dt.date == dt.now().date()]
        return result['osoba'].value_counts().to_dict()

    def get_stats(self):
        return self.gss_data['osoba'].value_counts().to_dict()
