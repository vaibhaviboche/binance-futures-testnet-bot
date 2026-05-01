\## Run Examples



Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001



Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000



\## Environment Variables



Create a `.env` file:



BINANCE\_API\_KEY=your\_api\_key

BINANCE\_API\_SECRET=your\_api\_secret



\## Logs



Logs are generated in `logs/trading\_bot.log`

