# Binance Futures Trading Bot

A modular Python application for trading on the Binance Futures Testnet.


## Project Structure
The code is organized into a modular package structure for maintainability:
- `cli.py`: Entry point handling user interaction and display.
- `bot/client.py`: Encapsulates Binance API authentication and connection.
- `bot/orders.py`: Contains core order placement logic.
- `bot/validators.py`: Dedicated input validation logic.
- `bot/logging_config.py`: Centralized logging configuration.

## Setup
1. Install dependencies:
   `pip install -r requirements.txt`
2. Create `.env` file with your Testnet credentials:

   BINANCE_TESTNET_API_KEY=your_key BINANCE_TESTNET_API_SECRET=your_secret 

3. Run the application:
`python cli.py`

## Usage (Bonus Feature)
The application uses an interactive CLI menu (Enhanced UX) to guide the user through:
- Validating inputs (Symbol, Side, Quantity).
- Placing **MARKET** and **LIMIT** orders.
- Viewing real-time response data (Order ID, Status).

Logs are automatically saved to `trading_bot.log`.   