import logging
from binance.exceptions import BinanceAPIException

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }

        if order_type == 'LIMIT':
            params['timeInForce'] = 'GTC'
            params['price'] = str(price)

        logging.info(f"Sending Order: {params}")
        
        # Call Binance API
        response = client.futures_create_order(**params)
        
        logging.info(f"Order Created: ID {response['orderId']}")
        return response

    except BinanceAPIException as e:
        logging.error(f"Binance API Error: {e.message}")
        return {"error": e.message}
    except Exception as e:
        logging.error(f"System Error: {str(e)}")
        return {"error": str(e)}