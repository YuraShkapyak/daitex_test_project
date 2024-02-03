import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

class StockAnalyzer:
    """Клас для аналізу та візуалізації фінансових даних за допомогою свічкових графіків."""
    def __init__(self, symbol, start_date, end_date):
        """
            Ініціалізує об'єкт класу StockAnalyzer.

            Параметри:
            - symbol (str): Символ фінансового інструменту (наприклад, 'AAPL' для Apple).
            - start_date (str): Початкова дата аналізу в форматі 'YYYY-MM-DD'.
            - end_date (str): Кінцева дата аналізу в форматі 'YYYY-MM-DD'.
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = self.fetch_stock_data()

    def fetch_stock_data(self):
        """
            Отримання фінансових даних для вказаного інструменту та діапазону дат.

            Повертає:
            - stock_data (pd.DataFrame): DataFrame з фінансовими даними.
        """

        stock_data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return stock_data

    def plot_candlestick(self, title="Candlestick Chart", support_zones=None, resistance_zones=None):
        """
            Відображення свічкового графіка для фінансових даних.

            Параметри:
            - title (str): Заголовок графіка.
            - support_zones (list): Список цін, які позначають зони підтримки.
            - resistance_zones (list): Список цін, які позначають зони супротиву.

            Не повертає нічого, просто відображає графік.
        """

        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('black')

        self.stock_data.reset_index(inplace=True)
        self.stock_data['Date'] = self.stock_data['Date'].apply(mdates.date2num)

        candlestick_ohlc(ax, self.stock_data[['Date', 'Open', 'High', 'Low', 'Close']].values, width=0.6, colorup='g', colordown='r')

        # Вставте горизонтальні лінії для зон підтримки та супротиву
        if support_zones:
            for price in support_zones:
                ax.axhline(price, color='grreen', linestyle='-', linewidth=2, label='Support Zone')
        if resistance_zones:
            for price in resistance_zones:
                ax.axhline(price, color='red', linestyle='-', linewidth=2, label='Resistance Zone')

        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.set_title(title, color='white')
        ax.set_xlabel('Date', color='white')
        ax.set_ylabel('Stock Prices', color='white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.legend()  # Додайте легенду для зон підтримки та супротиву
        ax.grid(True, linestyle='--', linewidth=0.5, color='grey')

        plt.show()

# Використання класу StockAnalyzer
symbol = 'AAPL'
start_date = '2023-08-04'
end_date = '2024-01-18'
support_zones = [150, 160]  # Додайте ваші ціни зони підтримки
resistance_zones = [180, 190]  # Додайте ваші ціни зони супротиву

stock_analyzer = StockAnalyzer(symbol, start_date, end_date)
stock_analyzer.plot_candlestick(title=f"{symbol} Candlestick Chart", support_zones=support_zones, resistance_zones=resistance_zones)
# мені не дістає навичок зробити це.
