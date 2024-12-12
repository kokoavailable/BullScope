# test_fa_calculations.py
import pandas as pd
import pytest

import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)

from common.fundamental_analysis import calculate_per, calculate_pbr, calculate_roe

def test_calculate_per():
    data = pd.DataFrame({'Price': [100, 200], 'EPS': [10, 20]})
    result = calculate_per(data)
    assert result['PER'][0] == 10  # 100 / 10 = 10
    assert result['PER'][1] == 10  # 200 / 20 = 10

def test_calculate_pbr():
    data = pd.DataFrame({'Price': [150, 300], 'Book Value per Share': [50, 100]})
    result = calculate_pbr(data)
    assert result['PBR'][0] == 3  # 150 / 50 = 3
    assert result['PBR'][1] == 3  # 300 / 100 = 3

def test_calculate_roe():
    data = pd.DataFrame({'Net Income': [1000, 2000], 'Shareholder Equity': [5000, 10000]})
    result = calculate_roe(data)
    assert result['ROE'][0] == 0.2  # 1000 / 5000 = 0.2
    assert result['ROE'][1] == 0.2  # 2000 / 10000 = 0.2