import argparse
import json
from scraper.api_client import APIClient
from db.models import Property
from db.database import SessionLocal
from db.database import init_db
from scraper.interactive_search import run_interactive_mode


def save_to_json(data, filename="properties_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_to_db(data):
    db = SessionLocal()
    try:
        for item in data.get('_embedded', {}).get('estates', []):
            property = Property(
                category_main_cb=item.get('category_main_cb'),
                category_sub_cb=item.get('category_sub_cb'),
                category_type_cb=item.get('category_type_cb'),
                locality_region_id=item.get('locality', {}).get('region_id'),
                locality_district_id=item.get('locality', {}).get('district_id'),
                price=item.get('price'),
                name=item.get('name'),
                latitude=item.get('gps', {}).get('lat'),
                longitude=item.get('gps', {}).get('lon'),
            )
            db.add(property)
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

def main():
    parser = argparse.ArgumentParser(description="Fetch properties from Sreality API and optionally save them to a .json file.")
    parser.add_argument("--interactive", help="Run in interactive mode", action='store_true')
    parser.add_argument("--mode", help="Mode of operation: fetch, visualize, db_init", default="fetch")
    parser.add_argument("--json", help="Save to .json instead of db", action='store_true')
    init_db()  # Initialize the database tables if they don't exist.

    # Fetch and save modes
    if parser.parse_args().mode in ["fetch", "visualize", "interactive"]:
        client = APIClient()
        data = client.fetch_properties({k: v for k, v in vars(parser.parse_args()).items() if v is not None and k not in ['mode', 'json']})

        if data:
            if parser.parse_args().json:
                save_to_json(data)
                print("Data has been saved to a .json file.")
            else:
                save_to_db(data)
                print("Data has been saved to the database.")
        else:
            print("Failed to fetch data.")

    # Visualization mode
    if parser.parse_args().mode == "visualize":
        from visualization.visualize import generate_price_distribution
        generate_price_distribution()

    # Database initialization mode
    elif parser.parse_args().mode == "db_init":
        # Assuming init_db() function initializes the database. If not, adjust accordingly.
        print("Database has been initialized.")

    # Interactive search mode
    if parser.parse_args().mode == "interactive":
            client = APIClient()  # Assuming you have a class APIClient for fetching properties
            run_interactive_mode(client)
    
            run_interactive_mode(data)
    else:
            print("Failed to fetch data.")
        # Normal operation based on command line arguments
pass

if __name__ == "__main__":
    main()

