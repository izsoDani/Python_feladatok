auto = {}
autok = []

with open('autok.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        adatok = sor.strip().split()
        auto['nap'] = int(adatok[0])
        auto['idopont'] = adatok[1]
        auto['rendszam'] = adatok[2]
        auto['azonosito'] = adatok[3]
        auto['km'] = int(adatok[4])
        if adatok[5] == '0':
            auto['ki'] = True
        else:
            auto['ki'] = False
        autok.append(auto)
        auto = {}
print(autok)

print("2.feladat")

utolso_kilepes = 0
for index, auto in enumerate(autok):
    if auto['ki']:
        utolso_kilepes = index
print(f"{autok[utolso_kilepes]['nap']}. nap rendszám: {autok[utolso_kilepes]['rendszam']}")

print("3.feladat")
nap = int(input('Nap: '))
print(f"Forgalom a(z) {nap}. napon:")
for auto in autok:
    if auto['nap'] == nap:
        irany = 'ki' if auto['ki'] else 'be'
        print(f"{auto['idopont']} {auto['rendszam']} {auto['azonosito']} {irany}")

print("4.feladat")
kint_van = set()
for auto in autok:
    if auto['ki']:
        kint_van.add(auto['rendszam'])
    else:
        kint_van.remove(auto['rendszam'])
print(f"A hónap végén {len(kint_van)} autót nem hoztak vissza.")

print("5.feladat")
megtett_km = {}
for auto in autok:
    if megtett_km.get(auto['rendszam'], 0):
        megtett_km[auto['rendszam']]['aktualis km'] = auto['km']
    else:
        megtett_km[auto['rendszam']] = {}
        megtett_km[auto['rendszam']]['kezdo km'] = auto['km']
        megtett_km[auto['rendszam']]['aktualis km'] = auto['km']
print(megtett_km)
for rendszam in megtett_km:
    print(rendszam, megtett_km[rendszam]['aktualis km'] - megtett_km[rendszam]['kezdo km'])

print("6.feladat")
max_km = 0
max_azonosito = None
for index, auto in enumerate(autok):
    if not auto['ki']:
        vissza_index = index - 1
        while auto['rendszam'] != autok[vissza_index]['rendszam']:
            vissza_index -= 1
        if auto['km'] - autok[vissza_index]['km'] > max_km:
            max_km = auto['km'] - autok[vissza_index]['km']
            max_azonosito = auto['azonosito']
print(f"Leghosszabb út: {max_km} km, személy: {max_azonosito}")




