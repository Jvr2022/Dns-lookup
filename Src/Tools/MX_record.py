import dns.resolver

DNS_SERVERS = ["8.8.8.8", "8.8.4.4"]

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

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    mx_result = retrieve_mx_records(domain_name)
    
    if mx_result[0].startswith("No MX records"):
        print(mx_result[0])
    else:
        print("MX records for {} are:".format(domain_name))
        for mx_server in mx_result:
            print("- {}".format(mx_server))

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
