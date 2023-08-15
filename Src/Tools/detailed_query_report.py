import whois

def view_detailed_query_report(domain):
    w = whois.whois(domain)
    return w

def ask_to_continue():
    choice = input("Do you want to view the detailed query report for another domain? (y/n): ").lower()
    return choice == 'y'

if __name__ == "__main__":
    print("Welcome to the Detailed Query Report Viewer!")

    while True:
        domain_name = input("\nEnter the domain name: ")
        detailed_report = view_detailed_query_report(domain_name)
        print("\nDetailed Query Report for {}:\n{}".format(domain_name, detailed_report))
        
        if not ask_to_continue():
            print("Program closed. Thank you for using the Detailed Query Report Viewer!")
            break
