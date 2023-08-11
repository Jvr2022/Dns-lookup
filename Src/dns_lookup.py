import socket

def view_ip_addresses(domain):
    try:
        ip_addresses = socket.getaddrinfo(domain, None)
        ipv4_set = set(ip[4][0] for ip in ip_addresses if ip[1] == socket.AF_INET)
        ipv6_set = set(ip[4][0] for ip in ip_addresses if ip[1] == socket.AF_INET6)
        
        ip_set = ipv4_set.union(ipv6_set)
        return list(ip_set)
    except socket.gaierror:
        return ["DNS lookup failed for {}".format(domain)]

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    result = view_ip_addresses(domain_name)
    
    if result[0].startswith("DNS lookup failed"):
        print(result[0])
    else:
        print("IP addresses for {} are: {}".format(domain_name, ', '.join(result)))
