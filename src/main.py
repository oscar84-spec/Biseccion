import math
simbolos = ["cos","sin","tan","e^x","^"]
constantes = ["math.cos","math.sin","math.tan","math.exp()","**"]
numeros = []
numEvaluados = []

#Calculamos los puntos a y b
def calcular_puntos():
    resultado_anterior = 0
    print("Calculando ...")
    for i in range(-5, 6):
        x = i
        resultado = eval(func)
        print(resultado)
        if (resultado > 0 > resultado_anterior) or (resultado < 0 < resultado_anterior):
            print(f"Cambio de signo detectado entre x = {i - 1} y x = {i}")
            numeros.append(i - 1)
            numeros.append(i)
        resultado_anterior = resultado

#evaluando los puntos en la función
def evaluar_puntos(num):
    x = num
    resultado = eval(func)
    return resultado

#primera regla en las iteraciones, cuando fxn * fa < 0
def menor_que_cero(i):
    valor_anterior = (numeros[0] + numeros[1]) / 2
    numeros[1] = valor_anterior
    fun_a = evaluar_puntos(numeros[0])
    fun_b = evaluar_puntos(numeros[1])
    xn = (numeros[0] + numeros[1]) / 2
    fxn = evaluar_puntos(xn)
    signo = fxn * fun_a
    error = abs(xn - valor_anterior) / xn
    print(f"{i} | [{numeros[0], numeros[1]}] | {fun_a:.6f} | {fun_b:.6f} | {xn:.6f} | {signo:.3f} | {error:.6f}")
    return signo

def mayor_que_cero(i):
    valor_anterior = (numeros[0] + numeros[1]) / 2  # 1 + 2 / 2 = 1.5
    numeros[0] = valor_anterior
    fun_a = evaluar_puntos(numeros[0])
    fun_b = evaluar_puntos(numeros[1])
    xn = (numeros[0] + numeros[1]) / 2  # 1 + 1.5 / 2 = 1.25
    # numeros[1] = xn
    fxn = evaluar_puntos(xn)
    signo = fxn * fun_a
    error = abs(xn - valor_anterior) / xn
    print(f"{i} | [{numeros[0], numeros[1]}] | {fun_a:.6f} | {fun_b:.6f} | {xn:.6f} | {signo:.2f} | {error:.6f}")
    return signo

def igual_a_cero(i):
    valor_anterior = (numeros[0] + numeros[1]) / 2  # 1 + 2 / 2 = 1.5
    fun_a = evaluar_puntos(numeros[0])
    fun_b = evaluar_puntos(numeros[1])
    xn = (numeros[0] + numeros[1]) / 2  # 1 + 1.5 / 2 = 1.25
    # numeros[1] = xn
    fxn = evaluar_puntos(xn)
    signo = fxn * fun_a
    error = abs(xn - valor_anterior) / xn
    print(f"{i} | [{numeros[0], numeros[1]}] | {fun_a:.6f} | {fun_b:.6f} | {xn:.6f} | {signo:.2f} | {error:.6f}")
    return signo

#Leyendo la función por el usuario
func = input("Ingrese la función en términos de x:\n")
#Reescribimos la función
for i in range(len(simbolos)):
    if simbolos[i] in func:
        func = func.replace(simbolos[i], constantes[i])

#Preguntamos si tiene los puntos a y b, si los tiene lo guardamos en numeros[] si no, llamamos
#la funcion calcular_puntos
num_init = input("¿Tiene los números iniciales a y b?\n")
if num_init =="s" or num_init == "si":
    for i in range(1,3):
        num = float(input(f"Dígite el número {i}: "))
        numeros.append(num)
    print(f"Los números son: a: {numeros[0]} y b: {numeros[1]}")
else:
    calcular_puntos()

#Preguntamos el número de iteraciones
iteraciones = int(input("¿Cuántas iteraciones desea?: "))
print("----------------------------------------------------------------------------")
print("N | [a,b] | f(ab) | f(b) | Xn | f(Xn)*f(a) | Error\n")
fa = evaluar_puntos(numeros[0])
fb = evaluar_puntos(numeros[1])
xn = (numeros[0] + numeros[1]) / 2
fxn = evaluar_puntos(xn)
signo = fxn * fa
print(f"1 | [{numeros[0],numeros[1]}] | {fa:.6f} | {fb:.6f} | {xn:.6f} | {signo:.2f} | --- ")
for i in range(2,iteraciones + 1):
    if signo < 0:
        signo = menor_que_cero(i)
    elif signo > 0:
        signo = mayor_que_cero(i)
    else:
        signo = igual_a_cero(i)