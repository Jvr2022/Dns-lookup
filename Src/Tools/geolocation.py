import requests
import socket

def geolocate_ip_address(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if data["status"] == "success":
            city = data.get("city", "Unknown")
            region = data.get("regionName", "Unknown")
            country = data.get("country", "Unknown")
            isp = data.get("isp", "Unknown")
            lat = data.get("lat", "Unknown")
            lon = data.get("lon", "Unknown")

            geolocation_info = f"City: {city}\nRegion: {region}\nCountry: {country}\nISP: {isp}\nLatitude: {lat}\nLongitude: {lon}"
            return geolocation_info
        else:
            return f"Geolocation data not available for {ip_address}."
    except requests.exceptions.RequestException as e:
        return f"Geolocation lookup failed: {e}"

if __name__ == "__main__":
    print("Welcome to the Advanced IP Geolocation Tool!")

    while True:
        ip_address = input("\nEnter an IP address for geolocation: ")

        # Check if the input is a valid IP address
        try:
            socket.inet_pton(socket.AF_INET, ip_address)
            result = geolocate_ip_address(ip_address)
            
            if "failed" in result.lower():
                print(result)
            else:
                print("Geolocation details for {}:\n{}".format(ip_address, result))
        except socket.error:
            print("Invalid IP address format.")
        
        if not input("\nDo you want to geolocate another IP address? (y/n): ").lower() == 'y':
            print("Program closed. Thank you for using the Advanced IP Geolocation Tool!")
            break
