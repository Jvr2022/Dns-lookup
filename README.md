# DNS Lookup Tool
[![Stars](https://img.shields.io/github/stars/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/stargazers) [![License](https://img.shields.io/github/license/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/blob/main/LICENSE) [![Issues](https://img.shields.io/github/issues/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/issues) [![Forks](https://img.shields.io/github/forks/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/network/members)

> [!WARNING]  
> This project was deprecated on January 1, 2024. We have now resumed updates for this tool as of June 11, 2024. During this transition period, some features may not function as expected. We appreciate your patience and understanding as we work to improve and enhance the tool.

Welcome to the DNS Lookup Tool repository! This tool allows you to perform various DNS-related queries for domain names. Explore the provided functionalities and stay tuned for further updates and enhancements as the project evolves.

## Installation Guide

To get started with the DNS Lookup Tool, follow these steps:

### Download the Release

1. Visit the [Releases page](https://github.com/Jvr2022/Dns-lookup/releases) of this repository.
2. Locate the latest release and download the ZIP file.
3. Extract the downloaded ZIP file to your desired location.

### Run the Tool

1. Open a terminal window.
2. Navigate to the directory where you extracted the source code using the `cd` command.
3. Run the following command to start the tool: `python dns_lookup.py`
4. Follow the on-screen instructions to perform DNS-related queries.

## Tools Directory

In addition to the main script `dns_lookup.py`, this repository includes a `tools` directory that contains individual scripts for each DNS-related query function. These standalone scripts can be used separately if you only need specific functionality.

### Script List

- `ip_addresses.py`: Perform DNS lookups and view IP addresses associated with a domain.
- `mx_records.py`: Retrieve MX records for email server information.
- `geolocation.py`: Geolocation of IP addresses.
- `reverse_dns.py`: Reverse DNS lookup for IP addresses.
- `check_domain_availability.py`: Check domain availability.

To use any of these scripts individually, navigate to the `tools` directory in your terminal and run the desired script using the `python` command.

### Example Usage

For example, to perform a reverse DNS lookup, you can do the following:

1. Open a terminal window.
2. Navigate to the `tools` directory using the `cd` command.
3. Run the following command: `python reverse_dns.py`
4. Follow the on-screen instructions to input the IP address and view the reverse DNS lookup result.

## License

This project is licensed under the terms of the Apache License 2.0.
