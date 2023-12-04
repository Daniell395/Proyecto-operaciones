from tkinter import *
from Principal import *
import sys
import os

class Data:

    def __init__(self, master):

        self.root = root
        self.root.title("Metodo por 2 fases")
        
        frame = Frame(master)
        frame.pack(side=TOP)
        
        minMax = ["max","min"]
        self.opcion = StringVar()
        self.opcion.set(minMax[0])
        self.titulo = Label(frame,text="Escoja Máximo o Mínimo:")
        self.titulo.grid(row=0,sticky=W)
        self.menuOpciones = OptionMenu(frame,self.opcion,*minMax)
        self.menuOpciones.grid(row=0,column=1)

        self.space = Label(frame,text=" ")
        self.space.grid(row=2,sticky=W)

        self.varLab = Label(frame,text="Variables")
        self.varLab.grid(row=3,sticky=W)
        self.variables = Spinbox(frame,from_=2, to=10,state="readonly",width=10)
        self.variables.grid(row=4,sticky=W)


        self.resLab = Label(frame,text="Restricciones")
        self.resLab.grid(row=5,sticky=W)
        self.restricciones = Spinbox(frame,from_=2, to=10,state="readonly",width=10)
        self.restricciones.grid(row=6,sticky=W)


        lin = Label(frame,text="")
        lin.grid(row=7,sticky=W)

        self.button = Button(frame,text="Aceptar", relief = RAISED,command = lambda:self.funcionObjetivo(master,self.opcion,self.variables,self.restricciones,self.button))
        self.button.grid(row=8,sticky=W)
        self.root.configure(bg='gray')

        self.reiniciarBoton = Button(frame, text="Reiniciar", relief=RAISED, command=lambda:self.reiniciar_programa)
        self.reiniciarBoton.grid(row=9, sticky=W)


        def reiniciar_programa(self):
        # Destruir los widgets actuales
            self.button.destroy()
            self.reiniciarBoton.destroy()
            self.titulo.destroy()
            self.menuOpciones.destroy()
            self.space.destroy()
            self.varLab.destroy()
            self.variables.destroy()
            self.resLab.destroy()
            self.restricciones.destroy()
            self.opcion.set("max")
            self.variables.delete(0, END)
            self.variables.insert(0, "2")
            self.restricciones.delete(0, END)
            self.restricciones.insert(0, "2")

            self.__init__(self.master)


    def funcionObjetivo(self, master, opcion, variables, restricciones, boton):
        """
        Función que crea la interfaz gráfica para ingresar la función objetivo.

        Args:
            master (Tk): Ventana principal de la aplicación.
            opcion (StringVar): Variable que almacena la opción seleccionada.
            variables (StringVar): Variable que almacena el número de variables.
            restricciones (StringVar): Variable que almacena el número de restricciones.
            boton (Button): Botón que se destruirá al llamar a esta función.

        Returns:
            None
        """
        boton.destroy()
        vas = int(variables.get())
        res = int(restricciones.get())
        frame2 = Frame(master)
        frame2.pack(side=TOP)
        columCount = 0
        func = Label(frame2, text=opcion.get() + " = ")
        func.grid(row=0, column=columCount)
        columCount += 1

        funcEspacios = []
        funcEspacios.append([])
        for i in range(0, vas):

            cuadrito = Entry(frame2, width=7, relief=RAISED)
            funcEspacios[0].append(cuadrito)
            cuadrito.grid(row=0, column=columCount)
            columCount += 1

            x = "x" + str(i + 1)
            xpos = Label(frame2, text=x)
            xpos.grid(row=0, column=columCount)
            columCount += 1

            if i + 1 != vas:
                suma = Label(frame2, text=" + ")
                suma.grid(row=0, column=columCount)
                columCount += 1

        lin = Label(frame2, text="")
        lin.grid(row=9, sticky=W)

        self.buttonx = Button(frame2, text="Aceptar", relief=RAISED,
                              command=lambda: self.restriccionesLlenar(master, self.opcion, vas, res, funcEspacios, self.buttonx))
        self.buttonx.grid(row=10, sticky=W)

        # self.button2 = Button(frame2,text="Aceptar", relief = RAISED,command = lambda:self.matriciar(master,self.opcion,vas,res,funcEspacios,self.button2))
        # self.button2.grid(row=10,sticky=W)
        # self.hola(master,opcion,variables,restricciones)


    def restriccionesLlenar(self,master,opcion,variables,restricciones,funcEspacios,buttonx):

        """
        Llena el formulario de restricciones en la interfaz gráfica.

        Args:
            master (Tk): La ventana principal de la aplicación.
            opcion (int): La opción seleccionada.
            variables (int): El número de variables.
            restricciones (int): El número de restricciones.
            funcEspacios (list): La lista de espacios de función.
            buttonx (Button): El botón a destruir.

        Returns:
            None
        """
        buttonx.destroy()
        for p in funcEspacios:
            for q in p:
                q.config(state="readonly")
        frame4 = Frame(master)
        frame4.pack()


        for i in range(0,restricciones):
            columCount=0
            funcEspacios.append([])
            for y in range(0,variables):
                cuadrito = Entry(frame4,width=7,relief=RAISED)
                funcEspacios[i+1].append(cuadrito)       #necesito control de cuadritos
                cuadrito.grid(row=i,column=columCount)
                columCount+=1

                x = "x"+str(y+1)
                xpos = Label(frame4,text=x)
                xpos.grid(row=i,column=columCount)
                columCount+=1

                if y+1!=variables:
                    suma = Label(frame4,text=" + ")
                    suma.grid(row=i,column=columCount)
                    columCount+=1

            simbolo = [">=","<=","="]
            self.simb = StringVar()
            self.simb.set(simbolo[0])
            self.menuOpciones = OptionMenu(frame4,self.simb,*simbolo)
            self.menuOpciones.grid(row=i,column=columCount)
            columCount+=1

            cuadrito = Entry(frame4,width=7,relief=RAISED)
            funcEspacios[i+1].append(cuadrito)
            cuadrito.grid(row=i,column=columCount)
            columCount+=1

            funcEspacios[i+1].append(self.simb)

        lin = Label(frame4,text="")
        lin.grid(row=9,sticky=W)

        self.button2 = Button(frame4,text="Aceptar", relief = RAISED,command = lambda:self.pintar(master,self.opcion,variables,restricciones,funcEspacios,self.button2,frame4))
        self.button2.grid(row=10,sticky=W)


    def pintar(self, master, opcion, variables, restricciones, funcEspacios, button2, frame4):
        """
        Pinta la interfaz gráfica y realiza operaciones basadas en los parámetros proporcionados.

        Args:
            master: El objeto maestro de la interfaz gráfica.
            opcion: La opción seleccionada.
            variables: El número de variables.
            restricciones: El número de restricciones.
            funcEspacios: La lista de espacios de función.
            button2: El botón a destruir.
            frame4: El marco de la interfaz gráfica.

        Returns:
            None
        """
        button2.destroy()
        simbolos = []
        for s in range(1, len(funcEspacios)):
            simbolos.append(funcEspacios[s][-1].get())

        resultado = []
        resultado.append(opcion.get())
        resultado.append(str(variables) + "," + str(restricciones))

        linea = []
        for x in funcEspacios[0]:
            linea.append(x.get())
        resultado.append(linea)

        for x in range(1, restricciones + 1):
            linea = []
            for y in range(0, len(funcEspacios[x]) - 1):
                linea.append(funcEspacios[x][y].get())
            linea.append(simbolos[x - 1])
            resultado.append(linea)

        resultado = self.estandarizarResultado(resultado)

        frame5 = Frame(master)
        frame5.pack(side=BOTTOM)
        ulabel = Label(frame5)
        ulabel.grid(row=0)

        main(resultado)
        archivo = open("solucionDosFases", "r")
        lineas = archivo.readlines()  # Fix: Define 'lineas' by reading lines from the file
        if lineas:
            ulabel.config(text=lineas[-1])
        else:
            ulabel.config(text="No tiene solucion")

    def estandarizarResultado(self, resultadoAux):
        """
        Estandariza el resultadoAux en forma de arreglo de strings.

        Args:
            resultadoAux (list): El resultadoAux a estandarizar.

        Returns:
            list: El resultado estandarizado como arreglo de strings.
        """
        arregloString = []

        arregloString.append(resultadoAux[0])
        arregloString.append(resultadoAux[1])
        for i in range(2, len(resultadoAux)):
            x = ""
            for j in range(len(resultadoAux[i])):
                if j < len(resultadoAux[i]) - 1:
                    x = x + str(resultadoAux[i][j]) + ","
                else:
                    x = x + str(resultadoAux[i][j])
            arregloString.append(x)
        return arregloString

    '''
    objeto matriz
    '''

root = Tk()
root.geometry("1200x600")
root.resizable(True, True)
matriz = Data(root)      
root.mainloop()
