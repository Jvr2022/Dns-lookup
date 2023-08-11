import socket

def perform_dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "DNS lookup failed for {}".format(domain)

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    result = perform_dns_lookup(domain_name)
    print("IP address for {} is: {}".format(domain_name, result))
