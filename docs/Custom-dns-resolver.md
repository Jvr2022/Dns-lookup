# Custom DNS Resolver Configuration Documentation

The "Custom DNS Resolver Configuration" feature allows users to input their preferred DNS server addresses, offering greater control over the DNS resolution process. This documentation explains how to use and benefit from this feature in the DNS Lookup Tool.

## How to Use

1. **Run the Script:** Execute the script in your terminal.
2. **Enter Domain:** Input the domain name you want to perform DNS queries for.
3. **Custom DNS Servers:** When prompted, indicate if you want to use custom DNS servers.
   - If yes, proceed to step 4.
   - If no, the script will use the default DNS servers (8.8.8.8 and 8.8.4.4).

4. **Input Custom DNS Servers:** If you chose to use custom DNS servers, provide the IP addresses separated by commas (e.g., "8.8.8.8,8.8.4.4").
5. The script will configure the DNS resolver to use the specified custom DNS servers for the query.

## Benefits

The "Custom DNS Resolver Configuration" feature offers the following benefits:

- **Flexibility:** Users can utilize their preferred DNS servers for queries, allowing customization of the DNS resolution process.
- **Potential Speed Improvement:** Custom DNS servers might offer faster query responses based on user preferences and server performance.

## Example

Suppose you want to use Google's DNS servers (8.8.8.8 and 8.8.4.4) for DNS resolution instead of the default servers. Here's how you can use the feature:

1. Run the script.
2. Enter the domain name you want to query.
3. When prompted, input "y" to use custom DNS servers.
4. Enter "8.8.8.8,8.8.4.4" as the custom DNS server addresses.
5. The script will configure the DNS resolver to use the specified custom DNS servers for the query.

## Note

- If you encounter any issues or want to revert to the default DNS servers, choose not to use custom DNS servers during the query process.
