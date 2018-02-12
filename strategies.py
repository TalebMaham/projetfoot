import math 
from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator   import settings
## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())

## Strategie fonceur 
class fonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"fonceur")
    def compute_strategy(self,state, id_team, id_player):
        player = state.player_state(id_team, id_player).position  
        ball = state.ball.position
        if id_team == 2:
            goal = Vector2D(0,settings.GAME_HEIGHT/2)
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
        if player.distance(ball) < settings.PLAYER_RADIUS+settings.BALL_RADIUS:
            return SoccerAction(shoot=goal-player)
        else:
            return SoccerAction(acceleration=ball-player)

## Strategie Defenseur
class defenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"deffenseur")
    def compute_strategy(self,state, id_team, id_player):
        player=state.player_state(id_team,id_player).position
        ball=state.ball.position 
        if id_team == 2:
            goal = Vector2D(0,settings.GAME_HEIGHT/2)
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            
        if player.distance(ball) < settings.PLAYER_RADIUS+settings.BALL_RADIUS:
            return SoccerAction(shoot=goal-player)
        else:
            return SoccerAction(acceleration=ball-player)
              
        
                   

