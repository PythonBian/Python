import   math
for  i in range(7,0,-1):
    for  j  in  range(i-1):
        print(' ',end="")
    for  k  in  range(15-2*i):
        if i==4 and k==0:
            print(".",end="")
        elif i<4 and  k==0:
            print(" ",end="")
        elif i<3 and 2*i+k==14:
            print("*", end="")
        elif i < 3:
            print(",", end="")
        else:
            print("*",end="")
    for  l  in range(5+2*i):
        if  l==0 and i==7:
            print(".", end="")
        elif  i<3:
            print("*",end="")
        else:
            print(" ",end="")
    for  k  in  range(15-2*i):
        if i==7:
            print("*.", end="")
        elif  i==3  and k==0  or i<3 and  k+2*i==14:
            print(" ", end="")
        # elif  i<3 and  k+2*i==14:
        #     print()
        elif i<3 and k==0:
            print("*", end="")
        elif  i<3:
            print(",",end="")
        else:
            print("*",end="")
    print("")
for  i in range(0,5):
    for  j  in  range(math.ceil(3.3*i+1)):
        # if j==1:
        #     print(",", end="")
        # else:
        print(' ',end="")
    for  k  in  range(math.floor(12-2.3*i)):
        if (i==0 or i==3)  and k==0:
            print('.', end="")
        elif i>2 and  3*i+k==13:
            print("*", end="")
        else:
            print(",",end="")
    for  l  in range(7-2*i):
        # if  i<3:
        #     print("*",end="")
        # else:
        #     print("a",end="")

        print("*", end="")
    for k in range(math.floor(12 - 2.3* i)):
        if i==1 and k==8:
            print(",.",end="")
        elif i==4:
            print(",.",end="")
            break
        elif  i>1 and  k==0:
            print("*", end="")
        else:
            print(",", end="")
    print("")
