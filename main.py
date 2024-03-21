#获取abi和字节码，并输出到csv文件中
import getABI
import getBYTECODE
import pandas as pd
import json
#从文件中读入合约地址，返回一个list= [add1,add2,...]
def read(path):
    df = pd.read_csv(path)
    contract_address = df['Contract']
    # print(contract_address)
    return contract_address



 #根据地址获取ABI和BYTECODE并输出到csv
def obtain(address_list):
    abis = []
    byte_codes = []
    for index,address in enumerate(address_list):
        if index <=3256:
            continue
        abi = getABI.get_abi(address)
        if abi ==None:
            abi='None'
        else:
            abi = abi['result']
        abis.append(abi)
        # print(abi)
        byte_code = getBYTECODE.get_bytecode(address)
        if byte_code == None :
            byte_code = "None"
        else:
            byte_code = byte_code['result']
        byte_codes.append(byte_code)
        #print(byte_code)
        print('正在处理第{}条',index)
        dic = {
            'address': [address],
            'bytecode': [byte_code],
            'ABI': [abi]
        }
        df = pd.DataFrame(dic)
        if index==0:
            df.to_csv('outputdata.csv',index = False)
        else:
            df.to_csv('outputdata.csv', mode='a',header=False,index=False)


if __name__ =="__main__":
    path = 'C:\\Users\\63474\\Desktop\\毕设\\Ponzi_label.csv'
    contract_address = read(path)
    obtain(contract_address)



