from datetime import datetime
import pytz
import pandas as pd

from sqlalchemy.exc import SQLAlchemyError

from get_all_tickers import get_tickers as gt
import yfinance as yf

import sys
import os

script_directory = os.path.dirname(__file__)
root_directory = os.path.abspath(os.path.join(script_directory, '..', '..'))
sys.path.append(root_directory)


from common import model, common


from src.data import Auxiliary
from src.data import macro
from src.data.fetch_ticker import merged_data

def macro_daily():
    pass

def get_store_etf_data():
    list_of_tickers = merged_data
    snp = yf.Ticker(f"^GSPC").history(period="5y")['Close']

    for ticker in list_of_tickers:
        stock = yf.Ticker(f"{ticker}")
        # return 판다스 df 형식이다.

        volume = stock.info['averageVolume10days']
        price = stock.info['previousClose']
        name = stock.info['shortName']
        
        #베타 계수 계산
        hist = stock.history(period="5y")
        beta = Auxiliary.calculate_beta(hist['Close'], snp)


        hist.index = pd.to_datetime(hist.index)

        # 보조지표 계산용 계산용 볼륨 줄이기
        # Determine the last month's date range
        end_date = hist.index.max()  # Latest date available
        start_date = end_date - pd.DateOffset(months=2)  # One month before the latest date

        # Filter the DataFrame to include only rows within this date range
        last_month_data = hist.loc[start_date:end_date]


        # rsi
        rsi, rsi_signal = Auxiliary.calculate_rsi(last_month_data['Close'], window=14)
        today_rsi = rsi.iloc[-1]
        rsi_flag = 'OS' if today_rsi <= 30 else 'OB' if today_rsi >= 70 else 'N'

        # MACD
        macd, macd_signal = Auxiliary.calculate_MACD(last_month_data['Close'], short_window=12, long_window=26, signal_window=9)
        today_macd = macd.iloc[-1]

        # stochastic
        stochastic_k, stochastic_d = Auxiliary.calculate_stochastic(last_month_data['Close'], window=14, smooth_k=3, smooth_d=3)
        today_stochastic_slow_k = stochastic_k.iloc[-1]
        today_stochastic_slow_d = stochastic_d.iloc[-1]

        stochastic_slow_k_flag = 'OS' if today_stochastic_slow_k <= 20 else 'OB' if today_stochastic_slow_k >= 80 else 'N'
        stochastic_slow_d_flag = 'OS' if today_stochastic_slow_d <= 20 else 'OB' if today_stochastic_slow_d >= 80 else 'N'

        
        # cci
        cci, cci_signal = Auxiliary.calculate_cci(last_month_data['Close'], window=20)
        today_cci = cci.iloc[-1]

        cci_flag = 'OS' if today_cci <= -100 else 'OB' if today_cci >= 100 else 'N'

        #bollingerband
        lower_band, middle_band, upper_band = Auxiliary.calculate_stochastic(last_month_data['Close'], window=14, smooth_k=3, smooth_d=3)
        today_lower_band = lower_band.iloc[-1]
        today_middle_band = middle_band.iloc[-1]
        today_upper_band = upper_band.iloc[-1]

        bollinger_band_flag = 'OS' if price <= today_lower_band else 'OB' if price >= today_upper_band else 'N'

        #시간대 설정
        utc_dt = datetime.now(pytz.utc)
        eastern_tz = pytz.timezone('America/New_York')
        eastern_dt = utc_dt.astimezone(eastern_tz)
        formatted_date_us = utc_dt.strftime('%Y%m%d')
        korea_tz = pytz.timezone('Asia/Seoul')
        korea_dt = utc_dt.astimezone(korea_tz)
        formatted_date_kr = korea_dt.strftime('%Y%m%d')

        data_instance = model.Stocks(
            ticker=ticker,
            date_info = formatted_date_us,
            stock_name=name,
            stock_price=price,
            category='ETF',
            rsi=today_rsi,
            rsi_flag=rsi_flag,
            beta=beta,
            macd=today_macd,
            stochastic_slow_d=today_stochastic_slow_d,
            stochastic_slow_k=today_stochastic_slow_k,
            stochastic_slow_d_flag=stochastic_slow_d_flag,
            stochastic_slow_k_flag=stochastic_slow_k_flag,
            cci=today_cci,
            cci_flag=cci_flag,
            bollinger_band_upper=today_upper_band,
            bollinger_band_middle=today_middle_band,
            bollinger_band_lower=today_lower_band,
            bollinger_band_flag=bollinger_band_flag,
            rgtr_dt = utc_dt
        )

        try:
            common.session.add(data_instance)
        except SQLAlchemyError as e:
            common.session.rollback()
            common.logger.error("DB OP failed", exc_info=True)
            raise e

        
    common.session.commit()
    common.session.close()

def get_store_macro_daily_data():
    fear_and_greed, fear_and_greed_flag, market_momentum, stock_price_strength, stock_price_breadth, put_and_call_option, market_volatility, safe_haven_demand, junk_bond_demand = macro.fear_and_greed_list 

    #시간대 설정
    utc_dt = datetime.now(pytz.utc)
    eastern_tz = pytz.timezone('America/New_York')
    eastern_dt = utc_dt.astimezone(eastern_tz)
    formatted_date_us = utc_dt.strftime('%Y%m%d')
    korea_tz = pytz.timezone('Asia/Seoul')
    korea_dt = utc_dt.astimezone(korea_tz)
    formatted_date_kr = korea_dt.strftime('%Y%m%d')

    data_instance = model.MacroDaily(
        date_info = formatted_date_us,
        fear_and_greed_idx=fear_and_greed,
        fear_and_greed_flag=fear_and_greed_flag,
        market_momentum=market_momentum,
        stock_price_strength=stock_price_strength,
        stock_price_breadth=stock_price_breadth,
        put_and_call_option=put_and_call_option,
        market_volatility=market_volatility,
        safe_haven_demand=safe_haven_demand,
        junk_bond_demand=junk_bond_demand,
        rgtr_dt=utc_dt
    )


    try:
        common.session.add(data_instance)
    except SQLAlchemyError as e:
        common.session.rollback()
        common.logger.error("DB OP failed", exc_info=True)
        raise e

def get_macro_indicator():
    #시간대 설정
    utc_dt = datetime.now(pytz.utc)
    eastern_tz = pytz.timezone('America/New_York')
    eastern_dt = utc_dt.astimezone(eastern_tz)
    formatted_date_us = utc_dt.strftime('%Y%m%d')

    korea_tz = pytz.timezone('Asia/Seoul')
    korea_dt = utc_dt.astimezone(korea_tz)
    formatted_date_kr = korea_dt.strftime('%Y%m%d')
    
    macro_event_list = macro.macro_event_list

    for macro_event in macro_event_list:

        time, importance, event, actual, forecast, previous, category = macro_event
        # 실행일 기준 날짜 해당 시간으로 저장.

        date_info = f"{formatted_date_us}"
        release_date = f"{formatted_date_us} {time}" 


        data_instance = model.MacroEvent(
            event_name= event,
            date_info = date_info,
            importance = importance,
            category = category,
            actual = actual,
            forecast = forecast,
            previous = previous,
            rgtr_dt=utc_dt
        )

        try:
            common.session.add(data_instance)
        except SQLAlchemyError as e:
            common.session.rollback()
            common.logger.error("DB OP failed", exc_info=True)
            raise e
    
    try: 
        common.session.commit()
        common.session.close()
    except SQLAlchemyError as e:
        common.session.rollback()
        common.logger.error("DB OP failed", exc_info=True)
        raise e

        #stock price 3$ 이상, 거래량 10k이상, rsi 35 이하, 베타 계수 1.5 이상.

        # 이후 rdb 해당 종목과 데이터 저장.

        
    # msft = yf.Ticker("MSFT")
