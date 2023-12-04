import copy
from MetodoSimplex import*
tabla=[[]]
varSeleccion=0
arregloColumnas=[]
arregloFilas=["Z"]
arregloZ=[]
arreglo_Z2=[]

class Z_Aux:


    def __init__(self,NUM,letra):
      
        self.NUM=NUM
        self.letra=letra 

class Z:

    def __init__(self,arreglo,min,u):
        self.min= min
        self.restricciones=arreglo
        self.u= u

    '''
    Funcion en la cual se crean los objetos
    correspondientes a las variables basicas
    con sus respectivos atributos del numero y
    letra ya sea x1 x2 etc
    Ademas se agrega la solucion identificada mediante SOL
    '''    
    def crearZ(self):
        global tabla
        self.conversionNulos()
        for i in range(len(self.u)):
            global arregloZ
            if self.min == True:
                z=Z_Aux(self.u[i]*-1,"x"+str(i+1))
            else:
                z=Z_Aux(self.u[i],"x"+str(i+1))
            arregloZ.append(z)
        sol=Z_Aux(0,"SOL")
        arregloZ.append(sol)


        """
        Busca un elemento en el arregloZ y devuelve su índice si se encuentra, de lo contrario devuelve -1.

        Parámetros:
        - identificador: El identificador a buscar en el arregloZ.

        Retorna:
        - El índice del elemento si se encuentra, de lo contrario -1.
        """

    def buscarArreglo(self, identificador):

        global arregloZ
        for x in range(len(arregloZ)):
            if arregloZ[x].letra == identificador:
                return x
        return -1


    def verificarMinX(self,NUM):
        if self.min is True:
            return NUM*-1
        else: return NUM
       
    '''
    Funcion la cual va agregando va recorriendo restriccion por restriccion
    para realizar la suma correspondiente de acuerdo al despeje
    de las variables artificiales con los valores de la funcion objetivo
    '''
    def agregarRestricciones(self):
        global arregloZ
        for i in range (len(self.restricciones)):
     
            if self.restricciones[i][len(self.restricciones[i])-1]!= "<=":
                for j in range(len(self.restricciones[i])-2): 
                    if self.buscarArreglo("x"+str(j+1)) != -1: 
                        numero = self.verificarMinX(self.restricciones[i][j])

                numero = self.verificarMinX(self.restricciones[i][len(self.restricciones[i])-2])
                x=self.buscarArreglo("SOL")
                 
            self.cambiarSignos()


    def cambiarSignos(self):
        global arregloZ,tabla
        arregloZ[len(arregloZ)-1].NUM=arregloZ[len(arregloZ)-1].NUM*-1
        for x in range(len(arregloZ)):
            tabla[0][self.ubicar(arregloZ[x])]=arregloZ[x]    


    def ubicar(self,elemento):
        global arregloColumnas
        for x in range(len(arregloColumnas)):
            if elemento.letra == arregloColumnas[x]:
                return x
        return -1         

    ''' 
    Funcion que se utliza para 
    la creacion de objetos pertenecientes a las 
    variables de holgura en donde el valor del numero 
    corresponde a 0 0
    '''
    def conversionNulos(self):
        for x in range(len(arregloColumnas)):
            z=Z_Aux(0,arregloColumnas[x])
            tabla[0][x]=z

class Matriz:
    def __init__(self, arreglo):
        self.matriz = arreglo
       
    def set_Matriz(self, valor): 
        print("Matriz cambiada")
        self.matriz = valor

    def get_Matriz(self): 
        return self.matriz

    '''
    Funcion en la cual se crea la matriz a utilizar
    contando las variables artificiales, holgura y basicas
    en caso de tenerlas
    Ademas se agregan dos columnas extra para colocar
    la solucion y el resultado de la division para
    la seleccion del fila pivot
    '''
    def cantidad_filas(self):
        if(len(self.matriz) != 0):
           global varSeleccion, tabla
           filas=varSeleccion+2 
           for i in range (len(self.matriz)):
               indica = self.matriz[i][len(self.matriz[i])-1]
               filas+=self.cantidad_filasAux(indica)
        tabla=[[0 for i in range(filas)] for i in range(len(self.matriz)+1)]

    def cantidad_filasAux(self,argument): 
        switcher = {">=": 2}
        return switcher.get(argument, 1)

    def variablesX(self):
        global varSeleccion
        for i in range (0,varSeleccion):
            arregloColumnas.append("x"+str(i+1))

class Restricciones:
    def __init__(self, arreglo,min):
        self.matriz = arreglo
        self.varR=1
        self.varS=1
        self.min=min
    '''
    Funcion en la cual se colococan dentro de la tabla general a utilizar
    un 1 0 -1 a las variables correspondientes a las artificiales
    '''   
    def colocar_Restricciones(self):
        global varSeleccion
        posicion = varSeleccion-1
        
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])-2):
                tabla[i+1][j]=self.matriz[i][j]
            m = Matriz(self.matriz)
            self.verificar_Signo(self.matriz[i][len(self.matriz[i])-1])
            x= m.cantidad_filasAux(self.matriz[i][len(self.matriz[i])-1])
            posicion += x
            tabla[i+1][len(tabla[i])-2]=self.matriz[i][len(self.matriz[i])-2]
            if x == 2:
                tabla[i+1][posicion-1]=1
                tabla[i+1][posicion]=-1
            else: tabla[i+1][posicion]=1

        arregloColumnas.append("SOL")
        arregloColumnas.append("XB")

    '''
    Funcion en la cual se agrega al arreglo que muestra las filas
    y las columnas una R representando variable artificial
    y una S en caso de ser una variable de holgura
    Se le adiciona el nuemero para poder diferenciarlas
    '''   
    def MayorIgual(self):
        arregloColumnas.append("R"+str(self.varR))
        arregloColumnas.append("S"+str(self.varS))
        arregloFilas.append("R"+str(self.varR))
        z=Z_Aux(0,"S"+str(self.varS))
        global arregloZ
        arregloZ.append(z)
        self.varR+=1
        self.varS+=1
        
    def verificar_Min(self,argument):
        switcher = {True: 1}
        return switcher.get(argument, -1)
            
    '''
    Funcion la cual agrega una S asemejando a una variable
    holgura tanto al arreglo de filas como el arreglo 
    de columnas , es cuando se recibe un signo <=
    '''
    def MenorIgual(self):
        arregloColumnas.append("S"+str(self.varS))
        arregloFilas.append("S"+str(self.varS))
        self.varS+=1

    '''
    Funcion en la que se agrega una R asimilando 
    una variable artificial, se agrega cuando 
    en la restriccion el signo es un =, se anade 
    al arreglo de filas y columnas
    '''
    def Igual(self):
        arregloColumnas.append("R"+str(self.varR))
        arregloFilas.append("R"+str(self.varR))
        self.varR+=1    
 
    def verificar_Signo(self,signo): 
        switcher = {">=": self.MayorIgual,"<=": self.MenorIgual, "=": self.Igual }
        switcher [signo]()



    '''
    Clase Controlador que se encarga de controlar la implementación del método simplex.

    Atributos:
    - minimo (bool): Indica si se busca minimizar (True) o maximizar (False) la función objetivo.
    - U (list): Lista que representa la función objetivo.
    - restricciones (list): Lista que contiene las restricciones del problema.
    - vars (list): Lista que contiene las variables de decisión del problema.
    - file (file): Archivo en el que se escribirán los resultados.
    - esDual (bool): Indica si se utiliza el método dual (True) o no (False).

    Métodos:
    - __init__(self, minimo, U, restricciones, vars, file, esDual): Constructor de la clase Controlador.
    - inicioControlador(self): Método que controla la implementación del método simplex.
    - imprimirResultadoDual(self, matrizDual): Método que imprime los resultados del problema original en caso de utilizar el método dual.
    - hacerCeros(self, nuevaTabla, arregloFilas, nuevoArregloCol): Método que realiza operaciones para hacer ceros en la tabla.
    - modificar_FilaZ(self, filaPivot, columnaPivot, nuevaTabla): Método que modifica una fila de la tabla.
    - generarTablaF1(self, nuevoN): Método que genera la tabla para la fase 1 del método dos fases.
    - generarNuevoN(self): Método que genera una fila de ceros y unos para la fase 1 del método dos fases.
    - generarTablaF2(self, MatrizF1): Método que genera la tabla para la fase 2 del método dos fases.
    - eliminarVariablesArtificiales(self): Método que elimina las columnas con variables artificiales de la tabla.
    - actualizarArregloCol(self): Método que actualiza el arreglo de columnas eliminando las variables artificiales.
    '''
   
class Controlador:
    '''
    Metodo main en donde se llaman a las funciones para
    la implementacion del metodo simplex
    '''
    def __init__(self,minimo,U,restricciones,vars,file,esDual):
        global varSeleccion
        self.esDual=esDual
        self.archivo=file
        varSeleccion=vars
        self.esMinimizar= minimo
        self.arregloZ=U
        self.arregloEntrada=restricciones


    '''
    Funcion en la cual se controla la creacion del areglo con objetos
    pertenecientes a la fila U, ademas se crea la tabla de forma estandarizada
    '''
    def inicioControlador(self):    
        print("\n * R = Var Artificial    \n * S = Var Holgura       \n * X = Var Decision      \n\n")
        self.archivo.write("\n * R = Var Artificial    \n * S = Var Holgura       \n * X = Var Decision      \n\n")
        dosFases = False
        for i in range(len(self.arregloEntrada)):
            if self.arregloEntrada[i][-1] != "<=":
                dosFases = True
                break

        matriz = Matriz(self.arregloEntrada) 
        matriz.cantidad_filas()
        matriz.variablesX()
        restricciones=Restricciones(self.arregloEntrada,self.esMinimizar)
        restricciones.colocar_Restricciones()
        
        z=Z(self.arregloEntrada,self.esMinimizar,self.arregloZ)
        z.crearZ()
        z.agregarRestricciones()

        global arregloFilas,arregloColumnas,tabla

        if self.esDual == True:
            pass

        else:

            if dosFases == False:
                MS=MetodoSimplex(tabla,arregloFilas,arregloColumnas,self.esMinimizar,self.archivo)
                MS.start_MetodoSimplex_Max()

            else:
                #Fase1#
                print("\n** Metodo dos fases **\n")
                print("\n-> Fase #1\n")
                nuevoN = self.generarNuevoN()
                nuevaTabla = self.generarTablaF1(nuevoN)

                MS=MetodoSimplex(nuevaTabla,arregloFilas,arregloColumnas,self.esMinimizar,self.archivo)
                MatrizF1 = MS.start_MetodoSimplex_Max()

                print("\nFase 1 Lista\n")
                
                #Fase2#
                print("\n->Fase #2\n")
                self.generarTablaF2(MatrizF1)
                nuevaTabla = self.eliminarVariablesArtificiales()    
                nuevoArregloCol = self.actualizarArregloCol()
                tablaCeros = self.hacerCeros(nuevaTabla,arregloFilas, nuevoArregloCol)            
                MS=MetodoSimplex(nuevaTabla,arregloFilas,nuevoArregloCol,self.esMinimizar,self.archivo)
                MatrizF1 = MS.start_MetodoSimplex_Max()
                print("Fase 2 Lista")
    
    def imprimirResultadoDual(self, matrizDual):
        arregloDual =  []
        for i in range(len(matrizDual[0])):

            if matrizDual[0][i].letra !=  "SOL":
                if "S" in matrizDual[0][i].letra:
                    arregloDual.append((round(matrizDual[0][i].NUM*-1,2)))
        return arregloDual

    def hacerCeros(self, nuevaTabla, arregloFilas, nuevoArregloCol):
        for i in range(len(nuevoArregloCol)):
            for j in range(len(arregloFilas)):
                if arregloFilas[j] == nuevoArregloCol[i]:
                    nuevaTabla = self.modificar_FilaZ(j,i, nuevaTabla)

        return nuevaTabla

    def modificar_FilaZ(self,filaPivot,columnaPivot,nuevaTabla):
        lista=[]
        lista2=[]
        for i in range(len(nuevaTabla[0])-2):
            arg2=nuevaTabla[0][columnaPivot].NUM
            y=nuevaTabla[0][i].NUM-arg2*nuevaTabla[filaPivot][i]
            lista2.append(y)
        arg2=nuevaTabla[0][columnaPivot].NUM
        if self.esMinimizar is True:
            y=nuevaTabla[0][len(nuevaTabla[0])-2].NUM-arg2*nuevaTabla[filaPivot][len(nuevaTabla[0])-2]
        else:
            y=nuevaTabla[0][len(nuevaTabla[0])-2].NUM+arg2*nuevaTabla[filaPivot][len(nuevaTabla[0])-2]
        lista2.append(y)
        x=0
        while x < len(lista2):
            nuevaTabla[0][x].NUM=lista2[x]
            x+=1
        return nuevaTabla
    ''' 
    Funcion encargada de colocar el nuevo U para realizar la primera fase
    '''
    def generarTablaF1(self,nuevoN):
        global tabla
        tablaAux = copy.deepcopy(tabla)
        nuevoZ = []
        x = 0
        for i in range(len(tablaAux[0])):
            x = nuevoN[i] + x
            for j in range(len(tablaAux)):
                if j != 0:
                    x = tablaAux[j][i] + x
            nuevoZ.append(x)
            x = 0
        for i in range(len(tablaAux[0])):
            tablaAux[0][i].NUM = nuevoZ[i]

        return tablaAux

    '''
    Crea una fila de 0 y -1(si es artificial), para realizar 
    la suma de columnas y poder calcular el U de la primera Fase
    '''
    def generarNuevoN(self):       
        arreglo = []
        for i in range(len(tabla[0])):
            if 'R' in tabla[0][i].letra:
                arreglo.append(-1)
            else:
                arreglo.append(0)
        return arreglo

    '''
    Coloca el U original en la matriz, con las filas (restricciones)
    de la fase #1
    '''
    def generarTablaF2(self, MatrizF1):
        global tabla
        for i in range(len(tabla)):
            if i > 0:
                tabla[i] = MatrizF1[i]

    '''
    Elmina las columnas con variables artificiales
    '''
    def eliminarVariablesArtificiales(self):
        global tabla 

        tablaF2 = []
        arregloF2 = []

        for i in range(len(tabla)):
            for j in range(len(tabla[0])):
                if 'R' not in tabla[0][j].letra:
                    arregloF2.append(tabla[i][j])

            tablaF2.append(arregloF2)
            arregloF2 = []

        return tablaF2

    '''
    Elimina las R de el arreglo que contiene los identificadores 
    de cada columna
    '''
    def actualizarArregloCol(self):
        global arregloColumnas
        nuevoArregloCol = []
        for i in range(len(arregloColumnas)):
            if 'R' not in arregloColumnas[i]:
                nuevoArregloCol.append(arregloColumnas[i])
        return nuevoArregloCol
    