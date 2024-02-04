from colorama import init, Fore, Style

init(autoreset=True)

def run_interactive_mode(client):
    location = input("Enter location (e.g., Praha): ")
    min_price = int(input("Enter minimum price in thousands CZK: ")) * 1000
    max_price = int(input("Enter maximum price in thousands CZK: ")) * 1000

    data = client.fetch_properties({})  # Placeholder for fetching properties

    if data:
        filter_properties(data, location, min_price, max_price)
    else:
        print(f"{Fore.RED}No properties found or failed to fetch data.")
def filter_properties(properties_data, location, min_price, max_price):
    filtered_properties = [prop for prop in properties_data.get('_embedded', {}).get('estates', []) if
                           location.lower() in prop.get('locality', '').lower() and
                           min_price <= prop.get('price', 0) <= max_price]

    print(f"{Fore.GREEN}Found {len(filtered_properties)} properties in {location} within this price range.")

    if filtered_properties:
        show_recent = input("Do you want to display the 10 most recent listings? (yes/no): ").lower()
        if show_recent == 'yes':
            for prop in filtered_properties[:10]:  # Assuming properties are sorted by recency
                # Check for empty phones list before accessing
                phone_numbers = prop.get('_embedded', {}).get('premise', {}).get('phones', [])
                broker_contact = phone_numbers[0].get('number', 'N/A') if phone_numbers else "No contact number available"

                print(f"{Fore.CYAN}Name: {prop.get('name')}")
                print(f"Description: {prop.get('text', {}).get('value', 'N/A')}")
                print(f"Price: {prop.get('price_czk', {}).get('value_raw')} Kč")
                print(f"Locality: {prop.get('locality')}")
                print(f"Broker Contact: {broker_contact}")

                # Constructing and displaying the URL for the JSON data
                json_url = f"https://sreality.cz/api/v2/estates/{prop.get('hash_id')}"
                print(f"{Fore.YELLOW}JSON URL: {json_url}")

                # Display website URL
                website_url = f"https://www.sreality.cz/detail/prodej/{prop.get('category_main_cb')}/{prop.get('category_sub_cb')}/{prop.get('locality')}/{prop.get('hash_id')}#img=0"
                print(f"Website URL: {website_url}")

                print(Style.RESET_ALL + "-" * 20)

