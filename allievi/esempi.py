# risposta = input("Scrivi la tua risposta: ")
# print(type(risposta))
# print(risposta.isalnum())

# a = False
# b = False
# if a and b:
#     print("Entrambe vere")
# elif a or b:
#     print("Solo una vera")
# else:
#     print("Nessuna vera")

# In alternativa all'operatore ternario in linea si può usare l'operatore ternario annidato
# (nested ternary operator) per valutare più condizioni in una sola riga di codice.
# Ad esempio:
punteggio = 55
giudizio = "Ottimo" \
    if punteggio >= 75 \
    else "Sufficiente" \
        if punteggio >= 60 \
        else "Insufficiente"
print(giudizio)

