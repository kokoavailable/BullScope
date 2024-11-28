import pandas as pd

# RSI 계산 함수
def calculate_rsi(data, window=14):
    """
    일정기간안 상승가와 하락가 간의 비율.
    매수 매도 심리를 나타내며, 강도를 나타내는 지수라고 할 수 있다.
    """
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    # RSI 시그널(6일 이동평균)
    rsi_signal = rsi.rolling(window=6).mean()
    return rsi, rsi_signal

# MACD 계산 함수
def calculate_macd(data):
    """
    단기 가중이평에서 장기 가중이평을 뻄.
    골든 크로스나 데드 크로스의 의미를 함축하고 있다.
    """
    ema_12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = data['Close'].ewm(span=26, adjust=False).mean()
    macd_line = ema_12 - ema_26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    return macd_line, signal_line

# CCI 계산 함수
def calculate_cci(data, window=20):
    """
    전형가가 전형가의 평균에서 멀어진 정도/
    전형가의 표준편차 * 상수

    볼린저 밴드와 같이 편차를 이용한 지표.
    """
    typical_price = (data['High'] + data['Low'] + data['Close']) / 3
    cci = (typical_price - typical_price.rolling(window=window).mean()) / \
          (0.015 * typical_price.rolling(window=window).std())
    # CCI 시그널(8일 이동평균)
    cci_signal = cci.rolling(window=8).mean()
    return cci, cci_signal

# 스토캐스틱 오실레이터 계산 함수
def calculate_stochastic(data, k_window=5, d_window=3):
    """
    현재 종가는, 기간 안 최고가 몇프로에 위치해 있는가.
    단기 추세 포착.
    """
    low = data['Low'].rolling(window=k_window).min()
    high = data['High'].rolling(window=k_window).max()
    percent_k = (data['Close'] - low) / (high - low) * 100
    # 슬로우 %K(5,3)
    slow_k = percent_k.rolling(window=d_window).mean()
    # 슬로우 %D(3)
    slow_d = slow_k.rolling(window=d_window).mean()
    return slow_k, slow_d

def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    """
    20 sma를 기준으로 2 시그마 만큼 떨어진 값.
    상단 볼린저, 하단 볼린저
    """
    data['Middle Band'] = data['Close'].rolling(window=window).mean()
    data['Std Dev'] = data['Close'].rolling(window=window).std()
    data['Upper Band'] = data['Middle Band'] + (num_std_dev * data['Std Dev'])
    data['Lower Band'] = data['Middle Band'] - (num_std_dev * data['Std Dev'])
    return data

def calculate_moving_averages(data, short_window=10, long_window=50):
    """
    단기, 중장기 sma 계산.
    단기 추세 전환 포착
    """
    data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()
    return data