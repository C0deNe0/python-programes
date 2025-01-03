
#Design and implement ShapeFactory class that generates different types of Shape objects (Circle, Square, Rectangle) based on input parameters using Factory Design Pattern.
from abc import ABC,abstractmethod
class shape(ABC):
  @abstractmethod
  def draw(self):
    pass

#concrete shapes
class circle(shape):
  def __init__(self,radius):
    self.radius = radius
  def draw(self):
     return f"drawing a circle with radius {self.radius}"

class square(shape):
  def __init__(self,side):
    self.side = side
  def draw(self):
    return f"drawing a square with side {self.side}"

#shapefactory class
class shapeFactory:
  @staticmethod
  def create_shape(shapetype,*args):
    if shapetype =="circle":
      return circle(*args)
    elif shapetype == "square":
      return square(*args)
    else:
      raise valueError(f"unknown shape type:{shapetype}")



#usage
if __name__== "__main__":
      fact = shapeFactory()

      circle1 = fact.create_shape("circle",5)
      print(circle1.draw())
      square1 = fact.create_shape("square",4)
      print(square1.draw())














      














      
