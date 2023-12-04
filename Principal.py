import argparse
import sys
import re 

global tipoDeOptimizacion;
global numeroVariablesDecision;
global numeroRestricciones;
global variableU

from Controlador import*
from Imprimir import*

coeficientesFuncionObjetivo = []
restricciones = []

def main(elementosEntrada):

    global coeficientesFuncionObjetivo
    global restricciones

    archivoSalida = "solucionDosFases"
    asignarElementos(elementosEntrada)

    global numeroVariablesDecision
    file = Archivo(archivoSalida)

    controlador = Controlador(tipoDeOptimizacion,coeficientesFuncionObjetivo,restricciones,int(numeroVariablesDecision),file.getArchivo(),False)
    controlador.inicioControlador()
    float

def fname(arg):
    pass

def asignarElementos(elementosEntrada):
    """
    Asigna los elementos de entrada y realiza las validaciones correspondientes.

    Args:
        elementosEntrada (list): Lista que contiene los elementos de entrada.

    Returns:
        None
    """
    validarTipoOptimizacion(elementosEntrada[0])
    validarNumeroArgumentos(elementosEntrada[1])
    validarCoeficientesFuncionObjetivo(elementosEntrada[2])
    validarRestricciones(elementosEntrada)


def validarTipoOptimizacion(optimizacion):
    """
    Valida el tipo de optimización ingresado.

    Parámetros:
    optimizacion (str): El tipo de optimización a validar.

    Retorna:
    None
    """
    global tipoDeOptimizacion
    if optimizacion == "min" or optimizacion == "max":
        if optimizacion == "min":
            tipoDeOptimizacion = True
            return
        else:
            tipoDeOptimizacion = False
    else:
        print("ERROR: Tipo de optimizacion incorrecto")
        print("Usted ingreso : " + str(optimizacion))
        print("Esperaba : min o max")
        exit(0)


def validarNumeroArgumentos(linea2Archivo):
    """
    Valida el número de argumentos en la línea 2 del archivo.

    Parameters:
    linea2Archivo (str): La línea 2 del archivo que contiene los argumentos.

    Returns:
    None

    Raises:
    ValueError: Si alguno de los valores ingresados no es un entero.

    """
    global numeroRestricciones
    global numeroVariablesDecision
    numeroArgumentos = len(re.split(",| ",linea2Archivo))
    if numeroArgumentos == 2:
        numeroVariablesDecision,numeroRestricciones = linea2Archivo.split(",")
        try:
            val = float(eval(numeroVariablesDecision))
            val2 = float(eval(numeroRestricciones))
        except ValueError:
            print("ERROR: Alguno de los valores ingresados no es un entero")
            exit(0)
        return
    else:
        print("ERROR: exceso de argumentos en la linea 2 del archivo")
        print("Usted ingreso : " + str(numeroArgumentos))
        print("Se esperan 2 argumentos : Variables de Decision, Restricciones")
        exit(0)


def validarCoeficientesFuncionObjetivo(linea3Archivo):
    """
    Valida los coeficientes de la función objetivo.

    Parámetros:
    - linea3Archivo: cadena de texto que contiene los coeficientes separados por comas.

    Retorna:
    None
    """
    global numeroVariablesDecision
    global coeficientesFuncionObjetivo
    numeroArgumentos = len(re.split(",",linea3Archivo))
    args = re.split(",",linea3Archivo)
    i = 0
    if(int(numeroArgumentos) == int(numeroVariablesDecision)):
        for i in range(int(numeroVariablesDecision)):
            try:
                val = float(args[i])
            except ValueError:
                print("ERROR: Alguno de los valores ingresados no es un entero")
                exit(0)
            coeficientesFuncionObjetivo.append(float(args[i]))
    else:
        print("ERROR: El numero de coeficientes de la funcion objetivo es distinto al numero de variables de decision")
        print("Usted ingreso : " + str(numeroArgumentos))
        print("Se esperaban : " + str(numeroVariablesDecision))
        exit(0)
    return

def validarRestricciones(listaDeElementos):
    """
    Valida las restricciones ingresadas en la lista de elementos.

    Args:
        listaDeElementos (list): Lista de elementos que contiene las restricciones.

    Returns:
        None
    """
    global numeroRestricciones
    global restricciones
    global numeroVariablesDecision

    if (len(listaDeElementos)-3) == int(numeroRestricciones):

        for k in range(3,len(listaDeElementos)):

            listaAux = listaDeElementos[k]
            args = re.split(",",listaAux)

            if (len(args)-1) != (int(numeroVariablesDecision) + 1):
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

