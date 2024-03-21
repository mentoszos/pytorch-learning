import requests
import json

# url = 'https://red-tiniest-hill.quiknode.pro/09f02c80ed7d825353643080c653d3a34dc1534b/'
# # url = 'https://mainnet.infura.io/v3/6fecd335ff59422abf3617ea28f4874e'
#
# payload = {
#     "jsonrpc": "2.0",
#     "method": "eth_getCode",
#     "params": [
#         "0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74",
#         "latest"
#     ],
#     "id": 1
# }
#
# headers = {'content-type': 'application/json',
#            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
#
# response = requests.post(url, data=json.dumps(payload), headers=headers).json()
#
# print(response)

def get_bytecode(contract_address):
    #url二选一，有时因为网络因素不一定能用
    url = 'https://red-tiniest-hill.quiknode.pro/09f02c80ed7d825353643080c653d3a34dc1534b/'
    # url = 'https://mainnet.infura.io/v3/6fecd335ff59422abf3617ea28f4874e'

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getCode",
        "params": [
            contract_address,
            "latest"
        ],
        "id": 1
    }

    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    try:
        response = response.json()
        return response
    except Exception:
        print(f"地址：{contract_address}获取字节码错误")
        return None


if __name__ == "__main__":
    contract = get_bytecode('0x268b7976e94e84a48bf8B2B57Ba34b59eD836A74')
    print(contract)