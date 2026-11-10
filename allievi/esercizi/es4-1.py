# Scrivi un programma che analizza una lista di temperature giornaliere
# utilizzando le operazioni base sulle liste. Il programma deve:
# 1. Creare una lista iniziale con cinque temperature e mostrarla
# 2. Trovare e mostrare la temperatura massima e minima
# 3. Mostrare la temperatura del primo giorno (posizione 0)
# 4. Mostrare la temperatura del terzo giorno (posizione 2)
# 5. Mostrare le temperature degli ultimi due giorni

temperature = [24.5, 21.2, 20.7, 26.1, 23.0]

print("Lista delle temperature:", temperature)

print(f"Temperatura massima: {max(temperature)}°")
print(f"Temperatura minima: {min(temperature)}°")

print(f"Temperatura del primo giorno: {temperature[0]}°")
print(f"Temperatura del terzo giorno: {temperature[2]}°")

print(f"Temperature degli ultimi due giorni: {temperature[-2]}°, {temperature[-1]}°")