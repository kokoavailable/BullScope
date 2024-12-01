import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)

import yfinance as yf
import pandas as pd
from common.technical_analysis import calculate_macd, calculate_cci, calculate_stochastic, calculate_rsi, calculate_bollinger_bands, calculate_moving_averages
from common.common import etf_tickers
# ETF 티커 리스트

def fetch_and_calculate(ticker_symbol):
    """
    주어진 티커에 대해 데이터를 가져오고 기술적 지표를 계산하며, 티커명을 포함합니다.
    """
    try:
        # 데이터 가져오기
        ticker = yf.Ticker(ticker_symbol)
        historical_data = ticker.history(period="3mo")  # 지난 2개월 데이터
        if historical_data.empty:
            print(f"데이터를 가져올 수 없습니다: {ticker_symbol}")
            return None

        # 데이터 준비
        historical_data = historical_data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

        # 티커명 추가
        historical_data['Ticker'] = ticker_symbol

        # 기술적 지표 계산
        historical_data['RSI'], historical_data['RSI_Signal'] = calculate_rsi(historical_data)
        historical_data['MACD'], historical_data['MACD_Signal'] = calculate_macd(historical_data)
        historical_data['SlowK'], historical_data['SlowD'] = calculate_stochastic(historical_data)
        historical_data['CCI'], historical_data['CCI_Signal'] = calculate_cci(historical_data)
        historical_data = calculate_bollinger_bands(historical_data)
        historical_data = calculate_moving_averages(historical_data)

        # 티커 열을 맨 앞으로 이동
        cols = ['Ticker'] + [col for col in historical_data.columns if col != 'Ticker']
        historical_data = historical_data[cols]

        # 필요한 데이터만 출력
        print(f"\n지표 계산 완료: {ticker_symbol}")
        print(historical_data.tail())

        # RSI 35 이하 필터링
        if historical_data['RSI'].iloc[-1] >= 70:
            print(f"RSI가 35 이하인 종목: {ticker_symbol}")
            return historical_data.tail(1)  # 최신 값 반환
        else:
            return None
    except Exception as e:
        print(f"에러 발생: {ticker_symbol} - {e}")
        return None


# 모든 티커에 대해 데이터 처리
all_results = []
for ticker in etf_tickers:
    result = fetch_and_calculate(ticker)
    if result is not None:
        all_results.append(result)

# 결과 병합
if all_results:
    final_df = pd.concat(all_results, ignore_index=True)
    print("\n모든 계산 결과:")
    print(final_df)

    # CSV 파일로 저장 (선택 사항)
    # final_df.to_csv("etf_indicators.csv", index=False)
    # print("\n결과가 'etf_indicators.csv'로 저장되었습니다.")
else:
    print("\n데이터를 처리할 수 없습니다.")