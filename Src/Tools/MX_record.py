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
    except dns.resolver.NXDOMAIN:
        return ["Domain {} not found.".format(domain)]
    except dns.resolver.NoAnswer:
        return ["No MX records found for {}".format(domain)]
    except dns.exception.DNSException as e:
        return ["Error retrieving MX records: {}".format(e)]

if __name__ == "__main__":
    while True:
        domain_name = input("Enter the domain name: ")
        mx_result = retrieve_mx_records(domain_name)
        
        if mx_result[0].startswith("Domain") or mx_result[0].startswith("No MX records") or mx_result[0].startswith("Error"):
            for error_message in mx_result:
                print(error_message)
        else:
            print("MX records for {} are:".format(domain_name))
            for mx_server in mx_result:
                print("- {}".format(mx_server))
        
        choice = input("Do you want to start again? (y/n): ").lower()
        if choice != 'y':
            print("Program closed.")
            break
