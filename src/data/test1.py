import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)

import yfinance as yf
import pandas as pd
# from common.technical_analysis import calculate_macd, calculate_cci, calculate_stochastic, calculate_rsi, calculate_bollinger_bands, calculate_moving_averages
# from common.fundamental_analysis import calculate_all_metrics

pd.set_option('display.max_columns', None)

def test1():
    ticker_symbol = ["AAL", "MSFT"]

    ticker = yf.Ticker(["AAL", "MSFT"])

    historical_data = ticker.history(period="3mo")  # 지난 2개월 데이터

    if historical_data.empty:
        print(f"데이터를 가져올 수 없습니다: {ticker_symbol}")
        return None

    # 데이터 준비
    historical_data = historical_data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    # 티커명 추가
    historical_data['Ticker'] = ticker_symbol

    print(historical_data)

    # print(ticker.info)

    # financials = ticker.financials
    # balance_sheet = ticker.balance_sheet
    # print(balance_sheet)
    # print(financials)
    # expense = financials.loc['Interest Expense', financials.columns[0]]
    # print(expense)

    # debt = balance_sheet.loc['Total Debt', balance_sheet.columns[0]]

    # print(debt)
    # print(ticker.history(period="3mo"))
    # cashflow = ticker.cashflow
    # print(cashflow)
    # cfo = cashflow.loc['Free Cash Flow', cashflow.columns[0]]  # 최신 CFO
    # print(cfo)

    # capex = cashflow.loc['Capital Expenditures'][0]  # 최신 CAPEX

    # print(cfo, capex)

    # fcf = cfo - abs(capex)

    # print(fcf)

test1()