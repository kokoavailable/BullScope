from stock_data import get_macro_indicator, get_store_macro_daily_data, get_store_etf_data


def main():
    """
    Main function to retrieve and store ETF and macroeconomic data.
    """
    try:
        # Store ETF data and macroeconomic data.
        get_store_etf_data()
        get_store_macro_daily_data()
        get_macro_indicator()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()