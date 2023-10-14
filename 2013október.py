autok = []

fajl = open("2013oktober.txt", "r")

for sor in fajl:
    auto = {}
    adatok = sor.strip(). split()
    auto['ora'] = adatok[0]
    auto['perc'] = adatok[1]
    auto['mp'] = adatok[2]
    auto['rendszam'] = adatok[3]
    autok.append(auto)
print(autok)

print("2.feladat")

for ellenorzes in autok:
    utolso_adat = autok[-1]
    elso_adat = autok[0]
    utolso_mp = int(utolso_adat['ora']) * 3600 + int(utolso_adat['perc']) * 60 + int(utolso_adat['mp'])
    elso_mp = int(elso_adat['ora']) * 3600 + int(elso_adat['perc']) * 60 + int(elso_adat['mp'])
    veg_mp = (utolso_mp - elso_mp) / 3600
print(utolso_mp)
print(elso_mp)
print("Ennyi orat dolgozak a rendorok legalabb:",veg_mp)

print("3.feladat")
ellenorzes_ideje = 0
mar_volt = []
for ora_ell in autok:
    if ora_ell['ora'] not in mar_volt:
        mar_volt.append(ora_ell['ora'])
        print(ora_ell['ora'], ora_ell['rendszam'])
    else:
        continue

