import model

def initialize():
    db_name = 'bus.db'
    main_url = 'https://www.transitlink.com.sg/eservice/eguide/service_idx.php'

    # Check DB exists
    if(not model.check_db_exists(db_name)):
        # Scrape data from URL
        site_data = model.get_all_bus_number(main_url)

        model.create_db(db_name)   

def main():
    initialize()

if __name__ == '__main__':
    main()