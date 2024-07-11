import requests

def query_threat_intelligence(ip):
    url = f"https://api.abuseipdb.com/api/v2/check"
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'API_KEY'  
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return {'ip': ip, 'error': 'Failed to retrieve information'}
