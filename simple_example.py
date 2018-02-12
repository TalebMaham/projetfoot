from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy

from strategies  import fonceurStrategy
from strategies  import defenseStrategy
## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",fonceurStrategy()) #Strategie qui ne fait rien
thon.add("ThonPlayer",defenseStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
