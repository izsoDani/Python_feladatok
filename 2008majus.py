smsek = []
ujsms = []

fajl = open("2008majus.txt", "r")
for sor in fajl:
    adatok = sor.strip().split()
    smsek.append(adatok)
smsek.remove(smsek[0])
print(smsek)


for i in range(0, len(smsek)-1, 2):
    kuldemeny = {}
    ido = smsek[i]
    uzenetek = smsek[i+1]
    kuldemeny['ora'] = ido[0]
    kuldemeny['perc'] = ido[1]
    kuldemeny['telefonszam'] = ido[2]
    kuldemeny['uzenet'] = uzenetek
    ujsms.append(kuldemeny)
print(ujsms)

print("2.feladat")

print(ujsms[-1])

print("3.feladat")
print("3.feladat")

leghosszabb_uzenet = ""
legrovidebb_uzenet = None

for uzenet in ujsms:
    uzenet_szovege = uzenet['uzenet']
    if len(uzenet_szovege) > len(leghosszabb_uzenet):
        leghosszabb_uzenet = uzenet_szovege
        telefonszam_hosszu = uzenet['telefonszam']
        leghosszabb_ora = uzenet['ora']
        leghosszabb_perc = uzenet['perc']

    if legrovidebb_uzenet is None or len(uzenet_szovege) < len(legrovidebb_uzenet):
        legrovidebb_uzenet = uzenet_szovege
        telefonszam = uzenet['telefonszam']
        legrovidebb_ora = uzenet['ora']
        legrovidebb_perc = uzenet['perc']

print(f"A leghosszabb üzenet {leghosszabb_ora}:{leghosszabb_perc}-kor érkezett {telefonszam_hosszu} és a szövege: {leghosszabb_uzenet}")
print(f"A legrövidebb üzenet {legrovidebb_ora}:{legrovidebb_perc}-kor érkezett {telefonszam} és a szövege: {legrovidebb_uzenet}")