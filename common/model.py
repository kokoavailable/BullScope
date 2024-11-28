from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stocks(Base):
    __tablename__ = 'stocks'

    ticker = Column(String(10), nullable=False)
    stock_name = Column(String(200), nullable=False)
    stock_price = Column(Numeric(10, 4), nullable=False)
    category = Column(String(50), nullable=False)
    rsi = Column(Numeric(8, 4), nullable=False)
    rsi_signal = Column(Numeric(8, 4), nullable=False)
    rsi_flag = Column(String(3), nullable=False)
    beta = Column(Numeric(8, 4), nullable=False)
    macd = Column(Numeric(8, 4), nullable=False)
    macd_signal = Column(Numeric(8, 4), nullable=False)
    macd_flag = Column(String(3), nullable=False)
    stochastic_slow_d = Column(Numeric(8, 4), nullable=False)
    stochastic_slow_k = Column(Numeric(8, 4), nullable=False)
    stochastic_slow_d_flag = Column(String(3), nullable=False)
    stochastic_slow_k_flag = Column(String(3), nullable=False)
    cci = Column(Numeric(8, 4), nullable=False)
    cci_signal = Column(Numeric(8, 4), nullable=False)
    cci_flag = Column(String(3), nullable=False)
    bollinger_band_upper = Column(Numeric(8, 4), nullable=False)
    bollinger_band_middle = Column(Numeric(8, 4), nullable=False)
    bollinger_band_lower = Column(Numeric(8, 4), nullable=False)
    bollinger_band_flag = Column(String(3), nullable=False)
    date_info = Column(String(10), nullable=False)
    rgtr_dt = Column(DateTime, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('ticker', 'date_info'),
    )

class MacroDaily(Base):
    __tablename__ = 'macro_daily'

    date_info = Column(String(10), primary_key=True, nullable=False)
    fear_and_greed_idx = Column(Numeric(3), nullable=False)
    fear_and_greed_flag = Column(String(30), nullable=False)
    market_momentum = Column(String(20), nullable=False) 
    stock_price_strength = Column(String(20), nullable=False)
    stock_price_breadth = Column(String(20), nullable=False)
    put_and_call_options = Column(String(20), nullable=False)
    market_volatility = Column(String(20), nullable=False)
    safe_haven_demand = Column(String(20), nullable=False)
    junk_bond_demand = Column(String(20), nullable=False)
    rgtr_dt = Column(DateTime, nullable=False)

class MacroEvent(Base):
    __tablename__ = 'macro_event'

    event_name = Column(String(255), nullable=False)
    date_info = Column(String(10), nullable=False)
    importance = Column(Numeric(1), nullable=False)
    category = Column(String(255), nullable=True)
    actual = Column(String(20), nullable=True) 
    forecast = Column(String(20), nullable=True)
    previous = Column(String(20), nullable=True)
    release_date = Column(String(30), nullable=False)
    related_link = Column(String(255), nullable=True)
    content = Column(String, nullable=True)
    rgtr_dt = Column(DateTime, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('event_name', 'date_info'),
    )