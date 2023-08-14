import socket

def reverse_dns_lookup(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        return host_name[0]
    except socket.herror as e:
        return "Reverse DNS lookup failed: {}".format(e)

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
    while True:
        ip_address = input("Enter an IP address for reverse DNS lookup: ")
        result = reverse_dns_lookup(ip_address)

        if result.startswith("Reverse DNS lookup failed"):
            print(result)
        else:
            print("Reverse DNS lookup for {} is: {}".format(ip_address, result))

        if not ask_to_restart():
            print("Program closed.")
            break
