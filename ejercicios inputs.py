#INPUTS 1
nombre=input("DAME TU NOMBRE: ")
print(nombre)

#INPUTS 2
edad=int(input("CUAL ES TU EDAD: "))
print(edad+5)

#ejercicio 3
ciu_naci = input("Donde naciste? ")
print("Naciste en " + ciu_naci)

#Ejercicio 4
print("Dame  2 numeros")
num1 = int(input())
num2 = int(input())
suma = num1 + num2
print(suma)

#Ejercicio 5
numero = int(input("Dame un numero"))
print(numero*2)

#Ejercicio 6
print("dame 3 numeros:")
nume1 = int(input())
nume2 = int(input())
nume3 = int(input())
suma2 = (nume1 + nume2 + nume3)/3
print = suma2

#Ejercicio 7
edad2 = int(input("En que año naciste?"))
print = 2025 - edad2

#INPUTS 8
mascota=str(input("COMO SE LLAMA TU MASCOTA: "))
print(mascota.upper())

#inputs 9 
cali = int(input("Dame un numero del \"0\" al \"100\""))
if cali > 70:
    print("Es mayor a 70")
else:
    print("Es menor a 70")
#TRIANGULO
filas = 5
for i in range(1, filas + 1):
    espacios = " " * (filas - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
