# Sample list to be used
T_L=[1,2,3,4,5,6]

#input value to search for
BSN=input('input search number ')

#Created Function
def binary(T_L,BSN):
    BSN=int(BSN)
    count=len(T_L)
    mid=count%2
    point=int(count/2)
    s1=[]
    s2=[]
    if(mid==0):
        for r in range (0,point):
            s1.append(T_L[r])
        for u in range (point,count):
            s2.append(T_L[u])
        t=int(len(s1)-1)
        if(len(s1)==0):
            print("All hope has been lost")
        else:
            if(BSN==s1[t]):
                print('Value located in list ')
                print(BSN)
                print(s1)
            elif(BSN<s1[t]):
                T_L=s1
                binary(T_L,BSN)
            else:
                T_L=s2
                binary(T_L,BSN)
    elif(mid==1):
        point=point+1
        try:
            for r in range (0,point):
                s1.append(T_L[r])
        except:
            point=(point-1)
            for r in range (0,point):
                s1.append(T_L[r])
        try:
            for u in range (point,count):
                s2.append(T_L[u])
        except:
            print('Last inner list under evaluation')
        t=int(len(s1)-1)
        if(BSN==s1[t]):
            print('Value located in list ')
            print(BSN)
            print(s1)
        elif(BSN<s1[t]):
            T_L=s1
            binary(T_L,BSN)
        else:
            T_L=s2
            binary(T_L,BSN)
binary(T_L,BSN)