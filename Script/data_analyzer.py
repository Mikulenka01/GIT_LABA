class DataAnalyzer:
    # Podkapitola 4: Konstruktory
    def __init__(self, data):
        self.data = data  # Atribut, který obsahuje data k analýze (Podkapitola 3: Atributy)

    # Podkapitola 3: Metody
    def summary_statistics(self):
        # Metoda pro získání základních statistik dat
        return self.data.describe()

    def calculate_average(self, column):
        # Vypočítá průměrnou hodnotu pro zadaný sloupec
        total = sum(self.data[column])
        count = len(self.data[column])
        average = total / count
        return average

    # Rozšíření pro kapitolu 3: Výpočet variance
    def calculate_variance(self, column):
        # Vypočítá varianci pro zadaný sloupec
        mean = self.calculate_average(column)
        variance = sum((x - mean) ** 2 for x in self.data[column]) / len(self.data[column])
        return variance

    # pro polymorfismus
    def analyze(self):
        # Obecná metoda pro analýzu, která bude přepsána v dceřiných třídách
        print("Provádí se obecná analýza dat.")
        return self.summary_statistics()


# dědění -podkapitola 5
class FinancialDataAnalyzer(DataAnalyzer):
    def calculate_return(self, column):
        # Výpočet jednoduchého výnosu mezi první a poslední hodnotou
        # využití metody (data)
        return (self.data[column].iloc[-1] / self.data[column].iloc[0] - 1) * 100
    def calculate_volatility(self, column):
        # Výpočet roční volatility
        return self.data[column].pct_change().std() * (252**0.5)  # předpokládáme 252 obchodních dní

    # využití metod (calculate_xxx) z hlavní třídy dataAnalyzer
    def analyze(self):
        # Přepsaná metoda pro specifické potřeby finanční analýzy
        print("Provádí se finanční analýza.")
        return {
            "Průměr": self.calculate_average("Price"),
            "Volatilita": self.calculate_volatility("Price"),
            "Výnos": self.calculate_return("Price")
        }


# polymorfismus - podkapitola 6
class WeatherDataAnalyzer(DataAnalyzer):
    def max_temperature(self, column):
        return self.data[column].max()

    def min_temperature(self, column):
        return self.data[column].min()

    def analyze(self):
        # Přepsaná metoda pro specifické potřeby meteorologické analýzy
        print("Provádí se meteorologická analýza.")
        return {
            "Maximální teplota": self.max_temperature("Temperature"),
            "Minimální teplota": self.min_temperature("Temperature")
        }
