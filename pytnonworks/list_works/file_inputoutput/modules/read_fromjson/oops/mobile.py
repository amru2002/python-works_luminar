class Mobile:
    brand:str
    model:str
    price:int
    color:str
    def create(self,brand,model,price,color):
        self.brand=brand
        self.model=model
        self.price=price
        self.color=color
    def display_mob(self):
        print(self.name,self.model,self.price,self.color)
        
        
