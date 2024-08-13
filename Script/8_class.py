class Kniha:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor

    def vypis_info(self):
        print(f"Kniha: {self.nazev}, Autor: {self.autor}")

# Vytvoření instance třídy Kniha
kniha1 = Kniha("Válka s Mloky", "Karel Čapek")
kniha1.vypis_info()  # Výstup: Kniha: Válka s Mloky, Autor: Karel Čapek

#Třídy v Pythonu jsou šablony pro vytváření objektů,
# které mohou mít atributy a metody.
# Umožňují vytvářet složitější struktury a definovat vlastní typy dat.

#V tomto příkladu třída Kniha definuje objekt,
# který má atributy nazev a autor, a metodu vypis_info, která vypíše informace o knize.