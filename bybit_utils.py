import hmac
import hashlib
import json
import time

# Other imports and functions

def get_timestamp():
    return int(time.time() * 1000)

def generate_signature(secret, params):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    return hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

