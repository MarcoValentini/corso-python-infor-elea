# Scrivi un programma che gestisce una lista della spesa utilizzando
# le operazioni base sulle liste. Il programma deve:
# 1. Creare una lista iniziale con tre prodotti e mostrarla
# 2. Aggiungere due nuovi prodotti alla fine della lista e mostrarla
# 3. Inserire un prodotto all'inizio della lista e mostrarla
# 4. Rimuovere un prodotto specifico dalla lista e mostrarla
# 5. Ordinare la lista in ordine alfabetico e mostrarla come lista finale

prodotti = ["Farina", "Burro", "Lievito"]

prodotto1 = input("Inserisci il primo prodotto da aggiungere: ").strip().capitalize()
prodotto2 = input("Inserisci il secondo prodotto da aggiungere: ").strip().capitalize()

nuovi_prodotti = [prodotto1, prodotto2]

prodotti.extend(nuovi_prodotti)
print(prodotti)

prodotto3 = input("Inserisci un prodotto da aggiungere all'inizio della lista: ").strip().capitalize()
prodotti.insert(0, prodotto3)
print(prodotti)

richiesta = "Seleziona un prodotto da rimuovere dalla lista: "
for prodotto in prodotti:
    richiesta += "[" + str(prodotti.index(prodotto)) + "] " + prodotto + " "
indice_prodotto = int(input(richiesta))
if prodotti[indice_prodotto] in prodotti:
    prodotti.remove(prodotti[indice_prodotto])

# PROMEMORIA: gestire il caso in cui l'indice inserito non sia valido

print(prodotti)

prodotti.sort()
print("Lista finale:", prodotti)