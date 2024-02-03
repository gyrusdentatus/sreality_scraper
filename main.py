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
    parser = argparse.ArgumentParser(description="Fetch properties from API and optionally save them to a .json file or database.")
    parser.add_argument("--interactive", help="Run in interactive mode", action='store_true')
    parser.add_argument("--mode", help="Mode of operation: fetch, visualize, db_init, interactive", default="fetch")
    parser.add_argument("--json", help="Save to .json instead of db", action='store_true')
    init_db()  # Initialize the database tables if they don't exist.
    args = parser.parse_args()

    if args.mode in ["fetch", "visualize"]:
        client = APIClient()
        data = client.fetch_properties({k: v for k, v in vars(args).items() if v is not None and k not in ['mode', 'json', 'interactive']})

        if data:
            if args.json:
                save_to_json(data)
                print("Data has been saved to a .json file.")
            else:
                save_to_db(data)
                print("Data has been saved to the database.")
        else:
            print("Failed to fetch data.")

    elif args.mode == "db_init":
        print("Database has been initialized.")

    if args.interactive or args.mode == "interactive":
        client = APIClient()
        run_interactive_mode(client)

if __name__ == "__main__":
    main()

