def funcion(transiciones, cadena, caracteres_validos, edo):  # Recibimos parametros
    edo = validar(transiciones, cadena, edo, 0, caracteres_validos)
    return edo  # Retornamos estado final


def validar(transiciones, cad, edo, index, caracteres_validos):
    print('Entrando en funcion')
    i = 0 
    if index < len(cad):
        if cad[index] in caracteres_validos: 
            print(f'{edo}')
            estados = []
            print(f'i = {i}')
            while i < len(transiciones):
                if transiciones[i][0] == edo:
                    # Hacemos la revision en el intervalo hecho antes
                    if cad[index] == transiciones[i][2]:
                        estados.append(validar(transiciones, cad, transiciones[i][4], index+1, caracteres_validos)) 
                i += 1
            print(f'i = {i}')
            return estados
        else:
            print(f'i = {i}')
            return validar(transiciones, cad, edo, index+1, caracteres_validos)
    else:
        print(f'i = {i}')
        return edo

def imprimir(cadenas, estados_aceptables):
    for x in cadenas:
        if x in estados_aceptables:
            print("\033[1;32m"+str(x)) 
        else:
            print("\033[1;31m"+str(x)) 

# leer arcchivo txt
f = open('1.txt', 'r')

EstadosQ = []
Epsilon = []
EdoInicial = ''
EdosAceptacion = []
Sigma = []

# Metemos los estados a nuestra lista de esados
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EstadosQ.append(caracter)

# Metemos los simbolos a nuestra lista de Epsilon
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        Epsilon.append(caracter)

# Metemos el estado de start a nuestra lista de Epsilon
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EdoInicial = caracter

# Metemos los estados finales a nuestra lista de estadosFinales
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EdosAceptacion.append(caracter)

# Sigue sigma UTF-8 = "\u03A3"

mensaje = f.readline()
while(mensaje):
    palabra = ""
    for caracter in mensaje:
        if caracter != '\n':
            palabra += caracter
    Sigma.append(palabra)
    mensaje = f.readline()

f.close()

print(f'\u03A3: {Sigma}')

"""
aux = len(EstadosQ)
print(aux)
"""

Estado_final = funcion(Sigma, input("Introduzca cadena: "), Epsilon, EdoInicial)
print(f'{Estado_final}')
# imprimir(Estado_final,EdosAceptacion)