from .tools import SuperState, Comportement, ProxyObj
from soccersimulator import Vector2D,SoccerAction
from soccersimulator.settings import maxPlayerShoot, maxPlayerSpeed,maxPlayerAcceleration

class ComportementNaif(Comportement):
    RUN_COEF = maxPlayerAcceleration
    GO_COEF = maxPlayerAcceleration/3.
    DOUC_COEF=maxPlayerAcceleration/9.
    SHOOT_COEF = maxPlayerShoot/3.
    THROW_COEF = maxPlayerShoot
    def __init__(self,state):
        super(ComportementNaif,self).__init__(state)
    def run(self,p):# aller vers quelque chose p donne avec max acceleration 

        return SoccerAction(acceleration=(p-self.me).normalize()*self.RUN_COEF)
    def go(self,p):#aller vers quelque chose à definir 
        return SoccerAction(acceleration=(p-self.me).normalize()*self.GO_COEF)
    def douc(self,p):#verision douc du go 
        return SoccerAction(acceleration=(p-self.me).normalize()*self.DOUC_COEF)
    def shoot(self,shoot_coef=None):# tirer le ballon 
        if shoot_coef is None: # donc le coiefficien du shoot doit etre non null 
            shoot_coef = self.SHOOT_COEF
        if self.can_kick: #et je doit avoir le pouvoir du shoot 
            return SoccerAction(shoot=(self.his_goal-self.ball_p).normalize()*self.SHOOT_COEF)#ici on shoot en definisant le sens et la force du shoot 
        return SoccerAction()
    def degage(self):
        if self.can_kick:#pour aussi faire un degage il faut d'abord qu'on puis shoot
            return SoccerAction(shoot=(self.his_goal-self.ball_p).normalize()*self.THROW_COEF)#ici on fait un autre shoot la difference c'est les coifficients 
        return SoccerAction()
  
class ComportementInteligent(Comportement):
    RUN_COEF = maxPlayerAcceleration
    GO_COEF = maxPlayerAcceleration/3.
    DOUC_COEF=maxPlayerAcceleration/9.
    SHOOT_COEF = maxPlayerShoot/3.
    THROW_COEF = maxPlayerShoot
    def __init__(self,state):
        super(ComportementInteligent,self).__init__(state)
    def run(self,p):
        return SoccerAction(acceleration=(p-self.me).normalize()*self.RUN_COEF)
    def go(self,p):
        return SoccerAction(acceleration=(p-self.me).normalize()*self.GO_COEF)
    def douc(self,p):
        return SoccerAction(acceleration=(p-self.me).normalize()*self.DOUC_COEF)
    def shoot(self,shoot_coef=None):
        if shoot_coef is None:
            shoot_coef = self.SHOOT_COEF
        if self.can_kick:
            return SoccerAction(shoot=(self.his_goal-self.ball_p).normalize()*self.SHOOT_COEF)

        return SoccerAction()
# ici je doit mettre le coeure de mon strategie c'est à dir l'astice qui va definir la difference 
    def passe(self):
        if self.can_kick:
             return SoccerAction(shoot=(self.mon_ami-self.ball_p).normalize()*self.THROW_COEF)
    def degage(self):
        if self.can_kick:
            return SoccerAction(shoot=(self.his_goal-self.ball_p).normalize()*self.THROW_COEF)
        return SoccerAction()
  
    
class ConditionDefenseur(ProxyObj):# ici on definit une condition mais on ne fait rien seulement definir une condition 
    COEF_DEF =0.5
    COEF_SDEF=0.5
    def __init__(self,state):
        super(ConditionDefenseur,self).__init__(state)
    def is_defense(self):
       	return self.ball_p.distance(self.my_goal)<self.COEF_DEF*self.width
    def spe_def(self):
     return self.me.distance(self.ball_p)>self.COEF_SDEF*self.width		


class ConditionAttaque(ProxyObj):
    COEF_SHOOT = 1
    COEF_BALL = 0.1
    def __init__(self,state):
        super(ConditionAttaque,self).__init__(state)
    def close_goal(self):
        return self.me.distance(self.his_goal)<self.COEF_SHOOT*self.width
    def close_ball(self):
        return self.me.distance(self.ball_p)<self.COEF_BALL*self.width
class ConditionSecret(ProxyObj):
    COEF_SHOOT = 1
    COEF_BALL = 0.1
    def __init__(self,state):
        super(ConditionSecret,self).__init__(state)
    def close_goal(self):
        return self.me.distance(self.his_goal)<self.COEF_SHOOT*self.width
    def close_ball(self):
        return self.me.distance(self.ball_p)<self.COEF_BALL*self.width
   

class ConditionSmart(ProxyObj):
    COEF_SHOOT = 1
    COEF_BALL = 0.1
    def __init__(self,state):
        super(ConditionSmart,self).__init__(state)
    def close_goal(self):
        return self.me.distance(self.his_goal)<self.COEF_SHOOT*self.width
    def close_ball(self):
        return self.me.distance(self.ball_p)<self.COEF_BALL*self.width


#une autre fois le problem de smart


    
def smart(I):
    if not I.can_kick:
        if I.close_ball():
           return I.run(I.ball_p)
        else:
            return I.go(I.my_goal)
    else:
        if I.close_goal():
            return I.passe()
    return I.degage()

def secret(I):
     if not I.can_kick:
        if I.close_ball():
           return I.run(I.ball_p)
        else:
            return I.go(I.my_goal)
     else:
        if I.close_goal():
            return I.shoot()
     return I.degage()






    
def fonceur(I):
    if not I.can_kick:
        if I.close_ball():
           return I.run(I.ball_p)
        else:
            return I.douc(I.ball_p)
    else:
        if I.close_goal():
            return I.shoot()
    return I.degage()

def defenseur(I):
    if I.is_defense():
      return I.degage()+I.run(I.ball_p)
    if I.spe_def():
        return I.run(I.his_goal)
	
    
    return I.go((I.me-I.his_goal).normalize()*I.width*0.1+I.my_goal)
