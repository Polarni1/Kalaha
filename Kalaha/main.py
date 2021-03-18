
import random
import numpy as np
import matplotlib.pyplot as plt
from user_interaction import *
from game_simulator import *


def Multiple_simulation(Starting_pieces, player_1_strategy,  player_2_strategy, \
    number_of_simulations):
    '''
    Skapar multipla simulationer och returnerar antalet vinster för respektive spelare.
    '''
        
    number_of_wins=[0,0]
        
    i=0
    while i < number_of_simulations:
        
        result=Kalaha.Play(Kalaha(Starting_pieces),player_1_strategy,  player_2_strategy)
        # Ovan: En omgång spelas.
        determined_result=Kalaha.Determine_winner(result) # Vinnare fastslås.
        number_of_wins[0]+=determined_result[0]
        number_of_wins[1]+=determined_result[1] 
            
        i+=1
            
    return(number_of_wins[0],number_of_wins[1])
        
def Plot(Starting_pieces, player_1_strategy,  player_2_strategy, number_of_simulations, all_results):
    '''
    Skapar ett diagram med två staplar. Staplarnas höjd visar antalet 
    vinster för respektive spelare.
    '''
        
    victories = plt.figure() # Skapar en figur.
        
    bars = ('Player 1 victories', 'Player 2 victories') # Namnger staplar.
    
    y_pos=np.arange(len(bars)) # Skapar antalet staplar, två i vårt fall.
    plt.bar(y_pos, all_results, color=['red', 'black']) # Ger staplarna höjd och färg.
    plt.xticks(y_pos, bars) # Tilldelar staplarna  dess namn. 
    plt.close(victories)
    end_message=(f'\n\nAntal vinster för spelare 1(strategi {player_1_strategy}): {all_results[0]}'
    f'\n\nAntal vinster för spelare 2(strategi {player_2_strategy}): {all_results[1]}\n\n'
    f'En figur som visar spelomgångarnas utfall är sparat i filen Kalaha_results.pdf.')
    print(end_message)
        
    victories.savefig("Kalaha_results.pdf", bbox_inches='tight')
    
def Start(Starting_pieces, player_1_strategy,  player_2_strategy, number_of_simulations):
    '''
    Startar merparten av programmet genom att kalla funktionen Multiple_simulation
    som är indirekt beroende av alla funktioner i programmet. 
    Kallar sedan funktionen Plot för skapa en figur som visar resultatet.
    '''
        
    all_results=Multiple_simulation(Starting_pieces, player_1_strategy,  player_2_strategy, \
    number_of_simulations) # Kör önskat antal spelomgångar.
        
    Plot(Starting_pieces, player_1_strategy,  player_2_strategy, \
                number_of_simulations, all_results) # Skapar ett diagram med slutresultat.
        
    

Finished_games=Start(Game_setup(), strategy_choice1(),strategy_choice2(),number_of_games())



