from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy

from strategies  import fonceurStrategy
from strategies  import defenseStrategy
from strategies  import  strmilStrategy
from strategies  import dribleStrategy
from strategies  import defensespeStrategy

#from strategies  import strmilStrategy
## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer1",fonceurStrategy()) #on a une nouvele strategie 
pyteam.add("PyPlayer2",defenseStrategy())
thon.add("ThonPlayer1",strmilStrategy())   #Strategie aleatoire
thon.add("ThonPlayer2", defenseStrategy())

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
