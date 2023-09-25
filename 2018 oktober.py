keritesek = []
paros = []
paratlan = []
with open('kerites.txt', 'r', encoding='utf-8') as file:
    for i in file:
        keritesek.append(i.rstrip())
        db = i.rstrip().split()
        if db[0] == '0':
            paros.append(i.rstrip())
        if db[0] == '1':
            paratlan.append(i.rstrip())
print(keritesek)
print(paros)
print(paratlan)

print("2.feladat")
print(f'Az eladott telkek száma: {len(keritesek)}')

print("3.feladat")
print(keritesek[-1])
db = keritesek[-1].split()
if db[0] == '0':
    print("A páros oldalon adták el az utolsó telket.")
    print(f'Az utolsó telek házszáma: {len(paros) * 2}')
if db[0] == '1':
    print("A páratlan oldalon adták el az utolsó telket.")
    print(f'Az utolsó telek házszáma: {len(paratlan) * 2 - 1}')


print("4.feladat")

hazszam = - 1
elozoszin = ""
for i in paratlan:
    db = i.split()
    db[2]
    if elozoszin == db[2] and db[2] != ":" and db[2] != "#" and elozoszin != ":" and elozoszin != "#":
        print(f"A szomszédossal egyezik a kerítés színe: {hazszam}")
        break
    hazszam = hazszam + 2
    elozoszin = db[2]

print("5.feladat")
haz_szam = int(input("Adja meg egy háznak a számát! "))
szin1 = ""
szin2 = ""

if haz_szam % 2 == 0: #paros
    index = int(haz_szam/2)
    print(f"A kerítés színe / állapota: {paros[index - 1].split()[2]}")
    szin1 = paros[index - 2].split()[2]
    szin2 = paros[index].split()[2]

if haz_szam % 2 == 1: # paratlan
    index = int(haz_szam / 2)
    print(f"A kerítés színe / állapota: {paratlan[index].split()[2]}")
    szin1 = paratlan[index - 1].split()[2]
    szin2 = paratlan[index + 1].split()[2]

szinek = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if szin1 != ":" and szin1 != "#":
    szinek.remove(szin1)
if szin2 != ":" and szin2 != "#":
    szinek.remove(szin2)

print(f"Egy lehetséges festési szín: {szinek.pop()}")








