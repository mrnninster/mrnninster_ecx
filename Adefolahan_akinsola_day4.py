cell=input('Enter Phone number')
#Number check funtion
def is_Nigerian(cell):
    N=['081','080','090','070','234']
    cc=len(cell)
    if(cc!=12) and (cc in range(11,15)):
        for n in range(0,5):
            checker=N[n] in cell
            if checker==True:
                print(str(cell)+' is Nigerian')
is_Nigerian(cell)