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

state = 0 # Var to indicate the state the FSM shall run
attempts_count = 0 # Counter Var to track runs through CODE_BREAKER state

while(True): # FSM Task 1
    try: 
        
# STATE 0 CODEMAKER    
        if (state == S0_CODEMAKER): # S0: Set/Reset, Set Up Grid, Make Secret Code
            
            print('State is ', state)
            
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
            
            # Make Secret Code
            secret_code = 1234
                                  
            state = S1_USER_INPUT_GUESS

# STATE 1 USER INPUT's THE GUESS            
        elif (state == S1_USER_INPUT_GUESS): # S1: remains here until user inputs proper guess                    
            print('State is', state) 
            
            # string joining
            num_string = input('Enter a 4 numbers between 0 and 5: ')
            print(num_string)
            
            nums_out_bounds_flg = 0
            nums_integers_flg = 0
            guess_length_flg = 0
            
            if not num_string:
                print('Empty String')
                
            elif len(num_string) == 4:
                print('length is 4')
                guess_length_flg = 1 # flg will raise if length is 4
                
                try:
                    num_string_ints = [int(char) for char in num_string]            # does this go thru all nums at that moment???
                    print('passed becoming integer')
                    nums_integers_flg = 1 # flg will raise if all nums integers
                    
                    for my_num in num_string_ints:
                        
                        if 0 <= my_num <= 5:   
                            pass
                        else: 
                            nums_out_bounds_flg = 1 # flg will raise if any num is out of 0-5 range
                            print('a number is too large')
                   
                except ValueError:
                    print('Only integers allowed')
                    
            elif len(num_string) < 4:
                print('length is too short')  
                
                # add more code about is any numb is out of range        
                
            elif len(num_string) > 4: 
                print('length is too long')           
            else: 
                pass
            
            print('done assessing sequence')          
            if guess_length_flg==1 and nums_integers_flg==1 and nums_out_bounds_flg==0:  
                nums_integers_flg = 0
                nums_in_bounds_flg = 0 
                guess_length_flg = 0
                state = S2_CODE_BREAKER
            else:
                nums_integers_flg = 0
                nums_in_bounds_flg = 0  
                guess_length_flg = 0
                state = S1_USER_INPUT_GUESS
                
# STATE 2 TRY TO BREAK THE SECRET CODE        
        elif (state == S2_CODE_BREAKER): # S2: trys to break secret code          
            print ('State is ', state)
            state = S3_WIN

# STATE 3 IF THE CORRECT GUESS WAS MADE            
        elif (state == S3_WIN):# S3: correct guess was made           
            print ('State is ', state)
 
# STATE 4 IF THE GAME WAS LOST
        elif (state == S4_LOSS): #S4: game over, out of attempts
            print ('State is ', state)
            
        else: 
            #raise ValueError('Invalid state')
            print('invalid state')
            
        time.sleep(1)
            
    except KeyboardInterrupt: # breaks out of program if Ctrl-C
        break
    
print('terminated')