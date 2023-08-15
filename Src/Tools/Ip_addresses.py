import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "DNS lookup failed for {}".format(domain)

def ask_to_continue():
    choice = input("Do you want to get the IP address of another domain? (y/n): ").lower()
    return choice == 'y'

if __name__ == "__main__":
    print("Welcome to the IP Address Retrieval Tool!")

    while True:
        domain_name = input("\nEnter the domain name: ")
        ip_address = get_ip_address(domain_name)
        
        if ip_address.startswith("DNS lookup failed"):
            print(ip_address)
        else:
            print("IP address of {} is: {}".format(domain_name, ip_address))
        
        if not ask_to_continue():
            print("Program closed. Thank you for using the IP Address Retrieval Tool!")
            break
