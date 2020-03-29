#String Input for number with or without country code
cell=input('Enter Phone number ')

#Function to check the country
def is_Nigerian(cell):
    cc=len(cell)
    if(cc!=12) and (cc in range(11,15)):
        #for numbers starting with 0** and 234
        if(cc==11) or (cc==13):
            N=['081','080','090','070','234']
            ccs=cell[:3]
            for n in range(0,5):
                checker=N[n] in ccs
                if checker==True:
                    print(str(cell)+' is Nigerian')
                
                #When the number id not nigerian
                else:
                    print(str(cell)+' is not Nigerian')
                    break
        #for numbers starting with +234
        if(cc==14):
            ccs=cell[:4]
            checker='+234' in ccs
            if checker==True:
                print(str(cell)+' is Nigerian')
                
            #When the number id not nigerian
            else:
                print(str(cell)+' is not Nigerian')
        
    #When the number id not nigerian
    else:
        print(str(cell)+' is not Nigerian')
                
is_Nigerian(cell)
