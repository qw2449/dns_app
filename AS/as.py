import socket
import json


as_ip = '0.0.0.0'
as_port = 53533
dns_records_file = 'dns_records.json'

# Load existing DNS records from the file
try:
    with open(dns_records_file, 'r') as file:
        dns_records = json.load(file)
except FileNotFoundError:
    dns_records = {}

# Function to save DNS records to a file
def save_dns_records(records):
    with open(dns_records_file, 'w') as file:
        json.dump(records, file)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((as_ip, as_port))

print(f"Authoritative Server listening on port {as_port}")

while True:
    # Listen for incoming datagrams
    data, address = sock.recvfrom(1024)
    
    # Parse the message
    message = data.decode()
    lines = message.split('\n')
    
    # Handle registration
    if lines[0] == 'TYPE=A':
        name = lines[1].split('=')[1]
        value = lines[2].split('=')[1]
        ttl = lines[3].split('=')[1]
        
        # Store the record
        dns_records[name] = {"TYPE": "A", "VALUE": value, "TTL": ttl}
        save_dns_records(dns_records)
        
        # Send a response to acknowledge the registration
        sock.sendto(b"200 Registration Successful", address)
    
    # Handle DNS query
    else:
        query_name = lines[1].split('=')[1]
        if query_name in dns_records:
            # Found the record, send it back
            record = dns_records[query_name]
            response = f"TYPE={record['TYPE']}\nNAME={query_name}\nVALUE={record['VALUE']}\nTTL={record['TTL']}"
            sock.sendto(response.encode(), address)
        else:
            # Record not found, send an error message
            sock.sendto(b"404 Not Found", address)
