<h1 align="center">
  <a href="" target="_blank">
  <img src="https://github.com/user-attachments/assets/5fe5f551-8c10-42b5-b5de-6f56947fe0c2" width=350 height=350/><br>
  BullScope
  </a>

</h1>
<h4 align="center">Powerful Invest Supporter</h4>

<div align="center">
  <a href="" target="_blank">
    <img src="https://github.com/lapce/lapce/actions/workflows/ci.yml/badge.svg" />
  </a>
  <a href="" target="_blank">
    <img src="https://img.shields.io/discord/946858761413328946?logo=discord" />
  </a>
<!--  <a href="https://" target="_blank">
      <img src="https://img.shields.io/static/v1?label=Docs&message=docs.lapce.dev&color=blue" alt="Lapce Docs">
  </a>-->
</div>
<br/>
<img width="1463" alt="image" src="https://github.com/user-attachments/assets/0c5e97b7-c768-4a0e-902d-20519e1d6e37">


BULLSCOPE (IPA: /ˈbʊl.skoʊp/) is written in pure Python, designed to assist with investment decisions by screening highly volatile, oversold stocks through technical analysis. It calculates and tracks various technical indicators, recording changes in trends. Using internal logic it helps investment decision. 

## Features

* Screens highly volatile, oversold stocks through technical analysis.
* Tracks various technical indicators, recording changes in trends.
* Uses internal logic to help make internal decisions.

It calculates technical indicators from collected data, tracking and recording them until the targeted stock diverges from the set threshold. Internal logic determines likely points of trend reversal, providing information. Additionally, through fundamental analysis, it offers insights into the intrinsic value of the stock, supporting steady investment decisions by grounding them in solid fundamentals, as fundamental analysis serves as the cornerstone of sound investing.

## Table of Contents

### [TA Indicators](#-ta-indicators)
1. [MACD (Moving Average Convergence Divergence)](#1-macd-moving-average-convergence-divergence)
2. [RSI (Relative Strength Index)](#2-rsi-relative-strength-index)
3. [Stochastic Oscillator](#3-stochastic-oscillator)
4. [CCI (Commodity Channel Index)](#4-cci-commodity-channel-index)
5. [Bollinger Bands](#5-bollinger-bands)
6. [SMA10, SMA50](#6-sma10-sma-50)

### [FA Metrics](#fa-metrics)
1. [PBR (Price-to-Book Ratio)](#1-pbr-price-to-book-ratio)
2. [PER (Price-to-Earnings Ratio)](#2-per-price-to-earnings-ratio)
3. [ROE (Return on Equity)](#3-roe-return-on-equity)
4. [Debt-to-Equity Ratio](#4-debt-to-equity-ratio)
5. [EPS (Earnings Per Share)](#5-eps-earnings-per-share)
6. [DCF (Discounted Cash Flow)](#6-dcf-discounted-cash-flow)
7. [Revenue](#7-revenue)
8. [PEG (Price/Earnings to Growth Ratio)](#8-peg-priceearnings-to-growth-ratio)

### [Market Indicators](#market-indicators)
1. [BDI (Baltic Dry Index)](#1-bdi-baltic-dry-index)
2. [PMI (Purchasing Managers' Index)](#2-pmi-purchasing-managers-index)
3. [Consumer Confidence Index (CCI)](#3-consumer-confidence-index-cci)
4. [FedWatch Expected Rate Spread](#4-fedwatch-expected-rate-spread)
5. [Dot Plot (Federal Reserve)](#5-dot-plot-federal-reserve)
6. [Buffett Indicator](#6-buffett-indicator)
7. [VIX (Volatility Index)](#7-vix-volatility-index)
8. [Fear & Greed Index](#8-fear--greed-index)
9. [M2 Growth Rate](#9-m2-growth-rate)
10. [Yield Curve Inversion](#10-yield-curve-inversion)
11. [Dollar Index (DXY)](#11-dollar-index-dxy)
12. [Labor Market Indicators](#12-labor-market-indicators)
13. [Inflation Indicators](#13-inflation-indicators)
14. [MSCI Emerging Markets Index (MSCI EM)](#14-msci-emerging-markets-index-msci-em)
15. [China PMI (Purchasing Managers' Index)](#15-china-pmi-purchasing-managers-index)

## [TA Indicators](#table-of-contents)

### 1. **MACD (Moving Average Convergence Divergence)**
- **Description**: The difference between short-term and long-term exponential moving averages (EMAs).  
It incorporates the concept of golden and dead crosses.
- **Components**:  
  - MACD Line = 12-day EMA - 26-day EMA  
  - Signal Line = 9-day EMA of MACD Line  

### 2. **RSI (Relative Strength Index)**
- **Description**: The ratio of gains to losses over a specific period.  
It reflects buying and selling sentiment and measures the strength of price movements.
- **Formula**:  
  RSI = 100 - (100 / (1 + RS))

### 3. **Stochastic Oscillator**
- **Description**: Tracks the current price relative to a given period’s high-low range.
- **Formula**:  
  %K = ((Close - Low) / (High - Low)) * 100
- **Components**:  
  %K (Fast): Measures the current price's position within the period's high-low range.
  %D (Slow): 3-day SMA of %K.
  Used to detect overbought or oversold conditions.

### 4. **CCI (Commodity Channel Index)**
- **Description**: The deviation of the typical price from its average,  
divided by the product of its standard deviation and a constant.  
Similar to Bollinger Bands, it utilizes deviations for analysis.
"""
- **Formula**:  
  CCI = (Typical Price - SMA(Typical Price)) / (0.015 * Standard Deviation)

### 5. **Bollinger Bands**
- **Description**: Values deviating by 2 standard deviations (σ) from the 20 SMA.  
Represents the upper and lower Bollinger Bands.
- **Components**:  
  - Middle Band = 20-day SMA  
  - Upper/Lower Bands = Middle Band ± 2 × Std Dev
 
### 6. **SMA10, SMA 50**
- **Description**: Calculates short-term and medium-to-long-term simple moving averages (SMAs).  
Used to detect short-term trend reversals.
- **Components**:  
  - 10-day SMA = (Sum of Closing Prices over 10 Days) / 10
  - 50-day SMA = (Sum of Closing Prices over 50 Days) / 50
 
## FA Matrics
The metrics provide meaningful analytical results depending on time and context. They are used to evaluate intrinsic and fundamental value.



### 1. PBR (Price-to-Book Ratio)

- **Description:** The market price per share reflects market sentiment and expectations, while the book value per share represents the actual asset value. However, in industries where intangible assets like technology, patents, or brand value play a significant role, PBR might be lower. A low PBR does not always indicate undervaluation—it could signal poor asset quality (e.g., excessive debt) or weak profitability. Therefore, it is crucial to analyze PBR alongside ROE to determine whether the assets are efficiently generating returns.

- **Formula:**

```
PBR = Market Price per Share / Book Value per Share
```

- **Components:**
  - **Market Price per Share:** Current trading price of the stock. Reflects market sentiment and future expectations.
  - **Book Value per Share:** Total assets minus total liabilities divided by the number of shares outstanding. Represents actual asset value.


### 2. PER (Price-to-Earnings Ratio)

- **Description:** The PER represents the ratio of a company's share price to its earnings per share, reflecting investor expectations about the company's future financial performance. It is used to evaluate the appropriateness of a stock's price relative to its earnings. High-growth industries like IT and biotech often exhibit higher ratios.

- **Formula:**

```
PER = Market Price per Share / Earnings per Share (EPS)
```

- **Components:**
  - **Market Price per Share:** Current trading price. Reflects market sentiment and future expectations.
  - **Earnings per Share (EPS):** Net earnings divided by the number of shares outstanding.


### 3. ROE (Return on Equity)

- **Description:** This measures how effectively a company uses shareholders' equity to generate profits. A consistently high ROE indicates stable profitability and efficient management. However, high ROE can sometimes indicate excessive leverage, so it should be analyzed along with the debt-to-equity ratio.

- **Formula:**

```
ROE = (Net Income / Shareholders’ Equity) × 100%
```

- **Components:**
  - **Net Income:** Profit after taxes and expenses. 
  - **Shareholders' Equity:** Total assets minus total liabilities.


### 4. Debt-to-Equity Ratio

**Description:** This ratio evaluates a company's financial leverage by comparing its total liabilities to shareholders' equity. It is crucial for assessing financial stability and risk. A higher ratio may signal increased risk due to heavy reliance on debt.

- **Formula:**

```
Debt-to-Equity Ratio = Total Liabilities / Shareholders’ Equity
```

- **Components:**
  - **Total Liabilities:** Total financial obligations. Utilization of external capital.
  - **Shareholders' Equity:** Total assets minus total liabilities. Internal capital.


### 5. EPS (Earnings Per Share)

- **Description:** EPS indicates the profitability of a company on a per-share basis. It helps compare the earning power of companies. It indicates how much profit a company can allocate to each shareholder, maximizing shareholder value. It also reflects the potential for the company to expand its market share. In the technology sector, where PER tends to be higher, the growth in EPS plays a critical role in evaluating the company's actual growth potential.

- **Formula:**

```
EPS = (Net Income − Preferred Dividends) / Average Outstanding Shares
```

- **Components:**
  - **Net Income:** Profit after taxes and expenses.
  - **Preferred Dividends:** Dividends owed to preferred shareholders.
  - **Average Outstanding Shares:** Weighted average of shares during the reporting period.


### 6. DCF (Discounted Cash Flow)

- **Description:** The DCF method estimates an investment's intrinsic value based on its expected future cash flows. It helps identify undervalued or overvalued assets by focusing on a company's inherent value rather than short-term market sentiment. It is particularly useful in stable industries like infrastructure and utilities, where estimates are more reliable. It is equally important in fields like IT and biotech, as accurately valuing future growth potential in present terms is crucial, though projections can be challenging and require careful assumptions.



- **Formula:**

```
DCF = Σ (Cash Flowₜ / (1 + r)ᵗ)
```

- **Components:**
  - **Cash Flowₜ:** Expected cash flow at time t. The assets that a company will generate in the future.
  - **n:** Total number of periods.
  - **r:** Discount rate reflecting investment risk and cost of capital.


### 7. Revenue

- **Description:** Revenue represents the total income generated from a company's underlying assets before expenses, serving as a key indicator of its competitiveness and overall scale in the market (measured in absolute terms). It is especially important in high-revenue industries such as retail and consumer goods, as well as for large-scale companies. However, in low-revenue, high-profit industries like IT and biotech, or for smaller companies, factors such as cost structure and profit margins often carry greater significance.

- **Formula:**

```
Revenue = Total Income from Sales or Operations
```

- **Components:**
  - **Revenue:** Income from selling goods or services.


### 8. PEG (Price/Earnings to Growth Ratio)

- **Description:** By dividing the P/E ratio by the company’s earnings growth rate, the PEG ratio incorporates growth into the valuation metric, allowing for an assessment of the stock price relative to its growth. In other words, it evaluates whether the price is reasonable compared to the expected future growth rate. This ratio is particularly important in growth-oriented industries and provides a quantitative method to value high-growth companies, which are often difficult to assess using the P/E ratio alone.

- **Formula:**

```
PEG = P/E Ratio / Earnings Growth Rate
```

- **Components:**
  - **P/E Ratio:** Price-to-Earnings ratio.
  - **Earnings Growth Rate:** Projected rate of earnings growth, usually over five years.

## Market Indicators
It covers global economic trends (BDI, PMI, CCI, MSCI EM, China PMI), market sentiment (VIX, Fear & Greed Index, Buffett Indicator), monetary policy (FedWatch, Dot Plot, Yield Curve Inversion, M2 Growth Rate, DXY), labor market indicators , and inflation metrics (CPI, Core CPI, PPI, Core PCE).

### 1. **BDI (Baltic Dry Index)**

- **Description:**  
  The BDI measures the cost of shipping raw materials such as iron ore, coal, and grain across the globe. It serves as a leading indicator of global economic activity and demand for raw materials.

- **Formula:**  
  The Baltic Exchange calculates the index using average shipping rates across major dry bulk routes. While the exact formula remains undisclosed, it is derived as a weighted average of the following three components.

- **Components:**  
  - **Capesize:** Rates for large vessels.  
  - **Panamax:** Rates for medium-sized vessels.  
  - **Supramax:** Rates for smaller vessels.

- **Usage:**  
  - **BDI Rising:** Increased demand for raw materials → Potential global economic recovery.  
  - **BDI Falling:** Reduced demand for raw materials → Economic slowdown signal.


### 2. **PMI (Purchasing Managers' Index)**

- **Description:**  
  The PMI measures the health of the manufacturing and service sectors, making it a key indicator of overall economic activity. It reflects business sentiment based on new orders, production, employment, supplier delivery times, and inventory levels.

- **Formula:**  
  ```
  PMI=(Proportion of respondents reporting improvement×1)+(Proportion of respondents reporting no change×0.5)+(Proportion of respondents reporting deterioration×0)
  ```

- **Components:**  
  - **New Orders:** Demand for goods or services.  
  - **Production:** Current output levels.  
  - **Employment:** Hiring trends.  
  - **Supplier Deliveries:** Speed of supply chains.  
  - **Inventory Levels:** Stockpile status.

- **Usage:**  
  - **PMI > 50:** Economic expansion → Increased manufacturing and service activity.  
  - **PMI < 50:** Economic contraction → Reduced activity and potential slowdown.


### 3. **Consumer Confidence Index (CCI)**

- **Description:**  
  The CCI evaluates consumer sentiment regarding the overall economy, reflecting the public’s willingness to spend. It serves as a leading indicator for retail sales and broader economic activity.

- **Formula:**  
  Based on surveys of households regarding current and future economic conditions, scaled to a baseline of 100.

- **Components:**  
  - **Current Conditions Index:** Measures perception of present economic conditions.  
  - **Expectations Index:** Reflects expectations for income, business conditions, and employment over the next 6 months.

- **Usage:**  
  - **Rising CCI:** Higher consumer confidence → Increased spending → Economic growth.  
  - **Falling CCI:** Lower confidence → Reduced spending → Potential economic slowdown.


### 4. **FedWatch Expected Rate Spread**

- **Description:**  
  The FedWatch tool reflects market expectations for Federal Reserve interest rate decisions. It uses CME Group's futures data to estimate the probability of rate hikes or cuts.

- **Formula:**  
  The probabilities are derived from Fed Funds Futures data.

- **Components:**  
  - **Current Rate Range:** The Fed's target interest rate range.  
  - **Expected Rate Change Probability:** Market-based expectations for rate changes.

- **Usage:**  
  - **High Probability:** Prepare for rate movement scenarios.  
  - **Rate Hike Expected:** Bond weakness, pressure on stock markets.  
  - **Rate Cut Expected:** Increased liquidity, positive for stock markets.


### 5. **Dot Plot (Federal Reserve)**

- **Description:**
  The Dot Plot, released quarterly after FOMC meetings, shows Federal Reserve members’ projections for interest rates. It provides insights into the pace of rate hikes or cuts and the Fed’s policy direction.
- **Components:**
  - **Projections:** Each dot represents a member’s expected federal funds rate for year-end and the long-term neutral rate.
  - Clustering of Dots:
    - Higher clusters suggest likely rate hikes.
    - Lower clusters suggest likely rate cuts.
  - **Release Frequency:** Published quarterly in March, June, September, and December.
- **Usage:**
  - Helps market participants anticipate future monetary policy decisions.
  - Offers insight into the Fed’s economic outlook but is not a binding commitment.


### 6. **Buffett Indicator**

- **Description:**  
  The Buffett Indicator measures the ratio of a country's total stock market capitalization to its GDP. It is used to assess whether the stock market is overvalued or undervalued relative to the economy.

- **Formula:**  
  ```
  Buffett Indicator = Total Stock Market Cap / GDP
  ```

- **Usage:**  
  - **Above 100%:** Market may be overvalued.  
  - **Below 100%:** Market may be undervalued.


### 7. **VIX (Volatility Index)**

- **Description:**  
  The VIX measures the implied volatility of S&P 500 options, reflecting investor fear and market uncertainty. It is often called the "Fear Index."

- **Formula:**  
  The VIX is derived from option prices on the S&P 500 index.

- **Usage:**  
  - **VIX Rising:** Increased market fear → Risk assets weaken.  
  - **VIX Falling:** Market stability → Risk assets strengthen.


### 8. **Fear & Greed Index**

- **Description:**
  This index, published by CNN, gauges market sentiment by balancing fear and greed among investors. It combines seven factors such as stock price momentum, market volatility (VIX), safe-haven demand, and junk bond demand to provide a score between 0 (Extreme Fear) and 100 (Extreme Greed).

- **Components:**

  - Stock Price Momentum:

    Measures whether the S&P 500 is above or below its 125-day moving average.

    - **Above:** Greed
    - **Below:** Fear

  - Stock Price Strength:

    Tracks the ratio of stocks hitting 52-week highs to 52-week lows.

    - **More highs:** Greed
    - **More lows:** Fear

  - Market Volatility (VIX):

    Uses the VIX index to measure market uncertainty.

    - **High VIX:** Fear
    - **Low VIX:** Greed

  - Safe-Haven Demand (Treasuries vs. Stocks):

    Compares returns on Treasuries to stocks.

    - **Preference for Treasuries:** Fear
    - **Preference for Stocks:** Greed

  - Junk Bond Demand:

    Measures the yield spread between investment-grade and junk bonds.

    - **Narrow Spread:** Greed
    - **Wide Spread:** Fear

- **Score Range:**

  - 0-24: Extreme Fear
  - 25-49: Fear
  - 50: Neutral
  - 51-74: Greed
  - 75-100: Extreme Greed

- **Usage:**

  - **High Fear:** Increased selling → Potential buying opportunities.
  - **High Greed:** Overheating markets → Defensive strategies recommended.


### 9. **M2 Growth Rate**

- **Description:**  
  The M2 growth rate measures the annual or monthly change in broad money supply, indicating the flow of liquidity in the economy.

- **Formula:**  
  ```
  M2 Growth Rate = (Current M2 - Previous M2) / Previous M2 × 100%
  ```

- **Usage:**  
  - **Growth Rate Rising:** Increased liquidity → Potential asset market strength.  
  - **Growth Rate Falling:** Reduced liquidity → Risk asset weakness.


### 10. **Yield Curve Inversion**

- **Description:**  
  Yield curve inversion occurs when long-term bond yields fall below short-term bond yields. It is often seen as a precursor to economic recessions.

- **Formula:**  
  ```
  Yield Curve Spread = 10-Year Treasury Yield - 2-Year Treasury Yield
  ```

- **Usage:**  
  - **Negative Spread:** Increased likelihood of a recession.  
  - **Positive Spread:** Normal economic growth signal.


### 11. **Dollar Index (DXY)**

- **Description:**  
  The Dollar Index measures the value of the US dollar relative to a basket of six major foreign currencies. It is a key indicator of global capital flows and forex market trends.

- **Formula:**  
  The DXY is calculated as a weighted geometric mean of the dollar’s value relative to the selected currencies.

- **Usage:**  
  - **Strong Dollar:** Capital outflows from emerging markets → Risk asset weakness.  
  - **Weak Dollar:** Capital inflows into emerging markets → Risk asset strength.


### **12. Labor Market Indicators**

- **Description:**
  Labor market data provide insights into employment trends, wage growth, and overall economic health, serving as key metrics for consumer spending and economic stability.

- **Key Indicators:**

  - Unemployment Rate:

     Measures the proportion of unemployed individuals within the labor force.

    - **Low Unemployment:** Indicates labor market strength and economic health.
    - **High Unemployment:** Suggests potential economic slowdown.

  - Initial Jobless Claims:

     Tracks weekly applications for unemployment benefits, reflecting short-term labor market trends.

    - **Increase:** Indicates weakening labor market.
    - **Decrease:** Suggests labor market resilience.

  - Continuing Jobless Claims:

     Measures ongoing unemployment claims, showing the persistence of unemployment.

    - **Increase:** Delayed recovery in labor market.
    - **Decrease:** Indicates improving employment conditions.

  - Average Hourly Earnings:

     Represents changes in hourly wages, providing insights into wage growth and consumer spending potential.

    - **Increase:** Suggests rising consumer purchasing power but could add inflationary pressure.
    - **Decrease:** Indicates weaker labor market and lower spending capacity.



### **13. Inflation Indicators**

- **Description:**
  Inflation metrics assess the rate at which prices for goods and services are rising, impacting purchasing power, central bank policies, and financial markets.

- **Key Indicators:**

  - CPI (Consumer Price Index):

     Tracks changes in the average price of consumer goods and services.

    - **Rising CPI:** Signals increasing inflation → Likely monetary tightening.
    - **Falling CPI:** Indicates deflation risks → Possible monetary easing.

  - PPI (Producer Price Index):

     Measures changes in production costs, serving as a leading indicator for consumer inflation.

    - **Rising PPI:** Suggests potential consumer price increases.
    - **Falling PPI:** Indicates reduced cost pressures on businesses.

  - Wage Growth:

     Tracks increases in wages, reflecting labor market strength and potential inflationary effects.

    - **High Wage Growth:** Boosts consumer spending but may fuel inflation.
    - **Low Wage Growth:** Limits spending and economic growth potential.


### **14. MSCI Emerging Markets Index (MSCI EM)**

- **Description:**
  The MSCI Emerging Markets Index evaluates the performance of equity markets in emerging economies, reflecting global capital flows and investor sentiment.
- **Usage:**
  - Rising MSCI EM:
    - Indicates strength in emerging market economies and suggests capital inflows.
  - Falling MSCI EM:
    - Suggests capital outflows and potential economic slowdown in emerging markets.
    - A strong US dollar (DXY increase) can negatively impact emerging market assets by causing capital flight.



### **15. China PMI (Purchasing Managers' Index)**

- **Description:**
  The China PMI assesses the health of China's manufacturing and service sectors, playing a critical role in understanding domestic market trends and global supply chain dynamics.

- **Usage:**

  - PMI > 50:
    - Indicates expansion in manufacturing and services, reflecting economic growth.
  - PMI < 50:
    - Signals contraction and potential economic slowdown.
  - Market Impact:
    - Strongly influences commodity prices (e.g., steel, copper, coal).
    - Early indicator of global supply chain issues and impacts emerging market sentiment and global economic growth.

-


<!-- ## Installation

You can find pre-built releases for Windows, Linux and macOS [here](https://github.com/lapce/lapce/releases), or [installing with a package manager](docs/installing-with-package-manager.md).
If you'd like to compile from source, you can find the [guide](docs/building-from-source.md).

## Contributing

Guidelines for contributing to Lapce can be found in [`CONTRIBUTING.md`](CONTRIBUTING.md). -->

<!-- ## Feedback & Contact

The most popular place for Lapce developers and users is on the [Discord server](https://discord.gg/n8tGJ6Rn6D).

Or, join the discussion on [Reddit](https://www.reddit.com/r/lapce/) where we are just getting started.

There is also a [Matrix Space](https://matrix.to/#/#lapce-editor:matrix.org), which is linked to the content from the Discord server.

## License

Lapce is released under the Apache License Version 2, which is an open source license. You may contribute to this project, or use the code as you please as long as you adhere to its conditions. You can find a copy of the license text here: [`LICENSE`](LICENSE). -->
