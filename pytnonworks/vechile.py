class Parent:
    vechiles=["passion pro,swift"]
    def properties(self):
        return self.vechiles
class Child(Parent):
    def properties(self):
        self.vech=super().properties()
        self.vech.append("hunder")
        return self.vech
ch=Child()
print(ch.properties())