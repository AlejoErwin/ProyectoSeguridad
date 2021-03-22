def convert(u,discoI):
    cont=0
    discoI1=""
    valiI=False
    for i in discoI:
        if i==u:
            valiI=True
        if valiI==True:
            discoI1=discoI1+i
        else:
            cont=cont+1
    for i in range(cont):
        discoI1=discoI1+discoI[i]
    discoI=discoI1
    return discoI

def palabraG(palabra):
    palabraF = ""
    import random
    ran = int(random.randrange(4))
    ran = ran + 1
    coran = 0
    for i in palabra:
        if coran == ran:
            palabraF = palabraF + str(ran)
            ran = int(random.randrange(4))
            ran = ran + 1
            # print(ran)
            coran = 1
            palabraF = palabraF + i
        else:
            palabraF = palabraF + i
            coran = coran + 1
    return palabraF

def cifrar(palabra,discoI,discoF):
    PaCifrado = ""
    for i in palabra:
        con = 0
        for j in range(24):
            if discoI[j] == i:
                if i == "1" or i == "2" or i == "3" or i == "4":
                    ccc = 0
                    cont = 0
                    discoI1 = ""
                    valiI = False
                    for rr in discoI:
                        if ccc == int(i):
                            valiI = True
                        if valiI == True:
                            discoI1 = discoI1 + rr
                        else:
                            cont = cont + 1
                        ccc = ccc + 1
                    for r in range(cont):
                        discoI1 = discoI1 + discoI[r]
                    discoI = discoI1
                    PaCifrado = PaCifrado + discoF[j]

                else:
                    PaCifrado = PaCifrado + discoF[j]

    print(PaCifrado, "cifrado")
    return PaCifrado

def decifrar(pacifrar,discoI11,discoF):
    discoI = discoI11
    palabra = pacifrar
    PaDescifrado = ""
    for i in palabra:
        con = 0
        for j in range(24):
            if discoF[j] == i:
                if discoI[j] == "1" or discoI[j] == "2" or discoI[j] == "3" or discoI[j] == "4":
                    ccc = 0
                    cont = 0
                    discoI1 = ""
                    valiI = False
                    for rr in discoI:
                        if ccc == (int(discoI[j])):
                            valiI = True
                        if valiI == True:
                            discoI1 = discoI1 + rr
                        else:
                            cont = cont + 1
                        ccc = ccc + 1
                    for r in range(cont):
                        discoI1 = discoI1 + discoI[r]
                    discoI = discoI1
                    # PaDescifrado=PaDescifrado+discoI[j]
                    break
                else:
                    PaDescifrado = PaDescifrado + discoI[j]
                    break
    print(PaDescifrado, "desifrado")
    return PaDescifrado



def discoCif(palabr):
    discoF = "acegklnprtvz&xysomqihfdb"
    discoI = "1234ABCDEFGILMNOPQRSTVXZ"
    u = "V"
    discoI = convert(u, discoI)
    f = "y"
    discoF = convert(f, discoF)
    palabra = palabr.upper()
    palabra=palabraG(palabra)
    palabra1=cifrar(palabra,discoI,discoF)
    return palabra1

def discoDesf(palabra):
    discoF = "acegklnprtvz&xysomqihfdb"
    discoI = "1234ABCDEFGILMNOPQRSTVXZ"
    u = "V"
    discoI = convert(u, discoI)
    discoI11 = discoI
    f = "y"
    discoF = convert(f, discoF)
    palabra2 = decifrar(palabra, discoI11, discoF)
    return palabra2



