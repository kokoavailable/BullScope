from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from common.common import driver

import yfinance as yf

import time

def create_driver():
    service = Service(executable_path='/Users/koko/Downloads/chromedriver-mac-arm64/chromedriver')
    return webdriver.Chrome(service=service)

def fetch_etf_data_mutualfunds(driver):
    all_etfs = []

    # 사이트 접속
    url = f"https://www.mutualfunds.com/equity-categories/leveraged-equity-funds-and-etfs/"
    driver.get(url)

    # 모든 페이지 번호 요소를 가져온다.
    pagination_numbers = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "mp-table-pagination-page-button"))
    )

    last_page = pagination_numbers[-1]

    for page_number in range(1, last_page + 1):
        page_button = driver.find_element(By.XPATH, f"//button[text()='{page_number}']")
        page_button.click()

        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        rows = soup.find_all('div', {'data-table-target': 'container'})

        for row in rows:
            symbol_info = row.find('p', class_='m-table-body-subtext')
            symbol = symbol_info.find('span').text.strip()
            all_etfs.append(symbol)

    return all_etfs

def fetch_etf_data_etfdb(driver):
    all_etfs = []
    # 하드 코딩.
    for page in range(1, 8 + 1):
        url = f"https://etfdb.com/etfs/leveraged/#etfs&sort_name=assets_under_management&sort_order=desc&page={page}"
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
        driver.execute_script("window.location.reload()")
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tbody = soup.find('tbody')
        print(f'페이지 {page} 가져오기: {url}')  # URL 출력

        
        for row in tbody.find_all('tr'):
            cols = row.find_all('td')
            symbol = cols[0].text.strip()
            all_etfs.append(symbol)


    return all_etfs

def fetch_etf_data_etfcom(driver):
    all_etfs = []

    # 사이트 접속
    url = f"https://www.etf.com/topics/leveraged"
    driver.get(url)

    # "페이지네이션 설정" 버튼 클릭
    button_100 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., '100')]"))
    )
    button_100.click()

    # 모든 페이지 번호 요소를 가져온다.
    pagination_numbers = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "page-item"))
    )

    last_page = pagination_numbers[-1]

    for page_number in range(1, last_page + 1):
        page_button = driver.find_element(By.XPATH, f"//a[text()='{page_number}']")
        page_button.click()

        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tbody = soup.find('tbody')

        for row in tbody.find_all('tr'):
            cols = row.find_all('td')
            symbol = cols[0].text.strip()
            all_etfs.append(symbol)

    return all_etfs

def merge_lists(*lists):
    merged_data = list(set().union(*lists))
    return merged_data



def get_macro_daily(driver):
    url = "https://www.investing.com/economic-calendar/"
    pass



# 데이터 가져오기
data_etfcom = fetch_etf_data_etfcom(driver)
data_etfdb = fetch_etf_data_etfdb(driver)
data_mutualfunds = fetch_etf_data_mutualfunds(driver)

# # 드라이버 종료
# driver.quit()

# 데이터 병합
merged_data = merge_lists(data_etfcom, data_etfdb, data_mutualfunds)