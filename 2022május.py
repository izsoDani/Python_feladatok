from pprint import pprint

epitmenyek = []
with open('utca.txt', 'r') as fajl:
    adok = fajl.readline().strip().split()
    adosavok = {'A': int(adok[0]), 'B': int(adok[1]), 'C': int(adok[2])}
    for sor in fajl:
        adatok = sor.strip().split()
        epitmeny = {'adoszam': adatok[0],
                    'utca': adatok[1],
                    'hazszam': adatok[2],
                    'adosav': adatok[3],
                    'terulet': int(adatok[4])}
        epitmenyek.append(epitmeny)
print(adosavok)
print (epitmenyek)

print(f'2. feladat. A mintában {len(epitmenyek)} telek szerepel')

adoszam = input('3. feladat. Egy tulajdonos adószáma: ')
talalat = False
for epitmeny in epitmenyek:
    if adoszam == epitmeny['adoszam']:
        print(epitmeny['utca'], epitmeny['hazszam'])
        talalat = True
if not talalat:
    print('Nem szerepel az adatállományban.')



#4.feladat
def ado(ado_savonkent, adosav, alapterulet):
    ado = alapterulet * ado_savonkent[adosav]
    if ado < 10000:
        return 0
    else:
        return ado

#5.feladat
ado_osszesites = {'A': [0, 0], 'B': [0, 0], 'C': [0, 0]}
for epitmeny in epitmenyek:
    ado_osszesites[epitmeny['adosav']][0] += 1
    ado_osszeg = ado(adosavok, epitmeny['adosav'], epitmeny['terulet'])
    ado_osszesites[epitmeny['adosav']][1] += ado_osszeg

print(f'A sávba {ado_osszesites["A"][0]} telek esik, az adó {ado_osszesites["A"][1]} Ft')
print(f'B sávba {ado_osszesites["B"][0]} telek esik, az adó {ado_osszesites["B"][1]} Ft')
print(f'C sávba {ado_osszesites["C"][0]} telek esik, az adó {ado_osszesites["C"][1]} Ft')


utca_sav = {}
for epitmeny in epitmenyek:
    if epitmeny['utca'] in utca_sav:
        utca_sav[epitmeny['utca']].add(epitmeny['adosav'])
    else:
        utca_sav[epitmeny['utca']] = set(epitmeny['adosav'])

print('6. feladat. A több sávba sorolt utcák:')
for utca in utca_sav:
    if len(utca_sav[utca]) > 1:
        print(utca)

ado_tulajdonoskent= {}
for epitmeny in epitmenyek:
    if epitmeny['adoszam'] in ado_tulajdonoskent:
        ado_tulajdonoskent[epitmeny['adoszam']] += ado(adosavok, epitmeny['adosav'], epitmeny['terulet'])
    else:
        ado_tulajdonoskent[epitmeny['adoszam']] = ado(adosavok, epitmeny['adosav'], epitmeny['terulet'])
pprint(ado_tulajdonoskent)

with open('fizetendo.txt', 'w', encoding='utf-8') as fizetendo:
    for azonosito in ado_tulajdonoskent:
        print(azonosito, ado_tulajdonoskent[azonosito], file=fizetendo)