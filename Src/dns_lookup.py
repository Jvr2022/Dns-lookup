import socket
import requests
import dns.resolver
import whois

DNS_SERVERS = ["8.8.8.8", "8.8.4.4"]
IPINFO_API_URL = "http://ipinfo.io/{}/json"

def view_ip_addresses(domain):
    try:
        ipv4_addresses = socket.gethostbyname_ex(domain)[2]
        ipv6_addresses = set(ip_info[4][0] for ip_info in socket.getaddrinfo(domain, None, socket.AF_INET6))
        
        print("IPv4 addresses:", ipv4_addresses)
        print("IPv6 addresses:", ipv6_addresses)

        if not ipv4_addresses and not ipv6_addresses:
            print("No IP addresses found.")
            return [], []

        return ipv4_addresses, list(ipv6_addresses)
    except socket.gaierror as e:
        print("Error:", e)
        return [], []
    except IndexError:
        print("Index error.")
        return [], []

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

if __name__ == "__main__":
    print("Welcome to the DNS Lookup Tool!")

    while True:
        domain_name = input("\nEnter the domain name: ")

        use_custom_dns = input("Do you want to use custom DNS servers? (y/n): ").lower()
        if use_custom_dns == 'y':
            custom_dns_servers = input("Enter custom DNS servers (comma-separated): ")
            custom_dns_list = custom_dns_servers.split(',')
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = custom_dns_list
        else:
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Default DNS servers
        
        output_filename = f"{domain_name}_query_results.txt"  # Define output_filename here

        availability_result = check_domain_availability(domain_name)
        dns_propagation_result = check_dns_propagation_status(domain_name)
        dnssec_result = check_dnssec_validation(domain_name)

        ip_v4_addresses, ip_v6_addresses = view_ip_addresses(domain_name)

        ip_output = ""
        if ip_v4_addresses or ip_v6_addresses:
            ip_output = f"IP addresses for {domain_name}:\n"
            if ip_v4_addresses:
                ip_output += "\n".join([f"- IPv4 address: {ip}" for ip in ip_v4_addresses])
            if ip_v6_addresses:
                ip_output += "\n" + "\n".join([f"- IPv6 address: {ip}" for ip in ip_v6_addresses])
            if not ip_v4_addresses and not ip_v6_addresses:
                ip_output += "\n" + f"- Single IP address: {ip_address}"
        else:
            ip_output = f"No IP addresses found for {domain_name}"

        mx_result = retrieve_mx_records(domain_name)

        if mx_result[0].startswith("No MX records"):
            mx_output = mx_result[0]
        else:
            mx_output = "\nMX records for {} are:\n{}".format(domain_name, "\n".join(["- " + mx for mx in mx_result]))

        dns_query_result = fast_dns_query(domain_name)
        ip_address = dns_query_result
        reverse_dns_result = reverse_dns_lookup(ip_address)

        output = f"""
Query results exported to: {output_filename}

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

        with open(output_filename, "w") as file:
            file.write(output)
        print(f"\nQuery results exported to: {output_filename}")
        print(output)

        if not input("\nDo you want to perform another query? (y/n): ").lower() == 'y':
            print("Program closed. Thank you for using the DNS Lookup Tool!")
            break
