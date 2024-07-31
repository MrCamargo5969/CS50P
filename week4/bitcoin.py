import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit(1)

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    texto_completo = response.text
    dados = response.json()
    data = dados["bpi"]["USD"]["rate_float"]

except requests.RequestException:
    sys.exit(1)

if sys.argv[1].isalpha():
    sys.exit(1)
else:
    amount = float(data) * float(sys.argv[1].replace(",","."))
    print(f"${amount:,.4f}")
    sys.exit(0)
