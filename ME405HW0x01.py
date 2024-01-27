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
attempts_count = 0 # Counter Var to track runs through CODE_BREAKER state

while(True): # FSM Task 1
    try: 
        if (state == S0_CODEMAKER): # S0: Set/Reset, Set Up Grid, Make Secret Code
            
            print('State is ', state)
            
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
            
            # Make Secret Code
                                  
            state = S1_USER_INPUT_GUESS
            
        elif (state == S1_USER_INPUT_GUESS): # S1: remains here until user inputs proper guess                    
            print('State is', state) 
            
            # string joining
            num_string = input('Enter a 4 digit number between 0 and 5: ')
            print(num_string)
            
            if not num_string:
                print('Empty String')
                state = S1_USER_INPUT_GUESS
                
            else: 
                nums_in_guess= 0 # Keeps track of how many nums input for guess
                
                for my_number in num_string:
    
                    nums_in_guess += 1 # increments each numb 
                
                    if nums_in_guess > 4:
                        try:
                            my_number_int = int(my_number) 
                            print('nums in guess too long')
                            state = S1_USER_INPUT_GUESS
                        except ValueError:
                            print('Incorrect Input & too long')
                            state = S1_USER_INPUT_GUESS
                        
                    else:    
                        try:
                            my_number_int = int(my_number)                           
                            guess_too_lg = 0 # guess_too_lg flag false initially
                            
                            if my_number_int >= 6:
                                guess_too_lg = 1 # guess_too_lg flag true
                            else: 
                                print('numb ok size')
                            
                        except ValueError:
                            print('Incorrect Input')
                            state = S1_USER_INPUT_GUESS
                            break
                        
                        else:
                            if guess_too_lg == 1: # check if guess_too_lg raised
                                print('num too large')
                                state = S1_USER_INPUT_GUESS
                            else:
                                state = S2_CODE_BREAKER
                                pass
                                
                print(num_string,'ran through')
                
                if nums_in_guess < 4 :
                    print('num too small')
                    state = S1_USER_INPUT_GUESS
                else:
                    pass                      
        
        elif (state == S2_CODE_BREAKER): # S2: trys to break secret code          
            print ('State is ', state)
            state = S3_WIN
            
        elif (state == S3_WIN):# S3: correct guess was made           
            print ('State is ', state)
            
        elif (state == S4_LOSS): #S4: game over, out of attempts
            print ('State is ', state)
            
        else: 
            #raise ValueError('Invalid state')
            print('invalid state')
            
        time.sleep(1)
            
    except KeyboardInterrupt: # breaks out of program if Ctrl-C
        break
    
print('terminated')