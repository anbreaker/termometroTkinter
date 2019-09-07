from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    def __init__(self):
        #Heredamos de Tk y somos nuestra propia pantalla
        Tk.__init__(self) #Instancia de Tk
        #self.root = Tk()       #Iniciamos tkinter

        #Instacinas modificadas de Tk


        self.geometry("640x480")       #Asinamos tamaño ventana
        self.title("Mi Termometro")    #Titulo de la ventana
        self.configure(bg = "blue")    #Titulo de la ventana
        
    def start(self):
        #Loop de espera para eventos
        self.mainloop()



if __name__ == '__main__':
    
    app = mainApp()
    app.start()                             #Loop de espera para eventos
