szavak = []

sms = open("2007május.txt", "r")
for sor in sms:
    sor = sor.strip()
    szavak.append(sor)
print(szavak)

print("1.feladat")

egyszo = input("Adjon meg egy betűt: ")

if egyszo == 'a' and 'b' and 'c':
    print('2')
elif egyszo == 'd' and 'e' and 'f':
    print('3')
elif egyszo == 'g' and 'h' and 'i':
    print('4')
elif egyszo == 'j' and 'k' and 'l':
    print('5')
elif egyszo == 'm' and 'n' and 'o':
    print('6')
elif egyszo == 'p' and 'q' and 'r' and 's':
    print('7')
elif egyszo == 't' and 'u' and 'v':
    print('8')
elif egyszo == 'w' and 'x' and 'y' and 'z':
    print('9')


print("2.feladat")

bevitel = input("Adjon meg egy szót: ")
karakterek = []

for i in bevitel:
    if i in ['a', 'b', 'c']:
        karakterek.append("2")
        continue
    if i in ['d', 'e', 'f']:
        karakterek.append("3")
        continue
    if i in ['g', 'h', 'i']:
        karakterek.append("4")
        continue
    if i in ['j', 'k', 'l']:
        karakterek.append("5")
        continue
    if i in ['m', 'n', 'o']:
        karakterek.append("6")
        continue
    if i in ['p', 'q', 'r', 's']:
        karakterek.append("7")
        continue
    if i in ['t', 'u', 'v']:
        karakterek.append("8")
        continue
    if i in ['w', 'x', 'y', 'z']:
        karakterek.append("9")
szamok = ''.join(karakterek)
print(szamok)

print("4.feladat")
hoszu = []
leghosszabb = 0
for szo in szavak:
    for i in szo:
        if len(i) > leghosszabb:
            leghosszabb = len(i)
print(leghosszabb)


print("5.feladat")
rovidek = []

for i in szavak:
    if len(i) <= 5:
        rovidek.append(i)
print(rovidek)

print("6.feladat")
def karakter_szam(egyszo):
    karakterek = []
    for i in egyszo:
        if i in ['a', 'b', 'c']:
            karakterek.append("2")
            continue
        if i in ['d', 'e', 'f']:
            karakterek.append("3")
            continue
        if i in ['g', 'h', 'i']:
            karakterek.append("4")
            continue
        if i in ['j', 'k', 'l']:
            karakterek.append("5")
            continue
        if i in ['m', 'n', 'o']:
            karakterek.append("6")
            continue
        if i in ['p', 'q', 'r', 's']:
            karakterek.append("7")
            continue
        if i in ['t', 'u', 'v']:
            karakterek.append("8")
            continue
        if i in ['w', 'x', 'y', 'z']:
            karakterek.append("9")
    return ''.join(karakterek)

szavazat = 'sziaszia'
eredmeny = karakter_szam(szavazat)
print(eredmeny)
with open('kodok.txt', 'w') as fajl:
    for szo in szavak:
        karakter_szam_sor = f"{szo} {karakter_szam(szo)}\n"
        fajl.write(karakter_szam_sor)

for szo in szavak:
    print(szo, karakter_szam(szo))

print("7.feladat")
ujszavak = []
szamesszo = []
szamsor = input("Adjon meg egy a listában szereplő számot: ")
for szo in szavak:
    szoszam = {}
    szoszam['szo'] = szo
    szoszam['szam'] = karakter_szam(szo)
    szamesszo.append(szoszam)
    if szoszam['szam'] == szamsor:
        ujszavak.append(szoszam['szo'])
print(szamesszo)
print(ujszavak)

print("8.feladat")

ujlista = []

for szo in szavak:
    sorszam = {}
    sorszam['szo'] = szo
    sorszam['szam'] = karakter_szam(szo)
    ujlista.append(sorszam)
    #print(sorszam['szo'],":",sorszam['szam'])

kodok_szavakkal = {}

for sorszam in ujlista:
    kod = sorszam['szam']
    szo = sorszam['szo']
    if kod in kodok_szavakkal:
        kodok_szavakkal[kod].append(szo)
    else:
        kodok_szavakkal[kod] = [szo]

for kod, szavak in kodok_szavakkal.items():
    if len(szavak) > 1:
        print(f"{kod}: {' '.join(szavak)}")

print("9.feladat")
leghosszabb = 0
for kod, szavak in kodok_szavakkal.items():
    if len(szavak) > leghosszabb:
        leghosszabb += (len(szavak))
        print(f"{kod}: {len(szavak)}")