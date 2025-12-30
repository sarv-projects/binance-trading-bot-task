import os
from dotenv import load_dotenv
from bot import BinanceBot
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# Load environment variables
load_dotenv()
API_KEY = os.getenv('BINANCE_TESTNET_API_KEY')
API_SECRET = os.getenv('BINANCE_TESTNET_API_SECRET')

def print_header():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "      CRYPTO FUTURES TRADING BOT (TESTNET)      ")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

def get_user_input():
    try:
        symbol = input(Fore.GREEN + "Enter Symbol (e.g., BTCUSDT): " + Style.RESET_ALL).upper()
        side = input(Fore.GREEN + "Enter Side (BUY/SELL): " + Style.RESET_ALL).upper()
        
        print("\nAvailable Types: MARKET, LIMIT, STOP_LOSS")
        order_type = input(Fore.GREEN + "Enter Order Type: " + Style.RESET_ALL).upper()
        
        quantity = float(input(Fore.GREEN + "Enter Quantity: " + Style.RESET_ALL))
        
        price = None
        if order_type in ['LIMIT', 'STOP_LOSS']:
            price = float(input(Fore.GREEN + "Enter Price: " + Style.RESET_ALL))
            
        return symbol, side, order_type, quantity, price
    except ValueError:
        print(Fore.RED + "Invalid number format. Please try again." + Style.RESET_ALL)
        return None

def main():
    if not API_KEY or not API_SECRET:
        print(Fore.RED + "Error: API keys not found in .env file." + Style.RESET_ALL)
        return

    bot = BinanceBot(API_KEY, API_SECRET)
    print_header()
    
    # Show current balance
    balance = bot.get_account_balance()
    print(f"Current USDT Balance: {Fore.YELLOW}{balance}{Style.RESET_ALL}\n")

    while True:
        data = get_user_input()
        if not data:
            continue
            
        symbol, side, order_type, quantity, price = data
        
        print(Fore.YELLOW + "\nProcessing Order..." + Style.RESET_ALL)
        result = bot.place_order(symbol, side, order_type, quantity, price)
        
        if "error" in result:
            print(Fore.RED + f"Order Failed: {result['error']}" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Order Executed Successfully!" + Style.RESET_ALL)
            print(f"Order ID: {result.get('orderId')}")
            print(f"Status: {result.get('status')}")
        
        # Ask to continue
        cont = input("\nPlace another order? (y/n): ").lower()
        if cont != 'y':
            print("Exiting. Check trading_bot.log for history.")
            break

if __name__ == "__main__":
    main()