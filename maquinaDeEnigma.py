from tkinter import *

window = Tk()
window.title("MUN Enigma Machine")
window.configure(background='white')
Label(window, background='white').pack(padx=10, pady=10, side=TOP)
Label(window, text="Enigma Machine Simulator", font=("times new roman", 25), background='white').pack(padx=10, pady=10, side=TOP)


def update1(x):
    x = int(x)
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    lab1.configure(text='position : {}'.format(alphabetList[x]))


def update2(x):
    x = int(x)
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    lab2.configure(text='position : {}'.format(alphabetList[x]))


def update3(x):
    x = int(x)
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    lab3.configure(text='position : {}'.format(alphabetList[x]))


frame1 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame1.pack(side=TOP, padx=10, pady=10)
rotor1_var = DoubleVar()
scale1 = Scale(frame1, from_=0, to=25, variable = rotor1_var, showvalue=0, command=update1, length= 150, background='white')
scale1.grid(row=1, column=0, padx=60, pady=10)
rotor2_var = DoubleVar()
scale2 = Scale(frame1, from_=0, to=25, variable = rotor2_var, showvalue=0, command=update2, length= 150, background='white')
scale2.grid(row=1, column=1, padx=60, pady=10)
rotor3_var = DoubleVar()
scale3 = Scale(frame1, from_=0, to=25, variable = rotor3_var, showvalue=0, command=update3, length= 150, background='white')
scale3.grid(row=1, column=2, padx=60, pady=10)
lab1 = Label(frame1, background='white')
lab1.grid(row=2, column=0)
lab2 = Label(frame1, background='white')
lab2.grid(row=2, column=1)
lab3 = Label(frame1, background='white')
lab3.grid(row=2, column=2)
lab1.configure(text='position : A')
lab2.configure(text='position : A')
lab3.configure(text='position : A')
alphabetlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rotor1list = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y',
              'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
rotor2list = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M',
              'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
rotor3list = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y',
              'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
rotor1listTemp = []
rotor2listTemp = []
rotor3listTemp = []
reflectorBlist = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N',
                  'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
dfltPB2 = ['A', 'C', 'D', 'X', 'N',
           'T', 'F', 'M', 'B', 'O']
dfltPB1 = ['A', 'C', 'D', 'X', 'N',
           'T', 'F', 'M', 'B', 'O']
reverse = False
countf = 0
countm = 0
countf1 = 0
countm1 = 0
counts1 = 0
exportCounter = 0
exportRotors = []
helpStatus = False
finalmsg = []



def rotorsetting(l, m, n):
    global rotor1list, rotor1listTemp, rotor2list, rotor2listTemp, rotor3list, rotor3listTemp, countf1, countm1, counts1
    countf1 = int(rotor3_var.get())
    countm1 = int(rotor2_var.get())
    counts1 = int(rotor1_var.get())
    for e in range(l - 1):
        rotor1list.append(rotor1list[0])
        del rotor1list[0]
        #print("I ran", e)
    rotor1listTemp = rotor1list
    rotor1list = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y',
                  'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
    for f in range(m - 1):
        rotor2list.append(rotor2list[0])
        del rotor2list[0]
    rotor2listTemp = rotor2list
    rotor2list = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M',
                  'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
    for g in range(n - 1):
        rotor3list.append(rotor3list[0])
        del rotor3list[0]
    rotor3listTemp = rotor3list
    rotor3list = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y',
                  'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']

def shift():
    global countf, countm, countf1, countm1, counts1, rotor1listTemp, rotor2listTemp, rotor3listTemp
    rotor3listTemp.append(rotor3listTemp[0])
    del rotor3listTemp[0]
    countf += 1

    countf1 += 1
    if countf1 == 26:
        scale3.set(0)
        countf1 = 0
        countm1 += 1
        if countm1 == 26:
            scale2.set(0)
            countm1 = 0
            counts1 += 1
            if counts1 == 26:
                scale1.set(0)
                counts1 = 0
            else:
                scale1.set(counts1)
        else:
            scale2.set(countm1)
    else:
        scale3.set(countf1)

    if countf % 26 == 0:
        rotor2listTemp.append(rotor2listTemp[0])
        del rotor2listTemp[0]

    if countm % 26 == 0 and countm != 0:
        rotor1listTemp.append(rotor1listTemp[0])
        del rotor1listTemp[0]

def reflector(mssg, reflect=reflectorBlist):
    postref = []

    for char in mssg:
        if char in alphabetlist:
            changedletter = reflect[alphabetlist.index(char)]
            postref.append(changedletter)
    #print("ref", postref)
    rotor1(postref)

def rotor1(mssg):
    global reverse
    postr1 = []

    if reverse == False:
        for char in mssg:

            if char in alphabetlist:
                changedletter = rotor1listTemp[alphabetlist.index(char)]
                postr1.append(changedletter)

        reverse = True
        #print("r1", postr1)
        reflector(postr1)
    else:
        for char in mssg:

            if char in alphabetlist:
                changedletter = alphabetlist[rotor1listTemp.index(char)]
                postr1.append(changedletter)
        #print("r1", postr1)
        rotor2(postr1)

def rotor2(mssg):
    global reverse
    postr2 = []

    if reverse == False:
        for char in mssg:

            if char in alphabetlist:
                changedletter = rotor2listTemp[alphabetlist.index(char)]
                postr2.append(changedletter)

        #print("r2", postr2)
        rotor1(postr2)
    else:
        for char in mssg:

            if char in alphabetlist:
                changedletter = alphabetlist[rotor2listTemp.index(char)]
                postr2.append(changedletter)
        #print("r2", postr2)
        rotor3(postr2)

def rotor3(mssg):
    global reverse
    postr3 = []

    if reverse == False:
        for char in mssg:
            test = []
            if char in alphabetlist:
                changedletter = rotor3listTemp[alphabetlist.index(char)]
                postr3.append(changedletter)
                test.append(postr3[-1])
                #print("r3inloop postr3andTest", postr3, test)
                #print("r3list is now", rotor3listTemp)
                rotor2(test)
                shift()
    else:
        for char in mssg:

            if char in alphabetlist:
                changedletter = alphabetlist[rotor3listTemp.index(char)]
                postr3.append(changedletter)
        #print("r3 (rev T)", postr3)
        plugboard(postr3)


def plugboard(mssg, lstplugboard1=dfltPB1, lstplugboard2=dfltPB2):
    global reverse, finalmsg
    postPB = []

    for char in mssg:

        if char in alphabetlist:

            if char in lstplugboard1:
                changedletter = lstplugboard2[lstplugboard1.index(char)]
                postPB.append(changedletter)

            elif char in lstplugboard2:
                changedletter = lstplugboard1[lstplugboard2.index(char)]
                postPB.append(changedletter)

            else:
                postPB.append(char)

    if reverse == False:
        #print("PB", postPB)
        rotor3(postPB)
    else:
        finalmsg.append(postPB)
        reverse = False



def maquinaDeE(omssg,scro1,scro2,scro3):
    global finalmsg, countf, countm, exportCounter, exportRotors
    scale1.set(scro1)
    scale2.set(scro2)
    scale3.set(scro3)
    omssg = omssg.upper()
    rotorsetting(int(rotor1_var.get()) + 1, int(rotor2_var.get()) + 1, int(rotor3_var.get()) + 1)
    exportRotors.append(
        alphabetlist[int(rotor1_var.get())] + alphabetlist[int(rotor2_var.get())] + alphabetlist[int(rotor3_var.get())])
    mssglst = list(omssg)
    plugboard(mssglst)
    flat_list = [item for sublist in finalmsg for item in sublist]
    fnlMsg = ''.join(flat_list)
    #print("final message", fnlMsg)

    flat_list = []
    finalmsg = []
    #print(countf, countm)
    countf = 0
    countm = 0
    #print("flat list is ", flat_list)
    #print("final msg is ", finalmsg)
    # output result
    value = StringVar()
    value.set(fnlMsg)
    #print(value.get())
    return value.get(),rotor1_var.get(),rotor2_var.get(),rotor3_var.get()
