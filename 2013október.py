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
    print((int(ellenorzes['ora'][-1])*3600 + int(ellenorzes['perc'][-1]*60) + int(ellenorzes['mp'][-1])) - (int(ellenorzes['ora'][0])*3600 + int(ellenorzes['perc'][0])*60 + int(ellenorzes['mp'][0])))