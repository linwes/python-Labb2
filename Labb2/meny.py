import json
import sys
användare = []
lista = []


def meny():
    print("1. läs in fil")
    print("2. visa json data")
    print("3. lägg till ny person")
    print("4. ta bort person")
    print("5. spara fil")
    print("6. avsluta")
    menyVal = input()
    while True:
        if menyVal == "1":
            läsfil('personer.csv', 'text/')
            meny()
            break
        elif menyVal == "2":
            visaJson = läsJson('personer.json')
            print(visaJson)
            meny()
            break
        elif menyVal == "3":
            läsJson('personer.json')
            läggTillPerson()
            meny()      
            break
        elif menyVal == "4":
            läsJson('personer.json')
            tabortPerson()
            meny()
            break
        elif menyVal == "5":
            print("din fil är sparad")
            sparaPerson('personer.json')
            meny()
            break
        elif menyVal == "6":
            sys.exit
            break
        else:
            print("Du måste skriva in rätt värde i menyn")
            print("försök igen")
            meny()
            break

def läsfil(filename, path='text/'):
    global användare
    fil = path + filename
    try:
        with open(fil, encoding='utf-8') as helaFilen:
            for x in helaFilen:
                lista.append(x)
    except FileNotFoundError as fel:
        print(fel)
        return None

    for x in lista:
        user = x.rstrip("\n").split(";")
        användare.append({"namn": user[0],
                          "efternamn": user[1],
                          "användarnamn": user[2],
                          "email": user[3]})
    sparaPerson('personer.json')


def läsJson(filename):
    global användare
    try:
        with open(filename, "r", encoding="utf-8") as läsa:
            användare = json.load(läsa)
            return användare
    except FileNotFoundError as fel:
        print(fel)
    sparaPerson('personer.json')


def läggTillPerson():
    global användare
    try:
        namn = input("skriv in namn: ")
        efternamn = input("skirv in efternamn: ")
        användarnamn = input("skriv in användarnamn: ")
        email = input("skriv in email: ")
        användare.append({
            "namn": namn,
            "efternamn": efternamn,
            "användarnamn": användarnamn,
            "email": email})
        sparaPerson('personer.json')
    except Exception as fel:
        print(fel)    


def sparaPerson(filename):
    global användare
    try:
        with open(filename, "w", encoding="utf-8") as spara:
            json.dump(användare, spara, ensure_ascii=False, indent=1)
    except FileNotFoundError as fel:
        print(fel)


def tabortPerson():
    global användare
    läsJson('personer.json')
    try:
        räknare = 0
        user = input("skriv in användarnamnet på personen du vill ta bort: ")
        for x in användare:
            if user == x['användarnamn']:
                användare.pop(räknare)
            räknare += 1
    except ValueError as fel:
        print(fel)
    sparaPerson('personer.json')