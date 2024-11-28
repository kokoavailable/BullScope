from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path

import os


config = configparser.ConfigParser()

current_dir = Path(__file__).resolve().parent
config_path = current_dir / 'config.ini'

if not config_path.exists():
    raise FileNotFoundError(f"Configuration file not found: {config_path}")


config_read = config.read(config_path, encoding='utf-8')

if not config_read:
    raise FileNotFoundError(f"Configuration file not read: {config_path}")



app_env = os.getenv('APP_ENV', 'DEV')

import logging
import os
from datetime import datetime

# 셀레니움 드라이버

def create_driver():
    service = Service(executable_path='/Users/koko/Downloads/chromedriver-mac-arm64/chromedriver')
    return webdriver.Chrome(service=service)

driver = create_driver()

def setup_logging():
    logger = logging.getLogger('main')

    # 로그 레벨 설정
    logger.setLevel(logging.DEBUG)  # 개별 로거 레벨 설정

    # 로그 파일 경로 설정
    app_env = os.getenv('APP_ENV', 'DEV')
    log_file_path = os.path.join('..', 'logs', f"{app_env}_{datetime.now().strftime('%Y-%m-%d')}.log")

    # 로그 디렉토리 생성
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # 파일 핸들러 설정
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)  # 파일에는 INFO 이상의 로그만 저장
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 콘솔 로그 레벨
    console_formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger('').addHandler(console_handler)

    return logger

# 로그 설정 함수 호출
logger = setup_logging()


def get_engine():

    rdb_user = config.get('DEV', 'POST_USER')
    rdb_password = config.get('DEV', 'POST_PASSWORD')
    rdb_host = config.get('DEV', 'POST_HOST')
    rdb_port = config.get('DEV', 'POST_PORT')
    rdb_name = config.get('DEV', 'POST_NAME')

    engine = create_engine(f'postgresql+psycopg2://{rdb_user}:{rdb_password}@{rdb_host}:{rdb_port}/{rdb_name}')
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

engine = get_engine()
session = get_session(engine)