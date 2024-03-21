import requests
import json
# url = 'https://api.etherscan.io/api?module=contract&action=getabi&address=0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74&apikey=KFSPQHM6SZUVAJVDDTGW48M5TGWVQ31TI3'
# headers = {'content-type': 'application/json'}
# resp = requests.get(url=url,headers=headers).json()
# print(resp)

def get_abi(contract_address):
    #api文档中链接为https，可能被拒绝访问
    url = 'https://api.etherscan.io/api?module=contract&action=getabi&address=0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74&apikey=KFSPQHM6SZUVAJVDDTGW48M5TGWVQ31TI3'
    headers = {'content-type': 'application/json'}
    resp = requests.get(url=url, headers=headers)
    try:
        resp = resp.json()
        return resp
    except Exception:
        print(f"地址{contract_address}获取abi序列错误")
        return None

if __name__ == "__main__":
    abi = get_abi('0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74')
    print(abi)