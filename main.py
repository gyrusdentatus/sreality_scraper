import argparse
import json
from api_client import APIClient

def save_to_json(data, filename="properties_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Fetch properties from Sreality API based on specified filters and save them to a .json file.")
    
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
        save_to_json(data)
        print("Data has been saved to properties_data.json.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()

