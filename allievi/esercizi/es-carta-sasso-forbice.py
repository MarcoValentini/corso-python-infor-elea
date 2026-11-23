# Scrivi un programma che gioca a Carta-Sasso-Forbice. Il programma deve:
# 1. Chiedere all'utente di scegliere: 1 (Carta), 2 (Sasso) o 3 (Forbice)
# 2. Generare una scelta casuale per il computer (1, 2 o 3)
# 3. Stampare cosa ha scelto il computer
# 4. Confrontare le scelte e determinare il vincitore
# 5. Stampare l'esito della partita

import random
import sys

# creo un dizionario con i numeri e i nomi delle giocate
nomi = {
    1: 'Carta',
    2: 'Sasso',
    3: 'Forbice'
}

# creo un set/insieme di combinazioni di vittoria
vittoria = {
    (1,2), (2,3), (3,1)
}

punti_utente = 0
punti_computer = 0

for partita in range (1,6):
    print(f"\n===Partita {partita} di 5===")
    try:
        utente = int(input("Scegli 1 (Carta), 2 (Sasso) o 3 (Forbice): "))
    except ValueError:
        print("Non hai inserito un numero valido!")
        sys.exit()

    if utente not in nomi:
        print("Non hai inserito un numero valido!")
        sys.exit()

    computer = random.randint(1,3)

    utente_str = "Carta" if utente == 1 else "Sasso" if utente == 2 else "Forbice"

    match computer:
        case 1:
            computer_str = "Carta"
        case 2:
            computer_str = "Sasso"
        case _:
            computer_str = "Forbice"

    print(f"Hai scelto {utente_str}")
    print(f"Il computer ha scelto {computer_str}")

    if utente == computer:
        print("Questa mano è finita in pareggio")
    elif (utente, computer) in vittoria:
        punti_utente += 1
        print("Hai vinto la mano!")
    else:
        punti_computer += 1
        print("Hai perso la mano!")

    print(f"Tu: {punti_utente}, Computer: {punti_computer}")

if punti_utente > punti_computer:
    print("Hai vinto la partita!")
elif punti_computer > punti_utente:
    print("Il computer ha vinto la partita!")
else:
    print("La partita è finita in pareggio")