from random import *
starter = [
    "Du er en ",
    "Du er en jæla ",
    "Du er en så ekstremt ",
    "Trynet ditt ligner en ",
    "Du minner meg om en ",
    "Jeg elsker"
]

middle = [
    "kuk",
    "fjompenisse",
    "klump",
    "knullt kebab",
    "påkjørt nakenrotte",
    "misbrukt bikkje",
    "søtnos",
    "nissemann"
]

ending = [
    ", og du fortjener det.",
    ", og moren din hater deg",
    ", og det er ingenting du kan gjøre med det.",
    ", din jæla taper",
    ", og jeg har vondt i magen."
]

def printDiss():
    string = f"{starter[randint(0, len(starter)-1)]}{middle[randint(0, len(middle)-1)]}"
    if randint(0,1):
        string+=ending[randint(0, len(ending)-1)]

    print(string)


while 1:
    inp = input("Kjør?   (Y/N)   ")
    match inp.lower():
        case "y": runAgain = True
        case "n": runAgain = False
        case _ : print("Invalid input mafakka")

    if runAgain:
        printDiss()
        print()
    else: exit()