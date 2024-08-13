import pandas as pd
from data_analyzer import DataAnalyzer

# Vytvoření datového rámce jako příklad dat
data = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Height': [165, 170, 175, 180],
    'Weight': [55, 60, 65, 70]
})

# Vytvoření instance třídy DataAnalyzer (Podkapitola 4: Konstruktory)
analyzer = DataAnalyzer(data)

# Výpis základních statistik (Podkapitola 3: Metody)
print("Summary Statistics:")
print(analyzer.summary_statistics().to_string())

# Výpočet a výpis průměrného věku (Podkapitola 3: Metody)
average_age = analyzer.calculate_average('Age')
print(f"Průměrný věk: {average_age}")

# Výpočet a výpis průměrné výšky (Podkapitola 3: Metody)
average_height = analyzer.calculate_average('Height')
print(f"Průměrná výška: {average_height}")
