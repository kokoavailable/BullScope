from get_all_tickers import get_tickers as gt
import yfinance as yf

import pandas as pd

from src.data import Auxiliary



def get_data():
    list_of_tickers = gt.get_tickers()
    snp = yf.Ticker(f"^GSPC").history(period="5y")['Close']

    for ticker in list_of_tickers:
        stock = yf.Ticker(f"{ticker}")
        # return 판다스 df 형식이다.
        
        #베타 계수 계산
        hist = stock.history(period="5y")
        beta = Auxiliary.calculate_beta(hist['Close'], snp)


        # rsi 계산용 볼륨 줄이기
        hist.index = pd.to_datetime(hist.index)

        # Determine the last month's date range
        end_date = hist.index.max()  # Latest date available
        start_date = end_date - pd.DateOffset(months=2)  # One month before the latest date

        # Filter the DataFrame to include only rows within this date range
        last_month_data = hist.loc[start_date:end_date]

        rsi = Auxiliary.calculate_rsi(last_month_data['Close'], window=14)
        todays_rsi = rsi.iloc[-1]

        if hist['Volume'].iloc[-1] < 10000 or todays_rsi > 40:
            break
        #거래량 10k이상, rsi 40 이하.

        # 이후 rdb 해당 종목과 데이터 저장. rsi, macd, cci, stochastic의 MAX 차트를 갖고 온다. 이건 분리.
        # 40이하인 종목에서 macd, cci, stochastic 를 저장하고 소위 말하는 과매수 구간이 되면 해당 플래그를 바꾼다.

        
    # msft = yf.Ticker("MSFT")

