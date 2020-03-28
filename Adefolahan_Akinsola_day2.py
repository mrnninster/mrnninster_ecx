import random, string
val=input('Define your password length ')
val=int(val)

def password_generator(val):
    #generating Alphanumeric string
    alphaNum=string.ascii_letters + string.digits
    password=""
    #Password Constructor
    for x in range(0,val):
        randalpha = random.randrange(0,len(alphaNum))
        password += alphaNum[randalpha]
    print(password)
        
if(val<8):
    print("Weak Password, increase the length.")
else:
    password_generator(val)
