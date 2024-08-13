for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

knihy = ["Bílá nemoc", "R.U.R.", "Válka s Mloky", "Továrna na Absolutno"]
hledana_kniha = "Válka s Mloky"

for kniha in knihy:
    if kniha == hledana_kniha:
        print(f"Kniha {hledana_kniha} byla nalezena v knihovně!")
        break
