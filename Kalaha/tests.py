
import random
import numpy as np
import matplotlib.pyplot as plt
from user_interaction import *
from game_simulator import *
import unittest

class Test_Kalaha(unittest.TestCase):
    '''
    Grundläggande tester för metoder i programmet. Enklare metoder och funktioner
    är utelämnade. Även funktioner som inte själva utför beräkningar, utan endast åberopar
    andra funktioner är utelämnade.
    '''
    def test_Pick(self):
        after_pick = Kalaha(3)
        after_pick.Pick(2)
        self.assertEqual(after_pick.Game_board,[3, 3, 0, 4, 4, 4, 0, 3, 3, 3, 3, 3, 3, 0])
        
    def test_Pick2(self):
        after_pick = Kalaha(6)
        after_pick.Pick(5)
        self.assertEqual(after_pick.Game_board,[6, 6, 6, 6, 6, 0, 1, 7, 7, 7, 7, 7, 6, 0])

    def test_Extra_turn_conditions(self):
        #game_board_after_play = [3,3,3,0,4,4,1,3,3,3,3,3,3,0]
        #test=Kalaha.Extra_turn_conditions(self, 1, 0, 1)
        bulls_eye=Kalaha(3)
        bulls_eye.Pick(3)
        self.assertTrue(bulls_eye.Extra_turn_conditions(1, 0, 3))
        
    def test_Collect_all_pieces(self):
        perfect_win=Kalaha(4)
        perfect_win.Collect_all_pieces(1)
        self.assertEqual(perfect_win.Game_board,[0, 0, 0, 0, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0])
        
    def test_Game_end_conditions(self):
        not_finished=Kalaha(5)
        not_finished.Pick(2)
        not_finished.Pick(10)
        self.assertFalse(not_finished.Game_end_conditions(2))
        
    def test_Determine_winner(self):
        end_of_game=[0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 26]
        result=Kalaha.Determine_winner(end_of_game)
        self.assertEqual(result,(0,1))
    
if __name__ == '__main__':
    unittest.main()
    