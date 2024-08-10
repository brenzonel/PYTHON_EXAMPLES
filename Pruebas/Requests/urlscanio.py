import requests
import os
from dotenv import load_dotenv
import json

load_dotenv(override=True)
key_scanio = os.getenv('KEY_SCANIO')

def urlscan(url):
    search_url = 'https://urlscan.io/api/v1/scan/'
    key = key_scanio

    #input_url = input('Enter the URL or domain to scan: ')
    data = {"url": url, "visibility": "public"}

    headers = {
        'API-Key': key,'Content-Type':'application/json'
    }

    response = requests.post(search_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print('URL submitted successfully')
        print(response)
        print(response.json())
    else:
        print('Failed to submit URL')
        print(response)
        print(response.json())
        print(data)

def scanurl_phishing(name):
    search_url = 'https://urlscan.io/api/v1/scan/'
    key = key_scanio

    #query = "*page.domain: *"+name+"* NOT page.domain:"+name+"e.com"
    query = "*page.domain: *tik* NOT page.domain:tiktok.com"

    headers = {
        'API-Key': key
    }

    response = requests.get(search_url, params={"q": query}, headers=headers)
    data = response.json()

    if response.status_code == 200:
        print('URL submitted successfully')
        unique_urls = set()

        for result in data.get('results', []):
            url = result['page']['url']
            unique_urls.add(url)
        
        print(f"Número total de enlaces: {len(unique_urls)}")
        print("Enlaces encontrados:")
        print(query)
        for url in unique_urls:
            print(url)

    else:
        print('Failed to submit URL')
        print(response)
        print(response.json())
        print(data)

if __name__ == '__main__':
    print("Menu:\n1. Escanear URL\n2. Buscar phishing")
    option = input('Elegir opcion: ')
    if option == '1':
        url = input('Enter the URL or domain to scan: ')
        urlscan(url)
    elif option == '2':
        name = input('Enter the domain name to search: ')
        scanurl_phishing(name)
    else:
        print('Opcion no valida')