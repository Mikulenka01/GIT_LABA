knihy = ("Bílá nemoc", "R.Ú.R" , "Válka s Mloky", "Továrna na absolutno")
hledana_kniha = "Válka s Mloky"

for kniha in knihy:

if kniha == hledana_kniha:
         print(f"Kniha '{hledana_kniha}' byla nalezena ")
break


max_pokusy = 3

for i in range (max_pokusy):
    heslo = input("Zadejte své heslo")
    if heslo == "tajneheslo":
        print("Přihlášení bylo úspěšné")
        break

    elif i == max_pokusy = 1:
        print("Překročen počet pokusů.")