def uloha3(retazec):
    samo = 'euioa'
    a = True
    for i in retazec:
        if i in samo:
            a = True
        else:
            a = False
            break
    return print(a)


uloha3("kukucka")
uloha3("aaaaaauuu")
uloha3("aeioux")
uloha3("o")
