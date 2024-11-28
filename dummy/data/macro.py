import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from datetime import datetime
from common.common import driver, logger

def get_fear_greed(driver):
    url = "https://edition.cnn.com/markets/fear-and-greed"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # fear_and_greed_idx
    fear_and_greed = int(soup.find('span', class_='market-fng-gauge__dial-number-value').text.strip())
    fear_and_greed_flag= 'Extreme Greed' if fear_and_greed > 75 else 'Greed' if fear_and_greed > 55 else 'Neutral' if fear_and_greed >= 45 else 'Fear' if fear_and_greed >= 24 else 'Extreme Fear'

    # market momentum
    market_momentum = soup.find('span', class_='market-fng-indicator__value-label market_momentum_sp500-index').text.strip()

    # stock price strength
    stock_price_strength = soup.find('span', class_='market-fng-indicator__value-label stock_price_strength-index').text.strip()

    # stock price breadth
    stock_price_breadth = soup.find('span', class_='market-fng-indicator__value-label stock_price_breadth-index').text.strip()

    # put and call option
    put_and_call_option = soup.find('span', class_='market-fng-indicator__value-label put_call_options-index').text.strip()

    # market volatility
    market_volatility = soup.find('span', class_='market-fng-indicator__value-label market_volatility_vix-index').text.strip()

    # safe haven demand
    safe_haven_demand = soup.find('span', class_='market-fng-indicator__value-label safe_haven_demand-index').text.strip()

    # junk bond demand
    junk_bond_demand = soup.find('span', class_='market-fng-indicator__value-label junk_bond_demand-index').text.strip()

    return [fear_and_greed, fear_and_greed_flag, market_momentum, stock_price_strength, stock_price_breadth, put_and_call_option, market_volatility, safe_haven_demand, junk_bond_demand]

def get_macro_indicator(driver):
    event_list=[]

    url = "https://www.investing.com/economic-calendar/"
    driver.get(url)

    try:
        # 요소가 존재할 때까지 기다림
        button_filters = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Filters']"))
        )
        logger.info("Found 'Filters' button")

        # 스크롤하여 요소로 이동
        driver.execute_script("arguments[0].scrollIntoView(true);", button_filters)
        logger.info("Scrolled to 'Filters' button")

        # 클릭 시도
        button_filters.click()
        logger.info("Clicked 'Filters' button")
    except Exception as e:
        logger.error(f"Error with 'Filters' button: {e}")
        return event_list

    try:
        button_restore_default_settings = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='restore']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", button_restore_default_settings)
        button_restore_default_settings.click()
        logger.info("Clicked 'Restore Default Settings' button")
    except Exception as e:
        logger.error(f"Error with 'Restore Default Settings' button: {e}")
        return event_list

    try:
        button_clearall = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Clear']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", button_clearall)
        button_clearall.click()
        logger.info("Clicked 'Clear All' button")
    except Exception as e:
        logger.error(f"Error with 'Clear All' button: {e}")
        return event_list

    try:
        checkbox_usa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='United States']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_usa)
        checkbox_usa.click()
        logger.info("Clicked 'United States' checkbox")
    except Exception as e:
        logger.error(f"Error with 'United States' checkbox: {e}")
        return event_list

    try:
        checkbox_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='importance2']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_2)
        checkbox_2.click()
        logger.info("Clicked 'importance2' checkbox")

        checkbox_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='importance3']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_3)
        checkbox_3.click()
        logger.info("Clicked 'importance3' checkbox")
    except Exception as e:
        logger.error(f"Error with 'importance' checkboxes: {e}")
        return event_list

    try:
        button_apply = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Apply']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", button_apply)
        button_apply.click()
        logger.info("Clicked 'Apply' button")
    except Exception as e:
        logger.error(f"Error with 'Apply' button: {e}")
        return event_list

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tbody = soup.find('tbody')

    # # 이벤트 카테고리 하드 코딩
    # event_to_category = {
    #     "Non"
    # }

    # today에 있는 모든 항목들을 긁어 저장. 
    for row in tbody.find_all('tr'):
        category = None
        cols = row.find_all('td')
        time = cols[0].text.strip()
        importance = len(cols[2].find_all('i', class_='grayFullBullishIcon'))
        event = cols[3].text.strip()
        actual = cols[4].text.strip()
        forecast = cols[5].text.strip()
        previous = cols[6].text.strip()
        
        if "Speaks" in event:
            category = "Speaks"
        
        event_list.append([time, importance, event, actual, forecast, previous, category])

    return event_list

fear_and_greed_list = get_fear_greed(driver)
macro_event_list = get_macro_indicator(driver)

# 한국 기준 아침 7시? 돌리면 될듯.