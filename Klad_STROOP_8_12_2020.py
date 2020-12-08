# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:46:16 2020

@author: Baptist Devos
"""

###Import modules

from psychopy import core, event, visual
import psychopy.visual
import random
import pandas as pd
import numpy as np

###Variables
##Non-changing variables
N_Words = 10                                                                   #How many words are going to be displayed in one round

List_of_colors = ["Blue", "Green", "Yellow", "Red", "Purple"]


#Making a list of all combinations of List_of colors
List_of_combinations = []       #name suggestion : combi_colors

for word in List_of_colors:                                                    

    for color in List_of_colors:
        if color!=word:
            List_of_combinations.append([word, color, str(word +'_'+ color)])  #First = text, second = kleur, third = whole stimulus


##Changing variables
i = 0                                                                          #Position of word of stimulus in list 
Score1 = 0
###Start
##Making the window          
win = psychopy.visual.Window(size = (800,600), units = 'pix', color = "grey")           #Grey is easier on my eyes

#________________________________________________________________________
#instructies, (visual textbox)


#screen 1
Instr1 = psychopy.visual.TextStim(win, text = "Welcome to the Stroop-task", color = "black")
Instr2 = psychopy.visual.TextStim(win, text = "First, we will practise a little bit. Type any key for <next>", color = "black", pos = (0,-100))
Instr1.draw()
Instr2.draw()

win.flip()
psychopy.event.waitKeys()

#screen 2
Instr3 = psychopy.visual.TextStim(win, text = "In the next screen, you will see three colorwords. Only the middle one is colored. Type any key for <next>", color = "black")
Instr3.draw()
win.flip()
psychopy.event.waitKeys()

#screen 3
Pos = [(-80,0),(0,0),(80,0),(0,-200), (0,200), (0,-100)]

Instr4 = psychopy.visual.TextStim(win, text = "You need to focus on the middle word. Remember the color of the middle word. Press any key for <Next>", color = "black" , pos = Pos[3])
word1 = psychopy.visual.TextStim(win, text = 'Yellow', color = "black", pos = Pos[0])
word2 = psychopy.visual.TextStim(win, text = 'Yellow', color = "blue", pos = Pos[1])
word3 = psychopy.visual.TextStim(win, text = 'Blue', color = "black", pos = Pos[2]) 

word1.draw()
word2.draw()
word3.draw()
Instr4.draw()
win.flip()
psychopy.event.waitKeys()

#screen 4 (first example)
Instr5 = psychopy.visual.TextStim(win, text= 'Press <g> for the answer on the left, press <h> for the answer on the right', color ='black', pos = Pos[4])
word1.draw()
word2.draw()
word3.draw()
Instr5.draw()

win.flip()
input_practise = psychopy.event.waitKeys(keyList=('g','h'))
input_practise


if 'h' in input_practise :
    Instr_TRUE = psychopy.visual.TextStim(win, text= 'You are right, blue is the correct color of the middle word. Press any key for <next>', color = 'black')
    Instr_TRUE.draw()
    win.flip()
    psychopy.event.waitKeys()
    
            
if 'g' in input_practise :  
    Instr_FALSE = psychopy.visual.TextStim(win, text= 'You are false, blue is the correct color of the middle word. You should have typed <h>. Press any key for <next>', color = 'black')
    Instr_FALSE.draw()
    win.flip()
    psychopy.event.waitKeys()
    
  
# Example 2

#screen 1
Instr4 = psychopy.visual.TextStim(win, text = "Remember the color of the middle word. Press any key for <Next>", color = "black" , pos = Pos[3])
word1 = psychopy.visual.TextStim(win, text = 'Green', color = "black", pos = Pos[0])
word2 = psychopy.visual.TextStim(win, text = 'Blue', color = "green", pos = Pos[1])
word3 = psychopy.visual.TextStim(win, text = 'Blue', color = "black", pos = Pos[2]) 

word1.draw()
word2.draw()
word3.draw()
Instr4.draw()
win.flip()
psychopy.event.waitKeys()

#screen 2
Instr5 = psychopy.visual.TextStim(win, text= 'Press <g> for the answer on the left, press <h> for the answer on the right', color ='black', pos = Pos[4])
word1.draw()
word2.draw()
word3.draw()
Instr5.draw()

win.flip()
input_practise = psychopy.event.waitKeys(keyList=('g','h'))
input_practise




if 'g' in input_practise :
    Instr_TRUE = psychopy.visual.TextStim(win, text= 'You are right, green is the correct color of the middle word. Press any key for <next>', color = 'black')
    Instr_TRUE.draw()
    win.flip()
    psychopy.event.waitKeys()
    
            
if 'h' in input_practise :  
    Instr_FALSE = psychopy.visual.TextStim(win, text= 'You are false, green is the correct color of the middle word. You should have typed <g>. Press any key for <next>', color = 'black')
    Instr_FALSE.draw()
    win.flip()
    psychopy.event.waitKeys()
    

#Transition to the 'real' test

Instr6 = psychopy.visual.TextStim(win, text= 'If you are ready, type any key to <start>', color = 'black')
Instr7 = psychopy.visual.TextStim(win, text =  'Again, focus on the color of the middle word, then type <g> for the left color, <h> for the right color', color = 'black' ,pos = Pos[5])
Instr6.draw()
Instr7.draw()
win.flip()
psychopy.event.waitKeys()


#___________________________________________________________________________
##For-loop

for question in range(N_Words):                                                #How many stimuli will be given
    List_of_positions = [(-80,0),(80,0)]
    
                                       #Where left and right words will be positioned

    i = random.randrange(0,len(List_of_combinations))
    j = random.randint(0,1)
    
    position1 = List_of_positions.pop(j)
    position2 = List_of_positions.pop()

    stimulus = visual.TextStim(win, text = List_of_combinations[i][0],         #The middle word
                               color = List_of_combinations[i][1])
    
    word = visual.TextStim(win, text = List_of_combinations[i][0], color = "black", pos = (position1))
    color = visual.TextStim(win, text = List_of_combinations[i][1], color = "black", pos = (position2))
                      
    stimulus.draw()
    word.draw()
    color.draw()
        
    win.flip()

    input_nextround = event.waitKeys(keyList=('g', 'h', 'q'))                  #Waiting on input 'g' or 'h' to display next word
    # if 'h' in input_nextround or 'g' in input_nextround:
    #         continue
    
    if position2 == tuple([80,0]) and 'h' in input_nextround :
        Score1 = Score1 + 1
        Score = psychopy.visual.TextStim(win, text= 'Score = 1', color = 'black')
        Score.draw()
        win.flip()
        event.waitKeys()
    elif position2 != tuple([80,0]) and 'h' in input_nextround: 
        Score = psychopy.visual.TextStim(win, text= 'Score = 0', color = 'black')
        Score.draw()
        win.flip()
        event.waitKeys()
    elif position2 == tuple([-80,0]) and 'g' in input_nextround :
        Score = psychopy.visual.TextStim(win, text= 'Score = 1', color = 'black')
        Score1 = Score1 + 1
        Score.draw()
        win.flip()
        event.waitKeys()
    else: 
        Score = psychopy.visual.TextStim(win, text= 'Score = 0', color = 'black')
        Score.draw()
        win.flip()
        event.waitKeys()
    
    continue
    
    win.flip()



Score1



# Ending message
#screen 1
Instr_End = psychopy.visual.TextStim(win, text = "You are finished, Thank you very much. Type any key to see you results", color = "black")
Instr_End.draw()
win.flip()
psychopy.event.waitKeys()
win.close()

Score1
Gem = Score1 / N_Words;Gem

# Results










