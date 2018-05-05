from soccersimulator import SoccerTeam, Simulation, show_simu
from profAI import FonceurStrategy,DefenseurStrategy,SmartStrategy,get_team


## Creation d'une equipe
pyteam = get_team(2)
thon = SoccerTeam(name="ThonTeam")
thon.add("PyPlayer",SmartStrategy()) #Strategie qui ne fait rien
thon.add("ThonPlayer",DefenseurStrategy())   #Strategie aleatoire
#thon.add("troisPlayer",DefenseurStrategy())
#thon.add("quatPlayer",FonceurStrategy())
#Creation d'une partie
simu = Simulation(pyteam,thon) # simu declaré mais Simulation est un class appelé
#Jouer et afficher la partie
show_simu(simu)  # appelé
