epizod = {}
epizodok = []

adatok = []
with open('lista.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        adatok.append(sor.strip())
        if len(adatok) == 5:
            epizod['datum'] = adatok[0]
            epizod['sorozat'] = adatok[1]
            epizod['resz'] = adatok[2]
            epizod['hossz'] = int(adatok[3])
            if adatok[4] == '1':
                epizod['latta'] = True
            else:
                epizod['latta'] = False

            epizodok.append(epizod)
            epizod = {}
            adatok = []

print(epizodok)

print("2.feladat")
ismert = 0
for epizod in epizodok:
    if epizod['datum'] != 'NI':
        ismert += 1
print(f'A listában {ismert} db vetítési dátummal rendelkező epizód van')


print("3.feladat")
latta = 0
for epizod in epizodok:
    if epizod['latta']:
        latta += 1
print(f"A listában lévő epizódok {(round((latta/len(epizodok) * 100), 2))}%-át látta ")

print("4.feladat")

perc_osszesen = 0
for epizod in epizodok:
    if epizod['latta']:
        perc_osszesen += epizod['hossz']
nap = perc_osszesen // (24 * 60)
ora = perc_osszesen % (24 * 60) // 60
perc = perc_osszesen % 60
print(f'Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.')

datum = input('Adjon meg egy dátumot! Dátum= ')
for epizod in epizodok:
    if epizod['datum'] <= datum and not epizod['latta']:
        print(epizod['resz'] + '\t' + epizod['sorozat'])

def hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if honap < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[honap - 1] + nap) % 7]

    return hetnapja

print("7.feladat")
vizsgalt_nap = input('Adja meg a hét egy napját (például cs)! Nap= ')
aznapi_sorozatok = set()
for epizod in epizodok:
    if 'NI' not in epizod['datum']:
        epizod_datum = epizod['datum'].split('.')
        epizod_napja = hetnapja(int(epizod_datum[0]), int(epizod_datum[1]), int(epizod_datum[2]))
    if vizsgalt_nap == epizod_napja:
        aznapi_sorozatok.add(epizod['sorozat'])
if len(aznapi_sorozatok):
    for elem in aznapi_sorozatok:
        print(elem)
else:
    print('Az adott napon nem kerül adásba sorozat.')

print("8.feladat")


sorozatok = {}
for epizod in epizodok:
    if sorozatok.get(epizod['sorozat'], 0):
        sorozatok[epizod['sorozat']]['darab_resz'] += 1
        sorozatok[epizod['sorozat']]['ossz_hossz'] += epizod['hossz']
    else:
        sorozatok[epizod['sorozat']] = {}
        sorozatok[epizod['sorozat']]['darab_resz'] = 1
        sorozatok[epizod['sorozat']]['ossz_hossz'] = epizod['hossz']

with open('summa.txt', 'w', encoding='utf-8') as kimenet:
    for kulcs in sorozatok:
        print(kulcs, sorozatok[kulcs]['ossz_hossz'], sorozatok[kulcs]['darab_resz'], file=kimenet)
