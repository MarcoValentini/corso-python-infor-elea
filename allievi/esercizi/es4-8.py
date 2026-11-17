# Scrivi un programma che analizza le competenze di due candidati
# per una posizione lavorativa utilizzando i set. Il programma deve:
#
# 1. Creare due set contenenti le competenze di due candidati diversi
# (es: linguaggi di programmazione, strumenti, soft skills)
# 2. Stampare le competenze di entrambi i candidati
# 3. Trovare e stampare le competenze comuni ad entrambi i candidati (intersezione)
# 4. Trovare e stampare le competenze che ha solo il primo candidato (differenza)
# 5. Trovare e stampare le competenze che ha solo il secondo candidato (differenza)
# 6. Trovare e stampare tutte le competenze presenti tra i due candidati (unione)
# 7. Contare e stampare il numero totale di competenze uniche tra i due candidati

#1
candidato1 = {"Python", "SQL", "HTML", "Esperienza", "Caparbia", "Tenacia"}
candidato2 = {"InDesign", "Blender", "HTML", "Lentezza", "Arroganza", "Caparbia", "Esperienza"}

#2
print("Competenze candidato 1:")
for competenza in candidato1:
    print(f"- {competenza}")
print("Competenze candidato 2:")
for competenza in candidato2:
    print(f"- {competenza}")

#3
competenze_comuni = candidato1 & candidato2
print(f"Competenze comuni: {competenze_comuni}")

#4
competenze_esclusive1 = candidato1 - candidato2
print(f"Competenze esclusive candidato 1: {competenze_esclusive1}")

#5
competenze_esclusive2 = candidato2 - candidato1
print(f"Competenze esclusive candidato 2: {competenze_esclusive2}")

#6
competenze_totali = candidato1 | candidato2
print(f"Competenze totali: {competenze_totali}")

#7
n_competenze_totali = len(competenze_totali)
print(f"Numero competenze totali: {n_competenze_totali}")