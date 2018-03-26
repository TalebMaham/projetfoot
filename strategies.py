import math 
from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator   import settings
from outils  import chkat
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
        player2=state.player_state(2,0).position
        ball=state.ball.position 
        if id_team == 1:
            goal = Vector2D(0,settings.GAME_HEIGHT/2)
            mygoal=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            mygoal=Vector2D(0,settings.GAME_HEIGHT/2)
        if player.distance(ball) < settings.PLAYER_RADIUS+settings.BALL_RADIUS:
           
            return SoccerAction(shoot=(player2-player))#il passe vers goal
            
        if player.distance(ball)<23*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
            return SoccerAction(acceleration=ball-player)
        if player.distance(ball)>38*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
            return SoccerAction(acceleration=goal-player)
        else:
            return SoccerAction(acceleration=mygoal-player)






# une strategy du deffenseur special 
## Strategie Defenseur
class defensespeStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"deffenseur")
    def compute_strategy(self,state, id_team, id_player):
        player=state.player_state(id_team,id_player).position
        player2=state.player_state(2,0).position
        ball=state.ball.position 
        if id_team == 1:
            goal = Vector2D(0,settings.GAME_HEIGHT/2)
            mygoal=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            mygoal=Vector2D(0,settings.GAME_HEIGHT/2)
        if player.distance(ball) < settings.PLAYER_RADIUS+settings.BALL_RADIUS:
           
            return SoccerAction(shoot=(player2-player))#il passe vers son collegue 
            
        if player.distance(ball)<15*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
            return SoccerAction(acceleration=ball-player)
        if mygoal.distance(ball)>50*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
            return SoccerAction(acceleration=goal-player)
            
        else:
            return SoccerAction(acceleration=mygoal-player)



























              
  #strategie deplacement vers le milieu dans une condition 

class strmilStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"strrmil")
    def compute_strategy(self,state, id_team, id_player):
        player=state.player_state(id_team,id_player).position
        player1=state.player_state(2,0).position 
        playervs=state.player_state(1,0).position
        ball=state.ball.position 
        if id_team == 2:
            goal = Vector2D(0,settings.GAME_HEIGHT/2)                         #ici j'ai defini mon goal
            mygoal=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)       
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            mygoal=Vector2D(0,settings.GAME_HEIGHT/2)
        if  player.distance(ball) <settings.PLAYER_RADIUS+settings.BALL_RADIUS: #si le ball est suffisement proche 

             if  player.distance(playervs)<6*(settings.PLAYER_RADIUS+settings.BALL_RADIUS): #attention l'adversaire peut etre proche s'il est vraiment proche 
               
                   return SoccerAction(shoot=(goal-player)) #passe le ballon à son colegue
             else:
                   return SoccerAction(shoot=(goal-player)/60) #s'il nest pas proche il tire vers le goal
        
        if player.distance(ball)<27*(settings.PLAYER_RADIUS+settings.BALL_RADIUS): #in ne bouge que si une distance de la ball est realise
            return SoccerAction(acceleration=ball-player) # il attaque le ball
        
        if player.distance(playervs)>30*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
           return SoccerAction(acceleration=goal-player)
        else:  
           return SoccerAction(acceleration=Vector2D(0,0)) # initialement le joueur ne bouge pas comme on a deja dit



 #hon lahi n3adlou 7ne une strategie

 
   



class dribleStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"drible")
    def compute_strategy(self,state, id_team, id_player):
        player=state.player_state(id_team,id_player).position
        player1=state.player_state(2,1).position 
        playervs=state.player_state(1,1).position
        playervs=state.player_state(1,0).position
        ball=state.ball.position 
        if id_team == 2:
            goal = Vector2D(0,settings.GAME_HEIGHT/2)                         #ici j'ai defini mon goal
            mygoal=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)       
        else:
            goal = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            mygoal=Vector2D(0,settings.GAME_HEIGHT/2)
        if  player.distance(ball) <settings.PLAYER_RADIUS+settings.BALL_RADIUS: #si le ball est suffisement proche 

             if  player.distance(playervs)<11*(settings.PLAYER_RADIUS+settings.BALL_RADIUS): #attention l'adversaire peut etre proche s'il est vraiment proche 
               if player.distance(goal)<10*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
                          return SoccerAction(shoot=(goal-player))
               else:
                   return  chkat()  #i7awl yecka6 
             else:
                   return SoccerAction(shoot=((goal-player)/70)) #l' adversaire mezal b3id donc le joueur yedribli chwei
        
        if player1.distance(ball)<25*(settings.PLAYER_RADIUS+settings.BALL_RADIUS): #in ne bouge que si une distance de la ball est realise
            return SoccerAction(acceleration=ball-player) # il attaque le ball
        
        if player.distance(playervs)<40*(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
           return SoccerAction(acceleration=goal-player)
        else:  
           return SoccerAction(acceleration=Vector2D(0,0)) # initialement le joueur ne bouge pas comme on a deja dit










     
     
                   

