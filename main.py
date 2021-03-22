import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from DiscoCifrado import discoCif, discoDesf
from maquinaDeEnigma import maquinaDeE

letra1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letra2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letra3="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class ejemplo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("frontend.ui",self)
        self.encriptarC.clicked.connect(self.fencriptarC)
        self.desencriptarC.clicked.connect(self.fdesencriptarC)
        self.encriptarV.clicked.connect(self.fencriptarV)
        self.desencriptarVV.clicked.connect(self.fdesencriptarVV)

        self.botonCifradoDCE.clicked.connect(self.discoCifrado)
        self.BatonCifradoDCD.clicked.connect(self.discoDecifrado)

        self.scroll1.setMinimum(0)
        self.scroll1.setMaximum(25)
        self.scroll1.setSingleStep(1)
        self.scroll1.setValue(0)
        self.scroll1.valueChanged.connect(self.getScroll1)

        self.scroll2.setMinimum(0)
        self.scroll2.setMaximum(25)
        self.scroll2.setSingleStep(1)
        self.scroll2.setValue(0)
        self.scroll2.valueChanged.connect(self.getScroll2)

        self.scroll3.setMinimum(0)
        self.scroll3.setMaximum(25)
        self.scroll3.setSingleStep(1)
        self.scroll3.setValue(0)
        self.scroll3.valueChanged.connect(self.getScroll3)

        self.correr.clicked.connect(self.correrME)

    def getScroll1(self):
        value = self.scroll1.value()
        a = int(value)
        self.textscroll1.setText(letra1[a])
        return letra1[a]

    def getScroll2(self):
        value = self.scroll2.value()
        a = int(value)
        self.textscroll2.setText(letra2[a])
        return letra2[a]

    def getScroll3(self):
        value = self.scroll3.value()
        a = int(value)
        self.textscroll3.setText(letra3[a])
        return letra3[a]

    def correrME(self):
        let1=letra1[self.scroll1.value()]
        let2=letra1[self.scroll2.value()]
        let3=letra1[self.scroll3.value()]

        cadena = self.datosME.text()
        palabra,scro1,scro2,scro3=maquinaDeE(cadena,self.scroll1.value(),self.scroll2.value(),self.scroll3.value())
        self.scroll1.setValue(int(scro1))
        self.scroll2.setValue(int(scro2))
        self.scroll3.setValue(int(scro3))
        self.respuesta.setText(palabra)
        s=let1+" "+let2+" "+let3
        self.resInicio.setText(s)


    def discoCifrado(self):
        cadena = self.DatoCifradoDCE.text()
        palabra=discoCif(cadena)
        self.datoDCE.setText(palabra)
        self.DatoCifradoDCD.setText(palabra)
        self.datoDCD.setText("")
        self.DatoCifradoDCE.setText("")


    def discoDecifrado(self):
        cadena = self.DatoCifradoDCD.text()
        palabra=discoDesf(cadena)
        self.datoDCE.setText("")
        self.DatoCifradoDCD.setText("")
        self.datoDCD.setText(palabra)
        self.DatoCifradoDCE.setText(palabra)


    def fencriptarC(self):
        cadena =self.datoEC1.text()
        clave1 = self.claveEC1.text()
        if cadena!="" and clave1!="":
            abc = 'abcdefghijklmnopqrstuvwxyz'
            text_cifrado = ""
            clave=int(clave1)
            for letra in cadena:
                suma = abc.find(letra) + clave
                modulo = int(suma) % len(abc)
                text_cifrado = text_cifrado + str(abc[modulo])
            self.palabraEncC.setText(text_cifrado)
            self.datoDC2.setText(text_cifrado)
            self.datoEC1.clear()
            self.claveEC1.clear()
        else:
            self.palabraEncC.setText("")

    def fdesencriptarC(self):
        cadena = self.datoDC2.text()
        clave1 = self.claveDC2.text()
        print(cadena)
        print(clave1)
        if cadena!="" and clave1!="":
            abc = 'abcdefghijklmnopqrstuvwxyz'
            text_cifrado = ""
            clave=int(clave1)
            for letra in cadena:
                suma = abc.find(letra) - clave
                modulo = int(suma) % len(abc)
                text_cifrado = text_cifrado + str(abc[modulo])
            self.palabreDesC.setText(text_cifrado)
            self.datoEC1.setText(text_cifrado)
            self.datoDC2.clear()
            self.claveDC2.clear()
        else:
            self.palabreDesC.setText("")

    def fdesencriptarVV(self):
        print("entreB")
        cadena = self.datoDV2.text()
        clave = self.claveDV2.text()
        if cadena!="" and clave!="":
            abc = 'abcdefghijklmnopqrstuvwxyz'
            text_cifrar = ""
            i = 0
            for letra in cadena:
                suma = abc.find(letra) - abc.find(clave[i % len(clave)])
                modulo = int(suma) % len(abc)
                text_cifrar = text_cifrar + str(abc[modulo])
                i = i + 1
            self.palabraDesV.setText(text_cifrar)
            self.datoEV1.setText(text_cifrar)
            self.datoDV2.clear()
            self.claveDV2.clear()
            self.palabraEncVV.clear()
        else:
            self.palabraDesV.setText("")
    def fencriptarV(self):
        print("entreA")
        cadena = self.datoEV1.text()
        clave = self.claveEV1.text()
        if cadena!="" and clave!="":
            abc = 'abcdefghijklmnopqrstuvwxyz'
            text_cifrar = ""
            i = 0
            for letra in cadena:
                suma = abc.find(letra) + abc.find(clave[i % len(clave)])
                modulo = int(suma) % len(abc)
                text_cifrar = text_cifrar + str(abc[modulo])
                i = i + 1
            self.palabraEncVV.setText(text_cifrar)
            self.datoDV2.setText(text_cifrar)
            self.claveEV1.clear()
            self.datoEV1.clear()
            self.palabraDesV.clear()
        else:
            self.palabraEncV.setText("")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = ejemplo()
    GUI.show()
    sys.exit(app.exec_())
