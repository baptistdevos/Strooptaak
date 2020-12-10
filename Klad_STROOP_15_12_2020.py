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
import matplotlib.pyplot as plt
import numpy as np
import glob


###Variables
##Non-changing variables
N_Words = 10                                                                   #How many words are going to be displayed in one round

List_of_colors = ["Blue", "Green", "Yellow", "Red", "Purple"]
Pos = [(-80,0),(0,0),(80,0),(0,-200), (0,200), (0,-100)]


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
##Making the window, preparing path (for the location of the images)          
win = psychopy.visual.Window(size = (800,600), units = 'pix', color = "grey")           #Grey is easier on my eyes
path =  r'C:\Users\Baptist Devos\Desktop\Bachelor psychologie\1eSemester_3dejaar\Programming for psychologists\Strooptaak\Images_Corr'

#________________________________________________________________________

###INSTRUCTIONS

##Welcome_screen

Welcome = visual.ImageStim(win, image = path + "\Welcome_screen.png") 
Welcome.draw()
win.flip()
event.waitKeys()

##screen 2 (Showing the general instruction)
Instr1 = visual.ImageStim(win, image = path + "\Instr_1.png")
Instr1.draw()
win.flip()
event.waitKeys()

##Exercise 1
#Ex1_Screen (Showing the first practice-task-instruction)

Ex1_Screen =  visual.ImageStim(win, image = path + "\Ex1_Screen.png")
Ex1_Screen.draw()
win.flip()
event.waitKeys()


#Ex1_Screen2 (Showing the 'g' or 'h' possibility)

Ex1_Screen2 =  visual.ImageStim(win, image = path + "\Ex1_Screen2.png")
Ex1_Screen2.draw()
win.flip()
event.waitKeys()

input_practise = event.waitKeys(keyList=('g','h')) #Possible keys : 'g' and 'h'
input_practise

#Feedback on exercise 1

if 'h' in input_practise : #feedback if typed 'h' (Ex1_ScreenH)
    Ex1_ScreenH =  visual.ImageStim(win, image = path + "\Ex1_ScreenH.png")
    Ex1_ScreenH.draw()
    win.flip()
    event.waitKeys()

else: #feedback if typed 'g' (Ex1_ScreenG)  
    Ex1_ScreenG =  visual.ImageStim(win, image = path + "\Ex1_ScreenG.png")
    Ex1_ScreenG.draw()
    win.flip()
    event.waitKeys()
    

## Exercise 2
#Ex2_Screen (Showing the second practice-task-instruction)

Ex2_Screen =  visual.ImageStim(win, image = path + "\Ex2_Screen.png")
Ex2_Screen.draw()
win.flip()
event.waitKeys()


#Ex2_Screen2 (Showing the 'g' or 'h' possibily)
Ex2_Screen2 =  visual.ImageStim(win, image = path + "\Ex2_Screen2.png")
Ex2_Screen2.draw()
win.flip()
event.waitKeys()

input_practise = event.waitKeys(keyList=('g','h')) #2 only two possible keys to type
input_practise

#Feedback on exercise 2

if 'h' in input_practise : #feedback if typed 'h' (Ex2_ScreenH)
    Ex2_ScreenH =  visual.ImageStim(win, image = path + "\Ex2_ScreenH.png")
    Ex2_ScreenH.draw()
    win.flip()
    event.waitKeys()
    
else: 
    Ex2_ScreenG =  visual.ImageStim(win, image = path + "\Ex2_ScreenG.png")
    Ex2_ScreenG.draw()
    win.flip()
    event.waitKeys()
    
## Start Real task 

Start_realTest = visual.ImageStim(win, image = path + "\Start_realTest.png") 
Start_realTest.draw()
win.flip()
event.waitKeys()

### REAL TASK
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



### ENDING MESSAGE
# Image to mark the end of the test


Finish = visual.ImageStim(win, image = path + "\Finish.png") 
Finish.draw()
win.flip()
event.waitKeys()
win.close() 




Score1
Gem = Score1 / N_Words;Gem

# Results










