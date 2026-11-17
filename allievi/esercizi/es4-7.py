# Scrivi un programma che gestisce una rubrica telefonica.
# Il programma deve:
#
# 1. Creare un dizionario con nomi e numeri di telefono
# 2. Chiedere all'utente una parola o una parte di nome da cercare
# 3. Cercare nel dizionario tutti i nomi che contengono quella parola
# 4. Stampare il nome trovato e il relativo numero di telefono

# metodo 1
rubrica = {
    "Marco": "+39 321 321 4321",
    "simona": "+39 765 321 4324",
    "MARIO": "+39 678 433 3456"
}

ricerca = input("Inserisci una parola o parte di nome da cercare: ").strip().lower()

corrispondenza = False

for nome, numero in rubrica.items():
    if ricerca in nome.lower():
        print(f"{nome.capitalize()}: {numero}")
        corrispondenza = True

if not corrispondenza:
    print("Nessun risultato trovato.")

# # metodo 2
# elenco_telefonico = {
#     'nomi': ['Marco', 'Simona', 'Mario'],
#     'numero_telefonico': ['+39 321 321 4321', '+39 765 321 4324', '+39 678 433 3456']
# }
#
# nome_input = input("Inserisci un nome o parte di nome da cercare: ").strip().lower()
#
# trovato = False
#
# for i in range(len(elenco_telefonico['nomi'])):
#     nome = elenco_telefonico['nomi'][i]
#     numero = elenco_telefonico['numero_telefonico'][i]
#
#     if nome_input in nome.lower():
#         print(f"{nome}: {numero}")
#         trovato = True
#
# if not trovato:
#     print("Nessun risultato trovato.")