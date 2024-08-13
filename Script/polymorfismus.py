import pandas as pd
from data_analyzer import FinancialDataAnalyzer, WeatherDataAnalyzer

# Příklad finančních dat
financial_data = pd.DataFrame({"Price": [100, 105, 110, 95, 120]})

# Příklad meteorologických dat
weather_data = pd.DataFrame({"Temperature": [22, 24, 19, 21, 23]})

# Vytvoření instancí analyzátorů
fin_analyzer = FinancialDataAnalyzer(financial_data)
weather_analyzer = WeatherDataAnalyzer(weather_data)

# Použití polymorfismu
fin_analyzer.analyze()
weather_analyzer.analyze()