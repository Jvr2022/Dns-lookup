import socket
import requests
import dns.resolver

DNS_SERVERS = ["8.8.8.8", "8.8.4.4"]
IPINFO_API_URL = "http://ipinfo.io/{}/json"

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
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = DNS_SERVERS
        
        mx_records = []
        answers = resolver.resolve(domain, 'MX')
        
        for answer in answers:
            mx_records.append(answer.exchange.to_text())
        
        return mx_records
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return ["No MX records found for {}".format(domain)]

def get_ip_geolocation(ip_address):
    try:
        response = requests.get(IPINFO_API_URL.format(ip_address))
        data = response.json()
        return data.get("city", "Unknown city"), data.get("region", "Unknown region"), data.get("country", "Unknown country")
    except requests.RequestException:
        return "Failed to fetch geolocation"

def fast_dns_query(domain):
    try:
        dns_query = socket.gethostbyname(domain)
        return dns_query
    except socket.gaierror:
        return "DNS query failed for {}".format(domain)

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    ip_result = view_ip_addresses(domain_name)
    mx_result = retrieve_mx_records(domain_name)

if ip_result[0].startswith("DNS lookup failed"):
    print(ip_result[0])
else:
    print("IP addresses for {} are:".format(domain_name))
    for ip in ip_result:
        city, region, country = get_ip_geolocation(ip)
        print("- IP address {}: {}, {}, {}".format(ip, city, region, country))

if mx_result[0].startswith("No MX records"):
    print(mx_result[0])
else:
    print("\nMX records for {} are:".format(domain_name))
    for mx_server in mx_result:
        print("- {}".format(mx_server))

dns_query_result = fast_dns_query(domain_name)
print("\nFast and reliable DNS query for {} is:".format(domain_name))
print("- {}".format(dns_query_result))
