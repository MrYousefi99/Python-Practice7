class Time :
    def __init__(self,H,M,S) :
        self.H = H
        self.M = M
        self.S = S
    
    
    def add(self , B) :
        result = Time(0, 0, 0)
        result.H = self.H + B.H
        result.M = self.M + B.M
        result.S = self.S + B.S
        return result
    
    def sub(self,B) :
        result = Time(0, 0, 0)
        result.H = self.H - B.H
        result.M = self.M - B.M
        result.S = self.S - B.S
        return result
    
    def fix(self) :
        if self.S >= 60 :
            self.S -= 60 
            self.M += 1
        
        if self.M >= 60 :
            self.M -= 60 
            self.H += 1
        
        if self.H > 24 :
            self.H -= 24
            print("One day has passed")
    
    def fix2(self) :
        if self.S < 0 :
            self.M - 1 
            self.S += 60
        
        if self.M < 0 :
            self.H -1 
            self.M += 60
        
        if self.H < 24 :
            print("We do not have a negative clock. I will make the result of the clock positive")
            self.H += 24

            
        
    def show(self) :
        print(self.H,":",self.M,":",self.S)
        

print("Time 1 : a1 : b1 : c1 ")
print("Time 2 : a2 : b2 : c2 ")
print()
a1 = int(input("Please input a1 : "))
b1 = int(input("Please input b1 : "))
c1 = int(input("Please input c1 : "))
a2 = int(input("Please input a2 : "))
b2 = int(input("Please input b2 : "))
c2 = int(input("Please input c2 : "))
print()
t1 = Time(a1, b1, c1)
t2 = Time(a2 , b2 , c2)

print("1 - Sum : ")
print("2 - Sub : ")
print()
n = int(input("Please Input the section number : "))
print()
if n == 1 :
    output  = t1.add(t2)    
    output.fix()
    output.show() 
elif n == 2 :
    output1 = t1.sub(t2)
    output1.fix2()
    output1.show() 

    