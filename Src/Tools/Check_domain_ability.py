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

def ask_to_restart():
    while True:
        choice = input("Do you want to start again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    print("Welcome to the Domain Availability Checker!")
    print("This tool allows you to check if a domain is available or not.")
    
    while True:
        domain_name = input("\nEnter the domain name: ")
        result = check_domain_availability(domain_name)
        print(result)
        
        choice = input("\nDo you want to check another domain? (y/n): ").lower()
        if choice != 'y':
            print("Program closed. Thank you for using the Domain Availability Checker!")
            break
