from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        score1 = cast.get_first_actor("scores1")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")        
        segments = snake.get_segments()
        snake_1 = cast.get_first_actor("snakes1")
        segments_1 = snake_1.get_segments()
        food_1 = cast.get_first_actor("foods1")
        messages = cast.get_actors("messages")
        

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actor(food_1)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments_1)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()