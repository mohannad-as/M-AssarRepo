class Laptop :
    def __init__(self,color='',model=0,Type=''):
        self._color= color
        self._model= model
        self._Type=  Type
    def setcolor(self, color):
      self._color = color
    def setmodel(self, model):
      self._model = model
    def setcompany(self, Type):
      self._Type = Type
    def getcolor(self):
      return self._color
    def getmodel(self):
      return self._model
    def getType(self):
      return self._Type    
    def __str__(self):
        return " color:"+self._color+\
           "model:" + str(self._model)+\
           "type:" + self.Type

class Asus(Laptop):
    def __init__(self,color='',model=0,Type='',Price=0):
     super().__init__(color,model,Type)
     self._Price = Price

    def Brand(self):
        print("The Brand of this Laptop is : Asus " )

class Hp (Laptop) :
    def __init__(self,color='',model=0,Type='',price=0,feature=''):
     super().__init__(color,model,Type)
     self._Type= Type
     self._feature= feature
    
    def Brand(self):
        print("The Brand of this Laptop is : Hp " )
