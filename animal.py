class Animal():
    __eyes = 2 #used to create an internal variable, not accessible
    
    def show(self):
        """"Shows number eyes""" #this comments are showned when you call the fcn in another script, helps you self document the code
        print("The number of eyes: ")
        print(self.__eyes)

    def __secret(self): #hidden class, whenever it starts with __
        print("secret")

    @property # make something visible outside of the class
    def eyes(self): #get the internal eyes value
        """" Gets the number of eyes """
        self.__secret() # without this line, the function secret is hidden
        return self.__eyes
    
    @eyes.setter #decorator for the setter
    def eyes(self, eyes): #set whatever value we assign to eyes and put it into the internal variable
        """" Sets the number of eyes """
        if eyes <= 3:
            self.__eyes = eyes
        else:
            self.__eyes = 2
        