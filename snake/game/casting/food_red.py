import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.food import Food


class Food1(Food):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
       
        self.set_color(constants.RED)
      
      
 