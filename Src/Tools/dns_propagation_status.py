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
        except dns.exception.DNSException:
            propagation_status[dns_server] = "Not propagated"
    
    return propagation_status

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    propagation_status = check_dns_propagation(domain_name)
    
    print("\nDNS Propagation Status for {}:".format(domain_name))
    for dns_server, status in propagation_status.items():
        print("- {}: {}".format(dns_server, status))

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
