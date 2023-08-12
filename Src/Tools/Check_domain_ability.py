import whois

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return "Domain {} is available.".format(domain)
        else:
            return "Domain {} is not available.".format(domain)
    except whois.parser.PywhoisError:
        return "Error checking availability for {}.".format(domain)

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    result = check_domain_availability(domain_name)
    print(result)
