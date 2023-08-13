import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "DNS lookup failed for {}".format(domain)

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    ip_address = get_ip_address(domain_name)
    
    if ip_address.startswith("DNS lookup failed"):
        print(ip_address)
    else:
        print("IP address of {} is: {}".format(domain_name, ip_address))

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
