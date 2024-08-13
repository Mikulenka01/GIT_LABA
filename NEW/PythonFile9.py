komentare ("To je super", "jsi hňup", "dobrá práce", "nesnáším to")
nevhodna_slova = ("hňup", "nesnáším")

for komentar in komentare:
    if any(slovo in komentar for slovo in nevhodna_slova):
        print("CENZURA")
        continue
        print(komentar)