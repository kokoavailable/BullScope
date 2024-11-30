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

## TA Indicators

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
