import pandas as pd
import yfinance as yf
import 


def get_tax_rate(country):
    tax_rate = tax_rate.get(country, 0.21) # 디폴트 미국

    return tax_rate

def calculate_beta(stock_ticker, index="^GSPC", period="5y"):
    """
    베타 구하기.
    """
    stock = yf.Ticker(stock_ticker)
    market = yf.Ticker(index)

    stock_data = stock.history(period=period)['Close'].pct_change().dropna()
    market_data = market.history(period=period)['Close'].pct_change().dropna()

    covariance = stock_data.cov(market_data)
    market_variance = market_data.var()

    beta = covariance / market_variance

    return beta



# Risk Free Rate
def get_risk_free_rate(maturity="10y"):
    """
    무위험 금리 가져오기
    - maturity: "3m" (3개월 T-Bill), "10y" (10년 국채 금리)
    """
    tickers = {
       "3m": "^IRX",  # 3개월 T-Bill
        "1y": "^FVX",  # 1년 국채 금리
        "10y": "^TNX"  # 10년 국채 금리
    }
    
    if maturity not in tickers:
        raise ValueError("지원되지 않는 만기입니다. '3m', '1y', '10y'를 선택하세요.")
    
    ticker = tickers[maturity]
    data = yf.Ticker(ticker).history(period="1d")

    risk_free_rate = data['Close'] / 100  # % 단위를 소수점으로 변환
    return risk_free_rate

def get_market_return(index="^GSPC", period="5y"):
    """
    시장 수익률 계산
    - index: 시장 지수 (예: "^GSPC" - S&P 500)
    - period: 과거 데이터 기간 (예: "1y", "5y", "10y")
    """
    market_data = yf.Ticker(index).history(period=period)
    market_data['Return'] = market_data['Close'].pct_change().dropna()
    annualized_return = market_data['Return'].mean() * 252  # 연평균 수익률
    return annualized_return

def calculate_cost_of_debt(company_financials, balance_sheet):
    interest_expense = company_financials.loc['Interest Expense', company_financials.columns[0]]
    total_debt = balance_sheet.loc['Total Debt', balance_sheet.columns[0]]

    cost_of_debt = interest_expense / total_debt

    if pd.isna(interest_expense) or pd.isna(total_debt):
            print("부채비용 계산에 필요한 값이 없습니다.")
    
    return cost_of_debt

def calculate_cost_of_equity(company_ticker, risk_free_rate, market_return, beta, cost_of_equity):
    """
    자본 비용 계산 (Cost of Equity)
    - company_ticker: 회사의 티커 심볼
    - risk_free_rate: 무위험 이자율
    - market_return: 시장 수익률
    - beta: 회사의 베타계수
    """
    cost_of_equity = risk_free_rate + beta * (market_return - risk_free_rate)

    return cost_of_equity

def calculate_capital_structure(ticker):
    market_cap = ticker.info['marketCap']
    total_debt = ticker.balance_sheet.loc['Total Debt']

    if pd.isna(market_cap) or pd.isna(total_debt):
        raise ValueError("자본 구조 계산에 필요한 데이터가 NaN입니다.")
    
    total_capital = market_cap + total_debt

    equity_weight = market_cap / total_capital
    debt_weight = total_debt / total_capital

    return equity_weight, debt_weight

def calculate_WACC(cost_of_equity, beta, cost_of_debt, equity_weight, debt_weight, tax_rate):
    """
    할인율 계산 (WACC 기반)
    - risk_free_rate: 무위험 금리
    - beta: 주식의 시장 민감도
    - market_return: 시장 수익률
    - equity_weight: 자본 비율
    - debt_weight: 채무 비율
    - tax_rate: 세금 비율
    """
    wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1 - tax_rate))

    return wacc

# DCF (Discounted Cash Flow)
def calculate_dcf(data, fcf):
    """
    단기 및 장기 DCF를 Pandas DataFrame에 추가
    - data: Pandas DataFrame
    - fcf: 현금흐름
    - beta: 주식의 시장 민감도 (기본값 1.2)
    """
    # 장기 할인율 계산
    risk_free_rate = get_risk_free_rate("10y")
    market_return = get_market_return("^GSPC", "5y")
    discount_rate = calculate_WACC()
    
    # DCF 계산
    dcf = sum(fcf / ((1 + discount_rate) ** i) for i, fcf in enumerate(fcf, start=1))
    
    # 데이터프레임에 결과 추가
    data['DCF'] = dcf
    
    return data


