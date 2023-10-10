class Cloth:
    dress=[
        {"brand":"nike","name":"skirt","price":550,"fabric":"chiffon"},
        {"brand":"prada","name":"jacket","price":659,"fabric":"velvet"},
        {"brand":"adidas","name":"tshirt","price":450,"fabric":"cotton"},
        {"brand":"burberry","name":"churidhar","price":1000,"fabric":"silk"},
        {"brand":"gucci","name":"saree","price":950,"fabric":"linen"},
        {"brand":"armani","name":"jeans","price":850,"fabric":"satin"},
        
    ]
# all clothes
    def get(self,*args,**kwargs):
        return self.dress
# take one clothe
    def retrieve(self,*args,**kwargs):
        brand=kwargs.get("brand")
        reco=[c for c in self.dress if c.get("brand")==brand]
        return reco
# add 
    def create(self,*args,**kwargs):
       self.dress.append(kwargs)  
# delete 
    def destroy(self,*args,**kwargs):
        brand=kwargs.get("brand")
        obj=[c for c in self.dress if c.get("brand")==brand][0]
        self.dress.remove(obj)
    
obj=Cloth()
# print(obj.get())
# print(obj.retrieve(brand="nike"))
# obj.create(brand="balos",name="frok",price=580,fabric="wool")
# print(obj.get())
obj.destroy(brand="nike")
print(obj.get())