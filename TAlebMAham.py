from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
#creation du joueur 
class StrategiepourUN(Strategy):
    def __init__(self):
        super(StrategiepourUN,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position+1)*100 #j'ai remarque que cette condition de tir est la bonne pour le cas d'une balle 
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
            return SoccerAction(shoot=shoot)
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=0.5
        return SoccerAction(acceleration=acc)


class StrategiepourDEUX(Strategy):
    def __init__(self):
        super(StrategiepourDEUX,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[1]#en tiran directement vers la deuxieme ball on marque le premier but 
        shoot = (oth.position-ball.position)*100
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
            return SoccerAction(shoot=shoot)

        
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=0.5
        return SoccerAction(acceleration=acc)



class StrategiepourTROIS(Strategy):
    def __init__(self):
        super(StrategiepourTROIS,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position+2)*50
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
            return SoccerAction(shoot=shoot)
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=0.5
        return SoccerAction(acceleration=acc)

myt = SoccerTeam("premierjoueur")
myt.add("M",StrategiepourUN())
#myt = SoccerTeam("premierjoueur")
#myt.add("M",StrategiepourUN())
#myt = SoccerTeam("deuxiemejoueur")
#myt.add("P",StrategiepourDEUX())
#myt = SoccerTeam("troisiemejoueur")
#myt.add("R",StrategiepourTROIS())


b = Billard(myt,type_game=0)

show_simu(b)

