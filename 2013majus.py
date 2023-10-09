szavazatok = []

fajl = open("2013majus.txt", "r")
for sor in fajl:
    jeloltek = {}
    adatok = sor.strip().split()
    jeloltek['kerulet'] = adatok[0]
    jeloltek['szavazatok'] = adatok[1]
    jeloltek['vezetek_nev'] = adatok[2]
    jeloltek['uto_nev'] = adatok[3]
    jeloltek['part'] = adatok[4]
    szavazatok.append(jeloltek)
print(szavazatok)

print("2.feladat")
print("A helyhatósági választáson", len(szavazatok) ,"képviselőjelölt indult.")

print("3.feladat")
vezeteknev = "Ablak"#input("Adja meg a jelolt vezeték nevét: ")
utonev = "Antal"#input("Adja meg a jelolt utónevét: ")

for jelolt in szavazatok:
    if vezeteknev == jelolt['vezetek_nev'] and utonev == jelolt['uto_nev']:
        print(jelolt['vezetek_nev'],jelolt['uto_nev'], jelolt['szavazatok'],"db szavazatot kapott")

print("4.feladat")

osszes_szavazat = 0
for szavazat in szavazatok:
    osszes_szavazat += int(szavazat['szavazatok'])
print("A választáson",osszes_szavazat, "állampolgár, a jogosultak",round(osszes_szavazat/12345*100, 2),"%-a vett részt.")

print("5.feladat")

GYEP = 0
HEP = 0
TISZ = 0
ZEP = 0
SEM = 0

for szavazo in szavazatok:
    if szavazo['part'] == "GYEP":
        GYEP += int(szavazo['szavazatok'])
    elif szavazo['part'] == "HEP":
        HEP += int(szavazo['szavazatok'])
    elif szavazo['part'] == "TISZ":
        TISZ += int(szavazo['szavazatok'])
    elif szavazo['part'] == "ZEP":
        ZEP += int(szavazo['szavazatok'])
    elif szavazo['part'] == "-":
        SEM += int(szavazo['szavazatok'])

print("Gyümölcsevők Pártja= ",round(GYEP/osszes_szavazat*100, 2),"%")
print("Húsevők Pártja= ",round(HEP/osszes_szavazat*100, 2),"%")
print("Tejivók Szövetsége= ",round(TISZ/osszes_szavazat*100, 2),"%")
print("Zöldségevők Pártja= ",round(ZEP/osszes_szavazat*100, 2),"%")
print("Független jelöltek= ",round(SEM/osszes_szavazat*100, 2),"%")


print("6.feladat")

legtobbek = []
legtobbszav = 0
legtobb_nber = ""
legtobb_part = ""
    
for legjobb in szavazatok:
    if int(legjobb['szavazatok']) >= legtobbszav:
        legtobbszav = int(legjobb['szavazatok'])
        legtobbek.append(legtobbszav)
        legtobb_nber = legjobb['vezetek_nev'] + " " + legjobb["uto_nev"]
        legtobb_part = legjobb['part']
print(legtobbszav, legtobb_nber, legtobb_part)

print("7.feladat")

valasztokeruletek_kepviseloi = {}

for szavazo in szavazatok:
    kerulet = szavazo['kerulet']
    gyoztes_nev = szavazo['vezetek_nev'] + ' ' + szavazo['uto_nev']
    part = szavazo['part']

    if kerulet not in valasztokeruletek_kepviseloi:
        valasztokeruletek_kepviseloi[kerulet] = []
    valasztokeruletek_kepviseloi[kerulet].append((gyoztes_nev, part))

with open('kepviselok.txt', 'w') as fajl:
    for kerulet, kepviselok in valasztokeruletek_kepviseloi.items():
        for kepviselo in kepviselok:
            gyoztes_nev, part = kepviselo
            sor = f'{kerulet} {gyoztes_nev} {part}\n'
            fajl.write(sor)

print("Az egyes választókerületek képviselői ki lettek írva a kepviselok.txt fájlba.")




