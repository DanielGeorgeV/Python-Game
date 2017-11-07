'''
Created on Nov 1, 2017

@author: Daniel
'''

class Brain(object):
    '''
    Mr.TicTacToe
    '''
    
    def Cerebrum(self, gameTable, cpu_coin, gameType):
        '''
        Cerebrum
        '''
        masala = Brain()
        global noOfOppnCoins
        global OpponentCoins
        if(gameType == 'E'):
            if(cpu_coin == 'X'):
                OpponentCoins = 'O'
                OpponPosition = masala.GetOpponentCoinsCount(OpponentCoins, gameTable)
            else:
                OpponentCoins = 'X'
                OpponPosition = masala.GetOpponentCoinsCount(OpponentCoins, gameTable)
            if(OpponPosition['count'] <= 1):
                location = masala.OppnWinningChange_0(cpu_coin, gameTable, OpponentCoins, OpponPosition)
                return location
            else:
                MyPosition = masala.GetMyCoinsCount('O', gameTable)
                location = masala.OppnWinningChange_More(cpu_coin, gameTable, OpponentCoins, OpponPosition, MyPosition)
                return location
        elif(gameType == 'M'):
            if(cpu_coin == 'X'):
                OpponentCoins = 'O'
                OpponPosition = masala.GetOpponentCoinsCount(OpponentCoins, gameTable)
            else:
                OpponentCoins = 'X'
                OpponPosition = masala.GetOpponentCoinsCount(OpponentCoins, gameTable)
            if(OpponPosition['count'] <= 1):
                location = masala.OppnWinningChange_0(cpu_coin, gameTable, OpponentCoins, OpponPosition)
                return location
            else:
                MyPosition = masala.GetMyCoinsCount('O', gameTable)
                location = masala.OppnWinningChange_More(cpu_coin, gameTable, OpponentCoins, OpponPosition, MyPosition)
                return location
            
    
    def GetOpponentCoinsCount(self, OpponentCoins, gameTable):
        global OpponPosition
        OpponPosition = {}
        global count
        count = 0
        position = 0
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                position = position + 1
                if gameTable[i][j] == OpponentCoins:
                    count = count + 1
                    OpponPosition[position] = [i, j]
                j = j + 1
            i = i + 1
        OpponPosition['count'] = count
        return OpponPosition
    
    def GetMyCoinsCount(self, OpponentCoins, gameTable):
        global OpponPosition
        OpponPosition = {}
        global count
        count = 0
        position = 0
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                position = position + 1
                if gameTable[i][j] == OpponentCoins:
                    count = count + 1
                    OpponPosition[position] = [i, j]
                j = j + 1
            i = i + 1
        OpponPosition['count'] = count
        return OpponPosition
    
    def OppnWinningChange_0(self, cpu_coin, gameTable, OpponentCoins, OpponPosition):
        global OpponCoinCount
        K = OpponPosition.keys()
        for key in K:
            if key == 'count':
                pass
            elif key != 5:
                # gameTable[1][1]=cpu_coin
                return 5
            elif key == 5:
                # gameTable[0][0]=cpu_coin
                return 1

    def OppnWinningChange_More(self, cpu_coin, gameTable, OpponentCoins, OpponPosition, MyPosition):
        global OpponCoinCount
        O = OpponPosition.keys()
        M = MyPosition.keys()
        global count
        count = 1
        while count < 10:
            if (count not in O) and (count not in M):
                return count
            count = count + 1
    
    def isDoubbleAttack(self, cpu_coin, gameTable, OpponentCoins, OpponPosition, MyPosition):
        O = OpponPosition.keys()
        oppCount = OpponPosition['count']
        myCount = MyPosition['count']
        if oppCount == 1 and myCount == 0:
            for key in O:
                if key == 'count':
                    pass
                elif key == 5:
                    return 1
                else:
                    return 5
        elif count>1:
            return isOpponWining(OpponentCoins,OpponPosition,MyPosition)
            
            
            
    def isOpponWining(self,OpponentCoins,OpponPosition,MyPosition):
        O = OpponPosition.keys()
        oppCount = OpponPosition['count']
        O.rem
            
            
            
            """def 
            
        for key in K:
            if key=='count':
                pass
            elif key!=5:
                gameTable[1][1]=cpu_coin
                return gameTable
            elif key==5:
                gameTable[0][0]=cpu_coin
                return gameTable
        i = 0
        while(i<3):
            j=0
            while(j<3):
                if gameTable[i][j]!=OpponentCoins:
                j+1
            i+1
        """
