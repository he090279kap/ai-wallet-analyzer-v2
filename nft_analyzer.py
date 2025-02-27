import requests
from config import OPENSEA_API_URL

def analyze_nft_activity(wallet_address):
    url = f"{OPENSEA_API_URL}/account/{wallet_address}/nfts"
    response = requests.get(url).json()

    if "nfts" in response:
        nft_activity = response["nfts"]
    else:
        nft_activity = []

    return nft_activity
