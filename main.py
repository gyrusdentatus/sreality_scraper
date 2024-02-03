import argparse
import json
from scraper.api_client import APIClient
#from db.database import SessionLocal, init_db
from db.models import Property
from db.database import SessionLocal, engine
from db.database import init_db
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
    parser = argparse.ArgumentParser(description="Fetch properties from Sreality API based on specified filters and save them to a .json file.")
    init_db()  # Ensure this is called to create the database tables if they don't exist.
    
    # Adding arguments based on sections 3.1, 3.2, and 3.3
    parser.add_argument("--category_main_cb", help="Main category of the property", type=int)
    parser.add_argument("--category_sub_cb", help="Subcategory of the property", type=int)
    parser.add_argument("--category_type_cb", help="Type of listing (sale, rent, auction)", type=int)
    parser.add_argument("--locality_region_id", help="Region ID", type=int)
    parser.add_argument("--locality_district_id", help="District ID", type=int)
    parser.add_argument("--no_auction", help="Exclude auctions", type=int, choices=[0, 1])
    parser.add_argument("--per_page", help="Number of results per page", type=int, default=20)
    parser.add_argument("--page", help="Page number", type=int, default=1)
    parser.add_argument("--tms", help="Timestamp for requests", type=int)

    args = parser.parse_args()

    # Building query params from provided args
    query_params = {k: v for k, v in vars(args).items() if v is not None}

    client = APIClient()
    data = client.fetch_properties(query_params)

    if data:
        # save_to_json(data) ## let's  save it in db instead ... might add optional output to .json later
        save_to_db(data)
        print("Data has been saved to properties_data.json.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()

