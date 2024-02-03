from colorama import init, Fore, Style
from scraper.api_client import APIClient

init(autoreset=True)

def run_interactive_mode(client):
    location = input("Enter location (e.g., Praha): ")
    min_price = int(input("Enter minimum price in thousands CZK: ")) * 1000
    max_price = int(input("Enter maximum price in thousands CZK: ")) * 1000
    # Assume every property meets size criteria unless specific fields are available
    # min_size = int(input("Enter minimum size in sqm: "))
    # max_size = int(input("Enter maximum size in sqm: "))

    data = client.fetch_properties({})  # Fetch properties without filtering by params in this example

    if data:
        filter_properties(data, location, min_price, max_price)
    else:
        print(f"{Fore.RED}No properties found or failed to fetch data.")

def filter_properties(properties_data, location, min_price, max_price):
    # Filter logic corrected based on provided JSON structure
    filtered_properties = [prop for prop in properties_data.get('_embedded', {}).get('estates', []) if
                           location.lower() in prop.get('locality', '').lower() and
                           min_price <= prop.get('price', 0) <= max_price]
                           # Add these lines if size data is available and relevant
                           # and min_size <= prop.get('size_attribute_here', 0) <= max_size]

    print(f"{Fore.GREEN}Found {len(filtered_properties)} properties in {location} within this price range.")

    if filtered_properties:
        show_recent = input("Do you want to display the 10 most recent listings? (yes/no): ").lower()
        if show_recent == 'yes':
            recent_properties = filtered_properties[:10]  # Assuming properties are sorted by recency
            for prop in recent_properties:
                print(f"{Fore.CYAN}Name: {prop.get('name')}")
                print(f"Price: {prop.get('price_czk', {}).get('value_raw')} CZK")
                print(f"Locality: {prop.get('locality')}")
                # Uncomment and adjust if size data is available
                # print(f"Size: {prop.get('size_attribute_here')} sqm") 
                for img in prop.get('_links', {}).get('images', []):
                    print(f"{Fore.YELLOW}Image URL: {img.get('href')}")
                print(Style.RESET_ALL + "-" * 20)

