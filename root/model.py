import requests
import os

from bs4 import BeautifulSoup

import database as db

def check_db_exists(file):
    return os.path.exists('/table/' + file)

def get_all_bus_number(url):
    site = web_scrape(url)
    soup = BeautifulSoup(site.text, 'html.parser')

    dataset = []

    # Append all types of busses
    for bus_type in soup.select('.eguide > dt > strong'):
        data = []
        data.append(bus_type.string)

        # Append all bus numbers according to bus type
        for bus_number in soup.select('.eguide > dd > select > option'):
            if(bus_number['value'] == '-'):
                continue

            data.append(bus_number.string)
        
        dataset.append(data)

    print(dataset)
          

def web_scrape(url):
    return requests.get(url)

def create_db(db_name):
    # Path for new table
    current_directory = os.path.dirname(os.path.abspath(__file__))
    new_directory = os.path.join(current_directory, 'table')
    
    if(not os.path.exists(new_directory)):
        os.mkdir(new_directory)

    db_path =  os.path.join(new_directory, db_name)

    db.createTable(db_path)

