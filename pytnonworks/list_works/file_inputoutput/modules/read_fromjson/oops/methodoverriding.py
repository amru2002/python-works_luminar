class Bike:
    def start(self):
        print("kicker start")
    def breaking(self):
        print("drum break")
class Herohondasplender(Bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs break")
hobj=Herohondasplender()
hobj.start()
hobj.breaking()

