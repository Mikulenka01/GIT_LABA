import pandas as pd
from data_analyzer import FinancialDataAnalyzer

# Simulace finančních dat
data = pd.DataFrame({
    'StockPrice': [100, 102, 104, 103, 105, 107]
})

# Vytvoření instance FinancialDataAnalyzer
financial_analyzer = FinancialDataAnalyzer(data)

# Výpočet a výpis výnosnosti a volatility
print("Výnosnost akcie:", financial_analyzer.calculate_return('StockPrice'), "%")
print("Volatilita akcie:", financial_analyzer.calculate_volatility('StockPrice'), "%")
