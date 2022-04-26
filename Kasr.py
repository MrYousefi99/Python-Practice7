class fractions :
    
    from fractions import Fraction
    
    def __init__(self , a , b , c , d):
        self.num1 = a
        self.num2 = b
        self.num3 = c
        self.num4 = d
    
    def add(self):
        first = fractions.Fraction(a,b)
        second = fractions.Fraction(c,d)
        sum = first + second
        
        print("sum is : ",sum)
    
    
    
    def sub(self):
        first = fractions.Fraction(a,b)
        second = fractions.Fraction(c,d)
        sub = first - second
        
        print("sub is : ",sub)
    
    
    
    def mul(self):
        first = fractions.Fraction(a,b)
        second = fractions.Fraction(c,d)
        mul = first * second
        
        print("mul is : ",mul)
    
    
    
    def div(self):
        first = fractions.Fraction(a,b)
        second = fractions.Fraction(c,d)
        div = first / second
        
        print("div is : ",div)
    
    
    
    def show(self):
        first = fractions.Fraction(a,b)
        second = fractions.Fraction(c,d)
        print("the first is : ",first)
        print("the second is : ",second)
    
    # def sim(self) :
    #     def gcd(x,y):
    #         if(x<y) :
    #             temp = x 
    #             x = y 
    #             y = temp
    #         while y != 0 :
    #             rim = x % y
    #             x = y
    #             y = rim
    #         r = x
            
    #         return r
        
    #     a1 = int(a / gcd(a,b))
    #     b1 = int(b / gcd(a,b))
    #     c1 = int(c / gcd(c,d))
    #     d1 = int(d / gcd(c,d))
    #     print(fractions.Fraction(a,b) , '==' , fractions.Fraction(a1,b1)) 
    #     print(fractions.Fraction(c,d) , '==' , fractions.Fraction(c1,d1))      
    


a = int(input("Please insert the first number of first fraction : "))
b = int(input("Please insert the second number of first fraction : "))
c = int(input("Please insert the first number of second fraction : "))
d = int(input("Please insert the second number of second fraction : "))


sum = fractions(a, b, c, d)

while True :
    inp = int(input("1-sum 2-sub 3-mul 4-div 5-show\n"))
    
    if inp == 1 :
        sum.add()
    elif inp == 2 :
        sum.sub()
    elif inp == 3 :
        sum.mul()
    elif inp == 4 :
        sum.div()
    elif inp == 5 :
        sum.show()                


# sum.sim()
