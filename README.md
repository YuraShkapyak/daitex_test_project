
# Stock Analyzer

Цей проект призначений для аналізу та відображення свічкових графіків акцій за допомогою бібліотек Python, зокрема yfinance, pandas та matplotlib з mplfinance.

## Встановлення залежностей

Перед початком використання переконайтеся, що у вас встановлені необхідні бібліотеки. Ви можете встановити їх за допомогою команди:

```bash
pip install -r requirements.txt
У разі проблем з встановленням бібліотек
pip install pandas matplotlib yfinance mplfinance
```

# Використання

Проект має один основний клас - StockAnalyzer. Цей клас призначений для завантаження та аналізу даних акцій, а також для відображення свічкових графіків.

python
Copy code
from stock_analyzer import StockAnalyzer

# Введіть символ акцій для аналізу
symbol = 'AAPL'\
start_date = '2023-08-04'\
end_date = '2024-01-18'

# Створення об'єкту StockAnalyzer
stock_analyzer = StockAnalyzer(symbol, start_date, end_date)

# Виведення свічкового графіка
stock_analyzer.plot_candlestick(title=f"{symbol} Candlestick Chart")\

# Структура проекту

 con_project.py: Містить клас StockAnalyzer, який відповідає за аналіз та відображення свічкових графіків.

 requirements.txt: Зазначає версії бібліотек, необхідних для проекту.

 TradingView.png та Project's.png: Зображення зі оригінальної площадки та пайтон аналога для перевірки на ідентичність.

# Особливості

 Даний проект дозволяє зручно аналізувати та відображати свічкові графіки акцій за допомогою Python.

 Свічкові графіки генеруються з використанням yfinance та mplfinance бібліотек.

# Автор
Мене звати Юрій Шкап'як

Для зв'язку ось мій телеграм https://t.me/stuckinwires
