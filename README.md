# DNS Lookup Tool
[![Stars](https://img.shields.io/github/stars/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/stargazers) [![License](https://img.shields.io/github/license/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/blob/main/LICENSE) [![Issues](https://img.shields.io/github/issues/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/issues) [![Forks](https://img.shields.io/github/forks/Jvr2022/Dns-lookup)](https://github.com/Jvr2022/Dns-lookup/network/members)

Welcome to the DNS Lookup Tool repository! This tool allows you to perform various DNS-related queries for domain names. Explore the provided functionalities and stay tuned for further updates and enhancements as the project evolves.

We're excited to announce that the tool has transitioned from beta to its first stable release (version 1.0.0). This release introduces comprehensive error handling and reporting, DNSSEC validation status checking, and other improvements.

We encourage you to provide feedback, report any issues you encounter, and contribute to the project's development. Your input is valuable in shaping the future of the DNS Lookup Tool.

## Features

- [x] Perform DNS lookups for domain names.
- [x] View IP addresses associated with a domain.
- [x] Retrieve MX records for email server information.
- [x] Fast and reliable DNS queries.
- [x] Geolocation of IP addresses.
- [x] Reverse DNS lookup for IP addresses.
- [x] Check domain availability.
- [x] Identify DNS propagation status.
- [x] Export query results to a file.
- [x] Support for custom DNS servers.
- [x] DNSSEC validation status.
- [x] Comprehensive error handling and reporting.

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
- `Check_domain_ability.py`: Check domain availability.

To use any of these scripts individually, navigate to the `tools` directory in your terminal and run the desired script using the `python` command.

### Example Usage

For example, to perform a reverse DNS lookup, you can do the following:

1. Open a terminal window.
2. Navigate to the `tools` directory using the `cd` command.
3. Run the following command: `python reverse_dns.py`
4. Follow the on-screen instructions to input the IP address and view the reverse DNS lookup result.

## License

This project is licensed under the terms of the Apache License 2.0.

## What's Coming in DNS Lookup Tool v1.0.1

We're excited to present the upcoming features and improvements planned for version 1.0.1 of the DNS Lookup Tool. Our goal is to enhance your DNS querying experience with added functionality and increased reliability. Here's a glimpse of what you can expect:

- [x] **Comprehensive Error Handling:** Enjoy a more robust tool with enhanced error handling and informative error messages.
- [x] **Detailed Query Reports:** Get more detailed and structured reports for each query, including success and failure cases.
- [x] **Enhanced User Prompts:** Improve user prompts and instructions for a smoother and friendlier experience.
- [x] **Bug Fixes:** Resolve reported issues.
- [x] **Stability Improvements:** General stability enhancements to ensure consistent and reliable performance.
- [x] **Updated Documentation:** Revised and expanded documentation to provide clearer usage instructions.

Stay tuned for the release of version 1.0.1, where these exciting features will become available. We value your feedback and suggestions, so please share your thoughts to help us refine the DNS Lookup Tool even further.

## Version 1.0.1 Progress Checklist

- [x] Comprehensive Error Handling
- [ ] Detailed Query Reports
- [ ] Enhanced User Prompts
- [x] Bug Fixes
- [ ] Stability Improvements
- [ ] Updated Documentation

As development progresses, we'll update this checklist to reflect the completion of each feature. Your support and feedback are invaluable in making the DNS Lookup Tool an indispensable resource.
