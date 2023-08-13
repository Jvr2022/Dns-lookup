import requests

def geolocate_ip_address(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        city = data.get("city", "Unknown")
        region = data.get("regionName", "Unknown")
        country = data.get("country", "Unknown")
        
        geolocation_info = f"{city}, {region}, {country}"
        return geolocation_info
    except requests.exceptions.RequestException:
        return "Geolocation lookup failed"

if __name__ == "__main__":
    ip_address = input("Enter an IP address for geolocation: ")
    result = geolocate_ip_address(ip_address)
    
    if result.startswith("Geolocation lookup failed"):
        print(result)
    else:
        print("Geolocation for {} is: {}".format(ip_address, result))

def ask_to_restart():
    while True:
        choice = input("Do you want to start again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

if ask_to_restart():
    pass
else:
    print("Program closed.")
