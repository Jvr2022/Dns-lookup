import socket

DNS_SERVER = "8.8.8.8"

def view_ip_addresses(domain):
    try:
        ip_addresses = socket.getaddrinfo(domain, None, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP, socket.AI_ADDRCONFIG)
        ipv4_set = set(ip[4][0] for ip in ip_addresses if ip[1] == socket.AF_INET)
        ipv6_set = set(ip[4][0] for ip in ip_addresses if ip[1] == socket.AF_INET6)
        
        ip_set = ipv4_set.union(ipv6_set)
        return list(ip_set)
    except socket.gaierror:
        return ["DNS lookup failed for {}".format(domain)]

def retrieve_mx_records(domain):
    try:
        mx_records = []
        answers = socket.getaddrinfo(domain, None, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        
        for answer in answers:
            if answer[1] == socket.SOCK_STREAM:
                mx_records.append(answer[4][0])
        
        return mx_records
    except socket.gaierror:
        return ["DNS lookup failed for {}".format(domain)]

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    ip_result = view_ip_addresses(domain_name)
    mx_result = retrieve_mx_records(domain_name)
    
    if ip_result[0].startswith("DNS lookup failed"):
        print(ip_result[0])
    else:
        print("IP addresses for {} are: {}".format(domain_name, ', '.join(ip_result)))

    if mx_result[0].startswith("DNS lookup failed"):
        print(mx_result[0])
    else:
        print("MX records for {} are: {}".format(domain_name, ', '.join(mx_result)))

    try:
        dns_query = socket.gethostbyname(domain_name)
        print("Fast and reliable DNS query for {} is: {}".format(domain_name, dns_query))
    except socket.gaierror:
        print("DNS query failed for {}".format(domain_name))
