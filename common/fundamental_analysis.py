import pandas as pd
import yfinance as yf

def fetch_fa_data(ticker):
    """
    주어진 티커 심볼에 대한 기본적 분석 데이터를 가져옵니다.
    """
    try:
        cashflow = ticker.cashflow
        financials = ticker.financials
        info = ticker.info

        # Book Value와 Shares Outstanding으로 Total Stockholder Equity 계산
        book_value = info.get('bookValue', None)
        shares_outstanding = info.get('sharesOutstanding', None)
        total_stockholder_equity = None
        interest_expense = financials.loc['Interest Expense', financials.columns[0]]

        if book_value is not None and shares_outstanding is not None:
            total_stockholder_equity = book_value * shares_outstanding

        # EBITDA 및 이자 비용 가져오기
        ebitda = info.get('ebitda', None)
        da = cashflow.loc['Depreciation & Amortization', cashflow.columns[0]]

        ebit = None
        if ebitda is not None and da is not None:
            ebit = ebitda - da

        # 기본적 분석 데이터 준비
        fa_data = {
            'Price': info.get('currentPrice', None),
            'EPS': info.get('trailingEps', None),
            'Net Income': info.get('netIncomeToCommon', None),
            'Shareholder Equity': total_stockholder_equity,  # 계산된 값 사용
            'Total Debt': info.get('totalDebt', None),
            'Revenue': info.get('totalRevenue', None),
            'Book Value per Share': book_value,
            'Earnings Growth': info.get('earningsGrowth', None),
            'Shares Outstanding': shares_outstanding,
            'EBITDA': ebitda,
            'Interest Expense': interest_expense,
            'DA': da,
            'EBIT': ebit
        }

        fa_data_df = pd.DataFrame([fa_data])


        # 결측값 확인
        for key, value in fa_data.items():
            if value is None:
                print(f"Warning: {key} is missing for ticker {ticker_symbol}.")

        return fa_data_df

    except Exception as e:
        print(f"Error fetching data for ticker {ticker_symbol}: {e}")
        return None


# PER (Price-to-Earnings Ratio)
def calculate_per(data):
    """
    PER = 주가 / 주당순이익 (EPS)
    """
    data['PER'] = data['Price'] / data['EPS']
    return data



# PBR (Price-to-Book Ratio)
def calculate_pbr(data):
    """
    PBR = 주가 / 주당장부가치 (BVPS)
    """
    data['PBR'] = data['Price'] / data['Book Value per Share']
    return data

# ROE (Return on Equity)
def calculate_roe(data):
    """
    ROE = 순이익 / 자기자본
    """
    data['ROE'] = data['Net Income'] / data['Shareholder Equity']
    return data

# Debt-to-Equity Ratio
def calculate_debt_to_equity(data):
    """
    Debt-to-Equity Ratio = 총부채 / 자기자본
    """
    data['Debt-to-Equity'] = data['Total Debt'] / data['Shareholder Equity']
    return data

# PEG Ratio
def calculate_peg(data):
    """
    PEG = PER / 이익 성장률
    """
    data['PEG'] = data['PER'] / data['Earnings Growth']
    return data

# EPS (Earnings Per Share)
def calculate_eps(data):
    """
    EPS = 순이익 / 주식수
    """
    data['EPS'] = data['Net Income'] / data['Shares Outstanding']
    return data

# Revenue Growth
def calculate_revenue_growth(data):
    """
    Revenue Growth = (현재 매출액 - 이전 매출액) / 이전 매출액
    """
    data['Revenue Growth'] = data['Revenue'].pct_change()
    return data

def calculate_ebitda_margin(data):
    """
    EBITDA% = EBITDA / Revenue
    """
    if 'EBITDA' in data.columns and 'Revenue' in data.columns:
        data['EBITDA%'] = data['EBITDA'] / data['Revenue']
    else:
        data['EBITDA%'] = None
    return data

# Profit% (Net Profit Margin)
def calculate_profit_margin(data):
    """
    Profit% = Net Income / Revenue
    """
    if 'Net Income' in data.columns and 'Revenue' in data.columns:
        data['Profit%'] = data['Net Income'] / data['Revenue']
    else:
        data['Profit%'] = None
    return data

# Coverage Ratio (이자보상배율)
def calculate_coverage(data):
    """
    Coverage = EBIT / Interest Expense
    """
    if 'EBIT' in data.columns and 'Interest Expense' in data.columns:
        data['Coverage'] = data['EBIT'] / data['Interest Expense']
    else:
        data['Coverage'] = None
    return data

def calculate_fa_metrics(data):
    """
    주어진 기본적 분석 데이터를 기반으로 모든 FA 지표를 계산하고, 계산된 지표만 반환합니다.
    """
    try:
        # 계산된 지표 추가
        data['PER'] = data['Price'] / data['EPS']
        data['PBR'] = data['Price'] / data['Book Value per Share']
        data['ROE'] = data['Net Income'] / data['Shareholder Equity']
        data['Debt-to-Equity'] = data['Total Debt'] / data['Shareholder Equity']
        data['EPS'] = data['Net Income'] / data['Shares Outstanding']
        data['PEG'] = data['PER'] / data['Earnings Growth']
        data['Revenue Growth'] = data['Revenue'].pct_change()
        data['EBITDA%'] = data['EBITDA'] / data['Revenue']
        data['Profit%'] = data['Net Income'] / data['Revenue']
        data['Coverage'] = data['EBIT'] / data['Interest Expense']

        # 필요한 지표만 선택
        selected_columns = [
            'PER', 'PBR', 'ROE', 'Debt-to-Equity', 'EPS', 'PEG', 
            'Revenue Growth', 'EBITDA%', 'Profit%', 'Coverage'
        ]
        calculated_data = data[selected_columns].copy()
        
        return calculated_data

    except Exception as e:
        print(f"Error calculating FA metrics: {e}")
        return None