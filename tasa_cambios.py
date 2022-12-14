import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=85698D70-C07F-437D-A26D-5B6802968843')

print(r.status_code)
print(r.text)

