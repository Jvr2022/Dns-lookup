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
    print("Welcome to the IP Geolocation Tool!")

    while True:
        ip_address = input("\nEnter an IP address for geolocation: ")
        result = geolocate_ip_address(ip_address)
        
        if "failed" in result.lower():
            print(result)
        else:
            print("Geolocation for {} is: {}".format(ip_address, result))
        
        if not input("\nDo you want to geolocate another IP address? (y/n): ").lower() == 'y':
            print("Program closed. Thank you for using the IP Geolocation Tool!")
            break
