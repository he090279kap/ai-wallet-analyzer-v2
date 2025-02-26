import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
SOLANA_API_URL = "https://api.solana.com"
