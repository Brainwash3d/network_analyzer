import requests

def query_threat_intelligence(ip):
    url = f"https://api.abuseipdb.com/api/v2/check"
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': '7610580cdbf58d483ded2e0c552bbfe072c3460ad184313a31a56b4d199833d049138089813bf37d'  
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return {'ip': ip, 'error': 'Failed to retrieve information'}
