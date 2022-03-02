from game.scripting.action import Action



class MoveActorsAction(Action):
        
    # TODO: Implement MoveActorsAction class here! 

    # Override the execute(cast, script) method as follows:
    # 1) get all the actors from the cast
    # def MoveActorsAction():
    #     all_actor = get_actors()
    # 2) loop through the actors
    # 3) call the move_next() method on each actor
    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        # snake = cast.get_first_actor("snakes")
        all_actors = cast.get_all_actors()
        all_actors1 = cast.get_all_actors()
        # for _ in range (1, 100):
        #     snake.move_next() 

    
        for  snake in (all_actors):
              snake.move_next()
      
                
    