import yfinance as yf


msft = yf.Ticker("MSFT")

# print(msft)
# yfinance.Ticker object <MSFT>

# get all stock info
# msft.info
# address1': 'One Microsoft Way', 'city': 'Redmond', 'state': 'WA', 'zip': '98052-6399', 'country': 'United States', 'phone': '425 882 8080', 
print(msft.info)
# get historical market data
hist = msft.history(period="1mo")
#                                  Open        High         Low       Close    Volume  Dividends  Stock Splits
# Date                                                                                                        
# 2024-04-01 00:00:00-04:00  423.950012  427.890015  422.220001  424.570007  16316000        0.0           0.0
# print(hist)


# show meta information about the history (requires history() to be called first)
# msft.history_metadata
# print(msft.history_metadata)
# {'currency': 'USD', 'symbol': 'MSFT', 'exchangeName': 'NMS', 'fullExchangeName': 'NasdaqGS', 'instrumentType': 'EQUITY', 'firstTradeDate': 511108200,

# show actions (dividends, splits, capital gains)
# msft.actions
# # print(msft.actions)
# msft.dividends
# print(msft.dividends)
# msft.splits
# print(msft.splits)
# msft.capital_gains  # only for mutual funds & etfs
# print(msft.capital_gains)

# show share count 전체 발행주수
# msft.get_shares_full(start="2022-01-01", end=None)
# print(msft.get_shares_full(start="2022-01-01", end=None))
# # 2024-05-01 00:00:00-04:00    7432309760
# # 2024-05-01 00:00:00-04:00    7678949888

# show financials: 기본적 분석 할때 유용
# - income statement
# msft.income_stmt
# print(msft.income_stmt)
# msft.quarterly_income_stmt
# print(msft.quarterly_income_stmt)
# # - balance sheet
# msft.balance_sheet
# print(msft.balance_sheet)
# msft.quarterly_balance_sheet
# print(msft.quarterly_balance_sheet)
# - cash flow statement
# msft.cashflow
# print(msft.cashflow)
# msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
# msft.major_holders
# print(msft.major_holders)
# msft.institutional_holders
# print(msft.institutional_holders)
# msft.mutualfund_holders
# print(msft.mutualfund_holders)
# msft.insider_transactions
# print(msft.insider_transactions)
# msft.insider_purchases
# print(msft.insider_purchases)
# msft.insider_roster_holders
# print(msft.insider_roster_holders)

# # show recommendations
# msft.recommendations
# print(msft.recommendations)
# msft.recommendations_summary
# print(msft.recommendations_summary)
# msft.upgrades_downgrades
# print(msft.upgrades_downgrades)

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates
# print(msft.earnings_dates)

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
# msft.isin
# print(msft.isin)

# show options expirations
# msft.options
# print(msft.options)

# # show news
# msft.news
# print(msft.news)

# # get option chain for specific expiration
# opt = msft.option_chain('2024-05-10')
# print(opt)
# data available via: opt.calls, opt.puts