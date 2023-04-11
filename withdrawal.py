import requests
from bybit_utils import get_timestamp, generate_signature

api_key = ''
api_secret = ''
# base_url = 'https://api-testnet.bybit.com'
base_url = 'https://api.bybit.com'
# base_url = 'https://api.bytick.com'

def withdraw_usdc(amount, address, chain):
    timestamp = get_timestamp()
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': str(timestamp),
        'Content-Type': 'application/json'
    }
    params = {
        'coin': 'MATIC',
        'chain': chain,
        'address': address,
        'amount': amount,
        'timestamp': timestamp,
        'forceChain': 0,
        'accountType': 'SPOT'
    }
    signature = generate_signature(api_secret, params)
    headers['X-BAPI-SIGN'] = signature

    response = requests.post(base_url + '/v5/asset/withdraw/create', headers=headers, json=params)
    return response.json()

if __name__ == "__main__":
    amount = 1.4
    address = '0x5885E0B0b00D512aD115C8727553755204A89a45'
    chain = 'MATIC'

    print(f"Request:\nCoin: USDC\nChain: {chain}\nAddress: {address}\nAmount: {amount}\n")

    withdrawal_response = withdraw_usdc(amount, address, chain)
    print(f"Response:\n{withdrawal_response}")