import requests
import json
url = 'http://api.etherscan.io/api?module=contract&action=getabi&address=0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74&apikey=KFSPQHM6SZUVAJVDDTGW48M5TGWVQ31TI3'
headers = {'content-type': 'application/json'}
resp = requests.get(url=url,headers=headers).json()
print(resp)