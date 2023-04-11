import requests
from bybit_utils import get_timestamp, generate_signature

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
# base_url = 'https://api-testnet.bybit.com'
base_url = 'https://api.bybit.com'
# base_url = 'https://api.bytick.com'

def get_withdrawal_records(coin, withdraw_type, limit):
    timestamp = get_timestamp()
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': str(timestamp),
    }
    params = {
        'coin': coin,
        'withdrawType': withdraw_type,
        'limit': limit
    }
    signature = generate_signature(api_secret, params)
    headers['X-BAPI-SIGN'] = signature

    response = requests.get(base_url + '/v5/asset/withdraw/query-record', headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    coin = 'MATIC'
    withdraw_type = 2
    limit = 2

    withdrawal_records = get_withdrawal_records(coin, withdraw_type, limit)
    print(withdrawal_records)
