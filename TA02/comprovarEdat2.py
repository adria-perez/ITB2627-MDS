try:
    edat = int(input("Quina edat tens? "))

    if edat >= 18:
        print("Ets major d'edat.")
    else:
        print("No ets major d'edat.")

except ValueError:
    print("Has d'introduir un número.")
