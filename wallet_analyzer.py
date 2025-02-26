import requests
from config import ETHERSCAN_API_KEY, SOLANA_API_URL

def analyze_wallet(wallet_address):
    # Получение транзакций Ethereum
    eth_transactions = get_eth_transactions(wallet_address)
    
    # Получение транзакций Solana
    sol_transactions = get_solana_transactions(wallet_address)
    
    return {
        "wallet_address": wallet_address,
        "eth_transactions": eth_transactions,
        "sol_transactions": sol_transactions
    }

def get_eth_transactions(wallet_address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    return response["result"] if "result" in response else []

def get_solana_transactions(wallet_address):
    url = f"{SOLANA_API_URL}/account/{wallet_address}/transactions"
    response = requests.get(url).json()
    return response if response else []
