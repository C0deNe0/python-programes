# Design and Implement an AbstractFactory class to create families of related or
# dependent objects with respect to decathlon store without specifying their concrete classes using Abstract Factory.

from abc import ABC,abstractmethod

#abstract product classes
class sportsEquipment(ABC):
    @abstractmethod
    def getname(self):
        pass
    @abstractmethod
    def getprice(self):
        pass
    
class apparel(ABC):
    @abstractmethod
    def getname(self):
        pass
    @abstractmethod
    def getprice(self):
        pass
    
    
#concrete product classes for running
class runningShoes(sportsEquipment):
    def getname(self):
        return "neo running shoes"
    def getprice(self):
        return 50
        
class runningTshirt(apparel):
    def getname(self):
        return "neo running tshirt"
    def getprice(self):
        return 50
  
 #concrete  product classes for cycling  
class cyclingShoes(sportsEquipment):
    def getname(self):
        return "neo cycling shoes"
    def getprice(self):
        return 50
        
class cyclingTshirt(apparel):
    def getname(self):
        return "neo cycling tshirt"
    def getprice(self):
        return 50
    


#abstrct factory class
class neoFactory(ABC):
    @abstractmethod
    def create_sportsEquipment(self):
        pass
    @abstractmethod
    def create_apparel(self):
        pass


#concrete factory classes
class runningFact(neoFactory):
    def create_sportsEquipment(self):
        return runningShoes()
    
    def create_apparel(self):
        return runningTshirt()
        

class cyclingFact(neoFactory):
    def create_sportsEquipment(self):
        return cyclingShoes()
    
    def create_apparel(self):
        return cyclingTshirt()


#================================================================#
#CLIENT CODE

def create_neo_products(ftr : neoFactory):
    eq = ftr.create_sportsEquipment()
    ap = ftr.create_apparel()
    
    print(f"     equipmeth: {eq.getname()},cost:{eq.getprice()}")
    print(f"      apparel: {ap.getname()},cost:{ap.getprice()}")


if __name__== "__main__":
    runfact = runningFact()
    cycfact = cyclingFact()
    
    print("Running products;")
    create_neo_products(runfact)
    print("cycling products:")
    create_neo_products(cycfact)






      
