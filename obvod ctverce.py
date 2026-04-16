# Funkce pro výpočet obvodu čtverce
def obvod_ctverce(strana):
    # Obvod čtverce = 4 × délka jedné strany. Zadejte vzorec
    obvod=4*strana
    return obvod
a=float(input("Zadej stranu čtverce: "))

# Ukázkové volání funkce
print("Ukázka pro zadání 4: ",obvod_ctverce(4))  # Očekávaný výstup: 16
print(obvod_ctverce(a))