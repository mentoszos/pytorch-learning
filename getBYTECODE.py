import requests
import json

# url = 'https://red-tiniest-hill.quiknode.pro/09f02c80ed7d825353643080c653d3a34dc1534b/'
url = 'https://mainnet.infura.io/v3/6fecd335ff59422abf3617ea28f4874e'

payload = {
    "jsonrpc": "2.0",
    "method": "eth_getCode",
    "params": [
        "0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74",
        "latest"
    ],
    "id": 1
}

headers = {'content-type': 'application/json',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()

print(response)