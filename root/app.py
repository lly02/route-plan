import model

def initialize():
    db_name = 'bus.db'
    main_url = 'https://www.transitlink.com.sg/eservice/eguide/service_idx.php'

    bus = model.bus(db_name)

    # Check DB exists
    if(not bus.check_db_exists()):
        # Scrape data from URL
        site_data = bus.get_all_bus_number(main_url)

        # Table initialization
        bus.create_db()
        bus.insert_data(site_data)

def main():
    initialize()

if __name__ == '__main__':
    main()