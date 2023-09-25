szavak = []

sms = open("2007május.txt", "r")
for sor in sms:
    sor = sor.strip().split()
    szavak.append(sor)
print(szavak)

print("1.feladat")

egyszo = input("Adjon meg egy betűt: ")

if egyszo == 'a' and 'b' and 'c':
    print('2')
elif egyszo == 'd' and 'e' and 'f':
    print('3')
elif egyszo == 'g' and 'h' and 'i':
    print('4')
elif egyszo == 'j' and 'k' and 'l':
    print('5')
elif egyszo == 'm' and 'n' and 'o':
    print('6')
elif egyszo == 'p' and 'q' and 'r' and 's':
    print('7')
elif egyszo == 't' and 'u' and 'v':
    print('8')
elif egyszo == 'w' and 'x' and 'y' and 'z':
    print('9')


print("2.feladat")

szo = input("Adjon meg egy szót: ")
karakterek = []

for i in szo:
    if i == 'a' or 'b' or 'c':
        karakterek.append("2")
        continue
    if i == 'd' or 'e' or 'f':
        karakterek.append("3")
        continue
    if i == 'g' or 'h' or 'i':
        karakterek.append("4")
        continue
    if i == 'j' or 'bk' or 'cl':
        karakterek.append("5")
        continue
    if i == 'm' or 'n' or 'o':
        karakterek.append("6")
        continue
    if i == 'p' or 'q' or 'r' or 's':
        karakterek.append("7")
        continue
    if i == 't' or 'u' or 'v':
        karakterek.append("8")
        continue
    if i == 'w' or 'x' or 'y' or 'z':
        karakterek.append("9")
print(karakterek)