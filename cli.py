import sys
from colorama import Fore, Style, init
from bot.logging_config import setup_logging
from bot.client import BinanceClientWrapper
from bot.orders import place_order
from bot.validators import validate_input

# Init
init(autoreset=True)
setup_logging()

def main():
    print(Fore.CYAN + "=== Binance Futures Bot (Testnet) ===")

    # 1. Connect
    try:
        wrapper = BinanceClientWrapper()
        client = wrapper.get_client()
        print(Fore.GREEN + "✔ Connected to Binance")
    except Exception as e:
        print(Fore.RED + f"✘ Connection Failed: {e}")
        sys.exit(1)

    # 2. Input Loop
    while True:
        try:
            print("\n" + Fore.YELLOW + "--- New Order ---")
            symbol = input("Symbol (e.g. BTCUSDT): ").strip().upper()
            side = input("Side (BUY/SELL): ").strip().upper()
            order_type = input("Type (MARKET/LIMIT): ").strip().upper()
            qty_str = input("Quantity: ").strip()
            
            # Basic type conversion
            try:
                quantity = float(qty_str)
            except ValueError:
                print(Fore.RED + "Invalid quantity.")
                continue

            price = None
            if order_type == 'LIMIT':
                p_str = input("Price: ").strip()
                try:
                    price = float(p_str)
                except ValueError:
                    print(Fore.RED + "Invalid price.")
                    continue

            # 3. Validate
            errors = validate_input(symbol, side, order_type, quantity, price)
            if errors:
                for e in errors:
                    print(Fore.RED + f"Validation Error: {e}")
                continue

            # 4. Execute
            print("Processing...")
            result = place_order(client, symbol, side, order_type, quantity, price)

            # 5. Output
            if "error" in result:
                print(Fore.RED + f"Failed: {result['error']}")
            else:
                print(Fore.GREEN + "✔ SUCCESS")
                print(f"Order ID: {result['orderId']}")
                print(f"Status: {result['status']}")

            # Log location reminder
            print(Style.DIM + "(Logged to trading_bot.log)")

            if input("\nQuit? (y/n): ").lower() == 'y':
                break

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()