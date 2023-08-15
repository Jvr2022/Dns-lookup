import socket

def get_ip_addresses(domain):
    try:
        ipv4_addresses = []
        ipv6_addresses = []
        
        # Retrieve IPv4 addresses
        ipv4_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        ipv4_addresses = [ip[4][0] for ip in ipv4_info]
        
        # Retrieve IPv6 addresses
        ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
        ipv6_addresses = [ip[4][0] for ip in ipv6_info]
        
        return ipv4_addresses, ipv6_addresses
    except socket.gaierror as e:
        return [], []

if __name__ == "__main__":
    print("Welcome to the IP Address Retrieval Tool!")

    while True:
        domain_name = input("\nEnter the domain name: ")
        ipv4_addresses, ipv6_addresses = get_ip_addresses(domain_name)
        
        if not ipv4_addresses and not ipv6_addresses:
            print(f"No IP addresses found for {domain_name}.")
        else:
            print(f"IP addresses of {domain_name} are:")
            for ipv4 in ipv4_addresses:
                print(f"- {ipv4} (IPv4)")
            for ipv6 in ipv6_addresses:
                print(f"- {ipv6} (IPv6)")
        
        choice = input("\nDo you want to get the IP addresses of another domain? (y/n): ").lower()
        if choice != 'y':
            print("Program closed. Thank you for using the IP Address Retrieval Tool!")
            break
