class Book:
    id:int
    name:str
    price:int
    author:str
    publisher:str
    def create(self,id,name,price,author,publisher):
        self.id=id
        self.name=name
        self.price=price
        self.author=author
        self.publisher=publisher
    def display_book(self):
        print(self.id,self.name,self.price,self.author,self.publisher)
obj=Book()
obj.create(101,"the life of stars",165,"mahadevi","ramkumar")
obj.display_book()