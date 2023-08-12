import socket

def reverse_dns_lookup(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        return host_name[0]
    except socket.herror:
        return "Reverse DNS lookup failed for {}".format(ip_address)

if __name__ == "__main__":
    ip_address = input("Enter an IP address for reverse DNS lookup: ")
    result = reverse_dns_lookup(ip_address)
    
    if result.startswith("Reverse DNS lookup failed"):
        print(result)
    else:
        print("Reverse DNS lookup for {} is: {}".format(ip_address, result))
