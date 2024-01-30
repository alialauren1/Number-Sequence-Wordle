#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:46:10 2024

@author: aliawolken
"""

# AUTHOR: ALIA WOLKEN
# ME 405 HW0x01 

import time
import random

S0_CODEMAKER=0
S1_USER_INPUT_GUESS=1 
S2_CODE_BREAKER=2 
S3_WIN=3
S4_LOSS=4 

state = 0 # Var to indicate the state the FSM shall run

win_score = 0 # keeps track of how many wins
loss_score = 0 # keeps track of how many losses

def print_grid():
    tot_attempts=12
    print('-----------------------------------------')
    #print('[','Wins:',win_score,'  Losses:',loss_score,']')
    print('CODE TO BREAK:',SC_str)

    if attempts_count == 0:
        print('[','Wins:',win_score,'  Losses:',loss_score,']')
        for _ in range(tot_attempts):
            print('+---+---+---+---+')
            print('|   |   |   |   |')
        print('+---+---+---+---+')
        
    elif 1 <= attempts_count <= 12:
        
        for _ in range(tot_attempts-attempts_count):
            print('+---+---+---+---+')
            print('|   |   |   |   |')
            
        for n in range(attempts_count):
            joined = ' | '.join(guesses[attempts_count-1-n])
            print('+---+---+---+---+')
            print('| '+joined+' |'+feedbacks[attempts_count-1-n]) 
        print('+---+---+---+---+')
    
    else: 
        pass

while(True): # FSM Task 1
    try: 
        
# STATE 0 CODEMAKER    
        if (state == S0_CODEMAKER): # S0: Set/Reset, Set Up Grid, Make Secret Code
            
            print('State is ', state)
            
            attempts_count = 0 # Counter Var to track runs through CODE_BREAKER state
            guesses = [] # list to store all guesses
            feedbacks = [] # list to store all feedback
            
            SC = []
            SC_length = 4
            for _ in range(SC_length):
                SN = random.randrange(0,6)
                SN_str = str(SN)
                SC.append(SN_str)
            SC_str = ''.join(SC)
            # my_string = ' '.join(my_list)
            
            # Make Secret Code
            #SC = '4321'
            # print('CODE TO BREAK:',SC)
            # SC_str = str(SC)           
            SC_list_str = [char for char in SC_str] 
            
            print_grid()
                                 
            state = S1_USER_INPUT_GUESS

# STATE 1 USER INPUT's THE GUESS            
        elif (state == S1_USER_INPUT_GUESS): # S1: remains here until user inputs proper guess                    
            print('State is', state) 
            
            # string joining
            guess_str = input('Enter 4 numbers between 0 and 5: ')
            # print(guess_str)
            
            nums_out_bounds_flg = 0
            guess_ints_flg = 0
            guess_length_flg = 0
            
            if not guess_str:
                print('Empty String')
                
            elif len(guess_str) == 4:
                guess_length_flg = 1 # flg will raise if length is 4
                
                try:
                    guess_str_ints = [int(char) for char in guess_str]            
                    # print('passed becoming integer')
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
            
            # print('done assessing sequence')          
            if guess_length_flg==1 and guess_ints_flg==1 and nums_out_bounds_flg==0:  
                guess_ints_flg = 0
                nums_in_bounds_flg = 0 
                guess_length_flg = 0
                
                state = S2_CODE_BREAKER
            else:
                time.sleep(2)
                print_grid()
                guess_ints_flg = 0
                nums_in_bounds_flg = 0  
                guess_length_flg = 0
                state = S1_USER_INPUT_GUESS
                                                  
# STATE 2 TRY TO BREAK THE SECRET CODE        
        elif (state == S2_CODE_BREAKER): # S2: trys to break secret code          
            print ('State is ', state)
            
            
            #print(guess_str)
            
            guess_list_str = [char for char in guess_str]
            guess_list_str_COPY1 = [char for char in guess_str] # strings are immutable, list of strs
            
            SC_list_str_COPY = [char for char in SC_str] 
                       
            attempts_count +=1 # keeps track of which attempt 
            
            
      # first pass -> matches its same placement  
            feedback_chars = []
            #print('FIRST PASS')
            for idx in range(4):
                secret_char_p1=SC_list_str_COPY[idx]
                guess_char_p1=guess_list_str_COPY1[idx]
                #print(secret_char_p1,guess_char_p1) 
                
                if secret_char_p1 == guess_char_p1: 
                    # print('Match (right place)')
                    # print('idx',idx)
                    SC_list_str_COPY[idx]='X'
                    guess_list_str_COPY1[idx]='Y'
                    feedback_chars.append('+')
                                  
                else:
                    pass
                
            #print(feedback_chars)
            #print(guess_list_str_COPY1,SC_list_str_COPY)
            
      # second pass -> matches any placement
            #print('SECOND PASS')
            for i in range(4):
                guess_char_p2=guess_list_str_COPY1[i]
                for j in range(4):                                  
                    secret_char_p2=SC_list_str_COPY[j]
                    if not i == j:
                        # print('---------')
                        # print('not i == j')
                        # print('secret char',secret_char_p2)
                        # print('guess char',guess_char_p2)
                        
                        if secret_char_p2 == guess_char_p2:
                            # print('Match')
                            # print('j=',j,' i=',i)
                            SC_list_str_COPY[j]= 'A' 
                            # print(SC_list_str_COPY1)
                            feedback_chars.append('-')
                            break
                        else:
                            # print('No match')
                            pass
              
                    else:
                        pass
                        # print('---------')
                        # print('already checked in P1')

            # print('----------')
            feedback_chars_str = ''.join(feedback_chars)
            # print(feedback_chars_str)
            feedbacks.append(feedback_chars_str) # save current feedback in list of all feedback    

            # save current guess in a list of all guesses
            guesses.append(guess_str)
            
            print_grid()            
                
      # check if all ++++
            #print('words')
            if feedback_chars_str == '++++':
                state = S3_WIN
                
      # check if attempts over      
            elif attempts_count == 12:
                state = S4_LOSS
      
      # check if more attempts left 
            elif 1 <= attempts_count <12:
                state = S1_USER_INPUT_GUESS
                
      # >>>>>>>>>> Error      
            else:
                print('error in state 2 w/ either feedback_chars_str or attempts_count')

# STATE 3 IF THE CORRECT GUESS WAS MADE            
        elif (state == S3_WIN):# S3: correct guess was made           
            print ('State is ', state)
            print('Congratulations, you have won this round')
            win_score += 1
            
            time.sleep(2)
            state = S0_CODEMAKER
            
 
# STATE 4 IF THE GAME WAS LOST
        elif (state == S4_LOSS): #S4: game over, out of attempts
            print ('State is ', state)
            print('Out of attempts, you have lost')
            loss_score += 1
            
            time.sleep(2)
            state = S0_CODEMAKER
            
# >>>>>>>>>> Error            
        else: 
            #raise ValueError('Invalid state')
            print('invalid state')
            
        #time.sleep(1)
            
    except KeyboardInterrupt: # breaks out of program if Ctrl-C
        break
    
print('terminated')