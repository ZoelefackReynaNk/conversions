#funtion converting from decimal to binary
def dec_bin(n1):
    n2=n1
    a=[]  #creat an emty list a
    i=0 #n2 is divided by 2 and remainder is append in list a using the loop
    while(abs(n2)>0):
       t=abs(n2)%2;      a.append(t)
       n2=abs(n2)//2;   i+=1
       b=[] #another list b is created
       j=i-1#this loop adds elements of a to b in a reverse order
    while(j>=0):
        b.append(a[j])  ;    j=j-1
    l=len(b)
    if(l<=7): #verify whether length of n2>7
        c=8-l
        j=0 #append 0 in list b till length of b is 8
        while(j<c):
            b.insert(0,0)
            j+=1
        l=len(b)
        if(n1>=0): #verify if n1 is possitive
            print("the binary of ",n1,"=\t",b)
        else: #if n1 is negetive
            i=0 #reverse all the 1s to 0 and 0s to 1 that is the 1CC
            while(i<l):
                if(b[i]==0):
                    del b[i]; b.insert(i,1)
                elif(b[i]==1):
                    del b[i];b.insert(i,0)
                i+=1#add 1 to 1sc to get 2sc
            #convert list b to a binary integer b
            b=bin(int(''.join(map(str, b)),2))
            t="0b00000001"
            b=bin(int(b,2) + int(t,2)) ; b=b[2:]
            l=len(b)
            if(l==8): #if len(b)=8 after convertion,print b
                print("the binary of ",n1,"=\t",b)
            elif(l<8): #if length of b<8
                c=8-l
                i=0 #add 0s till length of b=8
                while(i<c):
                    b='0'+b; i+=1
                print("the binary of ",n1,"=\t",b)    
    else: #if n1>127 or n1<-128 we call back the funtion main_dec_bin() 
        print("\tthe value entered is out of range\n\tre-enter  a value between -128 and 127")
        main_dec_bin(p-1)
#funtion converting from binary to decimal
def bin_dec(n):
    n=bin(int(n, 2)); n=n[2:] #is converted restricted to be in base 2
    l=len(n)
    a=[]; i=0 #this loop populates list a with every bit in n
    while(i<l):
        a.insert(i,n[i]); i+=1
    if(l<=8): #if length of a is less than or equal 
        c=8-l; i=0#to 8, 0 is inserted in a till l=8
        while(i<c):
            a.insert(0,0);i+=1
        a= [int(item) for item in a] #covert each element of list a into integers
        b=[] #emty list b is created
        i=1#item in index a[i] is multiplied by 2^(coresponding power) and stored in b[i]
        while(i<len(a)):
            r=a[i]*(2**((len(a)-1)-i));i+=1
            b.insert(i,r)
        dec=sum(b)+(-a[0]*2**(len(a)-1))
        print("\t\tthe decimal of \n",a,"=\t",dec)
    else:# if len(n)>8 we re-call main_bin_dec()
        print("\t\tthe element entered is out of range\n\t\tre-enter an 8 bit binary integer")
        main_bin_dec(p-1)
#driving code
t=int(input("what do you want to do \n1=decimal to binary conversion\n2=binary to decimal conversion\n"))
if(t==2):
    #void main for bin_dec
    p=int(input("\thow many times do you wish  to compute\t")) ;print("\t_________________________________________")
    def main_bin_dec(p):
        i=1
        while (i<=abs(p)):
            n=(input("\nenter the binary number to be converted to decimal\n"))
            bin_dec(n)
            i+=1
    main_bin_dec(p)
elif(t==1):
    #void main dec_bin
    p=int(input("\thow many times do you wish  to compute\t"));print("\t_________________________________________")
    def main_dec_bin(p):
        i=1
        while (i<=abs(p)):
            n1=int((input("\nenter the decimal number to be converted in base 2\n")))
            dec_bin(n1)
            i+=1
    main_dec_bin(p)