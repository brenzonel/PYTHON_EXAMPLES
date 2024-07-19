import requests
import os
from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv(override=True)
api_allprod = os.getenv('URL_PRODUCT_LIST')
api_prod = os.getenv('URL_PRODUCT')
api_loggin = os.getenv('URL_LOGIN')
api_reg = os.getenv('URL_REGISTER')
user = os.getenv('USER')
pwd = os.getenv('PWD')

try:
    #response = requests.get(api_url)
    #print(response.json())
    loggin = {
        "email": user,
        "password": pwd
    }
    new_user = {
        "name": "Python",
        "email": "pruebapython@python.com",
        "password": "123456",
        "phone": "1234567890",
        "address": "Python",
        "answer": "Python",
        "role": 1
    }
    
    #resp_loggin = requests.post(api_loggin, json=loggin)
    #resp_loggin.raise_for_status()
    #resp_loggin_dict = resp_loggin.json()
    #print(resp_loggin_dict)
    #print(resp_loggin_dict['token'])

    res_reg = requests.post(api_reg, json=new_user)
    res_reg.raise_for_status()
    res_reg_dict = res_reg.json()
    print(res_reg_dict)

except Exception as e:
    print(f'Other Error: {e}')
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")