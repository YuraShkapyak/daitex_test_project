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

    def plot_candlestick(self, title="Candlestick Chart"):
        """
            Відображення свічкового графіка для фінансових даних.

            Параметри:
            - title (str): Заголовок графіка.

            Не повертає нічого, просто відображає графік.
        """

        fig, ax = plt.subplots(figsize=(12, 6))  # Змінено колір фону на чорний
        fig.patch.set_facecolor('black')  # Змінено колір фону на чорний

        # Перетворення дат у числовий формат, який розуміє matplotlib
        self.stock_data.reset_index(inplace=True)
        self.stock_data['Date'] = self.stock_data['Date'].apply(mdates.date2num)

        candlestick_ohlc(ax, self.stock_data[['Date', 'Open', 'High', 'Low', 'Close']].values, width=0.6, colorup='g', colordown='r')

        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Змінено форматтер для осі X
        ax.set_title(title, color='white')  # Змінено колір тексту заголовка
        ax.set_xlabel('Date', color='white')  # Змінено колір тексту осі X
        ax.set_ylabel('Stock Prices', color='white')  # Змінено колір тексту осі Y

        ax.tick_params(axis='x', colors='white')  # Змінено колір поділок на осі X
        ax.tick_params(axis='y', colors='white')  # Змінено колір поділок на осі Y

        ax.grid(True, linestyle='--', linewidth=0.5, color='grey')  # Додано сітку

        plt.show()

# Використання класу StockAnalyzer
symbol = 'AAPL' 
start_date = '2023-08-04'  # Змініть дату початку на 4 серпня 2023
end_date = '2024-01-18'   # Змініть дату кінця на 18 січня 2024

stock_analyzer = StockAnalyzer(symbol, start_date, end_date)
stock_analyzer.plot_candlestick(title=f"{symbol} Candlestick Chart")
