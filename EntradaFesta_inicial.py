edat = int(input("¿Cuantos años tienes?"))
vestit = input("¿De que color vas vestido/a?")
entrada = input("¿Dispones de entrada?")

if edat >= 18 and vestit == "Blanco" and entrada == "Si":
    print("Puedes pasar")
else: 
    print("No puedes pasar")