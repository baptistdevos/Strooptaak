# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:27:24 2020

@author: Natalie & Baptist 
"""

###Import modules

from psychopy import core, event, visual
import random
import pandas
import numpy as np

###Variables
##Non-changing variables
N_Words = 100                                                                   #How many words are going to be displayed in one round

List_of_colors = ["Blue", "Green", "Yellow", "Red", "Purple"]


#Making a list of all combinations of List_of colors
List_of_combinations = []

for word in List_of_colors:                                                    

    for color in List_of_colors:
        if color!=word:
            List_of_combinations.append([word, color, str(word +'_'+ color)])  #First = text, second = kleur, third = whole stimulus


##Changing variables
i = 0                                                                          #Position of word of stimulus in list 

###Start
##Making the window          
win = visual.Window(size = (800,600), units = 'pix', color = "grey")           #Grey is easier on my eyes

#instructies, (visual textbox)

##For-loop
for question in range(N_Words):                                                #How many stimuli will be given
    List_of_positions = [(-80,0),(80,0)]                                       #Where left and right words will be positioned

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
    if 'h' in input_nextround or 'g' in input_nextround:
            continue
        
    elif 'q' in input_nextround:                                               #If 'q' is pressed, window will close
        break

win.close()
            

