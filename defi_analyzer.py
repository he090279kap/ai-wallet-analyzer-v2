import requests
from config import DEFI_LLAMA_API_URL

def analyze_defi_activity(wallet_address):
    url = f"{DEFI_LLAMA_API_URL}/user/{wallet_address}"
    response = requests.get(url).json()

    if "protocols" in response:
        defi_activity = response["protocols"]
    else:
        defi_activity = []

    return defi_activity
