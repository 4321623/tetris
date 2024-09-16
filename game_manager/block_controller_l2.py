#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pprint
import random

class Block_Controller(object):

    # init parameter
    board_backboard = 0
    board_data_width = 0
    board_data_height = 0
    ShapeNone_index = 0
    CurrentShape_class = 0
    NextShape_class = 0

    # GetNextMove is main function.
    # input
    #    GameStatus : this data include all field status, 
    #                 in detail see the internal GameStatus data.
    # output
    #    nextMove : this data include next shape position and the other,
    #               if return None, do nothing to nextMove.
    def GetNextMove(self, nextMove, GameStatus):

        t1 = datetime.now()

        # print GameStatus
        print("=================================================>")
        pprint.pprint(GameStatus, width = 61, compact = True)
        self.board_backboard=GameStatus["field_info"]["backboard"]
        board = self.board_backboard

        print(self.GetZerocount(board))
        
        
        # search best nextMove -->
        # random sample
        nextMove["strategy"]["direction"] = random.randint(0,4)
        nextMove["strategy"]["x"] = random.randint(0,9)
        nextMove["strategy"]["y_operation"] = 1
        nextMove["strategy"]["y_moveblocknum"] = random.randint(1,8)
        # search best nextMove <--

        # return nextMove
        print("===", datetime.now() - t1)
        print(nextMove)
        return nextMove

    def GetZerocount(self,board):
        width = self.board_data_width
        height = self.board_data_height
        zerocount=[0]*10
        for x in range (0,10):
            for y in range (0,22):
                if board[y*10+x]==self.ShapeNone_index:
                 zerocount[x]+=1
                else:
                    break
        return zerocount


BLOCK_CONTROLLER = Block_Controller()

