while cislo <=5:
    print("Toto je" , cislo, "opakovani")
    cislo +=1

    for i in range (1,6):
        if i == 3:
        break
    print(i)

    for i in range(1, 6):
        if i == 3:
        continue
        print(i)