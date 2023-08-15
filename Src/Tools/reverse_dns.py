import socket

def reverse_dns_lookup(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        return host_name[0]
    except socket.herror:
        return "Reverse DNS lookup failed for {}".format(ip_address)

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
    print("Welcome to the Reverse DNS Lookup Tool!")

    while True:
        ip_address = input("\nEnter an IP address for reverse DNS lookup: ")
        result = reverse_dns_lookup(ip_address)
        
        if "failed" in result.lower():
            print(result)
        else:
            print("Reverse DNS lookup for {} is: {}".format(ip_address, result))
        
        if not input("\nDo you want to perform another reverse DNS lookup? (y/n): ").lower() == 'y':
            print("Program closed. Thank you for using the Reverse DNS Lookup Tool!")
            break
