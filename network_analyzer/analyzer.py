import psutil
import requests
import json
from .utils import query_threat_intelligence

def gather_network_info():
    connections = psutil.net_connections()
    network_info = []

    for conn in connections:
        if conn.raddr:
            network_info.append({
                'local_address': conn.laddr.ip,
                'local_port': conn.laddr.port,
                'remote_address': conn.raddr.ip,
                'remote_port': conn.raddr.port,
                'status': conn.status
            })

    return network_info

def main():
    network_info = gather_network_info()
    unique_ips = {conn['remote_address'] for conn in network_info if conn['remote_address']}

    print(f"Checking {len(unique_ips)} unique IPs against threat intelligence...")

    results = []
    for ip in unique_ips:
        result = query_threat_intelligence(ip)
        results.append(result)

    with open('network_threat_report.json', 'w') as f:
        json.dump(results, f, indent=4)

    print("Network threat report saved as 'network_threat_report.json'.")

if __name__ == '__main__':
    main()
