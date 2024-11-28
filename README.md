<h1 align="center">
  <a href="" target="_blank">
  <img src="https://github.com/user-attachments/assets/5e554173-a7c1-43bb-a039-2e2468d5031c" width=400 height=400/><br>
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


BULLSCOPE (IPA: /ˈbʊl.skoʊp/) is written in pure Python, designed to assist with investment decisions by screening highly volatile, oversold stocks through technical analysis. It calculates and tracks various auxiliary indicators, recording changes in trends. Using internal logic it helps investment decision.


## Features

* Screens highly volatile, oversold stocks through technical analysis.
* Tracks various technical indicators, recording changes in trends.
* Uses internal logic to help make internal decisions.

It calculates technical indicators from collected data, tracking and recording them until the targeted stock diverges from the set threshold. Internal logic determines likely points of trend reversal, providing information.

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
