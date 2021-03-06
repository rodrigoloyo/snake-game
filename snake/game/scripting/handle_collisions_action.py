import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        score1 = cast.get_first_actor("scores1")
        
        food = cast.get_first_actor("foods")
        food_1 = cast.get_first_actor("foods1")
        snake = cast.get_first_actor("snakes")
        snake_1 = cast.get_first_actor("snakes1")
        head = snake.get_head()
        head_1 = snake_1.get_head()

        # if head.get_position().equals(food.get_position()) or head.get_position().equals(food_1.get_position()):

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            # points = food_1.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()
        # if head_1.get_position().equals(food_1.get_position()) or head_1.get_position().equals(food.get_position()) :

        if head_1.get_position().equals(food_1.get_position()):    
            # points1 = food_1.get_points()
            points1 = food.get_points()
            snake_1.grow_tail(points1)
            score1.add_points(points1)
            food_1.reset()
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        snake1 = cast.get_first_actor("snakes1")
        food = cast.get_first_actor("foods")
        food_1 = cast.get_first_actor("foods1")

        head1 = snake1.get_segments()[0]
        segments1 = snake1.get_segments()[1:]
        for segment1 in segments1:
            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    
                    self._is_game_over = True
                elif  head.get_position().equals(segment1.get_position()):    
                     self._is_game_over = True
            
                if head1.get_position().equals(segment1.get_position()):
                    
                    self._is_game_over = True
                elif  head1.get_position().equals(segment.get_position()):    
                      self._is_game_over = True
                elif  head1.get_position().equals(food.get_position()):    
                      self._is_game_over = True
                elif  head.get_position().equals(food_1.get_position()):    
                      self._is_game_over = True      


                     
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")
            food_1 = cast.get_first_actor("foods")
            snake1 = cast.get_first_actor("snakes1")
            segments_1 = snake1.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)

            for segment_1 in segments_1:
                segment_1.set_color(constants.WHITE)
            food_1.set_color(constants.WHITE)