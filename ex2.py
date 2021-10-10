import csv

students = [
    {"surname": "Ivkuchev", "name": "Dmitriy", "birthday": 2002},
    {"surname": "Samigulin", "name": "Alexander", "birthday": 2003},
    {"surname": "Bystrushkin", "name": "Mikhail", "birthday": 2002},
    {"surname": "Egorova", "name": "Irina", "birthday": 2006},
    {"surname": "Kutuzova", "name": "Eva", "birthday": 2006},
]

with open("students_input.csv", "w", newline="") as file:
    columns = ["surname", "name", "birthday"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(students)

result_students = dict()

with open("students_input.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    youngest = {"birthday": 0}
    oldest = {"birthday": 9999}
    for row in reader:
        if int(row["birthday"]) > int(youngest["birthday"]):
            youngest = row
        if int(row["birthday"]) < int(oldest["birthday"]):
            oldest = row
    result_students = [oldest, youngest]

with open("students_output.csv", "w", newline="") as file:
    columns = ["surname", "name", "birthday"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(result_students)
