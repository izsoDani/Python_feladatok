reports = []

with open('tavirathu13.txt', 'r', encoding='utf-8') as meteorjelentes:
    for line in meteorjelentes:
        sor = line.strip().split(" ")
        report = {'city': sor[0],
                   'hour': sor[1][:2],
                   'minute': sor[1][2:],
                   'deg': sor[2][:3],
                   'speed': int(sor[2][3:]),
                   'temperature': int(sor[3])}
        reports.append(report)
print(reports)

print("2.feladat")
city = input("Adja meg egy település kódját! Település:")
last_report = None
for report in reports:
    if report["city"] == city:
        last_report = report
print(f'Az utolsó mérési adat a megadott településről {last_report["hour"]}:{last_report["minute"]}-kor  érkezett.')

print("3.feladat")
min_report = reports[0]
max_report = reports[0]
for report in reports:
    if report["temperature"] > max_report["temperature"]:
        max_report = report
    if report["temperature"] < min_report["temperature"]:
        min_report = report
print(f"A legalacsonyabb hőmérséklet: {min_report['city']} {min_report['hour']}:{min_report['minute']} {min_report['temperature']} fok.")
print(f"A legalacsonyabb hőmérséklet: {max_report['city']} {max_report['hour']}:{max_report['minute']} {max_report['temperature']} fok.")

print("4.feladat")
lull_reports = []
for report in reports:
    if report['speed'] == 0:
        lull_reports.append(report)
if lull_reports.__len__() == 0:
    print("Nem volt szélcsend a mérések idején")
else:
    for report in lull_reports:
        print(f"{report['city']} {report['hour']}:{report['minute']}")

print("5.feladat")
cities = set()
for report in reports:
    cities.add(report['city'])
for city in cities:
    reports_from_city = [report for report in reports if report['city'] == city]
    temperature_from_city = [report['temperature'] for report in reports_from_city]
    mean_temperature_measurements = [report['temperature'] for report in reports_from_city
                                     if report['hour'] == '01'
                                     or report['hour'] == '07'
                                     or report['hour'] == '13'
                                     or report['hour'] == '19']
    mean_temp_01 = [report['temperature'] for report in reports_from_city if report['hour'] == '01']
    mean_temp_07 = [report['temperature'] for report in reports_from_city if report['hour'] == '07']
    mean_temp_13 = [report['temperature'] for report in reports_from_city if report['hour'] == '13']
    mean_temp_19 = [report['temperature'] for report in reports_from_city if report['hour'] == '19']

    min_temp = min(temperature_from_city)
    max_temp = max(temperature_from_city)
    mean_temperature = 0
    mean_count = 0
    for temperature in mean_temperature_measurements:
        mean_temperature += temperature
        mean_count += 1
    if mean_temp_01.__len__() > 0 and mean_temp_07.__len__() > 0 and mean_temp_13.__len__() > 0 and mean_temp_19.__len__() > 0:
        mean_temperature /= mean_count
        print(f"{city} Középhőmérséklet: {int(mean_temperature.__round__(0))}; Hőmérséklet-ingadozás: {max_temp - min_temp}")
    else:
        print(f"{city} NA; Hőmérséklet-ingadozás: {max_temp - min_temp}")


print("6.feladat")
for city in cities:
    with open(f"{city}.txt", "w", encoding="utf-8") as file:
        file.write(f"{city}\n")
        reports_from_city = [report for report in reports if report["city"] == city]
        for report in reports_from_city:
            file.write(f"{report['hour']}:{report['minute']} {report['speed'] * '#'}\n")
print("A fájlok elkészültek.")





