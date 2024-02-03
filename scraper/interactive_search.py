import json
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def filter_properties(properties_data, location, min_price, max_price, min_size, max_size):
    # Filter properties based on the criteria
    filtered_properties = [prop for prop in properties_data if
                           location.lower() in prop.get('locality', '').lower() and
                           min_price <= prop.get('price_czk', {}).get('value_raw', 0) <= max_price and
                           min_size <= prop.get('size', 0) <= max_size]
    
    print(f"{Fore.GREEN}Found {len(filtered_properties)} properties in {location} in this price range and size range!")

    # Ask if user wants to see the 10 most recent listings
    show_recent = input("Do you want to display the 10 most recent listings? (yes/no): ").lower()
    if show_recent == 'yes':
        recent_properties = filtered_properties[:10]  # Assuming properties_data is sorted by recency
        for prop in recent_properties:
            print(f"{Fore.CYAN}Name: {prop.get('name')}")
            print(f"Price: {prop.get('price_czk', {}).get('value_raw', 0)} CZK")
            print(f"Locality: {prop.get('locality')}")
            print("URLs:")
            for img in prop.get('_links', {}).get('images', []):
                print(f"{Fore.YELLOW}{img.get('href')}")
            print(Style.RESET_ALL + "-" * 20)

# Example usage
properties_data = [...]  # Your JSON data
location = input("Enter location (e.g., Plzen): ")
min_price = int(input("Enter minimum price in thousands CZK: ")) * 1000
max_price = int(input("Enter maximum price in thousands CZK: ")) * 1000
min_size = int(input("Enter minimum size in sqm: "))
max_size = int(input("Enter maximum size in sqm: "))

filter_properties(properties_data, location, min_price, max_price, min_size, max_size)

