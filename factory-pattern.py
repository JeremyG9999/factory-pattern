from abc import ABC, abstractmethod
class Sandwhich_Factory(ABC): #creator
    @abstractmethod
    def factory(self):
        pass
class Ham_Creator(Sandwhich_Factory): #concrete creators
    def factory(self):
        return Ham_Product()
class Turkey_Creator(Sandwhich_Factory): #concrete creators
    def factory(self):
        return Turkey_Product()
class Chicken_Creator(Sandwhich_Factory): #concrete creators
    def factory(self):
        return Chicken_Product()
class Sandwhich_Product(ABC): #product
    @abstractmethod
    def interface(self):
        pass
class Ham_Product(Sandwhich_Product): #concrete product
    def interface(self):
        print("You made a ham sandwhich")
class Turkey_Product(Sandwhich_Product): #concrete product
    def interface(self):
        print("You made a turkey sandwhich")
class Chicken_Product(Sandwhich_Product): #concrete product
    def interface(self):
        print("You made a chicken sandwhich")
class Sandwhich: #client
    def __init__(self):
        self.option = None
    def ham_sandwhich(self):
        return Ham_Creator().factory().interface()
    def turkey_sandwhich(self):
        return Turkey_Creator().factory().interface()
    def chicken_sandwhich(self):
        return Chicken_Creator().factory().interface()
def main():
    run = Sandwhich()
    run.ham_sandwhich()
    run.turkey_sandwhich()
    run.chicken_sandwhich()
main()