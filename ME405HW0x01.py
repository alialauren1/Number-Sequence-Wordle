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

# -->>>> write function to print grid

while(True): # FSM Task 1
    try: 
        
# STATE 0 CODEMAKER    
        if (state == S0_CODEMAKER): # S0: Set/Reset, Set Up Grid, Make Secret Code
            
            print('State is ', state)
            
            # Make Secret Code
            SC = 1234
            print('Secret Code:',SC)
            SC_str = str(SC)           
            SC_list_str = [char for char in SC_str]           
            
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            print('+---+---+---+---+')
                                  
            state = S1_USER_INPUT_GUESS

# STATE 1 USER INPUT's THE GUESS            
        elif (state == S1_USER_INPUT_GUESS): # S1: remains here until user inputs proper guess                    
            print('State is', state) 
            
            # string joining
            guess_str = input('Enter a 4 numbers between 0 and 5: ')
            print(guess_str)
            
            nums_out_bounds_flg = 0
            guess_ints_flg = 0
            guess_length_flg = 0
            
            if not guess_str:
                print('Empty String')
                
            elif len(guess_str) == 4:
                print('length is 4')
                guess_length_flg = 1 # flg will raise if length is 4
                
                try:
                    guess_str_ints = [int(char) for char in guess_str]            # ---> does this go thru all nums at that moment???
                    print('passed becoming integer')
                    guess_ints_flg = 1 # flg will raise if all nums integers
                    
                    for my_num in guess_str_ints:
                        
                        if 0 <= my_num <= 5:   
                            pass
                        else: 
                            nums_out_bounds_flg = 1 # flg will raise if any num is out of 0-5 range
                            print('a number is too large')
                   
                except ValueError:
                    print('Only integers allowed')
                    
            elif len(guess_str) < 4:
                print('length is too short')  
                
                # add more code about is any numb is out of range        
                
            elif len(guess_str) > 4: 
                print('length is too long')           
            else: 
                pass
            
            print('done assessing sequence')          
            if guess_length_flg==1 and guess_ints_flg==1 and nums_out_bounds_flg==0:  
                guess_ints_flg = 0
                nums_in_bounds_flg = 0 
                guess_length_flg = 0
                state = S2_CODE_BREAKER
            else:
                guess_ints_flg = 0
                nums_in_bounds_flg = 0  
                guess_length_flg = 0
                state = S1_USER_INPUT_GUESS
                                                  
# STATE 2 TRY TO BREAK THE SECRET CODE        
        elif (state == S2_CODE_BREAKER): # S2: trys to break secret code          
            print ('State is ', state)
            
            print(guess_str)
            
            SC_list_str_copy = SC_list_str
            guess_str_copy = guess_str
            guess_list_str = [char for char in guess_str_copy] # strings are immutable
            print(guess_list_str)
            
      # first pass     
            feedback_chars = []
            for idx in range(4):
                secret_char_p1=SC_list_str_copy[idx]
                guess_char_p1=guess_list_str[idx]
                print(secret_char_p1,guess_char_p1) 
                
                if secret_char_p1 == guess_char_p1:
                    feedback_chars.append('+')
                else:
                    feedback_chars.append('x')
            print(feedback_chars)
            
      # second pass
            print('Words')
            for i in range(4):
                guess_char_p2=guess_list_str[i]
                for j in range(4):
                    secret_char_p2=SC_list_str_copy[j]
                    if not i == j:
                        print('not i==j')
                    else: 
                        print('already determined +')
                print('----------')
    
    
            
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