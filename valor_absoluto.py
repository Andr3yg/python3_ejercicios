numero_a_convertir = input("Ingresa el numero: ")
try:
    numero_a_convertir=int(numero_a_convertir)
except Exception as e:
    numero_a_convertir=float(numero_a_convertir)
    
print(abs(numero_a_convertir))
