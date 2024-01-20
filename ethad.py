from ecpy.curves import Curve
from ecpy.keys import ECPublicKey, ECPrivateKey
from sha3 import keccak_256
import requests
import json
import time
nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337
def fastcheck(string,tokename):
        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
        response_API = requests.get('https://api.blockchair.com/ethereum/dashboards/address/'+str(string)+'?'+str(tokename)+'=true&nonce=true',headers=headers)
        old=0
        if (response_API.status_code)==200:
          try:  
            data = response_API.text
            parse_json = json.loads(data)
            active_case = parse_json['data'][str(string)]['address']['balance_usd']
            if active_case!=0:
                print(string)
                print(active_case)
            
          except:
            old+=1
            if old>50000:
                print('maybe its time to change the range')
            
        elif (response_API.status_code)=='404':
            ha='ssss'
        elif (response_API.status_code)=='500':
            print(response_API.status_code)
            print('you should change ip, i dont like to change it, you do it.')
            print(number)
            number=100000000000
        else:
            print(response_API.status_code)
#private_key = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
def converter(string):
    private_key=(int(string)%nnn)
    cv = Curve.get_curve('secp256k1')
    pv_key = ECPrivateKey(private_key, cv)
    pu_key = pv_key.get_public_key()
    concat_x_y = pu_key.W.x.to_bytes(32, byteorder='big') + pu_key.W.y.to_bytes(32, byteorder='big')
    eth_addr = '0x' + keccak_256(concat_x_y).digest()[-20:].hex()
    fastcheck(eth_addr,'trc_20')
##    fastcheck(eth_addr,'erc_20')
# equivalent alternative for illustration:
# concat_x_y = bytes.fromhex(hex(pu_key.W.x)[2:] + hex(pu_key.W.y)[2:])

with open("vicx") as f:
    k=0
    for needle3d in f:
        time.sleep(60) 
        converter(needle3d.strip())
        k+=1
        if k%20==0:
            time.sleep(600) 

#fastcheck('0x71e74889810dfe04e6ab9b19f0b7d59b8d22177d','trc_20')

#print('private key: ', hex(private_key))
#print('eth_address: ', eth_addr)