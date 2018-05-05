from soccersimulator import Vector2D, SoccerAction
from soccersimulator.settings import GAME_GOAL_HEIGHT,GAME_HEIGHT, GAME_WIDTH,BALL_RADIUS,PLAYER_RADIUS

def get_random_vec():
    return Vector2D.create_random(-1,1)

def get_random_SoccerAction():
    return SoccerAction(get_random_vec(),get_random_vec())

class ProxyObj(object):
    def __init__(self,state):
        self._obj = state
    def __getattr__(self,attr):
        return getattr(self._obj,attr)

class SuperState(ProxyObj):
    def __init__(self,state,idt,idp):
        super(SuperState,self).__init__(state)
        self.key = (idt,idp)
    @property
    def my_team(self):
        return self.key[0]
    @property
    def his_team(self):
        return (2 -self.key[0])+1
    @property
    def me(self):
        return self.player_state(*self.key).position
    
    @property
    def mon_ami(self):
        return self.player_state(0,1).posion 
       
    @property
    def my_goal(self):
        return Vector2D((self.my_team-1)*self.width,self.goal_center)
    @property
    def his_goal(self):
        return Vector2D((self.his_team-1)*self.width,self.goal_center)
    @property
    def ball_p(self):
        return self.ball.position
    @property
    def can_kick(self):
        return self.distance(self.ball_p)<(PLAYER_RADIUS+BALL_RADIUS)#donc si je peut faire le shoot 
    @property
    def width(self):
        return GAME_WIDTH  #largeur de du terrain 
    @property
    def height(self):  #hauteur du terrain 
        return GAME_HEIGHT
    @property
    def goal_center(self):
        return self.goal_radius+self.height/2.
    @property
    def goal_radius(self):
        return GAME_GOAL_HEIGHT/2.
    def distance(self,p):# la distance de quelque chose p de moi 
        return self.me.distance(p)

class Comportement(ProxyObj):
    def __init__(self,obj):
        super(Comportement,self).__init__(obj)
    def run(self,p):
        raise(NotImplementedError)
    def go(self,p):
        raise(NotImplementedError)
    def shoot(self):
        raise(NotImplementedError)
    def degage(self):
        raise(NotImplementedError)
