import numpy as np

lotto = []

with open('2005május.txt', 'r', encoding='utf-8') as adatok:
    for line in adatok:
        sor = line.strip().split()
        lotto.append(list(map(int, sor)))


print(lotto)
print("1.feladat")

utolsohet = "89 24 34 11 64" #input("Adja meg az 52.hét nyerő számait:")

print("2.feladat")
rendezett = []
rendezett2 = utolsohet.split()
rendezett.append(rendezett2)
#print(rendezett2)

rendezve= []
for szam in rendezett2:
    rendezve.append(int(szam))
#print(teljes)
teljes = sorted(rendezve)

print(teljes)

print("3.feladat")
index = 1 #int(input("Adj meg egy számot 1 és 52 között: "))
print("4.feladat")
egesz_szam = index - 1
print(lotto[egesz_szam])

print('5.feladat')

kihuzottak = []

for szam in lotto:
    for i in szam:
        if i not in kihuzottak:
            kihuzottak.append(i)
        else:
            continue

'''eredmeny = [False] * 90
print(eredmeny)
for szam in lotto:
    for i in szam:
        eredmeny[i-1] = True
print(eredmeny)'''

sorrend = sorted(kihuzottak)
#print(sorrend)

lista = list(range(1, 91))
#print(lista)

if len(sorrend) < 90:
    print("Van")
else:
    print("Nincs")

print("6.feladat")
paratlan = 0


for i in sorrend:
    if i % 2 == 1:
        paratlan += 1
print("Összesen", paratlan ,"páratlan számot húztak ki!")

print("7.feladat")

lotto.append(teljes)
print(lotto)

f = open("lotto52.txt", "a")
for sor in lotto:
    string_list = list(map(str,sor))
    string = f"{' '.join(string_list)}\n"
    f.write(string)
f.close()


f = open("alap.txt", "a")
for i in lotto:
    f.write(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}\n")
f.close()

print("8.feladat")

values, counts = np.unique(lotto, return_counts=True)
print(counts)

print("9.feladat")



nyertes = [False] * 90
#print(nyertes)
for aka in lotto:
    for i in aka:
        nyertes[i - 1] = True
#print(nyertes)
primszam = 0
primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

for index, value in enumerate(nyertes):
    if value == False:
        print(index + 1)










