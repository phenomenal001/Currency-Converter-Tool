# Currency Converter Tool

The Currency Converter Tool is a convenient Python script for retrieving and displaying the latest exchange rates between different currencies. It utilizes the Free Currency API to fetch real-time exchange rate data and supports conversions for a predefined list of currencies.

## Features

- **Real-Time Exchange Rates:** Fetches the latest exchange rates from the Free Currency API.
- **Multiple Currency Support:** Supports conversions between a variety of major currencies.
- **User-Friendly Interface:** Provides a simple command-line interface for inputting base currency and viewing conversion rates.
- **Error Handling:** Handles invalid inputs gracefully and prompts users to retry or exit the program.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Open a terminal window and navigate to the project directory.
4. Modify the `CURRENCIES` list in the script to include or exclude specific currencies as needed.
5. Run the script using the appropriate command for your operating system (e.g., `python currency_converter.py`).
6. Follow the on-screen instructions to input the base currency or enter "Q" to quit the program.

## Dependencies

- This project requires the `requests` library for making HTTP requests. You can install it via pip: pip install requests
- The script also uses the `pycountry` library for working with country and currency data. However, this dependency is currently commented out in the script.

## Contributing

Contributions to the Currency Converter Tool are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit a pull request.

Happy currency conversion!