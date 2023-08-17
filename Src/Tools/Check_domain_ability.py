import whois
import re

def is_valid_domain(domain):
    return re.match(r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$", domain, re.IGNORECASE)

def check_domain_availability(domain):
    if not is_valid_domain(domain):
        return "Invalid domain format: Please enter a valid domain name."
    
    try:
        w = whois.whois(domain)
        if w.status is None:
            return "Domain {} is available.".format(domain)
        else:
            return "Domain {} is not available.".format(domain)
    except whois.parser.PywhoisError:
        return "Error checking availability for {}.".format(domain)
    except ConnectionError:
        return "Connection error: Unable to establish a connection to the WHOIS server."
    except TimeoutError:
        return "Timeout error: The connection to the WHOIS server timed out."
    except whois.whois.ServerNotFoundError:
        return "Server not found error: Unable to locate the WHOIS server for the domain."
    except whois.whois.WhoisCommandFailed:
        return "WHOIS command failed error: The WHOIS command for the domain failed."
    except whois.whois.WhoisRateLimitError:
        return "WHOIS rate limit error: The rate limit for WHOIS queries has been exceeded."
    except whois.whois.WhoisRateLimitExceeded:
        return "WHOIS rate limit exceeded error: The rate limit for WHOIS queries has been exceeded."
    except whois.whois.FailedParsingWhoisOutput:
        return "Failed parsing WHOIS output error: Unable to parse the WHOIS response."
    except Exception as e:
        return "An error occurred: {}".format(e)

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
        
        restart = ask_to_restart()
        if not restart:
            print("Program closed. Thank you for using the Enhanced Domain Availability Checker!")
            break
