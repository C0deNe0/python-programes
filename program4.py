# Design and Implement to Extend a Coffee object with dynamic features (e.g., milk, sugar, whipped cream) using Decorators.

from abc import ABC, abstractmethod

# Base Coffee class
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Abstract Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Coffee class
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base price of coffee

    def description(self):
        return "Simple Coffee"

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3

    def description(self):
        return self._coffee.description() + ", Whipped Cream"

# Example usage
if __name__ == "__main__":
    # Start with a simple coffee
    coffee = SimpleCoffee()
    print(f"Description: {coffee.description()}")
    print(f"Cost: ${coffee.cost()}")

    # Add milk
    coffee = MilkDecorator(coffee)
    print(f"Description: {coffee.description()}")
    print(f"Cost: ${coffee.cost()}")

    # Add sugar
    coffee = SugarDecorator(coffee)
    print(f"Description: {coffee.description()}")
    print(f"Cost: ${coffee.cost()}")

    # Add whipped cream
    coffee = WhippedCreamDecorator(coffee)
    print(f"Description: {coffee.description()}")
    print(f"Cost: ${coffee.cost()}")
