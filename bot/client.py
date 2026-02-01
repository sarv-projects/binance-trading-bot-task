import os
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load env vars
load_dotenv()

class BinanceClientWrapper:
    def __init__(self):
        self.api_key = os.getenv('BINANCE_TESTNET_API_KEY')
        self.api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API Keys missing from .env file")

        try:
            # Connect to Futures Testnet
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            self.client.futures_ping()
            logging.info("Connected to Binance Futures Testnet")
        except Exception as e:
            logging.error(f"Connection failed: {e}")
            raise e

    def get_client(self):
        return self.client