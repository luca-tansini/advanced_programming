'''a function validate that checks if a string composed of 'X', 'O' and ' ' is a correct configuration for the tic-tac-toe game and if it is a winning configuration for the 'X' or the 'O' symbols, an even configuration or if there are still moves.'''

import unittest

def validate(str):
    if(len(str)!=9): return False
    d = {'X':0,'O':0," ":0}
    try:
        for i in str:
            d[i]+=1
    except Exception as e: return False
    if((d['X']-d['O'])**2 > 1): return False

    winner = set()
    for i in range(3):
        if(len(set(str[i:i+3]))==1):     winner.add(set(str[i:i+3]).pop())
        if(len(set(str[i:9:3]))==1):     winner.add(set(str[i:9:3]).pop())
        if(len(set(str[i:9-i:4-i]))==1): winner.add(set(str[i:9-i:4-i]).pop())

    if(len(winner)==1): return winner.pop()
    if(d[' ']>0): return 'notfinished'
    return 'even'


class tictactoetest(unittest.TestCase):

    correctness_values = {"XOXOXOXOX":True,"XXXXXXXXX":False,"OOOAAAOOO":False,"OOOOOXXXX":True,"XXOOXOOXX":True,"X X O O X":True,"":False,"X X O X X":False}

    def test_correctness_values(self):
        for k in self.correctness_values:
            self.assertEqual(self.correctness_values[k],bool(validate(k)))

    outcome_values = {'XOXOXOOXO':'even','XOXOXOOOX':'X','OXXOXOOOX':'O','XOXOX O O':'notfinished',}

    def test_outcome_values(self):
        for k in self.outcome_values:
            self.assertEqual(self.outcome_values[k],validate(k))

if __name__ == '__main__':
    unittest.main()
