import whois

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status is None:
            return "Domain {} is available.".format(domain)
        else:
            return "Domain {} is not available.".format(domain)
    except whois.parser.PywhoisError:
        return "Error checking availability for {}.".format(domain)

if __name__ == "__main__":
    while True:
        domain_name = input("Enter the domain name: ")
        result = check_domain_availability(domain_name)
        print(result)
        
        choice = input("Do you want to start again? (y/n): ").lower()
        if choice != 'y':
            print("Program closed.")
            break
