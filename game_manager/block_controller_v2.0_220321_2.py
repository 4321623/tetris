#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pprint
import random
from re import S
from turtle import width
import numpy as np
from telnetlib import theNULL

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

        # get data from GameStatus
        # current shape info
        CurrentShapeDirectionRange = GameStatus["block_info"]["currentShape"]["direction_range"]
        self.CurrentShape_class = GameStatus["block_info"]["currentShape"]["class"]
        self.CurrentShape_index = GameStatus["block_info"]["currentShape"]["index"]

        print("===Current_block_info===")
        print("Direction Range",CurrentShapeDirectionRange)
        print("index",self.CurrentShape_index)

        # next shape info
        NextShapeDirectionRange = GameStatus["block_info"]["nextShape"]["direction_range"]
        self.NextShape_class = GameStatus["block_info"]["nextShape"]["class"]
        self.NextShape_index = GameStatus["block_info"]["nextShape"]["index"]

        print("===Next_block_info===")
        print("Direction Range",NextShapeDirectionRange)
        print("index",self.NextShape_index)

        # current board info
        self.board_backboard=GameStatus["field_info"]["backboard"]
        board = self.board_backboard

        # Print GetZerocount
        print("===zerocount===")
        print(self.GetZerocount(board))

        # default board definition ボードのデフォルト定義
        self.board_data_width = GameStatus["field_info"]["width"] #横方向の定義
        self.board_data_height = GameStatus["field_info"]["height"]  #縦方向の定義

        width = self.board_data_width
        height = self.board_data_height


        # define rotetion & x
        kekka_x = 0
        kekka_kaiten = 0

        # def A[x] zerocount left_3&light_6 0 add
        left_zero=[0,0,0]
        A=left_zero
        A[len(A):len(A)]=self.GetZerocount(board)

        right_zero=[0,0,0,0,0,0]
        A[len(A):len(A)]=right_zero

        print("===A(x)===")
        print(A)

        HyoukaVAL = 0
        Kaiten = 0

        kekka = [[0]*4 for i in range(width)]

        for x in range (0,width):

        #HAIを定義(for x 内で行う)

#            a = A[x+3]
#            b = A[x+4]
#            c = A[x+5]
#            d = A[x+6]
#            e = A[x+7]
#            f = A[x+8]

            HAI=self.HAI_type(self.NextShape_index)


#            HAI=[[a,2,1,d,1,2,10,1],
#                [a,2,1,d,1,f,8,1],
#                [a,b,1,d,1,2,7,1],
#                [a,b,1,d,1,f,5,1],
#                [a,b,c,d,1,f,3,0],
#                [a,b,1,d,e,f,2,2],
#                [a,b,0,d,0,f,1,3]
#                ]
            
            JyoukenNoMAX=len(HAI)
            print("JyoukenMAX",JyoukenNoMAX)

            HyoukaVAL = 0
            Kaiten = 0

            HAI_Hyouka = 6 #HAIの評価値に該当
            HAI_Kaiten = 7 #HAIの回転に該当

            print("x=",x)

          
            for jyouken in range (0,JyoukenNoMAX):
                
                if A[x+3] - A[x] == HAI[jyouken][0]: #A(x)-A(x-3)
                 
                    if A[x+3] - A[x+1] == HAI[jyouken][1]: #A(x)-A(x-2)
                        
                        if A[x+3] - A[x+2] == HAI[jyouken][2]: #A(x)-A(x-1)
                            
                            if A[x+3] - A[x+4] == HAI[jyouken][4]: #A(x)-A(x+1)

                                if A[x+3] - A[x+5] == HAI[jyouken][5]: #A(x)-A(x+2)
            
                                    if HAI[jyouken][HAI_Hyouka] > HyoukaVAL:
                                        HyoukaVAL = HAI[jyouken][HAI_Hyouka]
                                        Kaiten = HAI[jyouken][HAI_Kaiten]
            
            kekka[x][0] = x
            kekka[x][1] = HyoukaVAL
            kekka[x][2] = HyoukaVAL+A[x+3]
            kekka[x][3] = Kaiten

            pprint.pprint(kekka)

        # 評価値最大探索
        max_value = np.amax(kekka)
        print("max_value=",max_value)

        for i in kekka:
            print(i, max_value in i)
            if max_value in i:
                result = True
                break
        result
        print(i)
        print(i[0],i[3])

        kekka_x = i[0]
        kekka_kaiten = i[3]
        
        # search best nextMove -->
        nextMove["strategy"]["direction"] = kekka_kaiten
        nextMove["strategy"]["x"] = kekka_x
        nextMove["strategy"]["y_operation"] = 1
        nextMove["strategy"]["y_moveblocknum"] = 1
        # search best nextMove <--

        # return nextMove
        print("===", datetime.now() - t1)
        print(nextMove)
        return nextMove

    def GetZerocount(self,board):
        width = self.board_data_width
        height = self.board_data_height
        zerocount = [0]*width       
        for x in range (0,width):
            for y in range (0,height):
                if board[y*width+x]==self.ShapeNone_index:
                 zerocount[x]+=1
                else:
                    break
        return zerocount

    def HAI_type(self,current_index):
        current_index = self.CurrentShape_index

        a = A[x+3]
        b = A[x+4]
        c = A[x+5]
        d = A[x+6]
        e = A[x+7]
        f = A[x+8]

        if current_index == 1: # ShapeI (仮にTを入れている)
            HAI=[[a,2,1,d,1,2,10,1],
            [a,2,1,d,1,f,8,1],
            [a,b,1,d,1,2,7,1],
            [a,b,1,d,1,f,5,1],
            [a,b,c,d,1,f,3,0],
            [a,b,1,d,e,f,2,2],
            [a,b,0,d,0,f,1,3]
            ]

        elif current_index == 2: # ShapeL
            HAI=[[a,3,2,d,3,f,25,2],
            [a,3,2,d,e,f,23,2],
            [a,b,2,d,3,f,22,2],
            [a,b,2,d,e,f,20,2],
            [a,1,-1,d,0,1,18,1],
            [a,1,-1,d,0,f,16,1],
            [a,b,-1,d,0,1,15,1],
            [a,b,-1,d,0,f,13,1],
            [a,1,0,d,0,2,11,3],
            [a,1,0,d,0,1,9,3],
            [a,b,3,d,0,1,7,0],
            [a,b,1,d,0,1,5,0],
            [a,b,0,d,0,f,3,3],
            [a,b,c,d,0,f,1,0]
            ]

        elif current_index == 3: # ShapeJ
            HAI=[[a,b,3,d,2,1,25,2],
            [a,b,3,d,2,f,23,2],
            [a,b,c,d,2,1,22,2],
            [a,b,c,d,2,f,20,2],
            [a,1,1,d,1,1,18,3],
            [a,1,1,d,1,f,16,3],
            [a,b,1,d,1,1,15,3],
            [a,b,1,d,1,f,13,3],
            [a,2,0,d,0,1,11,1],
            [a,1,0,d,0,1,9,1],
            [a,1,0,d,3,f,7,0],
            [a,1,0,d,1,f,5,0],
            [a,b,0,d,0,f,3,1],
            [a,b,0,d,e,f,1,0]
            ]

        elif current_index == 4: # ShapeT
            HAI=[[a,2,1,d,1,2,10,1],
            [a,2,1,d,1,f,8,1],
            [a,b,1,d,1,2,7,1],
            [a,b,1,d,1,f,5,1],
            [a,b,c,d,1,f,3,0],
            [a,b,1,d,e,f,2,2],
            [a,b,0,d,0,f,1,3]
            ]

        elif current_index == 5: # ShapeO
            HAI=[[a,b,2,d,2,f,10,1],
            [a,b,2,d,1,f,8,1],
            [a,b,1,d,2,f,7,1],
            [a,b,2,d,e,f,5,1],
            [a,b,c,d,2,f,3,0],
            [a,b,c,d,0,f,2,2]
            ]

        elif current_index == 6: # ShapeS
            HAI=[[a,1,0,d,1,2,13,0],
            [a,1,0,d,1,1,11,0],
            [a,b,0,d,1,2,9,0],
            [a,b,2,d,-1,0,7,1],
            [a,b,0,d,1,f,5,0],
            [a,b,0,d,-1,0,3,1],
            [a,b,c,d,-1,f,1,1]
            ]

        elif current_index == 7: # ShapeZ
            HAI=[[a,2,1,d,0,1,13,0],
            [a,1,1,d,0,1,11,0],
            [a,2,1,d,0,f,9,0],
            [a,b,1,d,0,f,7,0],
            [a,b,1,d,1,2,5,1],
            [a,b,1,d,1,1,3,1],
            [a,b,c,d,1,f,1,1]
            ]

        return HAI


        




BLOCK_CONTROLLER = Block_Controller()

