# Binance Futures Testnet Bot

A Python-based command-line application that demonstrates REST API integration with the Binance Futures Demo/Test environment. The project focuses on modular Python development, API communication, input validation, error handling, and application logging.

> **Note:** This project is intended for learning and development purposes and uses a test/demo environment.

## Features

* Command-line interface using Python `argparse`
* REST API communication using `requests`
* HMAC-SHA256 request signing
* Support for MARKET and LIMIT order requests
* BUY and SELL side validation
* Input validation for symbols, quantity, and price
* Environment variable support for API credentials
* Network and API error handling
* Application logging
* Modular project structure

## Technologies Used

* **Python**
* **Requests**
* **python-dotenv**
* **REST API**
* **HMAC-SHA256**
* **argparse**
* **Logging**

## Project Structure

```text
binance-futures-testnet-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── cli.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Module Overview

**`cli.py`**

Provides the command-line interface and handles user-provided arguments such as symbol, side, order type, quantity, and price.

**`bot/client.py`**

Handles communication with the API, request signing, HTTP requests, and API/network error handling.

**`bot/orders.py`**

Contains the `OrderManager` responsible for preparing order parameters and passing requests to the API client.

**`bot/validators.py`**

Validates order information such as symbol, side, order type, quantity, and price.

**`bot/logging_config.py`**

Configures application logging and stores application logs in the `logs/` directory.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/vaibhaviboche/binance-futures-testnet-bot.git
cd binance-futures-testnet-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```text
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

**Never commit your `.env` file or API credentials to GitHub.**

## Application Usage

The application accepts command-line arguments for the order request.

Example command structure:

```bash
python cli.py --symbol SYMBOL --side SIDE --type ORDER_TYPE --quantity QUANTITY
```

For a LIMIT order, a price can also be provided.

The application displays an order request summary and handles the API response or error message.

## Validation

The application performs basic validation before sending a request.

It checks:

* USDT-M futures symbol format
* BUY or SELL side
* MARKET or LIMIT order type
* Positive quantity
* Required price for LIMIT requests
* Positive price for LIMIT requests

## Error Handling

The application handles:

* Missing API credentials
* Invalid input values
* Network-related errors
* API errors
* Unexpected request failures

Errors are also recorded through the application's logging system.

## Logging

Application logs are stored in:

```text
logs/trading_bot.log
```

The logging system records application events, API requests, API responses, and errors.

## Learning Outcomes

Through this project, I practiced:

* Python modular programming
* REST API integration
* HTTP requests
* HMAC-based request signing
* Command-line application development
* Input validation
* Exception handling
* Logging
* Environment variable management
* Organizing a Python project into reusable modules

## Future Improvements

Possible future improvements include:

* Automated unit testing
* Improved API response handling
* More comprehensive input validation
* Additional command-line options
* Better configuration management
* Improved application documentation

## Disclaimer

This project is created for educational and development purposes using a test/demo environment. It is not financial advice and should not be used as a production trading system.
