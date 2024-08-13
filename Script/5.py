

"Máte proměnnou, která označuje věk osoby, a chcete zjistit, zda je osoba dospělá a zda má řidičský průkaz."

vek = 17
ridicak = True

if vek >= 18:
    print("Osoba je dospělá")
    if ridicak:
        print("Dospělá osoba a má řidičák")
    else:
        print("Dospělá osoba a nemá řidičák")
else:
    print("Osoba je nezletilá")
