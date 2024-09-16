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

        # ブロックを何回回転させるか、x座標を定義する
        block_location_list = [
            # [direction, x]
            [0,0],	# 1 
            [0,1],	# 2
            [1,4],	# 3
            [3,7],	# 4
            [0,4],	# 5
            [1,7],	# 6
            [1,2],	# 7
            [	0,9	]	,	# 8
            [	2,6	]	,	# 9
            [	3,7	]	,	# 10
            [	1,4	]	,	# 11
            [	0,1	]	,	# 12
            [	1,8	]	,	# 13
            [	1,0	]	,	# 14
            [	0,0	]	,	# 15
            [	3,3	]	,	# 16
            [	2,7	]	,	# 17
            [	2,2	]	,	# 18
            [	0,5	]	,	# 19
            [	0,6	]	,	# 20
            [	1,3	]	,	# 21
            [	0,9	]	,	# 22
            [	1,6	]	,	# 23
            [	2,8	]	,	# 24
            [	1,3	]	,	# 25
            [	0,2	]	,	# 26
            [	0,7	]	,	# 27
            [	1,5	]	,	# 28
            [	0,1	]	,	# 29
            [	2,4	]	,	# 30
            [	3,8	]	,	# 31
            [	1,5	]	,	# 32
            [	0,1	]	,	# 33
            [	1,6	]	,	# 34
            [	1,3	]	,	# 35
            [	0,0	]	,	# 36
            [	3,1	]	,	# 37
            [	0,9	]	,	# 38
            [	1,3	]	,	# 39
            [	0,0	]	,	# 40
            [	1,7	]	,	# 41
            [	0,8	]	,	# 42
            [	0,5	]	,	# 43
            [	2,6	]	,	# 44
            [	3,8	]	,	# 45
            [	3,1	]	,	# 46
            [	0,3	]	,	# 47
            [	1,1	]	,	# 48
            [	0,3	]	,	# 49
            [	0,0	]	,	# 50
            [	3,6	]	,	# 51
            [	3,3	]	,	# 52
            [	1,1	]	,	# 53
            [	0,5	]	,	# 54
            [	1,2	]	,	# 55
            [	0,8	]	,	# 56
            [	0,9	]	,	# 57
            [	3,6	]	,	# 58
            [	2,4	]	,	# 59
            [	1,3	]	,	# 60
            [	0,0	]	,	# 61
            [	0,1	]	,	# 62
            [	1,6	]	,	# 63
            [	0,8	]	,	# 64
            [	1,1	]	,	# 65
            [	3,4	]	,	# 66
            [	2,9	]	,	# 67
            [	0,7	]	,	# 68
            [	1,8	]	,	# 69
            [	0,3	]	,	# 70
            [	0,6	]	,	# 71
            [	1,2	]	,	# 72
            [	2,0	]	,	# 73
            [	2,5	]	,	# 74
            [	0,2	]	,	# 75
            [	1,6	]	,	# 76
            [	1,4	]	,	# 77
            [	0,9	]	,	# 78
            [	1,2	]	,	# 79
            [	2,0	]	,	# 80
            [	2,7	]	,	# 81
            [	0,5	]	,	# 82
            [	1,1	]	,	# 83
            [	1,0	]	,	# 84
            [	0,8	]	,	# 85
            [	2,4	]	,	# 86
            [	3,6	]	,	# 87
            [	2,9	]	,	# 88
            [	0,3	]	,	# 89
            [	0,8	]	,	# 90
            [	0,5	]	,	# 91
            [	0,2	]	,	# 92
            [	1,4	]	,	# 93
            [	0,7	]	,	# 94
            [	2,6	]	,	# 95
            [	0,8	]	,	# 96
            [	0,4	]	,	# 97
            [	1,1	]	,	# 98
            [	0,0	]	,	# 99
            [	1,4	]	,	# 100
            [	3,5	]	,	# 101
            [	0,1	]	,	# 102
            [	0,7	]	,	# 103
            [	1,2	]	,	# 104
            [	0,7	]	,	# 105
            [	0,9	]	,	# 106
            [	1,6	]	,	# 107
            [	2,4	]	,	# 108
            [	0,8	]	,	# 109
            [	0,6	]	,	# 110
            [	1,2	]	,	# 111
            [	1,5	]	,	# 112
            [	0,0	]	,	# 113
            [	2,7	]	,	# 114
            [	2,4	]	,	# 115
            [	2,1	]	,	# 116
            [	0,1	]	,	# 117
            [	1,8	]	,	# 118
            [	1,5	]	,	# 119
            [	0,0	]	,	# 120
            [	2,8	]	,	# 121
            [	2,4	]	,	# 122
            [	2,1	]	,	# 123
            [	0,2	]	,	# 124
            [	0,3	]	,	# 125
            [	1,0	]	,	# 126
            [	0,9	]	,	# 127
            [	1,3	]	,	# 128
            [	3,6	]	,	# 129
            [	2,5	]	,	# 130
            [	0,8	]	,	# 131
            [	0,3	]	,	# 132
            [	1,0	]	,	# 133
            [	1,8	]	,	# 134
            [	1,3	]	,	# 135
            [	3,4	]	,	# 136
            [	0,0	]	,	# 137
            [	0,6	]	,	# 138
            [	0,2	]	,	# 139
            [	0,4	]	,	# 140
            [	0,9	]	,	# 141
            [	2,8	]	,	# 142
            [	3,4	]	,	# 143
            [	0,6	]	,	# 144
            [	0,0	]	,	# 145
            [	1,7	]	,	# 146
            [	1,6	]	,	# 147
            [	0,9	]	,	# 148
            [	3,5	]	,	# 149
            [	3,1	]	,	# 150
            [	0,3	]	,	# 151
            [	0,1	]	,	# 152
            [	0,2	]	,	# 153
            [	1,5	]	,	# 154
            [	0,8	]	,	# 155
            [	1,2	]	,	# 156
            [	3,8	]	,	# 157
            [	0,4	]	,	# 158
            [	0,8	]	,	# 159
            [	1,6	]	,	# 160
            [	0,7	]	,	# 161
            [	0,0	]	,	# 162
            [	1,1	]	,	# 163
            [	3,4	]	,	# 164
            [	2,9	]	,	# 165
            [	0,0	]	,	# 166
            [	0,5	]	,	# 167
            [	1,3	]	,	# 168
            [	0,2	]	,	# 169
            [	2,7	]	,	# 170
            [	2,1	]	,	# 171
            [	0,8	]	,	# 172
            [	0,6	]	,	# 173
            [	1,4	]	,	# 174
            [	1,5	]	,	# 175
            [	0,0	]	,	# 176
            [	2,7	]	,	# 177
            [	2,3	]	,	# 178
            [	2,9	]	,	# 179
            [	0,1	]	,	# 180
            [	1,2	]	,	# 181
            # [0,0], # N
        ]

        # print GameStatus
        print("=================================================>")
        pprint.pprint(GameStatus, width = 61, compact = True)

        # search best nextMove -->
        current_block_No = GameStatus["judge_info"]["block_index"] - 1
        if current_block_No < len(block_location_list):
                # my_code
                nextMove["strategy"]["direction"] = block_location_list[current_block_No][0]
                nextMove["strategy"]["x"] = block_location_list[current_block_No][1]
                nextMove["strategy"]["y_operation"] = 1
                nextMove["strategy"]["y_moveblocknum"] = 1
        else:
                # random sample
                nextMove["strategy"]["direction"] = 0
                nextMove["strategy"]["x"] = 0
                nextMove["strategy"]["y_operation"] = 1
                nextMove["strategy"]["y_moveblocknum"] = 1
        # search best nextMove <--

        # return nextMove
        print("===", datetime.now() - t1)
        print(nextMove)
        return nextMove

BLOCK_CONTROLLER = Block_Controller()

