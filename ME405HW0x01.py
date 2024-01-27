#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:46:10 2024

@author: aliawolken
"""

# AUTHOR: ALIA WOLKEN
# ME 405 HW0x01 

import time

S0_CODEMAKER=0
S1_USER_INPUT_GUESS=1 
S2_CODE_BREAKER=2 
S3_WIN=3
S4_LOSS=4 

# Do i need the def & __name__=='__main__' stuff?

state = 0 # Var to indicate the state the FSM shall run
count = 0 # Counter Var to track runs through CODE_BREAKER state

while(True): # FSM Task 1
    try: 
        if (state == S0_CODEMAKER):
            # S0 will Set/Reset, Set Up Grid, Make Secret Code
            print('State is ', state)
            
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
                                  
            state = S1_USER_INPUT_GUESS
            
        elif (state == S1_USER_INPUT_GUESS):
            # S1  
            print('State is', state)
            state = S2_CODE_BREAKER
        
        elif (state == S2_CODE_BREAKER):
            # S2 CODE MAKER
            print ('State is ', state)
            state = S3_WIN
            
        elif (state == S3_WIN):
            # S3 correct guess was made
            print ('State is ', state)
            
        elif (state == S4_LOSS):
            # S4 game is over, ran out of attempts
            print ('State is ', state)
            

            
            # if enter not pressed, keep state at S3
            
        else: 
            raise ValueError('Invalid state')
            
        time.sleep(1)
            
    except KeyboardInterrupt: # breaks out of program if Ctrl-C
        break
    
print('terminated')