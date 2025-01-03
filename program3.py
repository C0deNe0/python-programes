# Design and implement a complex object like a House using a step-by-step Builder pattern, allowing different representations of the house (wooden, brick, etc.). 

#abstract product classes
class house:
    def __init__(self,material):
        self.address = None
        self.material = material
        self.size = None
        self.numbebrooms = None
        self.numbathrooms = None
    
    def __str__(self):
        return (f"House at {self.address}, size: {self.size} sqft, "
                f"material: {self.material}, bedrooms: {self.numbebrooms}, "
                f"bathrooms: {self.numbathrooms}")
                

##builder class
class houseBuilder:
    def __init__(self,material):
        if material == "wood":
            self.house = house("wood")
        elif material == "brick":
            self.house = house("brick")
        else:
            raise ValueError("invalid house type")
    
    def set_address(self,address):
        self.house.address = address
    
  
  
    def set_size(self, size):
        self.house.size = size

    def set_num_bedrooms(self, num_bedrooms):
        self.house.numbedrooms = num_bedrooms

    def set_num_bathrooms(self, num_bathrooms):
        self.house.numbathrooms = num_bathrooms
        
    def gethouse(self):
        return self.house
        
        
#=================================================================#
#CLIENT CODE
def createHouse(material,address,size, numbedrooms,numbathrooms):
    b = houseBuilder(material)
    b.set_address(address)
    b.set_size(size)
    b.set_num_bedrooms(numbedrooms)
    b.set_num_bathrooms(numbathrooms)
    return b.gethouse()
    
    

if __name__ == "__main__":
     wooden_house = createHouse("wood","123 street", 2000, 3, 2)
     print(wooden_house)
    

