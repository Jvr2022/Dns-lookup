import requests

def geolocate_ip_address(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        city = data.get("city", "Unknown")
        region = data.get("regionName", "Unknown")
        country = data.get("country", "Unknown")
        
        geolocation_info = f"{city}, {region}, {country}"
        return geolocation_info
    except requests.exceptions.RequestException as e:
        return f"Geolocation lookup failed: {e}"

if __name__ == "__main__":
    while True:
        ip_address = input("Enter an IP address for geolocation: ")
        result = geolocate_ip_address(ip_address)
        
        if "failed" in result.lower():
            print(result)
        else:
            print("Geolocation for {} is: {}".format(ip_address, result))
        
        choice = input("Do you want to start again? (y/n): ").lower()
        if choice != 'y':
            print("Program closed.")
            break
