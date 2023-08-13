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
    except socket.gaierror as e:
        return ["DNS lookup failed for {}: {}".format(domain, e)]

def retrieve_mx_records(domain):
    try:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = DNS_SERVERS
        
        mx_records = []
        answers = resolver.resolve(domain, 'MX')
        
        for answer in answers:
            mx_records.append(answer.exchange.to_text())
        
        return mx_records
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer) as e:
        return ["No MX records found for {}: {}".format(domain, e)]

def get_ip_geolocation(ip_address):
    try:
        response = requests.get(IPINFO_API_URL.format(ip_address))
        data = response.json()
        return data.get("city", "Unknown city"), data.get("region", "Unknown region"), data.get("country", "Unknown country")
    except requests.RequestException as e:
        return "Failed to fetch geolocation: {}".format(e)

def fast_dns_query(domain):
    try:
        dns_query = socket.gethostbyname(domain)
        return dns_query
    except socket.gaierror as e:
        return "DNS query failed for {}: {}".format(domain, e)

def reverse_dns_lookup(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        return hostnames[0]
    except socket.herror as e:
        return "Reverse DNS lookup failed for {}: {}".format(ip_address, e)

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return "Domain {} is available.".format(domain)
        else:
            return "Domain {} is not available.".format(domain)
    except whois.parser.PywhoisError as e:
        return "Error checking availability for {}: {}".format(domain, e)

def check_dns_propagation_status(domain):
    try:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = DNS_SERVERS
        
        answers = resolver.resolve(domain, 'A')
        if answers:
            return "DNS propagation for {} is complete.".format(domain)
        else:
            return "DNS propagation for {} is not complete yet.".format(domain)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer) as e:
        return "DNS propagation status check failed for {}: {}".format(domain, e)

def check_dnssec_validation(domain):
    try:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = DNS_SERVERS
        
        answers = resolver.resolve(domain, 'DS')
        if answers:
            return "DNSSEC validation for {} is enabled.".format(domain)
        else:
            return "DNSSEC validation for {} is not enabled.".format(domain)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer) as e:
        return "DNSSEC validation status check failed for {}: {}".format(domain, e)

def export_to_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return "Exported to file: {}".format(filename)
    except Exception as e:
        return "Error exporting to file {}: {}".format(filename, e)

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    
    use_custom_dns = input("Do you want to use custom DNS servers? (y/n): ").lower()
    if use_custom_dns == 'y':
        custom_dns_servers = input("Enter custom DNS servers (comma-separated): ")
        custom_dns_list = custom_dns_servers.split(',')
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = custom_dns_list
    else:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Default DNS servers
    
    availability_result = check_domain_availability(domain_name)
    dns_propagation_result = check_dns_propagation_status(domain_name)
    dnssec_result = check_dnssec_validation(domain_name)
    
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

DNSSEC validation status check for {domain_name}:
- {dnssec_result}

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
    
def ask_to_restart():
    while True:
        choice = input("Do you want to start again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

if ask_to_restart():
    pass
else:
    print("Program closed.")
