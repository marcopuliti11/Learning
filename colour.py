class Colour():
    r = 0
    g = 0
    b = 0
    
    def __init__(self,r=None,g=None,b=None):
        if r is None:
            self.r = 0
        else:
            self.r = r
        if g is None:
            self.g = 0 
        else:
            self.g = g      
        if b is None:
            self.b = 0 
        else:
            self.b = b
            
    def show(self):
        print("RGB value", self.r, self.g, self.b)
    
    def __add__(self,other): # both __add__ and toher are python reserved words to specify a polymorphism. for subtratcting the keyword is sub
        self.r += other.r
        self.g += other.g
        self.b += other.b
        return Colour(self.r,self.g, self.b) # this returns the newly create object with the sum
          
c1 = Colour(255,0,0)
c1.show()       

c2 = Colour(0,255,0)
c2.show()

c3 = c1 + c2
c3.show()