import math
naplo = []
telekonyv = []

with open("2006 február.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        naplo.append(adatok)

print(naplo)

for i in range(0, len(naplo)-1, 2):
    telefonszam = {}
    ido = naplo[i]
    telefon = naplo[i+1]
    telefonszam['kezd_ora'] = int(ido[0])
    telefonszam['kezd_perc'] = int(ido[1])
    telefonszam['kezd_mp'] = int(ido[2])
    telefonszam['bef_ora'] = int(ido[3])
    telefonszam['bef_perc'] = int(ido[4])
    telefonszam['bef_mp'] = int(ido[5])
    telefonszam['telefon_szam'] = telefon[0]

    telekonyv.append(telefonszam)
print(telekonyv)

bekert = input("Adjon meg egy telefonszámot: ")
mobil = ["39", "41", "71"]

if bekert[:2] in mobil:
    print("Mobil")
else:
    print("Nem mobil")


print("3.feladat")

kezd_ora = 8#int(input("Adj meg egy kezdő órát: "))
kezd_perc = 34#int(input("Adj meg egy kezdő percet: "))
kezd_mp = 12#int(input("Adj meg egy kezdő mp: "))
veg_ora = 8#int(input("Adj meg egy veg órát: "))
veg_perc = 40#int(input("Adj meg egy veg percet: "))
veg_mp = 12#int(input("Adj meg egy veg mp: "))

kezd_besz = kezd_ora*60 + kezd_perc
veg_besz = veg_ora*60 + veg_perc


csucs = 30
csucski = 15

if 7 <= kezd_ora and veg_ora <= 18:
    print("A telefonálás díja",(veg_besz - kezd_besz)*csucs,"Ft")
if 1 <= kezd_ora and veg_ora < 7 or 18 < kezd_ora and veg_ora < 24:
    print("A telefonálás díja",(veg_besz - kezd_besz)*csucski,"Ft")

print("4.feladat")

for telo in telekonyv:
    print(math.ceil((((telo['bef_ora']*3600+telo['bef_perc']*60+telo['bef_mp'])-(telo['kezd_ora']*3600+telo['kezd_perc']*60+telo['kezd_mp']))/60)))

with open("percek.txt", "w") as percek_fajl:
    for telo in telekonyv:
        percek_fajl.write(str((math.ceil((((telo['bef_ora']*3600+telo['bef_perc']*60+telo['bef_mp'])-(telo['kezd_ora']*3600+telo['kezd_perc']*60+telo['kezd_mp']))/60)))) + " " + telo['telefon_szam'] + "\n")

print("5.feladat")
hivasok = 0

for telefonszam in telekonyv:
    if 7<= telefonszam['kezd_ora'] <=18:
        hivasok += 1
print("Összesen",hivasok,"db hívás volt a csúcsidőben")

print("6.feladat")

mobilszam = ["39", "41", "71"]
mobilpercek = 0
vezeteksepercek = 0


for telo in telekonyv:
    if telo['telefon_szam'][:2] in mobilszam:
        mobilpercek += math.ceil((((telo['bef_ora']*3600+telo['bef_perc']*60+telo['bef_mp'])-(telo['kezd_ora']*3600+telo['kezd_perc']*60+telo['kezd_mp']))/60))
    else:
        vezeteksepercek += math.ceil((((telo['bef_ora']*3600+telo['bef_perc']*60+telo['bef_mp'])-(telo['kezd_ora']*3600+telo['kezd_perc']*60+telo['kezd_mp']))/60))

print("Mobil percek",mobilpercek)
print("Vezetékes",vezeteksepercek)


print("7.feladat")
dij = 0

for telefonszam in telekonyv:
    if 7 <= telefonszam['kezd_ora'] <= 18:
        dij += (math.ceil((((telefonszam['bef_ora']*3600+telefonszam['bef_perc']*60+telefonszam['bef_mp'])-(telefonszam['kezd_ora']*3600+telefonszam['kezd_perc']*60+telefonszam['kezd_mp']))/60)))*30
print("Csúcs időben összesen",dij,"Ft-ot kell fizetnie")