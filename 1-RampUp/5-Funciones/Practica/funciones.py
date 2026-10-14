def conv_num_dia (num):
    if num == 1:
        return "Lunes"
    if num == 2:
        return "Martes"
    if num == 3:
        return "Miércoles"
    if num == 4:
        return "Jueves"
    if num == 5:
        return "Viernes"
    if num == 6:
        return "Sábado"
    if num == 7:
        return "Domingo"

Dias = [1, 2, 3, 4, 5, 6, 7]

for i in Dias:
    print(conv_num_dia(i))



def num_fila_piram(fila):
    # Genera la pirámide invertida
    for i in range(fila, 0, -1):
        # Imprime los números de cada fila
        for j in range(1, i + 1):
            print(j, end=" ")
        # Cambia de línea
        print()

num_fila_piram(10)


def comp(num1, num2):
    if num1 > num2:
        print(f"El {num1} es mayor que {num2}")
    elif num1 == num2:
        print(f"{num1} y {num2} son iguales")
    else:
        print(f"{num1} es menor que {num2}")

comp(7, 1)



def cont_letras(texto, letra):
    contador = 0

    for i in texto:
        if i == letra:
            contador = contador + 1

    return contador
texto = input("Texto: ")
letra = input("Letra: ")
print(cont_letras(texto,letra))


def unic(texto):
    diccionario = {}

    for letra in texto:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1

    return diccionario

print(unic("holaaa"))



def mod_elem(lista,comando,elemento):
        if comando == "add":
                lista.append(elemento)
        elif comando == "remove":
            if elemento in lista:
                lista.remove(elemento) 
        else:
                print("comando erroneo")               
        return(lista)

lista = [1,2,3,4]
comando = "add"
elemento = 3

print(lista)
print(mod_elem(lista,comando,elemento))
print(mod_elem(lista,"add",5))
print(mod_elem(lista,"remove",5))




def num_arb_pal(palabras):
    frase = " ".join(palabras)

    return frase
 
palabras = ["gerardo", "mateo", "que", "tal", "estais"]
frase = num_arb_pal(palabras)
print(frase)



def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b  

    return a

print(fibonacci(8))



import math

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio ** 2



# Dos círculos de radio 10 + un triángulo de base 3 y altura 7
resultado1 = 2 * area_circulo(10) + area_triangulo(3, 7)

# Un cuadrado de lado 10 + un círculo de radio 4 + dos círculos de radio 6
# + 5 triángulos de base 2 y altura 4
resultado2 = (
    area_cuadrado(10)
    + area_circulo(4)
    + 2 * area_circulo(6)
    + 5 * area_triangulo(2, 4)
)

print(resultado1)
print(resultado2)