# import math
# numero = 3.3
# parte_decimale = numero - math.floor(numero)
# arrotondamento = math.ceil(numero) if parte_decimale >= 0.5 else math.floor(numero)
# print(arrotondamento)
# print(round(numero))

# risposta = input("Scrivi la tua risposta: ")
# print(type(risposta))
# print(risposta.isalnum())
import random

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
# punteggio = 55
# giudizio = "Ottimo" \
#     if punteggio >= 75 \
#     else "Sufficiente" \
#         if punteggio >= 60 \
#         else "Insufficiente"
# print(giudizio)

# print("5".isnumeric())

# frase = "il volo parte alle nove"
# vocali = 0
# consonanti = 0
#
# for i in frase:
#     if i in "aeiou":
#         vocali += 1
#     elif i.isalpha():
#         consonanti += 1
# print(vocali, consonanti)