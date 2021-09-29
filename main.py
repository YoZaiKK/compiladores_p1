def funcion(
    transiciones, cadena, caracteres_validos, edo  # Recibimos parametros
):
    caracteres_no_validos = []
    for caracter in cadena:
        if caracter in caracteres_validos:  # Si el caracter esta entre los caracterers validos, entra al if
            edo = validar(transiciones, caracter, edo)
        else:
            caracteres_no_validos.append(caracter)
    print(f'Los caracteres no validos en la cadena son: {caracteres_no_validos}')
    return edo  # Retornamos estado final


def validar(transiciones, car, edo):
    estados = []
    i = 0
    #edo = '3' 
    for x in transiciones:
        if x[0] == edo: 
            break
        i+=1 
    if i < len(transiciones):
        while transiciones[i][0] == edo:
            if car != transiciones[i][2]:
                i += 1
            else:
                estados.append(transiciones[i][4])
                i+=1
    print(estados)
    return edo


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
