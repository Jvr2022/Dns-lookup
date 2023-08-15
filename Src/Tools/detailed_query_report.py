import whois

def view_detailed_query_report(domain):
    w = whois.whois(domain)
    return w

if __name__ == "__main__":
    while True:
        domain_name = input("Enter the domain name: ")
        detailed_report = view_detailed_query_report(domain_name)
        print("\nDetailed Query Report for {}:\n{}".format(domain_name, detailed_report))
        
        restart_choice = input("Do you want to start again? (y/n): ").lower()
        if restart_choice != 'y':
            print("Program closed.")
            break
