import requests
import os

from bs4 import BeautifulSoup

import database as db

class bus:
    def __init__(self, db_name):
        self.db_name = db_name

        db_path = self.get_db_path()

        self.path = db_path
        self.bd_bus = db.db(self.path, self.db_name)
        
    def create_db(self):
        self.bd_bus.create_table()

    def insert_data(self, data):
        self.bd_bus.insert_data(data)

    def get_all_bus_number(self, url):
        site = self.web_scrape(url)
        soup = BeautifulSoup(site.text, 'html.parser')

        dataset = {}

        # Append all types of busses
        for bus_type in soup.select('.eguide > dt > strong'):
            data = []

            # Append all bus numbers according to bus type
            for bus_number in soup.select('.eguide > dd > select > option'):
                # Ignore default value. e.g. '-SBS Transit service'
                if(bus_number['value'] == '-'):
                    continue

                data.append(bus_number.string)
            
            dataset[bus_type.string] = data

        return dataset

    def check_db_exists(self):
        return os.path.exists('/table/' + self.db_name)

    def get_db_path(self):
        # Path for db
        current_directory = os.path.dirname(os.path.abspath(__file__))
        new_directory = os.path.join(current_directory, 'table')
        
        if(not os.path.exists(new_directory)):
            os.mkdir(new_directory)
            
        return os.path.join(new_directory, self.db_name)

    @staticmethod
    def web_scrape(url):
        return requests.get(url)
    