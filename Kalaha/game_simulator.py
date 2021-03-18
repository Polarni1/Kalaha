
import random
import numpy as np
import matplotlib.pyplot as plt
from user_interaction import *

class Kalaha:
    '''
    Klassens enda objekt är Game_board, en lista som representerar spelbrädet.
    Metoderna i klassen utför de olika moment som en speltur innehåller,
    tillsammans med metoden play skapar de sedan en hel spelrunda.
    '''
    def __init__(self, s):
        '''
        Skapar en lista som kommer att representera spelbrädet. 
        Spelbrädet får s kulor i varje skål(bortsett ifrån bon).
        '''
        self.Game_board = [s,s,s,s,s,s,0,s,s,s,s,s,s,0]
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
    def Pick(self, pit):
        '''
        Utför en spelrunda där skålen pit är vald och ändrar listans värden i enlighet därmed.
        '''
        n=1
        pieces_in_hand= self.Game_board[pit] # Plockar upp alla kulor ifrån vald skål.
        self.Game_board[pit]=0 # Ser till att vald skål töms.
        
        while pieces_in_hand>=1: # Loop medans vi forfarande har kulor kvar i handen att placera ut.
            if 0<=pit<=5 and (pit+n)%14==13: # Om skål 1-6 är vald vet vi att det är spelare 1 som 
                # spelar. Denna måste undvika att lägga kulor i spelare 2s bo. %14 försäkrar att detta
                # gäller för alla varv runt brädet som kulorna räcker
                pass
            elif 7<=pit<=12 and (pit+n)%14==6: # Vice versa för spelare 2. 
                pass
            else:
                pieces_in_hand+=-1 # Vid en skål där en kula ska placeras tar vi en kula ifrån handen.
                self.Game_board[(pit+n)%14]+=1 # Och lägger i skålen. 
                
            n+=1
            
    def Extra_turn_conditions(self, player, Home_pit, Pit_after_home):
        '''
        Kontrollerar om en spelare har uppfyllt villkoren för att få göra ett
        extra drag efter ett avslutat drag, och returnerar booleska värden därefter.
        
        Input:
        player - aktiv spelare(1 eller 2)
        Home_pit - Antalet kulor i spelarens bo innan draget gjorts.
        Pit_after_home - Antalet kulor i skålen direkt efter spelarens hem innan draget gjorts.
        '''
        if player ==1: # Vem som är aktiv spelare avgör vilken sida av brädet vi kontrollerar. 
            # Detta är endast för att låta resterande kod i metoden gälla bägge fallen,
            # och därmed undivka upprepningar.
            side=0 
        elif player ==2: 
            side=7
        
        if ((self.Game_board[6+side]-Home_pit)-(self.Game_board[7-side]-Pit_after_home))>0:
            # Den första parentesen ovan ger differensen mellan antalet kulor i hemmet före och efter draget.
            # Den andra parentesen ger differensen mellan antalet kulor i skålen efter hemmet före och efter draget.
            # Om differensen mellan dessa två parentesen i sin tur är positiv måste sista kulan lagts i hemmet.
            Extra_turn = True
        else:
            Extra_turn = False
        
        return Extra_turn
        
    def Collect_all_pieces(self, player):
        '''
        Tömmer alla skålar som inte är bon och lägger dessa kulor i players bo.
        '''
        if player == 1:
            side=0
        elif player == 2:
            side=7
        
        Remaining_peieces=self.Game_board[0]+self.Game_board[1]+self.Game_board[2] \
        + self.Game_board[3]+self.Game_board[4]+self.Game_board[5]+  \
        + self.Game_board[7]+self.Game_board[8]+self.Game_board[9]+ \
        self.Game_board[10]+self.Game_board[11]+self.Game_board[12] 
        # Ovan fås summan av alla kvarvarande kulor som inte ligger i bon.
            
        self.Game_board[6+side]+=Remaining_peieces # Denna summa adderas till players bo.
            
        self.Game_board[0]=self.Game_board[1]=self.Game_board[2] \
        =self.Game_board[3]=self.Game_board[4]=self.Game_board[5]  \
        =self.Game_board[7]=self.Game_board[8]=self.Game_board[9]= \
        self.Game_board[10]=self.Game_board[11]=self.Game_board[12]=0
        # Alla skålar som inte är bon töms.
        
    def Game_end_conditions(self, player):
        '''
        Kontrollerar om villkoren för spelets slut är uppfyllda. 
        Om så är fallet läggs kvarvarande kulor i players bo
        och spelet avslutas.
        '''
        if player == 1:
            side=0
        elif player == 2:
            side=7
        
        if self.Game_board[0+side]==self.Game_board[1+side]==self.Game_board[2+side] \
        ==self.Game_board[3+side]==self.Game_board[4+side]==self.Game_board[5+side]==0 :
        # Kontrollerar om alla players spelbara skålar är tomma. 
         
            Game_end_conditions=True
            self.Collect_all_pieces(player) # Är så fallet läggs kvarvarande kulor i players bo.
        else:
            Game_end_conditions=False
            
        return(Game_end_conditions)
    
    def Uniform_random_pick(self, player, options, side):
        '''
        Genomför ett slumpmässigt likformigt fördelat val mellan icke-tomma skålar för player.
        Returnerar index för denna skål.
        
        Övrig input:
        options - Spelbara skålar för player.
        side - Den sida av brädet som player sitter vid, detta ges av 0 eller 7. 
        '''
        # Ovan: Genom att ärva side ifrån metoden strategy slipper vi bestämma den igen.
        
        valid_pick=0
        pick=0
        
        while valid_pick==0 and self.Game_board[0+side]+self.Game_board[1+side]+self.Game_board[2+side] \
            +self.Game_board[3+side]+self.Game_board[4+side]+self.Game_board[5+side]!=0:
                pick=random.randrange(6)+side
                valid_pick=options[pick-side]
        # Ovan: En ny skål väljs tills en icke-tom skål är vald. Dessutom kontrolleras att 
        # inte alla valbara skålar är tomma.
        
        return pick
    
    def Max_pick(self, player , options, side):
        '''
        Returnerar index för den skål med flest kulor bland spelbara skålar för palyer.
        Då dessa utgörs av fler än en görs ett slumpmässigt likformigt fördelat val mellan dessa.
        
        Övrig input:
        options - Spelbara skålar för player.
        side - Den sida av brädet som player sitter vid, detta ges av 0 eller 7. 
        '''
        
        most_pieces=max(options) # Returnerar det högsta värdet bland spelbara skålar.
        pick=[i for i, n in enumerate(options) if n == most_pieces] # Returnerar index för 
        # skålar med detta värde.
            
        if len(pick)>1:
            pick=pick[random.randrange(len(pick))]+side # Väljer ut en av dessa skålar
            # slumpmässigt(om de utgörs av mer än en).
        else:
            pick=pick[0]+side
            
        return pick
    
    def User_pick(self, player, side):
        '''
        Låter användare player välja skål.
        
        Övrig input:
        side - Den sida av brädet som player sitter vid, detta ges av 0 eller 7. 
        '''
        
        Gb=self.Game_board
        board_display=(f'\n  {Gb[0]} {Gb[1]} {Gb[2]} {Gb[3]} {Gb[4]} {Gb[5]}'
        f'\n{Gb[13]}             {Gb[6]}\n  {Gb[12]} {Gb[11]} {Gb[10]} {Gb[9]} {Gb[8]} {Gb[7]}')
        print(board_display) # Visar användaren spelbrädet innan valet görs.
        pick=User_choice_validation(Gb,player,side,board_display)
        
        return pick
        
    def Strategies(self, player, player_strategy):
        '''
        Returnerar en siffra som representerar vald skål för player givet 
        players strategi(player_strategy).
        '''
        
        pick=0
        
        if player == 2:
            side = 7
        else:
            side = 0
        
        options=self.Game_board[0+side:6+side]
        
        if player_strategy == 1:
            pick=self.Uniform_random_pick(player, options, side)

        elif player_strategy == 2:
            pick=self.Max_pick(player, options, side)
            
        elif player_strategy == 3:
            pick=self.User_pick(player, side)
        
        return(pick)
        
    def Turn_procedure(self, player, player_strategy):
        '''
        Går igenom en spelturs faser givet spelare och dess strategi.
        Information om villkor för spelslut och extra speltur returneras.
        Utöver detta sker änringar i listan self.Game_board. Detta beskrivs
        mer detaljerat i metoderna som återkallas.
        '''
        
        if player == 2:
            side = 7
        else:
            side = 0
        
        Game_end=Kalaha.Game_end_conditions(self, player) # Kontrollerar om spelet bör avslutas.
        home_pit, pit_after_home=self.Game_board[6+side],self.Game_board[7-side] # Tilldelar värden 
        # som representerar antalet kulor i spelarens bo, och skålen efter bot(innan de förändras
        # av funktionen pick). Dessa värden behövs för metoden Extra_turn_conditions.
        Kalaha.Pick(self, Kalaha.Strategies(self, player, player_strategy)) # Spelaren gör sitt drag.
        Extra_turn=Kalaha.Extra_turn_conditions(self, player, \
        home_pit, pit_after_home) # Kontrollerar villkor för extra speltur.
        Game_end=Kalaha.Game_end_conditions(self, player) # Kontrollerar om spelet bör avslutas.
        
        return Game_end,Extra_turn
        
    def Play(self, player_1_strategy, player_2_strategy):
        '''
        Utför en spelomgång givet de två spelarnas strategier(1,2 eller 3).
        Returnerar klass objektet self.Game_board i sitt tillstånd vid spelets slut.
        '''
        Game_end=False
        
        while not Game_end:
            
            First_turn_player1, First_turn_player2=True,True
            Extra_turn1,Extra_turn2 = False,False
            
            while (First_turn_player1 or Extra_turn1) and not Game_end:
                
                (Game_end, Extra_turn1)=self.Turn_procedure(1,player_1_strategy)
                First_turn_player1=False
            
            while (First_turn_player2 or Extra_turn2) and not Game_end:
                
                (Game_end, Extra_turn2)=self.Turn_procedure(2, player_2_strategy)
                First_turn_player2=False
                
        return(self.Game_board)
        
        
    def Determine_winner(Game_board):
        '''
        Jämför element 7 och 14 i en lista. Metoden returnerar (1,0) ifall 
        element 7 är större, (0,0) ifall de är lika stora och (0,1) om element 14 
        är större. Utfallen används för att beräkna antal vinster per spelare
        i Multiple_simulation
        '''
        
        player1_wins=0
        player2_wins=0
       
        if Game_board[6]>Game_board[13]: # Om antalet kulor i skål 7 är högre
            # än antalet kulor i skål 13 vinner spelare 1.
            player1_wins+=1
            
        # Oavgjorda resultat ignoreras. 
        
        elif Game_board[6]<Game_board[13]:
            player2_wins+=1
            
        return (player1_wins,player2_wins)