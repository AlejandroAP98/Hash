#Alejandro Álvarez Patiño
#1053863761
####Métodos de búsqueda Hash

##Módulo
def h(item): return item % 13
print(h(8))

##Caracteres
def strAnum(s):
    suma=0
    for x in s:
        suma += ord(x)
    return suma
def hash_str(s): return strAnum(s) % 13

print(hash_str('alejo'))

##caraceteres ponderado
def strToWeightNum(s):
    suma = 0
    for i in range(len(s)): suma += (i+1) * ord(s[i])
    return suma
def hash_str_ponderado(cadena): return strToWeightNum(cadena) % 13

print(hash_str_ponderado("alejo"))

##CentroCuadrado

def metodocentrocuadrado(item):
    num=item*item
    digitos=len(str(num))
    numeros=str(num)
    posicion=len(numeros)//2 
    if (digitos > 1 and digitos % 2 == 0): return int(numeros[posicion-1]) + int(numeros[posicion])
    else: return int(numeros[posicion]) 

def hash_cc(item): return metodocentrocuadrado(item) % 13
    
print(hash_cc(22))


