# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:53:11 2020

@author: Baptist Devos
"""

### Alles importeren

##Import everything needed

import pip
import math #maths
import pandas as pd #data from other programs

import psychopy
from psychopy import visual, event, core, sound
import psychopy.visual
from psychopy.hardware import keyboard

#visual screen

import psychopy.visual

#openen van een screen

win = psychopy.visual.Window(size=[400, 400], units="pix", fullscr=False, color=[1, 1, 1])

#variables 

# select colours for experiment. 
expColours=['red','blue','green','yellow']
# Determine number of trials
trialNum = 20


#Initialize components for Stroop test
Stroop_clock = core.Clock()
Stroop_cross = visual.ShapeStim(win=win, name='Stroop_cross', vertices='cross', pos=(0.0, 0.0), size=0.2, lineColor='#ffffff', fillColor='#ffffff')
Stroop_cross.model_name = None
Stroop_cross.cname = 'Stroop_cross'

Stroop_text = visual.TextStim(win=win, name='Stroop_text', pos=(0.0, 0.0), height=0.2)
Stroop_text.model_name = None
Stroop_text.cname = 'Stroop_text'

Stroop_keyboard = keyboard.Keyboard()
Stroop_keyboard.model_name = None
Stroop_keyboard.cname = 'Stroop_keyboard'
Stroop_keyboard.valid_keys = ['left', 'down', 'right', 'up', 'quit']

Stroop_circle = visual.Circle(win=win, name='Stroop_circle', radius=1.0, fillColor='red', lineColor='red', pos=(0.0, 0.0), size=0.2)
Stroop_circle.model_name = None
Stroop_circle.cname = 'Stroop_circle'

Stroop_circle_2 = visual.Circle(win=win, name='Stroop_circle_2', radius=1.0, fillColor='green', lineColor='green', pos=(0.0, 0.0), size=0.2)
Stroop_circle_2.model_name = None
Stroop_circle_2.cname = 'Stroop_circle_2'

Stroop_sound = sound.backend_ptb.SoundPTB(value=500)
Stroop_sound.model_name = None
Stroop_sound.cname = 'Stroop_sound'

Stroop_sound_2 = sound.backend_ptb.SoundPTB(value=1000)
Stroop_sound_2.model_name = None
Stroop_sound_2.cname = 'Stroop_sound_2'


Stroop_components = [
    Stroop_cross,
    Stroop_text,
    Stroop_keyboard,
    Stroop_circle,
    Stroop_circle_2,
    Stroop_sound,
    Stroop_sound_2]

