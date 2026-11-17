# Scrivi un programma che gestisce le scorte di una libreria
# utilizzando un dizionario. Il programma deve:
#
# 1. Creare un dizionario con 3 libri e il numero di copie
# 2. Stampare ogni libro e la relativa disponibilità
# 3. Chiedere all'utente il titolo di un nuovo libro da aggiungere
# 4. Aggiungere il nuovo libro al dizionario con 5 copie
# 5. Stampare il dizionario finale

scorte = {
    "Il Signore degli Anelli": 3,
    "1984": 5,
    "Harry Potter": 2,
}

print("Scorte attuali della libreria:")
for titolo, copie in scorte.items():
    print(f"- {titolo}: {copie} copie")

nuovo_titolo = input("Inserisci il titolo di un nuovo libro da aggiungere: ").strip().title()

if nuovo_titolo in scorte:
    print(f"Il libro '{nuovo_titolo}' è già presente nella libreria.")
else:
    scorte[nuovo_titolo] = 5

print(scorte)

