# Python Crypto Trading Bot (Testnet)

A robust command-line trading bot developed for the Primetrade.ai Technical Assessment.

## Features
- **Smart Execution**: Supports MARKET, LIMIT, and STOP_LOSS orders.
- **Safety First**: Environment variable management for API keys.
- **Logging**: Comprehensive transaction logging to `trading_bot.log`.
- **Error Handling**: Graceful handling of network and API exceptions.

## Tech Stack
- Python 3.x
- python-binance
- Colorama (for CLI interface)

## Setup
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file with `BINANCE_TESTNET_API_KEY` and `BINANCE_TESTNET_API_SECRET`.
4. Run `python main.py`.