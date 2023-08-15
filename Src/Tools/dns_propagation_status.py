import dns.resolver
import time

def check_dns_propagation(domain):
    dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9"]
    propagation_status = {}
    
    for dns_server in dns_servers:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [dns_server]
        
        try:
            start_time = time.time()
            answers = resolver.resolve(domain, "A")
            end_time = time.time()
            
            propagation_status[dns_server] = "Propagated ({} ms)".format(int((end_time - start_time) * 1000))
        except dns.exception.DNSException as e:
            propagation_status[dns_server] = f"Error: {e}"
    
    return propagation_status

if __name__ == "__main__":
    print("Welcome to the DNS Propagation Status Checker!")

    while True:
        domain_name = input("\nEnter the domain name: ")
        propagation_status = check_dns_propagation(domain_name)
        
        print("\nDNS Propagation Status for {}:".format(domain_name))
        for dns_server, status in propagation_status.items():
            print("- {}: {}".format(dns_server, status))
        
        if not input("\nDo you want to check another domain's DNS propagation status? (y/n): ").lower() == 'y':
            print("Program closed. Thank you for using the DNS Propagation Status Checker!")
            break
