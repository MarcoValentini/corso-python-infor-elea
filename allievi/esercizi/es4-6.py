# Scrivi un programma che gestisce i voti scolastici di uno studente
# utilizzando un dizionario. Il programma deve:
#
# 1. Creare un dizionario con 4 materie e i relativi voti
# 2. Stampare la materia in cui lo studente ha preso il voto più alto
# 3. Modificare il voto di una materia a scelta (es. Matematica)
# 4. Verificare se la materia "Fisica" è presente nel dizionario
# 5. Stampare il dizionario finale

voti = {
    "italiano": 8,
    "matematica": 9,
    "informatica": 9,
    "inglese": 8.5
}

voto_max = 0
materie_max = []

for materia in voti:
    voto = voti[materia]

    if voto > voto_max:
        voto_max = voto

        materie_max.clear()
        materie_max.append(materia)
    elif voto == voto_max:
        materie_max.append(materia)

print("Il voto massimo è:", voto_max)
print("Materie massime:", materie_max)

voti["matematica"] = 6

if "fisica" in voti:
    print("La materia fisica è presente!")
else:
    print("La materia fisica non è presente!")

print(voti)