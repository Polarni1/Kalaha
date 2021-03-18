
def Game_setup():
    
    while True:
            try:
                starting_pieces=int(input('Välj antalet kulor som du vill ska finnas i varje skål vid spelets start. Traditionellt '
    'spelas med 3 till 6 kulor i varje skål: \n'))
                if not 3<=starting_pieces<=6:
                    raise ValueError
               
            except ValueError:
                bad_input_text=(f"""\nDitt val måste vara ett positivt heltal mellan 3 och 6.""")
                print(bad_input_text)
                continue
            
            break
        
    return starting_pieces

def strategy_choice1():
    
    while True:
            try:
                choice=int(input('Välj strategi för spelare 1, spelaren som gör första draget. Välj 1 för '
    'en helt slumpmässig strategi där spelaren väljer bland icke-tomma skålar efter '
    'en likformig fördelning. Välj 2 för en strategi där spelaren allid väljer den skål '
    'med flest kulor, och gör ett likformigt fördelat slumpmässigt val mellan de skålar som '
    'har flest kulor när dessa utgörs av fler än en. Välj 3 för att spela manuellt: \n'))
                if not 1<=choice<=3:
                    raise ValueError
               
            except ValueError:
                bad_input_text=(f"""\nDitt val måste vara ett positivt heltal 1,2 eller 3.""")
                print(bad_input_text)
                continue
            
            break
    return choice

def strategy_choice2():
    
    while True:
            try:
                choice2=int(input('Välj strategi för spelare 2. Välj 1 för '
    'en helt slumpmässig strategi där spelaren väljer bland icke-tomma skålar efter '
    'en likformig fördelning. Välj 2 för en strategi där spelaren allid väljer den skål '
    'med flest kulor, och gör ett likformigt fördelat slumpmässigt val mellan de skålar som '
    'har flest kulor när dessa utgörs av fler än en. Välj 3 för att spela manuellt: \n'))
                if not 1<=choice2<=3:
                    raise ValueError
               
            except ValueError:
                bad_input_text=(f"""\nDitt val måste vara ett positivt heltal 1,2 eller 3.""")
                print(bad_input_text)
                continue
            
            break
    
    return choice2

def number_of_games():
    
    while True:
            try:
                n=int(input('Välj antalet spelomgångar: \n'))
                if not n>0:
                    raise ValueError
               
            except ValueError:
                bad_input_text=(f"""\nDitt val måste vara ett positivt heltal.""")
                print(bad_input_text)
                continue
            
            break
    
    return n

def User_choice(side):
    if side==0:
        board_explantion=(f'Välj skål. Som spelare 1 är dina spelbara skålar' 
    ' placerade högst upp i figuren ovan. De representeras av talen 1-6 och är'
    ' utplacerade i numerisk ordning. Spelet går medsols.'
    ' Siffran längst till höger representerar ditt bo: \n')
    else:
        board_explantion=(f'Välj skål. Som spelare 2 är dina spelbara skålar' 
        ' placerade längst ned i figuren ovan. De representeras av talen 8-13 och är'
        ' utplacerade i omvänd numerisk ordning. Spelet går medsols.'
        ' Siffran längst till vänster representerar ditt bo: \n')
        
    pick=int(input(board_explantion))
    return pick

def User_choice_validation(game_board,player,side,board_display):
    '''
    Kontrollerar att indata som skickas till funktionen User_choice är godtagbar.
    Inputs ärvs av User_pick där de också beskrivs.
    '''

    while True: 
        try:
            pick=User_choice(side)-1
            if not side<=pick<=side+5:
                raise ValueError# Försäkrar att användaren håller sig till spelbara skålar.
            
            if  game_board[pick]==0: # Ber användaren välja en annan skål om vald skål är tom.
                raise ValueError
               
        except ValueError: # Hanterar opassande typer av indata(decimaltal, listor m.m.)
                
            bad_input_text=(f'\nDitt val måste vara ett positivt heltal mellan {side+1} och {side+6}.'
                            f' Den skål du väljer får inte vara tom.')
            print(bad_input_text) # 
            print(board_display)
            continue
        break
        
    return pick