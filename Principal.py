import argparse
import sys
import re 

global tipoDeOptimizacion;
global numVariablesOpcion;
global numeroRestricciones;

from Controlador import*
from Imprimir import*

coeficientesFO = []
restricciones = []

def main(elementosEntrada):

    global coeficientesFO
    global restricciones

    archivoSalida = "solucionDosFases"
    asignarElementos(elementosEntrada)

    global numVariablesOpcion
    file = Archivo(archivoSalida)

    controlador = Controlador(tipoDeOptimizacion,coeficientesFO,restricciones,int(numVariablesOpcion),file.getArchivo(),False)
    controlador.inicioControlador()
    float

def fname(arg):
    pass


def asignarElementos(elementosEntrada):
    validarTipoOptimizacion(elementosEntrada[0])
    validarNumeroArgumentos(elementosEntrada[1])
    validarCoeficientesFO(elementosEntrada[2])
    validarRestricciones(elementosEntrada)

    """
    Valida el tipo de optimización ingresado.

    Parámetros:
    optimizacion (str): El tipo de optimización a validar.

    Retorna:
    None
    """
def validarTipoOptimizacion(optimizacion):

    global tipoDeOptimizacion
    if optimizacion == "min" or optimizacion == "max":
        if optimizacion == "min":
            tipoDeOptimizacion = True
            return
        else:
            tipoDeOptimizacion = False
    else:
        print("optimizacion ingresada incorrecta")
        print("Usted ingreso : " + str(optimizacion))
        print("Esperaba : min o max")
        exit(0)

def validarNumeroArgumentos(linea2Archivo):
    global numeroRestricciones
    global numVariablesOpcion
    numeroArgumentos = len(re.split(",| ",linea2Archivo))
    if numeroArgumentos == 2:
        numVariablesOpcion,numeroRestricciones = linea2Archivo.split(",")

        try:
            val = float(eval(numVariablesOpcion))
            val2 = float(eval(numeroRestricciones))
        except ValueError:
            print("ERROR: Alguno de los valores ingresados no es un entero")
            exit(0)
        return
    else:
        print("ERROR: Se pasa de argumentos en la linea 2 del archivo")
        print("Usted ingreso : " + str(numeroArgumentos))
        print("Se esperan 2 argumentos : Variables de Decision, Restricciones")
        exit(0)

def validarCoeficientesFO(linea3Archivo):
    global numVariablesOpcion
    global coeficientesFO
    numeroArgumentos = len(re.split(",",linea3Archivo))
    args = re.split(",",linea3Archivo)
    i = 0

    if(int(numeroArgumentos) == int(numVariablesOpcion)):
        
            try:
                val = float(args[i])
            except ValueError:
                print("ERROR: Alguno de los valores ingresados no es un entero")
                exit(0)
            coeficientesFO.append(float(args[i]))
    else:
        print("ERROR: El numero de coeficientes de la funcion objetivo es distinto al numero de variables de decision")
        print("Usted ingreso : " + str(numeroArgumentos))
        print("Se esperaban : " + str(numVariablesOpcion))
        exit(0)
    return

def validarRestricciones(listaDeElementos):
    global numeroRestricciones
    global restricciones
    global numVariablesOpcion
    if (len(listaDeElementos)-3) == int(numeroRestricciones):
        for k in range(3,len(listaDeElementos)):
            listaAux = listaDeElementos[k]
            args = re.split(",",listaAux)
            if (len(args)-1) != (int(numVariablesOpcion) + 1):
                print("ERROR: Alguna restriccion se encuentra incomplete o el numero de variables de decision ingresada es incorrecto")
                exit(0)
            for i in range((len(args)-1) ):
                try:
                    val = float(eval(args[i]))
                    args[i] = float(eval(args[i]))
                except ValueError:
                    print("ERROR: Alguno de los valores ingresados no es un entero")
                    exit(0)
            if(args[-1] == "=" or args[-1] == "<=" or args[-1] == ">="):
                restricciones.append(args)
            else:
                print("ERROR: Alguna de las restricciones no cumple con ser =, <= o >=")
                print("Usted ingreso : " + str(args[-1]))
                print("Se esperaba: =, <=, o >=")
                exit(0)
    else:
        print("ERROR: Numero de restricciones diferente a la cantidad ingresada")
        print("Usted ingreso : " + str((len(listaDeElementos)-3)))
        print("Se esperaban : " + str(numeroRestricciones))
        exit(0)
    return