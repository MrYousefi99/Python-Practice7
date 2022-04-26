
class complex1 :
    def __init__(self,a,b,c,d ) :
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def sum(self):
        s1 = (a+c) 
        s2 = (b+d)
        s3 =abs(s2)
        
        if s2 <= 0 :
            print(s1,"-",s3,"i")
        elif s2>0:
            print(s1,"+",s3,"i")    
    
    def sub(self):
        t1 = (a-c)
        t2 =(b-d)
        t3 = abs(t2)
        
        
        if t2 <= 0 :
                print(t1,"-",t3,"i")
        elif t2>0:
            print(t1,"+",t3,"i")  

    
    def mul(self):
        a1 = (a*c - b*d)
        a2 =  (a*d + b*c)
        a3 = abs(a2)
        
        
        if a2 <= 0 :
                print(a1,"-",a3,"i")
        elif a2>0:
            print(a1,"+",a3,"i") 




print("------  a + bi ------")
print("------  c + di ------")
print()
a =int(input("Please input number a :"))
b = int(input("Please input number b :"))
c = int(input("Please input number c :"))
d = int(input("Please input number d :"))
print()

print(" 1 - sum")
print(" 2 - sub")
print(" 3 - mul")
print()
n =int(input("Please enter the section number : "))
print()
mycp = complex1(a, b, c, d)

if n == 1 :
    mycp.sum()
elif n == 2 :
    mycp.sub() 
elif n == 3 :
    mycp.mul()     






