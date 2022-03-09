import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.snake import Snake
class Snake1(Snake):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.
    Attributes:
        _points (int): The number of points the food is worth.
    # """
    def set_body_color(self):
        return constants.RED
    
    def set_coors(self):
        return [4, 4]