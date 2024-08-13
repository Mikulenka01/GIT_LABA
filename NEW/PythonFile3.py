jmeno = input('Jak se jmenuješ?')
vek = input('Kolik ti je let?')
print("Ahoj, jsem {jmeno} a je mi {vek} let" )

vek = 24
if vek < 18:
    print("Jsi nezletilý.")
elif vek == 18:
    print("Právě jsi dosáhl plnoletosti")
else:
    print("Jsi dospělý.")