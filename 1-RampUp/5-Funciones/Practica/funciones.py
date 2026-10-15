#en funciones solo debe quedar las funciones, sin input, sin pruebas para que no se ejecute nada. 

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





def num_fila_piram(fila):
    # Genera la pirámide invertida
    for i in range(fila, 0, -1):
        # Imprime los números de cada fila
        for j in range(1, i + 1):
            print(j, end=" ")
        # Cambia de línea
        print()




def comp(num1, num2):
    if num1 > num2:
        print(f"El {num1} es mayor que {num2}")
    elif num1 == num2:
        print(f"{num1} y {num2} son iguales")
    else:
        print(f"{num1} es menor que {num2}")





def cont_letras(texto, letra):
    contador = 0

    for i in texto:
        if i == letra:
            contador = contador + 1

    return contador



def unic(texto):
    diccionario = {}

    for letra in texto:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1

    return diccionario





def mod_elem(lista,comando,elemento):
        if comando == "add":
                lista.append(elemento)
        elif comando == "remove":
            if elemento in lista:
                lista.remove(elemento) 
        else:
                print("comando erroneo")               
        return(lista)






def num_arb_pal(palabras):
    frase = " ".join(palabras)

    return frase
 




def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b  

    return a





import math

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio ** 2



