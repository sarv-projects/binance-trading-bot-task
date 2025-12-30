import logging
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from binance.enums import *

# Setup Logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BinanceBot:
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the connection to Binance Spot Testnet.
        """
        try:
            # Initialize Client
            self.client = Client(api_key, api_secret)
            # FORCE the client to use the Spot Testnet URL
            self.client.API_URL = 'https://testnet.binance.vision/api'
            
            # Test connection by fetching account info
            self.client.get_account()
            logging.info("Initialized Binance Client on Spot Testnet.")
            print("Successfully connected to Binance Spot Testnet.")
        except Exception as e:
            logging.error(f"Initialization Error: {e}")
            raise e

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """
        Place an order on Binance Spot.
        """
        try:
            logging.info(f"Attempting to place {side} {order_type} order for {quantity} {symbol}")
            
            # Base parameters
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }

            # Handle LIMIT orders
            if order_type == ORDER_TYPE_LIMIT:
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params['timeInForce'] = TIME_IN_FORCE_GTC
                params['price'] = str(price)
            
            # BONUS: Handle STOP_LOSS (Mapped to STOP_LOSS_LIMIT for Spot)
            elif order_type == 'STOP_LOSS':
                if not price:
                    raise ValueError("Stop Price is required for STOP_LOSS orders.")
                params['type'] = ORDER_TYPE_STOP_LOSS_LIMIT
                params['timeInForce'] = TIME_IN_FORCE_GTC
                params['stopPrice'] = str(price)
                params['price'] = str(price) # Limit price same as stop price
            
            # Send request to Binance
            response = self.client.create_order(**params)
            
            logging.info(f"Order Success: {response}")
            return response

        except BinanceAPIException as e:
            # This catches specific Binance errors (like Insufficient Balance)
            logging.error(f"Binance API Error: {e.message}")
            return {"error": e.message}
        except Exception as e:
            logging.error(f"General Error: {str(e)}")
            return {"error": str(e)}

    def get_account_balance(self):
        """Helper to check USDT balance"""
        try:
            info = self.client.get_account()
            for asset in info['balances']:
                if asset['asset'] == 'USDT':
                    return asset['free']
            return "0.0"
        except Exception as e:
            logging.error(f"Error fetching balance: {e}")
            return "N/A"