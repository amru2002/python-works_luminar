class Student:
    id:int
    name:str
    gender:str
    course:str
    
    def __init__(self,id,name,gender,course):
        self.id=id
        self.name=name
        self.gender=gender
        self.course=course
        
    def display_stu(self):
        print(self.id,self.name,self.gender,self.course)
    def __str__(self):
        return self.name
obj1=Student(101,"ammu","female","python")
obj1.display_stu()
print(obj1)

    