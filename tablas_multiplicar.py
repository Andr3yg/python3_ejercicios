#Generador de tablas de multiplicar
numeros_por_multiplicar = 11 #Vamos a multiplicar hasta 10 los numeros
numero_tablas = int(input("Ingrese el numero de tablas a mostrar: ")) #Las tablas a mostrar
#numero_tablas =+ 1 #Incrementamos el valor, en programacion se cuenta desde 0
for numero in range(0,numero_tablas):
    for tabla in range(1,numeros_por_multiplicar):
        #Las tablas son hasta el numero ingresado
        print(numero,'x',tabla,'=',tabla*numero)

print("Fin")

##SIMPLIFICADO
"""
tablas_a_mostrar = int(input("Cuantas tablas quieres mostrar, desde la del 1 hasta n: "))
for tabla in range(0,tablas_a_mostrar):
    for numero in range(1,11):
        print(tabla,'x',numero,'=',tabla*numero)
"""
