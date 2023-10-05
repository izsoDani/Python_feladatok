import math
ulohelyek = []

fajl = open("2010majus.txt", "r")
for sor in fajl:
    adatok = sor.strip().split()
    ulohelyek.append(adatok)
fajl.close()
print(ulohelyek)

szemelyes = []
for adat in ulohelyek:
    mindenadat = {}
    mindenadat['ulohely'] = adat[0]
    mindenadat['felszall'] = adat[1]
    mindenadat['leszall'] = adat[2]
    szemelyes.append(mindenadat)
print(szemelyes)

fontos_adatok = []
elso_harom_adat = szemelyes[:1]
for elsoadatok in elso_harom_adat:
    alap_adatok = {}
    alap_adatok['elkelt'] = elsoadatok['ulohely']
    alap_adatok['uthossz'] = elsoadatok['felszall']
    alap_adatok['fizetendo'] = elsoadatok['leszall']
    fontos_adatok.append(alap_adatok)

print(fontos_adatok)

print("2.feladat")

utolso_adat = szemelyes[-1]
print("Legutolsó vásárló adatai, Sorszám:",utolso_adat['ulohely'],"Tavolsg:",(int(utolso_adat['leszall'])-int(utolso_adat['felszall'])),"km")

print("3.feladat")

for teljes in szemelyes:
    if int(teljes['leszall'])-int(teljes['felszall']) == 172:
        print(teljes['ulohely'])

print("4.feladat")

fizetendo_osszeg = []
for fizetendo in szemelyes:
    szemelyenkent = (math.ceil(int(fizetendo['leszall'])-int(fizetendo['felszall']))*71)
    fizetendo_osszeg.append(szemelyenkent)
fizetendo_osszeg = fizetendo_osszeg[1:]
print(sum(fizetendo_osszeg),"Ft")

print("5.feladat")

szaz_hatvan_ot_le = 0
szaz_hatvan_ot_fel = 0

for szazhatvanot in szemelyes:
    if szazhatvanot['leszall'] == "165":
        szaz_hatvan_ot_le += 1
    if szazhatvanot['felszall'] == "165":
        szaz_hatvan_ot_fel += 1
print(szaz_hatvan_ot_le,"leszallo volt és", szaz_hatvan_ot_fel,"felszállo")


print("6.feladat")

for megallok in szemelyes:
    megallok['leszall']









