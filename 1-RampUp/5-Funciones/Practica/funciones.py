<<<<<<< HEAD
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



=======
import math

def ejercicio_1(dia):
    dias_semana = {1: "Lunes",
               2: "Martes",
               3: "Miércoles",
               4: "Jueves",
               5: "Viernes",
               6: "Sábado",
               7: "Domingo"}
    return dias_semana.get(dia, "Día erróneo")

def ejercicio_2(tamaño:int=5):
    lista_8 = list(range(int(tamaño),0,-1))
    while len(lista_8) > 0:
        print(*lista_8)
        lista_8.pop(0)

def ejercicio_3(num_1, num_2):
    if num_1 == num_2:
        out = "Son iguales"
    elif num_1 > num_2:
        out = "Primer número mayor que segundo"
    else:
        out = "Segundo número mayor que primero"
    return out

def limpieza_texto(texto, dict_vocales={'á':'a',
                                        'é':'e',
                                        'í':'i',
                                        'ó':'o',
                                        'ú':'u'}):
    texto = texto.lower()

    for clave in dict_vocales:
        texto = texto.replace(clave, dict_vocales[clave])
    return texto

def ejercicio_4(frase, letra):
    frase = limpieza_texto(frase)
    return frase.count(letra.lower())

def ejercicio_5(frase):

    dict_conteo = {}
    frase = limpieza_texto(frase)

    for caracter in frase:
        if caracter not in dict_conteo.keys() and caracter not in [" ", ","]:
            dict_conteo[caracter] = frase.count(caracter)

    return dict_conteo

def ejercicio_6(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        try:
            lista.remove(elemento)
        except:
            print("El elemento no se encuentra en la lista")
    else:
        print("Comando no reconocido")
    return lista

def ejercicio_7(*args):
    return " ".join(args)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def cuadrado(l, n=1):
    return round(n * l ** 2, 2)

def triangulo(b, a):
    return round(b * a / 2, 2)

def circulo(r):
    return round(math.pi * r ** 2, 2)



if __name__ == "__main__":
    print(triangulo(3,7))
    print(circulo(10))
    print()
    
>>>>>>> upstream/main
