import socket
import requests
import dns.resolver
import whois

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

def reverse_dns_lookup(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        return hostnames[0]
    except socket.herror:
        return "Reverse DNS lookup failed for {}".format(ip_address)

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return "Domain {} is available.".format(domain)
        else:
            return "Domain {} is not available.".format(domain)
    except whois.parser.PywhoisError:
        return "Error checking availability for {}.".format(domain)
        
def check_dns_propagation_status(domain):
    try:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = DNS_SERVERS

        answers = resolver.resolve(domain, 'A')
        if answers:
            return "DNS propagation for {} is complete.".format(domain)
        else:
            return "DNS propagation for {} is not complete yet.".format(domain)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return "DNS propagation status check failed for {}.".format(domain)

def export_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        
if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    
    availability_result = check_domain_availability(domain_name)
    dns_propagation_result = check_dns_propagation_status(domain_name)
    
    ip_result = view_ip_addresses(domain_name)
    mx_result = retrieve_mx_records(domain_name)
    
    if ip_result[0].startswith("DNS lookup failed"):
        ip_output = ip_result[0]
    else:
        ip_output = "\nIP addresses for {} are:\n- {}".format(domain_name, "\n- ".join(ip_result))
    
    if mx_result[0].startswith("No MX records"):
        mx_output = mx_result[0]
    else:
        mx_output = "\nMX records for {} are:\n- {}".format(domain_name, "\n- ".join(mx_result))
    
    dns_query_result = fast_dns_query(domain_name)
    ip_address = dns_query_result
    reverse_dns_result = reverse_dns_lookup(ip_address)
    
    output = f"""
Domain availability check for {domain_name}:
- {availability_result}

DNS propagation status check for {domain_name}:
- {dns_propagation_result}

{ip_output}

{mx_output}

Fast and reliable DNS query for {domain_name} is:
- {dns_query_result}

Reverse DNS lookup for {ip_address} is:
- {reverse_dns_result}
"""
    output_filename = f"{domain_name}_query_results.txt"
    export_to_file(output_filename, output)
    
    print("\nQuery results exported to:", output_filename)
    
    # Display query results on the screen
    print("\nQuery Results:")
    print(output)
