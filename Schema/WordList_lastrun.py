#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 29, 2020, at 13:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'wordList'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\melchi\\Documents\\CourseMaterials\\CogSPLabs\\LabCodeFiles\\Schema\\wordList2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Welcome to the experiment!\n\nIn this experiment, you will be shown a set of words, twice. Don't write them down, but do pay attention as they go by! You'll be asked later if they showed up.\n\nIn between each list, you'll have a set of math problems to solve. Do your best, but don't worry if you get one or two wrong. \n\nAfter the lists of words, you'll be shown a list of words. Indicate whether the word is one you've seen earlier in the study. (There will be instructions again for this at the time.)\n\nEnjoy the experiment! \n\nPress any key when ready to start.",
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stop_intro = keyboard.Keyboard()

# Initialize components for Routine "beforeTrial"
beforeTrialClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press any key to start the next block of words',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "preTrialPause"
preTrialPauseClock = core.Clock()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "trial"
trialClock = core.Clock()
word = visual.TextStim(win=win, name='word',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "setTotalTime"
setTotalTimeClock = core.Clock()

# Initialize components for Routine "typeIn1"
typeIn1Clock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp = visual.TextStim(win=win, name='eqnDisp',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1 = visual.TextStim(win=win, name='letter1',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1 = visual.TextStim(win=win, name='ans1',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2 = visual.TextStim(win=win, name='letter2',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2 = visual.TextStim(win=win, name='ans2',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3 = visual.TextStim(win=win, name='letter3',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3 = visual.TextStim(win=win, name='ans3',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4 = visual.TextStim(win=win, name='letter4',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4 = visual.TextStim(win=win, name='ans4',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
key_resp_2 = keyboard.Keyboard()
countTheTime = 0


# Initialize components for Routine "checkResp"
checkRespClock = core.Clock()

# Initialize components for Routine "resp1"
resp1Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_3 = visual.TextStim(win=win, name='eqnDisp_3',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_3 = visual.TextStim(win=win, name='letter1_3',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_3 = visual.TextStim(win=win, name='ans1_3',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_3 = visual.TextStim(win=win, name='letter2_3',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_3 = visual.TextStim(win=win, name='ans2_3',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_3 = visual.TextStim(win=win, name='letter3_3',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_3 = visual.TextStim(win=win, name='ans3_3',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_3 = visual.TextStim(win=win, name='letter4_3',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_3 = visual.TextStim(win=win, name='ans4_3',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
countTheTime = 0


# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "beforeTrial"
beforeTrialClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press any key to start the next block of words',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
word_2 = visual.TextStim(win=win, name='word_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "setTotalTime"
setTotalTimeClock = core.Clock()

# Initialize components for Routine "typeIn2"
typeIn2Clock = core.Clock()
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_2 = visual.TextStim(win=win, name='eqnDisp_2',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_2 = visual.TextStim(win=win, name='letter1_2',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_2 = visual.TextStim(win=win, name='ans1_2',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_2 = visual.TextStim(win=win, name='letter2_2',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_2 = visual.TextStim(win=win, name='ans2_2',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_2 = visual.TextStim(win=win, name='letter3_2',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_2 = visual.TextStim(win=win, name='ans3_2',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_2 = visual.TextStim(win=win, name='letter4_2',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_2 = visual.TextStim(win=win, name='ans4_2',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
key_resp_4 = keyboard.Keyboard()
countTheTime = 0


# Initialize components for Routine "checkResp2"
checkResp2Clock = core.Clock()

# Initialize components for Routine "resp1"
resp1Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_3 = visual.TextStim(win=win, name='eqnDisp_3',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_3 = visual.TextStim(win=win, name='letter1_3',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_3 = visual.TextStim(win=win, name='ans1_3',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_3 = visual.TextStim(win=win, name='letter2_3',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_3 = visual.TextStim(win=win, name='ans2_3',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_3 = visual.TextStim(win=win, name='letter3_3',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_3 = visual.TextStim(win=win, name='ans3_3',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_3 = visual.TextStim(win=win, name='letter4_3',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_3 = visual.TextStim(win=win, name='ans4_3',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
countTheTime = 0


# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "beforeTrial"
beforeTrialClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press any key to start the next block of words',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "trials3"
trials3Clock = core.Clock()
word_3 = visual.TextStim(win=win, name='word_3',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "setTotalTime"
setTotalTimeClock = core.Clock()

# Initialize components for Routine "typeIn3"
typeIn3Clock = core.Clock()
instructions_4 = visual.TextStim(win=win, name='instructions_4',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_4 = visual.TextStim(win=win, name='eqnDisp_4',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_4 = visual.TextStim(win=win, name='letter1_4',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_4 = visual.TextStim(win=win, name='ans1_4',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_4 = visual.TextStim(win=win, name='letter2_4',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_4 = visual.TextStim(win=win, name='ans2_4',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_4 = visual.TextStim(win=win, name='letter3_4',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_4 = visual.TextStim(win=win, name='ans3_4',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_4 = visual.TextStim(win=win, name='letter4_4',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_4 = visual.TextStim(win=win, name='ans4_4',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
key_resp_5 = keyboard.Keyboard()
countTheTime = 0


# Initialize components for Routine "checkResp3"
checkResp3Clock = core.Clock()

# Initialize components for Routine "resp1"
resp1Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_3 = visual.TextStim(win=win, name='eqnDisp_3',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_3 = visual.TextStim(win=win, name='letter1_3',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_3 = visual.TextStim(win=win, name='ans1_3',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_3 = visual.TextStim(win=win, name='letter2_3',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_3 = visual.TextStim(win=win, name='ans2_3',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_3 = visual.TextStim(win=win, name='letter3_3',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_3 = visual.TextStim(win=win, name='ans3_3',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_3 = visual.TextStim(win=win, name='letter4_3',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_3 = visual.TextStim(win=win, name='ans4_3',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
countTheTime = 0


# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "beforeTrial"
beforeTrialClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press any key to start the next block of words',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "trials_4"
trials_4Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "setTotalTime"
setTotalTimeClock = core.Clock()

# Initialize components for Routine "typeIn4"
typeIn4Clock = core.Clock()
instructions_5 = visual.TextStim(win=win, name='instructions_5',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_5 = visual.TextStim(win=win, name='eqnDisp_5',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_5 = visual.TextStim(win=win, name='letter1_5',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_5 = visual.TextStim(win=win, name='ans1_5',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_5 = visual.TextStim(win=win, name='letter2_5',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_5 = visual.TextStim(win=win, name='ans2_5',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_5 = visual.TextStim(win=win, name='letter3_5',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_5 = visual.TextStim(win=win, name='ans3_5',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_5 = visual.TextStim(win=win, name='letter4_5',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_5 = visual.TextStim(win=win, name='ans4_5',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
key_resp_7 = keyboard.Keyboard()
countTheTime = 0


# Initialize components for Routine "checkResp4"
checkResp4Clock = core.Clock()

# Initialize components for Routine "resp1"
resp1Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='Solve as many equations as you can.\n\nNote: Solve from left to right, not according to orders of operations.',
    font='Arial',
    pos=[-.5, .5], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
eqnDisp_3 = visual.TextStim(win=win, name='eqnDisp_3',
    text='default text',
    font='Arial',
    pos=[-0.1, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
letter1_3 = visual.TextStim(win=win, name='letter1_3',
    text='1.',
    font='Arial',
    pos=[-0.4, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ans1_3 = visual.TextStim(win=win, name='ans1_3',
    text='default text',
    font='Arial',
    pos=[-0.4, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter2_3 = visual.TextStim(win=win, name='letter2_3',
    text='2.',
    font='Arial',
    pos=[-0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ans2_3 = visual.TextStim(win=win, name='ans2_3',
    text='default text',
    font='Arial',
    pos=[-0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
letter3_3 = visual.TextStim(win=win, name='letter3_3',
    text='3.',
    font='Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ans3_3 = visual.TextStim(win=win, name='ans3_3',
    text='default text',
    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
letter4_3 = visual.TextStim(win=win, name='letter4_3',
    text='4.',
    font='Arial',
    pos=[0.2, -0.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ans4_3 = visual.TextStim(win=win, name='ans4_3',
    text='default text',
    font='Arial',
    pos=[0.2, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
countTheTime = 0


# Initialize components for Routine "btwnTrialResp"
btwnTrialRespClock = core.Clock()
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instrPart2 = visual.TextStim(win=win, name='instrPart2',
    text="Study session finished.\n\nNext is the test session. You will be presented with a list of words. If the word is one you saw in the study session, press 'z'. If you did not see the word in the study session, press 'm'.\n\nPress any key to get started.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endInstr = keyboard.Keyboard()

# Initialize components for Routine "testRoutine"
testRoutineClock = core.Clock()
testText = visual.TextStim(win=win, name='testText',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press "z" if you saw on an earlier list.\nPress "m" if the word is new',
    font='Arial',
    pos=[-.3, .25], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "preTrialPause"
preTrialPauseClock = core.Clock()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
goodbye = visual.TextStim(win=win, name='goodbye',
    text="Yay! You're done",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
stop_intro.keys = []
stop_intro.rt = []
_stop_intro_allKeys = []
# keep track of which components have finished
introductionComponents = [text, stop_intro]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *stop_intro* updates
    waitOnFlip = False
    if stop_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop_intro.frameNStart = frameN  # exact frame index
        stop_intro.tStart = t  # local t and not account for scr refresh
        stop_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop_intro, 'tStartRefresh')  # time at next scr refresh
        stop_intro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(stop_intro.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(stop_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if stop_intro.status == STARTED and not waitOnFlip:
        theseKeys = stop_intro.getKeys(keyList=None, waitRelease=False)
        _stop_intro_allKeys.extend(theseKeys)
        if len(_stop_intro_allKeys):
            stop_intro.keys = _stop_intro_allKeys[-1].name  # just the last key pressed
            stop_intro.rt = _stop_intro_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "beforeTrial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
beforeTrialComponents = [text_2, key_resp_3]
for thisComponent in beforeTrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beforeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beforeTrial"-------
while continueRoutine:
    # get current time
    t = beforeTrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beforeTrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beforeTrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beforeTrial"-------
for thisComponent in beforeTrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "beforeTrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "preTrialPause"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
preTrialPauseComponents = [ISI_2]
for thisComponent in preTrialPauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
preTrialPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "preTrialPause"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = preTrialPauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=preTrialPauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_2* period
    if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_2.frameNStart = frameN  # exact frame index
        ISI_2.tStart = t  # local t and not account for scr refresh
        ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
        ISI_2.start(0.5)
    elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
        ISI_2.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preTrialPauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "preTrialPause"-------
for thisComponent in preTrialPauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_2.started', ISI_2.tStart)
thisExp.addData('ISI_2.stopped', ISI_2.tStop)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialList1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    word.setText(textOne)
    # keep track of which components have finished
    trialComponents = [word]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word* updates
        if word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word.frameNStart = frameN  # exact frame index
            word.tStart = t  # local t and not account for scr refresh
            word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
            word.setAutoDraw(True)
        if word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                word.tStop = t  # not accounting for scr refresh
                word.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word, 'tStopRefresh')  # time at next scr refresh
                word.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('word.started', word.tStartRefresh)
    trials.addData('word.stopped', word.tStopRefresh)
# completed 2 repeats of 'trials'


# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "setTotalTime"-------
continueRoutine = True
# update component parameters for each repeat
totalTime = 0
tempTotal = 0
# keep track of which components have finished
setTotalTimeComponents = []
for thisComponent in setTotalTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setTotalTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setTotalTime"-------
while continueRoutine:
    # get current time
    t = setTotalTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setTotalTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setTotalTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setTotalTime"-------
for thisComponent in setTotalTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setTotalTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pauseOne = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eqnTest.xlsx'),
    seed=None, name='pauseOne')
thisExp.addLoop(pauseOne)  # add the loop to the experiment
thisPauseOne = pauseOne.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPauseOne.rgb)
if thisPauseOne != None:
    for paramName in thisPauseOne:
        exec('{} = thisPauseOne[paramName]'.format(paramName))

for thisPauseOne in pauseOne:
    currentLoop = pauseOne
    # abbreviate parameter names if possible (e.g. rgb = thisPauseOne.rgb)
    if thisPauseOne != None:
        for paramName in thisPauseOne:
            exec('{} = thisPauseOne[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "typeIn1"-------
    continueRoutine = True
    # update component parameters for each repeat
    eqnDisp.setText(equationDisp)
    ans1.setText(answer1)
    ans2.setText(answ2)
    ans3.setText(answ3)
    ans4.setText(answ4)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    typeIn1Components = [instructions, eqnDisp, letter1, ans1, letter2, ans2, letter3, ans3, letter4, ans4, key_resp_2]
    for thisComponent in typeIn1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    typeIn1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "typeIn1"-------
    while continueRoutine:
        # get current time
        t = typeIn1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=typeIn1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions* updates
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            instructions.setAutoDraw(True)
        
        # *eqnDisp* updates
        if eqnDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp.frameNStart = frameN  # exact frame index
            eqnDisp.tStart = t  # local t and not account for scr refresh
            eqnDisp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp, 'tStartRefresh')  # time at next scr refresh
            eqnDisp.setAutoDraw(True)
        
        # *letter1* updates
        if letter1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1.frameNStart = frameN  # exact frame index
            letter1.tStart = t  # local t and not account for scr refresh
            letter1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1, 'tStartRefresh')  # time at next scr refresh
            letter1.setAutoDraw(True)
        
        # *ans1* updates
        if ans1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1.frameNStart = frameN  # exact frame index
            ans1.tStart = t  # local t and not account for scr refresh
            ans1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1, 'tStartRefresh')  # time at next scr refresh
            ans1.setAutoDraw(True)
        
        # *letter2* updates
        if letter2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2.frameNStart = frameN  # exact frame index
            letter2.tStart = t  # local t and not account for scr refresh
            letter2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2, 'tStartRefresh')  # time at next scr refresh
            letter2.setAutoDraw(True)
        
        # *ans2* updates
        if ans2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2.frameNStart = frameN  # exact frame index
            ans2.tStart = t  # local t and not account for scr refresh
            ans2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2, 'tStartRefresh')  # time at next scr refresh
            ans2.setAutoDraw(True)
        
        # *letter3* updates
        if letter3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3.frameNStart = frameN  # exact frame index
            letter3.tStart = t  # local t and not account for scr refresh
            letter3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3, 'tStartRefresh')  # time at next scr refresh
            letter3.setAutoDraw(True)
        
        # *ans3* updates
        if ans3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3.frameNStart = frameN  # exact frame index
            ans3.tStart = t  # local t and not account for scr refresh
            ans3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3, 'tStartRefresh')  # time at next scr refresh
            ans3.setAutoDraw(True)
        
        # *letter4* updates
        if letter4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4.frameNStart = frameN  # exact frame index
            letter4.tStart = t  # local t and not account for scr refresh
            letter4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4, 'tStartRefresh')  # time at next scr refresh
            letter4.setAutoDraw(True)
        
        # *ans4* updates
        if ans4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4.frameNStart = frameN  # exact frame index
            ans4.tStart = t  # local t and not account for scr refresh
            ans4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4, 'tStartRefresh')  # time at next scr refresh
            ans4.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        tempTheTime = typeIn1Clock.getTime() - countTheTime
        countTheTime = typeIn1Clock.getTime()
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pauseOne.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in typeIn1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "typeIn1"-------
    for thisComponent in typeIn1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pauseOne.addData('instructions.started', instructions.tStartRefresh)
    pauseOne.addData('instructions.stopped', instructions.tStopRefresh)
    pauseOne.addData('eqnDisp.started', eqnDisp.tStartRefresh)
    pauseOne.addData('eqnDisp.stopped', eqnDisp.tStopRefresh)
    pauseOne.addData('letter1.started', letter1.tStartRefresh)
    pauseOne.addData('letter1.stopped', letter1.tStopRefresh)
    pauseOne.addData('ans1.started', ans1.tStartRefresh)
    pauseOne.addData('ans1.stopped', ans1.tStopRefresh)
    pauseOne.addData('letter2.started', letter2.tStartRefresh)
    pauseOne.addData('letter2.stopped', letter2.tStopRefresh)
    pauseOne.addData('ans2.started', ans2.tStartRefresh)
    pauseOne.addData('ans2.stopped', ans2.tStopRefresh)
    pauseOne.addData('letter3.started', letter3.tStartRefresh)
    pauseOne.addData('letter3.stopped', letter3.tStopRefresh)
    pauseOne.addData('ans3.started', ans3.tStartRefresh)
    pauseOne.addData('ans3.stopped', ans3.tStopRefresh)
    pauseOne.addData('letter4.started', letter4.tStartRefresh)
    pauseOne.addData('letter4.stopped', letter4.tStopRefresh)
    pauseOne.addData('ans4.started', ans4.tStartRefresh)
    pauseOne.addData('ans4.stopped', ans4.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for pauseOne (TrialHandler)
    pauseOne.addData('key_resp_2.keys',key_resp_2.keys)
    pauseOne.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        pauseOne.addData('key_resp_2.rt', key_resp_2.rt)
    pauseOne.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    pauseOne.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "typeIn1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "checkResp"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    checkRespComponents = []
    for thisComponent in checkRespComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    checkRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "checkResp"-------
    while continueRoutine:
        # get current time
        t = checkRespClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=checkRespClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if int(key_resp_2.keys) == int(corrAns):
            respColor = "green"
        elif key_resp_2.keys != corrAns:
            respColor = "red"
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in checkRespComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "checkResp"-------
    for thisComponent in checkRespComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "checkResp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "resp1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    eqnDisp_3.setColor(respColor, colorSpace='rgb')
    eqnDisp_3.setText(equationDisp)
    letter1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setText(answer1)
    letter2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setText(answ2)
    letter3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setText(answ3)
    letter4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setText(answ4)
    # keep track of which components have finished
    resp1Components = [instructions_3, eqnDisp_3, letter1_3, ans1_3, letter2_3, ans2_3, letter3_3, ans3_3, letter4_3, ans4_3]
    for thisComponent in resp1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resp1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resp1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = resp1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resp1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_3* updates
        if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_3.frameNStart = frameN  # exact frame index
            instructions_3.tStart = t  # local t and not account for scr refresh
            instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
            instructions_3.setAutoDraw(True)
        if instructions_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                instructions_3.tStop = t  # not accounting for scr refresh
                instructions_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructions_3, 'tStopRefresh')  # time at next scr refresh
                instructions_3.setAutoDraw(False)
        
        # *eqnDisp_3* updates
        if eqnDisp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_3.frameNStart = frameN  # exact frame index
            eqnDisp_3.tStart = t  # local t and not account for scr refresh
            eqnDisp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_3, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_3.setAutoDraw(True)
        if eqnDisp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eqnDisp_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eqnDisp_3.tStop = t  # not accounting for scr refresh
                eqnDisp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eqnDisp_3, 'tStopRefresh')  # time at next scr refresh
                eqnDisp_3.setAutoDraw(False)
        
        # *letter1_3* updates
        if letter1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_3.frameNStart = frameN  # exact frame index
            letter1_3.tStart = t  # local t and not account for scr refresh
            letter1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_3, 'tStartRefresh')  # time at next scr refresh
            letter1_3.setAutoDraw(True)
        if letter1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter1_3.tStop = t  # not accounting for scr refresh
                letter1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter1_3, 'tStopRefresh')  # time at next scr refresh
                letter1_3.setAutoDraw(False)
        
        # *ans1_3* updates
        if ans1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_3.frameNStart = frameN  # exact frame index
            ans1_3.tStart = t  # local t and not account for scr refresh
            ans1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_3, 'tStartRefresh')  # time at next scr refresh
            ans1_3.setAutoDraw(True)
        if ans1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans1_3.tStop = t  # not accounting for scr refresh
                ans1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans1_3, 'tStopRefresh')  # time at next scr refresh
                ans1_3.setAutoDraw(False)
        
        # *letter2_3* updates
        if letter2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_3.frameNStart = frameN  # exact frame index
            letter2_3.tStart = t  # local t and not account for scr refresh
            letter2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_3, 'tStartRefresh')  # time at next scr refresh
            letter2_3.setAutoDraw(True)
        if letter2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter2_3.tStop = t  # not accounting for scr refresh
                letter2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter2_3, 'tStopRefresh')  # time at next scr refresh
                letter2_3.setAutoDraw(False)
        
        # *ans2_3* updates
        if ans2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_3.frameNStart = frameN  # exact frame index
            ans2_3.tStart = t  # local t and not account for scr refresh
            ans2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_3, 'tStartRefresh')  # time at next scr refresh
            ans2_3.setAutoDraw(True)
        if ans2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans2_3.tStop = t  # not accounting for scr refresh
                ans2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans2_3, 'tStopRefresh')  # time at next scr refresh
                ans2_3.setAutoDraw(False)
        
        # *letter3_3* updates
        if letter3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_3.frameNStart = frameN  # exact frame index
            letter3_3.tStart = t  # local t and not account for scr refresh
            letter3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_3, 'tStartRefresh')  # time at next scr refresh
            letter3_3.setAutoDraw(True)
        if letter3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter3_3.tStop = t  # not accounting for scr refresh
                letter3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter3_3, 'tStopRefresh')  # time at next scr refresh
                letter3_3.setAutoDraw(False)
        
        # *ans3_3* updates
        if ans3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_3.frameNStart = frameN  # exact frame index
            ans3_3.tStart = t  # local t and not account for scr refresh
            ans3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_3, 'tStartRefresh')  # time at next scr refresh
            ans3_3.setAutoDraw(True)
        if ans3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans3_3.tStop = t  # not accounting for scr refresh
                ans3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans3_3, 'tStopRefresh')  # time at next scr refresh
                ans3_3.setAutoDraw(False)
        
        # *letter4_3* updates
        if letter4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_3.frameNStart = frameN  # exact frame index
            letter4_3.tStart = t  # local t and not account for scr refresh
            letter4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_3, 'tStartRefresh')  # time at next scr refresh
            letter4_3.setAutoDraw(True)
        if letter4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter4_3.tStop = t  # not accounting for scr refresh
                letter4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter4_3, 'tStopRefresh')  # time at next scr refresh
                letter4_3.setAutoDraw(False)
        
        # *ans4_3* updates
        if ans4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_3.frameNStart = frameN  # exact frame index
            ans4_3.tStart = t  # local t and not account for scr refresh
            ans4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_3, 'tStartRefresh')  # time at next scr refresh
            ans4_3.setAutoDraw(True)
        if ans4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans4_3.tStop = t  # not accounting for scr refresh
                ans4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans4_3, 'tStopRefresh')  # time at next scr refresh
                ans4_3.setAutoDraw(False)
        
        tempTheTime = typeIn1Clock.getTime() - countTheTime
        countTheTime = typeIn1Clock.getTime()
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pauseOne.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resp1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resp1"-------
    for thisComponent in resp1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pauseOne.addData('instructions_3.started', instructions_3.tStartRefresh)
    pauseOne.addData('instructions_3.stopped', instructions_3.tStopRefresh)
    pauseOne.addData('eqnDisp_3.started', eqnDisp_3.tStartRefresh)
    pauseOne.addData('eqnDisp_3.stopped', eqnDisp_3.tStopRefresh)
    pauseOne.addData('letter1_3.started', letter1_3.tStartRefresh)
    pauseOne.addData('letter1_3.stopped', letter1_3.tStopRefresh)
    pauseOne.addData('ans1_3.started', ans1_3.tStartRefresh)
    pauseOne.addData('ans1_3.stopped', ans1_3.tStopRefresh)
    pauseOne.addData('letter2_3.started', letter2_3.tStartRefresh)
    pauseOne.addData('letter2_3.stopped', letter2_3.tStopRefresh)
    pauseOne.addData('ans2_3.started', ans2_3.tStartRefresh)
    pauseOne.addData('ans2_3.stopped', ans2_3.tStopRefresh)
    pauseOne.addData('letter3_3.started', letter3_3.tStartRefresh)
    pauseOne.addData('letter3_3.stopped', letter3_3.tStopRefresh)
    pauseOne.addData('ans3_3.started', ans3_3.tStartRefresh)
    pauseOne.addData('ans3_3.stopped', ans3_3.tStopRefresh)
    pauseOne.addData('letter4_3.started', letter4_3.tStartRefresh)
    pauseOne.addData('letter4_3.stopped', letter4_3.tStopRefresh)
    pauseOne.addData('ans4_3.started', ans4_3.tStartRefresh)
    pauseOne.addData('ans4_3.stopped', ans4_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'pauseOne'

# get names of stimulus parameters
if pauseOne.trialList in ([], [None], None):
    params = []
else:
    params = pauseOne.trialList[0].keys()
# save data for this loop
pauseOne.saveAsExcel(filename + '.xlsx', sheetName='pauseOne',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "beforeTrial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
beforeTrialComponents = [text_2, key_resp_3]
for thisComponent in beforeTrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beforeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beforeTrial"-------
while continueRoutine:
    # get current time
    t = beforeTrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beforeTrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beforeTrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beforeTrial"-------
for thisComponent in beforeTrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "beforeTrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialList2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    word_2.setText(textTwo)
    # keep track of which components have finished
    trial2Components = [word_2]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_2* updates
        if word_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word_2.frameNStart = frameN  # exact frame index
            word_2.tStart = t  # local t and not account for scr refresh
            word_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_2, 'tStartRefresh')  # time at next scr refresh
            word_2.setAutoDraw(True)
        if word_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word_2.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                word_2.tStop = t  # not accounting for scr refresh
                word_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word_2, 'tStopRefresh')  # time at next scr refresh
                word_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('word_2.started', word_2.tStartRefresh)
    trials_2.addData('word_2.stopped', word_2.tStopRefresh)
# completed 2 repeats of 'trials_2'


# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "setTotalTime"-------
continueRoutine = True
# update component parameters for each repeat
totalTime = 0
tempTotal = 0
# keep track of which components have finished
setTotalTimeComponents = []
for thisComponent in setTotalTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setTotalTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setTotalTime"-------
while continueRoutine:
    # get current time
    t = setTotalTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setTotalTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setTotalTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setTotalTime"-------
for thisComponent in setTotalTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setTotalTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pause2 = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eqnTest.xlsx'),
    seed=None, name='pause2')
thisExp.addLoop(pause2)  # add the loop to the experiment
thisPause2 = pause2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPause2.rgb)
if thisPause2 != None:
    for paramName in thisPause2:
        exec('{} = thisPause2[paramName]'.format(paramName))

for thisPause2 in pause2:
    currentLoop = pause2
    # abbreviate parameter names if possible (e.g. rgb = thisPause2.rgb)
    if thisPause2 != None:
        for paramName in thisPause2:
            exec('{} = thisPause2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "typeIn2"-------
    continueRoutine = True
    # update component parameters for each repeat
    eqnDisp_2.setText(equationDisp)
    ans1_2.setText(answer1)
    ans2_2.setText(answ2)
    ans3_2.setText(answ3)
    ans4_2.setText(answ4)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    typeIn2Components = [instructions_2, eqnDisp_2, letter1_2, ans1_2, letter2_2, ans2_2, letter3_2, ans3_2, letter4_2, ans4_2, key_resp_4]
    for thisComponent in typeIn2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    typeIn2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "typeIn2"-------
    while continueRoutine:
        # get current time
        t = typeIn2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=typeIn2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_2* updates
        if instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_2.frameNStart = frameN  # exact frame index
            instructions_2.tStart = t  # local t and not account for scr refresh
            instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
            instructions_2.setAutoDraw(True)
        
        # *eqnDisp_2* updates
        if eqnDisp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_2.frameNStart = frameN  # exact frame index
            eqnDisp_2.tStart = t  # local t and not account for scr refresh
            eqnDisp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_2, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_2.setAutoDraw(True)
        
        # *letter1_2* updates
        if letter1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_2.frameNStart = frameN  # exact frame index
            letter1_2.tStart = t  # local t and not account for scr refresh
            letter1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_2, 'tStartRefresh')  # time at next scr refresh
            letter1_2.setAutoDraw(True)
        
        # *ans1_2* updates
        if ans1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_2.frameNStart = frameN  # exact frame index
            ans1_2.tStart = t  # local t and not account for scr refresh
            ans1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_2, 'tStartRefresh')  # time at next scr refresh
            ans1_2.setAutoDraw(True)
        
        # *letter2_2* updates
        if letter2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_2.frameNStart = frameN  # exact frame index
            letter2_2.tStart = t  # local t and not account for scr refresh
            letter2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_2, 'tStartRefresh')  # time at next scr refresh
            letter2_2.setAutoDraw(True)
        
        # *ans2_2* updates
        if ans2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_2.frameNStart = frameN  # exact frame index
            ans2_2.tStart = t  # local t and not account for scr refresh
            ans2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_2, 'tStartRefresh')  # time at next scr refresh
            ans2_2.setAutoDraw(True)
        
        # *letter3_2* updates
        if letter3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_2.frameNStart = frameN  # exact frame index
            letter3_2.tStart = t  # local t and not account for scr refresh
            letter3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_2, 'tStartRefresh')  # time at next scr refresh
            letter3_2.setAutoDraw(True)
        
        # *ans3_2* updates
        if ans3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_2.frameNStart = frameN  # exact frame index
            ans3_2.tStart = t  # local t and not account for scr refresh
            ans3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_2, 'tStartRefresh')  # time at next scr refresh
            ans3_2.setAutoDraw(True)
        
        # *letter4_2* updates
        if letter4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_2.frameNStart = frameN  # exact frame index
            letter4_2.tStart = t  # local t and not account for scr refresh
            letter4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_2, 'tStartRefresh')  # time at next scr refresh
            letter4_2.setAutoDraw(True)
        
        # *ans4_2* updates
        if ans4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_2.frameNStart = frameN  # exact frame index
            ans4_2.tStart = t  # local t and not account for scr refresh
            ans4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_2, 'tStartRefresh')  # time at next scr refresh
            ans4_2.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # was this correct?
                if (key_resp_4.keys == str(corrAns)) or (key_resp_4.keys == corrAns):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        tempTheTime = typeIn2Clock.getTime() - countTheTime
        countTheTime = typeIn2Clock.getTime()
        
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pause2.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in typeIn2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "typeIn2"-------
    for thisComponent in typeIn2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pause2.addData('instructions_2.started', instructions_2.tStartRefresh)
    pause2.addData('instructions_2.stopped', instructions_2.tStopRefresh)
    pause2.addData('eqnDisp_2.started', eqnDisp_2.tStartRefresh)
    pause2.addData('eqnDisp_2.stopped', eqnDisp_2.tStopRefresh)
    pause2.addData('letter1_2.started', letter1_2.tStartRefresh)
    pause2.addData('letter1_2.stopped', letter1_2.tStopRefresh)
    pause2.addData('ans1_2.started', ans1_2.tStartRefresh)
    pause2.addData('ans1_2.stopped', ans1_2.tStopRefresh)
    pause2.addData('letter2_2.started', letter2_2.tStartRefresh)
    pause2.addData('letter2_2.stopped', letter2_2.tStopRefresh)
    pause2.addData('ans2_2.started', ans2_2.tStartRefresh)
    pause2.addData('ans2_2.stopped', ans2_2.tStopRefresh)
    pause2.addData('letter3_2.started', letter3_2.tStartRefresh)
    pause2.addData('letter3_2.stopped', letter3_2.tStopRefresh)
    pause2.addData('ans3_2.started', ans3_2.tStartRefresh)
    pause2.addData('ans3_2.stopped', ans3_2.tStopRefresh)
    pause2.addData('letter4_2.started', letter4_2.tStartRefresh)
    pause2.addData('letter4_2.stopped', letter4_2.tStopRefresh)
    pause2.addData('ans4_2.started', ans4_2.tStartRefresh)
    pause2.addData('ans4_2.stopped', ans4_2.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for pause2 (TrialHandler)
    pause2.addData('key_resp_4.keys',key_resp_4.keys)
    pause2.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        pause2.addData('key_resp_4.rt', key_resp_4.rt)
    pause2.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    pause2.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "typeIn2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "checkResp2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    checkResp2Components = []
    for thisComponent in checkResp2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    checkResp2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "checkResp2"-------
    while continueRoutine:
        # get current time
        t = checkResp2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=checkResp2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if int(key_resp_4.keys) == int(corrAns):
            respColor = "green"
        elif key_resp_4.keys != corrAns:
            respColor = "red"
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in checkResp2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "checkResp2"-------
    for thisComponent in checkResp2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "checkResp2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "resp1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    eqnDisp_3.setColor(respColor, colorSpace='rgb')
    eqnDisp_3.setText(equationDisp)
    letter1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setText(answer1)
    letter2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setText(answ2)
    letter3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setText(answ3)
    letter4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setText(answ4)
    # keep track of which components have finished
    resp1Components = [instructions_3, eqnDisp_3, letter1_3, ans1_3, letter2_3, ans2_3, letter3_3, ans3_3, letter4_3, ans4_3]
    for thisComponent in resp1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resp1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resp1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = resp1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resp1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_3* updates
        if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_3.frameNStart = frameN  # exact frame index
            instructions_3.tStart = t  # local t and not account for scr refresh
            instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
            instructions_3.setAutoDraw(True)
        if instructions_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                instructions_3.tStop = t  # not accounting for scr refresh
                instructions_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructions_3, 'tStopRefresh')  # time at next scr refresh
                instructions_3.setAutoDraw(False)
        
        # *eqnDisp_3* updates
        if eqnDisp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_3.frameNStart = frameN  # exact frame index
            eqnDisp_3.tStart = t  # local t and not account for scr refresh
            eqnDisp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_3, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_3.setAutoDraw(True)
        if eqnDisp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eqnDisp_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eqnDisp_3.tStop = t  # not accounting for scr refresh
                eqnDisp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eqnDisp_3, 'tStopRefresh')  # time at next scr refresh
                eqnDisp_3.setAutoDraw(False)
        
        # *letter1_3* updates
        if letter1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_3.frameNStart = frameN  # exact frame index
            letter1_3.tStart = t  # local t and not account for scr refresh
            letter1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_3, 'tStartRefresh')  # time at next scr refresh
            letter1_3.setAutoDraw(True)
        if letter1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter1_3.tStop = t  # not accounting for scr refresh
                letter1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter1_3, 'tStopRefresh')  # time at next scr refresh
                letter1_3.setAutoDraw(False)
        
        # *ans1_3* updates
        if ans1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_3.frameNStart = frameN  # exact frame index
            ans1_3.tStart = t  # local t and not account for scr refresh
            ans1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_3, 'tStartRefresh')  # time at next scr refresh
            ans1_3.setAutoDraw(True)
        if ans1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans1_3.tStop = t  # not accounting for scr refresh
                ans1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans1_3, 'tStopRefresh')  # time at next scr refresh
                ans1_3.setAutoDraw(False)
        
        # *letter2_3* updates
        if letter2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_3.frameNStart = frameN  # exact frame index
            letter2_3.tStart = t  # local t and not account for scr refresh
            letter2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_3, 'tStartRefresh')  # time at next scr refresh
            letter2_3.setAutoDraw(True)
        if letter2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter2_3.tStop = t  # not accounting for scr refresh
                letter2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter2_3, 'tStopRefresh')  # time at next scr refresh
                letter2_3.setAutoDraw(False)
        
        # *ans2_3* updates
        if ans2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_3.frameNStart = frameN  # exact frame index
            ans2_3.tStart = t  # local t and not account for scr refresh
            ans2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_3, 'tStartRefresh')  # time at next scr refresh
            ans2_3.setAutoDraw(True)
        if ans2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans2_3.tStop = t  # not accounting for scr refresh
                ans2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans2_3, 'tStopRefresh')  # time at next scr refresh
                ans2_3.setAutoDraw(False)
        
        # *letter3_3* updates
        if letter3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_3.frameNStart = frameN  # exact frame index
            letter3_3.tStart = t  # local t and not account for scr refresh
            letter3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_3, 'tStartRefresh')  # time at next scr refresh
            letter3_3.setAutoDraw(True)
        if letter3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter3_3.tStop = t  # not accounting for scr refresh
                letter3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter3_3, 'tStopRefresh')  # time at next scr refresh
                letter3_3.setAutoDraw(False)
        
        # *ans3_3* updates
        if ans3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_3.frameNStart = frameN  # exact frame index
            ans3_3.tStart = t  # local t and not account for scr refresh
            ans3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_3, 'tStartRefresh')  # time at next scr refresh
            ans3_3.setAutoDraw(True)
        if ans3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans3_3.tStop = t  # not accounting for scr refresh
                ans3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans3_3, 'tStopRefresh')  # time at next scr refresh
                ans3_3.setAutoDraw(False)
        
        # *letter4_3* updates
        if letter4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_3.frameNStart = frameN  # exact frame index
            letter4_3.tStart = t  # local t and not account for scr refresh
            letter4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_3, 'tStartRefresh')  # time at next scr refresh
            letter4_3.setAutoDraw(True)
        if letter4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter4_3.tStop = t  # not accounting for scr refresh
                letter4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter4_3, 'tStopRefresh')  # time at next scr refresh
                letter4_3.setAutoDraw(False)
        
        # *ans4_3* updates
        if ans4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_3.frameNStart = frameN  # exact frame index
            ans4_3.tStart = t  # local t and not account for scr refresh
            ans4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_3, 'tStartRefresh')  # time at next scr refresh
            ans4_3.setAutoDraw(True)
        if ans4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans4_3.tStop = t  # not accounting for scr refresh
                ans4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans4_3, 'tStopRefresh')  # time at next scr refresh
                ans4_3.setAutoDraw(False)
        
        tempTheTime = typeIn1Clock.getTime() - countTheTime
        countTheTime = typeIn1Clock.getTime()
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pauseOne.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resp1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resp1"-------
    for thisComponent in resp1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pause2.addData('instructions_3.started', instructions_3.tStartRefresh)
    pause2.addData('instructions_3.stopped', instructions_3.tStopRefresh)
    pause2.addData('eqnDisp_3.started', eqnDisp_3.tStartRefresh)
    pause2.addData('eqnDisp_3.stopped', eqnDisp_3.tStopRefresh)
    pause2.addData('letter1_3.started', letter1_3.tStartRefresh)
    pause2.addData('letter1_3.stopped', letter1_3.tStopRefresh)
    pause2.addData('ans1_3.started', ans1_3.tStartRefresh)
    pause2.addData('ans1_3.stopped', ans1_3.tStopRefresh)
    pause2.addData('letter2_3.started', letter2_3.tStartRefresh)
    pause2.addData('letter2_3.stopped', letter2_3.tStopRefresh)
    pause2.addData('ans2_3.started', ans2_3.tStartRefresh)
    pause2.addData('ans2_3.stopped', ans2_3.tStopRefresh)
    pause2.addData('letter3_3.started', letter3_3.tStartRefresh)
    pause2.addData('letter3_3.stopped', letter3_3.tStopRefresh)
    pause2.addData('ans3_3.started', ans3_3.tStartRefresh)
    pause2.addData('ans3_3.stopped', ans3_3.tStopRefresh)
    pause2.addData('letter4_3.started', letter4_3.tStartRefresh)
    pause2.addData('letter4_3.stopped', letter4_3.tStopRefresh)
    pause2.addData('ans4_3.started', ans4_3.tStartRefresh)
    pause2.addData('ans4_3.stopped', ans4_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'pause2'

# get names of stimulus parameters
if pause2.trialList in ([], [None], None):
    params = []
else:
    params = pause2.trialList[0].keys()
# save data for this loop
pause2.saveAsExcel(filename + '.xlsx', sheetName='pause2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "beforeTrial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
beforeTrialComponents = [text_2, key_resp_3]
for thisComponent in beforeTrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beforeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beforeTrial"-------
while continueRoutine:
    # get current time
    t = beforeTrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beforeTrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beforeTrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beforeTrial"-------
for thisComponent in beforeTrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "beforeTrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialList3.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials3"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    word_3.setText(textThree)
    # keep track of which components have finished
    trials3Components = [word_3]
    for thisComponent in trials3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trials3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trials3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trials3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_3* updates
        if word_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word_3.frameNStart = frameN  # exact frame index
            word_3.tStart = t  # local t and not account for scr refresh
            word_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_3, 'tStartRefresh')  # time at next scr refresh
            word_3.setAutoDraw(True)
        if word_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word_3.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                word_3.tStop = t  # not accounting for scr refresh
                word_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word_3, 'tStopRefresh')  # time at next scr refresh
                word_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials3"-------
    for thisComponent in trials3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('word_3.started', word_3.tStartRefresh)
    trials_3.addData('word_3.stopped', word_3.tStopRefresh)
# completed 2 repeats of 'trials_3'


# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "setTotalTime"-------
continueRoutine = True
# update component parameters for each repeat
totalTime = 0
tempTotal = 0
# keep track of which components have finished
setTotalTimeComponents = []
for thisComponent in setTotalTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setTotalTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setTotalTime"-------
while continueRoutine:
    # get current time
    t = setTotalTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setTotalTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setTotalTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setTotalTime"-------
for thisComponent in setTotalTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setTotalTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pause3 = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eqnTest.xlsx'),
    seed=None, name='pause3')
thisExp.addLoop(pause3)  # add the loop to the experiment
thisPause3 = pause3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPause3.rgb)
if thisPause3 != None:
    for paramName in thisPause3:
        exec('{} = thisPause3[paramName]'.format(paramName))

for thisPause3 in pause3:
    currentLoop = pause3
    # abbreviate parameter names if possible (e.g. rgb = thisPause3.rgb)
    if thisPause3 != None:
        for paramName in thisPause3:
            exec('{} = thisPause3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "typeIn3"-------
    continueRoutine = True
    # update component parameters for each repeat
    eqnDisp_4.setText(equationDisp)
    ans1_4.setText(answer1)
    ans2_4.setText(answ2)
    ans3_4.setText(answ3)
    ans4_4.setText(answ4)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    typeIn3Components = [instructions_4, eqnDisp_4, letter1_4, ans1_4, letter2_4, ans2_4, letter3_4, ans3_4, letter4_4, ans4_4, key_resp_5]
    for thisComponent in typeIn3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    typeIn3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "typeIn3"-------
    while continueRoutine:
        # get current time
        t = typeIn3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=typeIn3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_4* updates
        if instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_4.frameNStart = frameN  # exact frame index
            instructions_4.tStart = t  # local t and not account for scr refresh
            instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_4, 'tStartRefresh')  # time at next scr refresh
            instructions_4.setAutoDraw(True)
        
        # *eqnDisp_4* updates
        if eqnDisp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_4.frameNStart = frameN  # exact frame index
            eqnDisp_4.tStart = t  # local t and not account for scr refresh
            eqnDisp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_4, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_4.setAutoDraw(True)
        
        # *letter1_4* updates
        if letter1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_4.frameNStart = frameN  # exact frame index
            letter1_4.tStart = t  # local t and not account for scr refresh
            letter1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_4, 'tStartRefresh')  # time at next scr refresh
            letter1_4.setAutoDraw(True)
        
        # *ans1_4* updates
        if ans1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_4.frameNStart = frameN  # exact frame index
            ans1_4.tStart = t  # local t and not account for scr refresh
            ans1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_4, 'tStartRefresh')  # time at next scr refresh
            ans1_4.setAutoDraw(True)
        
        # *letter2_4* updates
        if letter2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_4.frameNStart = frameN  # exact frame index
            letter2_4.tStart = t  # local t and not account for scr refresh
            letter2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_4, 'tStartRefresh')  # time at next scr refresh
            letter2_4.setAutoDraw(True)
        
        # *ans2_4* updates
        if ans2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_4.frameNStart = frameN  # exact frame index
            ans2_4.tStart = t  # local t and not account for scr refresh
            ans2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_4, 'tStartRefresh')  # time at next scr refresh
            ans2_4.setAutoDraw(True)
        
        # *letter3_4* updates
        if letter3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_4.frameNStart = frameN  # exact frame index
            letter3_4.tStart = t  # local t and not account for scr refresh
            letter3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_4, 'tStartRefresh')  # time at next scr refresh
            letter3_4.setAutoDraw(True)
        
        # *ans3_4* updates
        if ans3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_4.frameNStart = frameN  # exact frame index
            ans3_4.tStart = t  # local t and not account for scr refresh
            ans3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_4, 'tStartRefresh')  # time at next scr refresh
            ans3_4.setAutoDraw(True)
        
        # *letter4_4* updates
        if letter4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_4.frameNStart = frameN  # exact frame index
            letter4_4.tStart = t  # local t and not account for scr refresh
            letter4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_4, 'tStartRefresh')  # time at next scr refresh
            letter4_4.setAutoDraw(True)
        
        # *ans4_4* updates
        if ans4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_4.frameNStart = frameN  # exact frame index
            ans4_4.tStart = t  # local t and not account for scr refresh
            ans4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_4, 'tStartRefresh')  # time at next scr refresh
            ans4_4.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # was this correct?
                if (key_resp_5.keys == str(corrAns)) or (key_resp_5.keys == corrAns):
                    key_resp_5.corr = 1
                else:
                    key_resp_5.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        tempTheTime = typeIn3Clock.getTime() - countTheTime
        countTheTime = typeIn3Clock.getTime()
        
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pause3.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in typeIn3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "typeIn3"-------
    for thisComponent in typeIn3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pause3.addData('instructions_4.started', instructions_4.tStartRefresh)
    pause3.addData('instructions_4.stopped', instructions_4.tStopRefresh)
    pause3.addData('eqnDisp_4.started', eqnDisp_4.tStartRefresh)
    pause3.addData('eqnDisp_4.stopped', eqnDisp_4.tStopRefresh)
    pause3.addData('letter1_4.started', letter1_4.tStartRefresh)
    pause3.addData('letter1_4.stopped', letter1_4.tStopRefresh)
    pause3.addData('ans1_4.started', ans1_4.tStartRefresh)
    pause3.addData('ans1_4.stopped', ans1_4.tStopRefresh)
    pause3.addData('letter2_4.started', letter2_4.tStartRefresh)
    pause3.addData('letter2_4.stopped', letter2_4.tStopRefresh)
    pause3.addData('ans2_4.started', ans2_4.tStartRefresh)
    pause3.addData('ans2_4.stopped', ans2_4.tStopRefresh)
    pause3.addData('letter3_4.started', letter3_4.tStartRefresh)
    pause3.addData('letter3_4.stopped', letter3_4.tStopRefresh)
    pause3.addData('ans3_4.started', ans3_4.tStartRefresh)
    pause3.addData('ans3_4.stopped', ans3_4.tStopRefresh)
    pause3.addData('letter4_4.started', letter4_4.tStartRefresh)
    pause3.addData('letter4_4.stopped', letter4_4.tStopRefresh)
    pause3.addData('ans4_4.started', ans4_4.tStartRefresh)
    pause3.addData('ans4_4.stopped', ans4_4.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_5.corr = 1;  # correct non-response
        else:
           key_resp_5.corr = 0;  # failed to respond (incorrectly)
    # store data for pause3 (TrialHandler)
    pause3.addData('key_resp_5.keys',key_resp_5.keys)
    pause3.addData('key_resp_5.corr', key_resp_5.corr)
    if key_resp_5.keys != None:  # we had a response
        pause3.addData('key_resp_5.rt', key_resp_5.rt)
    pause3.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    pause3.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "typeIn3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "checkResp3"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    checkResp3Components = []
    for thisComponent in checkResp3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    checkResp3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "checkResp3"-------
    while continueRoutine:
        # get current time
        t = checkResp3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=checkResp3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if int(key_resp_5.keys) == int(corrAns):
            respColor = "green"
        elif key_resp_5.keys != corrAns:
            respColor = "red"
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in checkResp3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "checkResp3"-------
    for thisComponent in checkResp3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "checkResp3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "resp1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    eqnDisp_3.setColor(respColor, colorSpace='rgb')
    eqnDisp_3.setText(equationDisp)
    letter1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setText(answer1)
    letter2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setText(answ2)
    letter3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setText(answ3)
    letter4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setText(answ4)
    # keep track of which components have finished
    resp1Components = [instructions_3, eqnDisp_3, letter1_3, ans1_3, letter2_3, ans2_3, letter3_3, ans3_3, letter4_3, ans4_3]
    for thisComponent in resp1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resp1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resp1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = resp1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resp1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_3* updates
        if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_3.frameNStart = frameN  # exact frame index
            instructions_3.tStart = t  # local t and not account for scr refresh
            instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
            instructions_3.setAutoDraw(True)
        if instructions_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                instructions_3.tStop = t  # not accounting for scr refresh
                instructions_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructions_3, 'tStopRefresh')  # time at next scr refresh
                instructions_3.setAutoDraw(False)
        
        # *eqnDisp_3* updates
        if eqnDisp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_3.frameNStart = frameN  # exact frame index
            eqnDisp_3.tStart = t  # local t and not account for scr refresh
            eqnDisp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_3, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_3.setAutoDraw(True)
        if eqnDisp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eqnDisp_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eqnDisp_3.tStop = t  # not accounting for scr refresh
                eqnDisp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eqnDisp_3, 'tStopRefresh')  # time at next scr refresh
                eqnDisp_3.setAutoDraw(False)
        
        # *letter1_3* updates
        if letter1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_3.frameNStart = frameN  # exact frame index
            letter1_3.tStart = t  # local t and not account for scr refresh
            letter1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_3, 'tStartRefresh')  # time at next scr refresh
            letter1_3.setAutoDraw(True)
        if letter1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter1_3.tStop = t  # not accounting for scr refresh
                letter1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter1_3, 'tStopRefresh')  # time at next scr refresh
                letter1_3.setAutoDraw(False)
        
        # *ans1_3* updates
        if ans1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_3.frameNStart = frameN  # exact frame index
            ans1_3.tStart = t  # local t and not account for scr refresh
            ans1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_3, 'tStartRefresh')  # time at next scr refresh
            ans1_3.setAutoDraw(True)
        if ans1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans1_3.tStop = t  # not accounting for scr refresh
                ans1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans1_3, 'tStopRefresh')  # time at next scr refresh
                ans1_3.setAutoDraw(False)
        
        # *letter2_3* updates
        if letter2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_3.frameNStart = frameN  # exact frame index
            letter2_3.tStart = t  # local t and not account for scr refresh
            letter2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_3, 'tStartRefresh')  # time at next scr refresh
            letter2_3.setAutoDraw(True)
        if letter2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter2_3.tStop = t  # not accounting for scr refresh
                letter2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter2_3, 'tStopRefresh')  # time at next scr refresh
                letter2_3.setAutoDraw(False)
        
        # *ans2_3* updates
        if ans2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_3.frameNStart = frameN  # exact frame index
            ans2_3.tStart = t  # local t and not account for scr refresh
            ans2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_3, 'tStartRefresh')  # time at next scr refresh
            ans2_3.setAutoDraw(True)
        if ans2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans2_3.tStop = t  # not accounting for scr refresh
                ans2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans2_3, 'tStopRefresh')  # time at next scr refresh
                ans2_3.setAutoDraw(False)
        
        # *letter3_3* updates
        if letter3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_3.frameNStart = frameN  # exact frame index
            letter3_3.tStart = t  # local t and not account for scr refresh
            letter3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_3, 'tStartRefresh')  # time at next scr refresh
            letter3_3.setAutoDraw(True)
        if letter3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter3_3.tStop = t  # not accounting for scr refresh
                letter3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter3_3, 'tStopRefresh')  # time at next scr refresh
                letter3_3.setAutoDraw(False)
        
        # *ans3_3* updates
        if ans3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_3.frameNStart = frameN  # exact frame index
            ans3_3.tStart = t  # local t and not account for scr refresh
            ans3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_3, 'tStartRefresh')  # time at next scr refresh
            ans3_3.setAutoDraw(True)
        if ans3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans3_3.tStop = t  # not accounting for scr refresh
                ans3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans3_3, 'tStopRefresh')  # time at next scr refresh
                ans3_3.setAutoDraw(False)
        
        # *letter4_3* updates
        if letter4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_3.frameNStart = frameN  # exact frame index
            letter4_3.tStart = t  # local t and not account for scr refresh
            letter4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_3, 'tStartRefresh')  # time at next scr refresh
            letter4_3.setAutoDraw(True)
        if letter4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter4_3.tStop = t  # not accounting for scr refresh
                letter4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter4_3, 'tStopRefresh')  # time at next scr refresh
                letter4_3.setAutoDraw(False)
        
        # *ans4_3* updates
        if ans4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_3.frameNStart = frameN  # exact frame index
            ans4_3.tStart = t  # local t and not account for scr refresh
            ans4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_3, 'tStartRefresh')  # time at next scr refresh
            ans4_3.setAutoDraw(True)
        if ans4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans4_3.tStop = t  # not accounting for scr refresh
                ans4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans4_3, 'tStopRefresh')  # time at next scr refresh
                ans4_3.setAutoDraw(False)
        
        tempTheTime = typeIn1Clock.getTime() - countTheTime
        countTheTime = typeIn1Clock.getTime()
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pauseOne.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resp1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resp1"-------
    for thisComponent in resp1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pause3.addData('instructions_3.started', instructions_3.tStartRefresh)
    pause3.addData('instructions_3.stopped', instructions_3.tStopRefresh)
    pause3.addData('eqnDisp_3.started', eqnDisp_3.tStartRefresh)
    pause3.addData('eqnDisp_3.stopped', eqnDisp_3.tStopRefresh)
    pause3.addData('letter1_3.started', letter1_3.tStartRefresh)
    pause3.addData('letter1_3.stopped', letter1_3.tStopRefresh)
    pause3.addData('ans1_3.started', ans1_3.tStartRefresh)
    pause3.addData('ans1_3.stopped', ans1_3.tStopRefresh)
    pause3.addData('letter2_3.started', letter2_3.tStartRefresh)
    pause3.addData('letter2_3.stopped', letter2_3.tStopRefresh)
    pause3.addData('ans2_3.started', ans2_3.tStartRefresh)
    pause3.addData('ans2_3.stopped', ans2_3.tStopRefresh)
    pause3.addData('letter3_3.started', letter3_3.tStartRefresh)
    pause3.addData('letter3_3.stopped', letter3_3.tStopRefresh)
    pause3.addData('ans3_3.started', ans3_3.tStartRefresh)
    pause3.addData('ans3_3.stopped', ans3_3.tStopRefresh)
    pause3.addData('letter4_3.started', letter4_3.tStartRefresh)
    pause3.addData('letter4_3.stopped', letter4_3.tStopRefresh)
    pause3.addData('ans4_3.started', ans4_3.tStartRefresh)
    pause3.addData('ans4_3.stopped', ans4_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'pause3'

# get names of stimulus parameters
if pause3.trialList in ([], [None], None):
    params = []
else:
    params = pause3.trialList[0].keys()
# save data for this loop
pause3.saveAsExcel(filename + '.xlsx', sheetName='pause3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "beforeTrial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
beforeTrialComponents = [text_2, key_resp_3]
for thisComponent in beforeTrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beforeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beforeTrial"-------
while continueRoutine:
    # get current time
    t = beforeTrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beforeTrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beforeTrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beforeTrial"-------
for thisComponent in beforeTrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "beforeTrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# set up handler to look after randomisation of conditions etc
trials4 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialList4.xlsx'),
    seed=None, name='trials4')
thisExp.addLoop(trials4)  # add the loop to the experiment
thisTrials4 = trials4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
if thisTrials4 != None:
    for paramName in thisTrials4:
        exec('{} = thisTrials4[paramName]'.format(paramName))

for thisTrials4 in trials4:
    currentLoop = trials4
    # abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
    if thisTrials4 != None:
        for paramName in thisTrials4:
            exec('{} = thisTrials4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials_4"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    text_4.setText(textFour)
    # keep track of which components have finished
    trials_4Components = [text_4]
    for thisComponent in trials_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trials_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trials_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trials_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials_4"-------
    for thisComponent in trials_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials4.addData('text_4.started', text_4.tStartRefresh)
    trials4.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials4'

# get names of stimulus parameters
if trials4.trialList in ([], [None], None):
    params = []
else:
    params = trials4.trialList[0].keys()
# save data for this loop
trials4.saveAsExcel(filename + '.xlsx', sheetName='trials4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "setTotalTime"-------
continueRoutine = True
# update component parameters for each repeat
totalTime = 0
tempTotal = 0
# keep track of which components have finished
setTotalTimeComponents = []
for thisComponent in setTotalTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setTotalTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setTotalTime"-------
while continueRoutine:
    # get current time
    t = setTotalTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setTotalTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setTotalTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setTotalTime"-------
for thisComponent in setTotalTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setTotalTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pause4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eqnTest.xlsx'),
    seed=None, name='pause4')
thisExp.addLoop(pause4)  # add the loop to the experiment
thisPause4 = pause4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPause4.rgb)
if thisPause4 != None:
    for paramName in thisPause4:
        exec('{} = thisPause4[paramName]'.format(paramName))

for thisPause4 in pause4:
    currentLoop = pause4
    # abbreviate parameter names if possible (e.g. rgb = thisPause4.rgb)
    if thisPause4 != None:
        for paramName in thisPause4:
            exec('{} = thisPause4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "typeIn4"-------
    continueRoutine = True
    # update component parameters for each repeat
    eqnDisp_5.setText(equationDisp)
    ans1_5.setText(answer1)
    ans2_5.setText(answ2)
    ans3_5.setText(answ3)
    ans4_5.setText(answ4)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    typeIn4Components = [instructions_5, eqnDisp_5, letter1_5, ans1_5, letter2_5, ans2_5, letter3_5, ans3_5, letter4_5, ans4_5, key_resp_7]
    for thisComponent in typeIn4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    typeIn4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "typeIn4"-------
    while continueRoutine:
        # get current time
        t = typeIn4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=typeIn4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_5* updates
        if instructions_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_5.frameNStart = frameN  # exact frame index
            instructions_5.tStart = t  # local t and not account for scr refresh
            instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_5, 'tStartRefresh')  # time at next scr refresh
            instructions_5.setAutoDraw(True)
        
        # *eqnDisp_5* updates
        if eqnDisp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_5.frameNStart = frameN  # exact frame index
            eqnDisp_5.tStart = t  # local t and not account for scr refresh
            eqnDisp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_5, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_5.setAutoDraw(True)
        
        # *letter1_5* updates
        if letter1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_5.frameNStart = frameN  # exact frame index
            letter1_5.tStart = t  # local t and not account for scr refresh
            letter1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_5, 'tStartRefresh')  # time at next scr refresh
            letter1_5.setAutoDraw(True)
        
        # *ans1_5* updates
        if ans1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_5.frameNStart = frameN  # exact frame index
            ans1_5.tStart = t  # local t and not account for scr refresh
            ans1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_5, 'tStartRefresh')  # time at next scr refresh
            ans1_5.setAutoDraw(True)
        
        # *letter2_5* updates
        if letter2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_5.frameNStart = frameN  # exact frame index
            letter2_5.tStart = t  # local t and not account for scr refresh
            letter2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_5, 'tStartRefresh')  # time at next scr refresh
            letter2_5.setAutoDraw(True)
        
        # *ans2_5* updates
        if ans2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_5.frameNStart = frameN  # exact frame index
            ans2_5.tStart = t  # local t and not account for scr refresh
            ans2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_5, 'tStartRefresh')  # time at next scr refresh
            ans2_5.setAutoDraw(True)
        
        # *letter3_5* updates
        if letter3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_5.frameNStart = frameN  # exact frame index
            letter3_5.tStart = t  # local t and not account for scr refresh
            letter3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_5, 'tStartRefresh')  # time at next scr refresh
            letter3_5.setAutoDraw(True)
        
        # *ans3_5* updates
        if ans3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_5.frameNStart = frameN  # exact frame index
            ans3_5.tStart = t  # local t and not account for scr refresh
            ans3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_5, 'tStartRefresh')  # time at next scr refresh
            ans3_5.setAutoDraw(True)
        
        # *letter4_5* updates
        if letter4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_5.frameNStart = frameN  # exact frame index
            letter4_5.tStart = t  # local t and not account for scr refresh
            letter4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_5, 'tStartRefresh')  # time at next scr refresh
            letter4_5.setAutoDraw(True)
        
        # *ans4_5* updates
        if ans4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_5.frameNStart = frameN  # exact frame index
            ans4_5.tStart = t  # local t and not account for scr refresh
            ans4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_5, 'tStartRefresh')  # time at next scr refresh
            ans4_5.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # was this correct?
                if (key_resp_7.keys == str(corrAns)) or (key_resp_7.keys == corrAns):
                    key_resp_7.corr = 1
                else:
                    key_resp_7.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        tempTheTime = typeIn4Clock.getTime() - countTheTime
        countTheTime = typeIn4Clock.getTime()
        
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pause4.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in typeIn4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "typeIn4"-------
    for thisComponent in typeIn4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pause4.addData('instructions_5.started', instructions_5.tStartRefresh)
    pause4.addData('instructions_5.stopped', instructions_5.tStopRefresh)
    pause4.addData('eqnDisp_5.started', eqnDisp_5.tStartRefresh)
    pause4.addData('eqnDisp_5.stopped', eqnDisp_5.tStopRefresh)
    pause4.addData('letter1_5.started', letter1_5.tStartRefresh)
    pause4.addData('letter1_5.stopped', letter1_5.tStopRefresh)
    pause4.addData('ans1_5.started', ans1_5.tStartRefresh)
    pause4.addData('ans1_5.stopped', ans1_5.tStopRefresh)
    pause4.addData('letter2_5.started', letter2_5.tStartRefresh)
    pause4.addData('letter2_5.stopped', letter2_5.tStopRefresh)
    pause4.addData('ans2_5.started', ans2_5.tStartRefresh)
    pause4.addData('ans2_5.stopped', ans2_5.tStopRefresh)
    pause4.addData('letter3_5.started', letter3_5.tStartRefresh)
    pause4.addData('letter3_5.stopped', letter3_5.tStopRefresh)
    pause4.addData('ans3_5.started', ans3_5.tStartRefresh)
    pause4.addData('ans3_5.stopped', ans3_5.tStopRefresh)
    pause4.addData('letter4_5.started', letter4_5.tStartRefresh)
    pause4.addData('letter4_5.stopped', letter4_5.tStopRefresh)
    pause4.addData('ans4_5.started', ans4_5.tStartRefresh)
    pause4.addData('ans4_5.stopped', ans4_5.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_7.corr = 1;  # correct non-response
        else:
           key_resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for pause4 (TrialHandler)
    pause4.addData('key_resp_7.keys',key_resp_7.keys)
    pause4.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        pause4.addData('key_resp_7.rt', key_resp_7.rt)
    pause4.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    pause4.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "typeIn4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "checkResp4"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    checkResp4Components = []
    for thisComponent in checkResp4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    checkResp4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "checkResp4"-------
    while continueRoutine:
        # get current time
        t = checkResp4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=checkResp4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if int(key_resp_5.keys) == int(corrAns):
            respColor = "green"
        elif key_resp_5.keys != corrAns:
            respColor = "red"
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in checkResp4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "checkResp4"-------
    for thisComponent in checkResp4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "checkResp4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "resp1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    eqnDisp_3.setColor(respColor, colorSpace='rgb')
    eqnDisp_3.setText(equationDisp)
    letter1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setColor(color1, colorSpace='rgb')
    ans1_3.setText(answer1)
    letter2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setColor(color2, colorSpace='rgb')
    ans2_3.setText(answ2)
    letter3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setColor(color3, colorSpace='rgb')
    ans3_3.setText(answ3)
    letter4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setColor(color4, colorSpace='rgb')
    ans4_3.setText(answ4)
    # keep track of which components have finished
    resp1Components = [instructions_3, eqnDisp_3, letter1_3, ans1_3, letter2_3, ans2_3, letter3_3, ans3_3, letter4_3, ans4_3]
    for thisComponent in resp1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resp1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resp1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = resp1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resp1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_3* updates
        if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_3.frameNStart = frameN  # exact frame index
            instructions_3.tStart = t  # local t and not account for scr refresh
            instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
            instructions_3.setAutoDraw(True)
        if instructions_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                instructions_3.tStop = t  # not accounting for scr refresh
                instructions_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructions_3, 'tStopRefresh')  # time at next scr refresh
                instructions_3.setAutoDraw(False)
        
        # *eqnDisp_3* updates
        if eqnDisp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eqnDisp_3.frameNStart = frameN  # exact frame index
            eqnDisp_3.tStart = t  # local t and not account for scr refresh
            eqnDisp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eqnDisp_3, 'tStartRefresh')  # time at next scr refresh
            eqnDisp_3.setAutoDraw(True)
        if eqnDisp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eqnDisp_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eqnDisp_3.tStop = t  # not accounting for scr refresh
                eqnDisp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eqnDisp_3, 'tStopRefresh')  # time at next scr refresh
                eqnDisp_3.setAutoDraw(False)
        
        # *letter1_3* updates
        if letter1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter1_3.frameNStart = frameN  # exact frame index
            letter1_3.tStart = t  # local t and not account for scr refresh
            letter1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter1_3, 'tStartRefresh')  # time at next scr refresh
            letter1_3.setAutoDraw(True)
        if letter1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter1_3.tStop = t  # not accounting for scr refresh
                letter1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter1_3, 'tStopRefresh')  # time at next scr refresh
                letter1_3.setAutoDraw(False)
        
        # *ans1_3* updates
        if ans1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans1_3.frameNStart = frameN  # exact frame index
            ans1_3.tStart = t  # local t and not account for scr refresh
            ans1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans1_3, 'tStartRefresh')  # time at next scr refresh
            ans1_3.setAutoDraw(True)
        if ans1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans1_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans1_3.tStop = t  # not accounting for scr refresh
                ans1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans1_3, 'tStopRefresh')  # time at next scr refresh
                ans1_3.setAutoDraw(False)
        
        # *letter2_3* updates
        if letter2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter2_3.frameNStart = frameN  # exact frame index
            letter2_3.tStart = t  # local t and not account for scr refresh
            letter2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter2_3, 'tStartRefresh')  # time at next scr refresh
            letter2_3.setAutoDraw(True)
        if letter2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter2_3.tStop = t  # not accounting for scr refresh
                letter2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter2_3, 'tStopRefresh')  # time at next scr refresh
                letter2_3.setAutoDraw(False)
        
        # *ans2_3* updates
        if ans2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans2_3.frameNStart = frameN  # exact frame index
            ans2_3.tStart = t  # local t and not account for scr refresh
            ans2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans2_3, 'tStartRefresh')  # time at next scr refresh
            ans2_3.setAutoDraw(True)
        if ans2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans2_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans2_3.tStop = t  # not accounting for scr refresh
                ans2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans2_3, 'tStopRefresh')  # time at next scr refresh
                ans2_3.setAutoDraw(False)
        
        # *letter3_3* updates
        if letter3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter3_3.frameNStart = frameN  # exact frame index
            letter3_3.tStart = t  # local t and not account for scr refresh
            letter3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter3_3, 'tStartRefresh')  # time at next scr refresh
            letter3_3.setAutoDraw(True)
        if letter3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter3_3.tStop = t  # not accounting for scr refresh
                letter3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter3_3, 'tStopRefresh')  # time at next scr refresh
                letter3_3.setAutoDraw(False)
        
        # *ans3_3* updates
        if ans3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans3_3.frameNStart = frameN  # exact frame index
            ans3_3.tStart = t  # local t and not account for scr refresh
            ans3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans3_3, 'tStartRefresh')  # time at next scr refresh
            ans3_3.setAutoDraw(True)
        if ans3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans3_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans3_3.tStop = t  # not accounting for scr refresh
                ans3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans3_3, 'tStopRefresh')  # time at next scr refresh
                ans3_3.setAutoDraw(False)
        
        # *letter4_3* updates
        if letter4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letter4_3.frameNStart = frameN  # exact frame index
            letter4_3.tStart = t  # local t and not account for scr refresh
            letter4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter4_3, 'tStartRefresh')  # time at next scr refresh
            letter4_3.setAutoDraw(True)
        if letter4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letter4_3.tStop = t  # not accounting for scr refresh
                letter4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letter4_3, 'tStopRefresh')  # time at next scr refresh
                letter4_3.setAutoDraw(False)
        
        # *ans4_3* updates
        if ans4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ans4_3.frameNStart = frameN  # exact frame index
            ans4_3.tStart = t  # local t and not account for scr refresh
            ans4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans4_3, 'tStartRefresh')  # time at next scr refresh
            ans4_3.setAutoDraw(True)
        if ans4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ans4_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ans4_3.tStop = t  # not accounting for scr refresh
                ans4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ans4_3, 'tStopRefresh')  # time at next scr refresh
                ans4_3.setAutoDraw(False)
        
        tempTheTime = typeIn1Clock.getTime() - countTheTime
        countTheTime = typeIn1Clock.getTime()
        
        
        if tempTheTime>0:
            tempTotal = totalTime + tempTheTime
        else:
            tempTotal = tempTotal
        
        totalTime = tempTotal
        
        
        if totalTime>= 9:
            pauseOne.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resp1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resp1"-------
    for thisComponent in resp1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pause4.addData('instructions_3.started', instructions_3.tStartRefresh)
    pause4.addData('instructions_3.stopped', instructions_3.tStopRefresh)
    pause4.addData('eqnDisp_3.started', eqnDisp_3.tStartRefresh)
    pause4.addData('eqnDisp_3.stopped', eqnDisp_3.tStopRefresh)
    pause4.addData('letter1_3.started', letter1_3.tStartRefresh)
    pause4.addData('letter1_3.stopped', letter1_3.tStopRefresh)
    pause4.addData('ans1_3.started', ans1_3.tStartRefresh)
    pause4.addData('ans1_3.stopped', ans1_3.tStopRefresh)
    pause4.addData('letter2_3.started', letter2_3.tStartRefresh)
    pause4.addData('letter2_3.stopped', letter2_3.tStopRefresh)
    pause4.addData('ans2_3.started', ans2_3.tStartRefresh)
    pause4.addData('ans2_3.stopped', ans2_3.tStopRefresh)
    pause4.addData('letter3_3.started', letter3_3.tStartRefresh)
    pause4.addData('letter3_3.stopped', letter3_3.tStopRefresh)
    pause4.addData('ans3_3.started', ans3_3.tStartRefresh)
    pause4.addData('ans3_3.stopped', ans3_3.tStopRefresh)
    pause4.addData('letter4_3.started', letter4_3.tStartRefresh)
    pause4.addData('letter4_3.stopped', letter4_3.tStopRefresh)
    pause4.addData('ans4_3.started', ans4_3.tStartRefresh)
    pause4.addData('ans4_3.stopped', ans4_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'pause4'

# get names of stimulus parameters
if pause4.trialList in ([], [None], None):
    params = []
else:
    params = pause4.trialList[0].keys()
# save data for this loop
pause4.saveAsExcel(filename + '.xlsx', sheetName='pause4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "btwnTrialResp"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
btwnTrialRespComponents = [ISI_4]
for thisComponent in btwnTrialRespComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwnTrialRespClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwnTrialResp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwnTrialRespClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwnTrialRespClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_4* period
    if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_4.frameNStart = frameN  # exact frame index
        ISI_4.tStart = t  # local t and not account for scr refresh
        ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
        ISI_4.start(0.5)
    elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
        ISI_4.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwnTrialRespComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwnTrialResp"-------
for thisComponent in btwnTrialRespComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_4.started', ISI_4.tStart)
thisExp.addData('ISI_4.stopped', ISI_4.tStop)

# ------Prepare to start Routine "instr2"-------
continueRoutine = True
# update component parameters for each repeat
endInstr.keys = []
endInstr.rt = []
_endInstr_allKeys = []
# keep track of which components have finished
instr2Components = [instrPart2, endInstr]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrPart2* updates
    if instrPart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrPart2.frameNStart = frameN  # exact frame index
        instrPart2.tStart = t  # local t and not account for scr refresh
        instrPart2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrPart2, 'tStartRefresh')  # time at next scr refresh
        instrPart2.setAutoDraw(True)
    
    # *endInstr* updates
    waitOnFlip = False
    if endInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endInstr.frameNStart = frameN  # exact frame index
        endInstr.tStart = t  # local t and not account for scr refresh
        endInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endInstr, 'tStartRefresh')  # time at next scr refresh
        endInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endInstr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endInstr.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            endInstr.tStop = t  # not accounting for scr refresh
            endInstr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endInstr, 'tStopRefresh')  # time at next scr refresh
            endInstr.status = FINISHED
    if endInstr.status == STARTED and not waitOnFlip:
        theseKeys = endInstr.getKeys(keyList=None, waitRelease=False)
        _endInstr_allKeys.extend(theseKeys)
        if len(_endInstr_allKeys):
            endInstr.keys = _endInstr_allKeys[-1].name  # just the last key pressed
            endInstr.rt = _endInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrPart2.started', instrPart2.tStartRefresh)
thisExp.addData('instrPart2.stopped', instrPart2.tStopRefresh)
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
testLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('testingList.xlsx'),
    seed=None, name='testLoop')
thisExp.addLoop(testLoop)  # add the loop to the experiment
thisTestLoop = testLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTestLoop.rgb)
if thisTestLoop != None:
    for paramName in thisTestLoop:
        exec('{} = thisTestLoop[paramName]'.format(paramName))

for thisTestLoop in testLoop:
    currentLoop = testLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTestLoop.rgb)
    if thisTestLoop != None:
        for paramName in thisTestLoop:
            exec('{} = thisTestLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testRoutine"-------
    continueRoutine = True
    # update component parameters for each repeat
    testText.setText(word)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    testRoutineComponents = [testText, key_resp_6, text_3]
    for thisComponent in testRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testRoutine"-------
    while continueRoutine:
        # get current time
        t = testRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testText* updates
        if testText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testText.frameNStart = frameN  # exact frame index
            testText.tStart = t  # local t and not account for scr refresh
            testText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testText, 'tStartRefresh')  # time at next scr refresh
            testText.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['m', 'z'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # was this correct?
                if (key_resp_6.keys == str(response)) or (key_resp_6.keys == response):
                    key_resp_6.corr = 1
                else:
                    key_resp_6.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testRoutine"-------
    for thisComponent in testRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    testLoop.addData('testText.started', testText.tStartRefresh)
    testLoop.addData('testText.stopped', testText.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
        # was no response the correct answer?!
        if str(response).lower() == 'none':
           key_resp_6.corr = 1;  # correct non-response
        else:
           key_resp_6.corr = 0;  # failed to respond (incorrectly)
    # store data for testLoop (TrialHandler)
    testLoop.addData('key_resp_6.keys',key_resp_6.keys)
    testLoop.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.keys != None:  # we had a response
        testLoop.addData('key_resp_6.rt', key_resp_6.rt)
    testLoop.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    testLoop.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    testLoop.addData('text_3.started', text_3.tStartRefresh)
    testLoop.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "testRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'testLoop'

# get names of stimulus parameters
if testLoop.trialList in ([], [None], None):
    params = []
else:
    params = testLoop.trialList[0].keys()
# save data for this loop
testLoop.saveAsExcel(filename + '.xlsx', sheetName='testLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "preTrialPause"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
preTrialPauseComponents = [ISI_2]
for thisComponent in preTrialPauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
preTrialPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "preTrialPause"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = preTrialPauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=preTrialPauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *ISI_2* period
    if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_2.frameNStart = frameN  # exact frame index
        ISI_2.tStart = t  # local t and not account for scr refresh
        ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
        ISI_2.start(0.5)
    elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
        ISI_2.complete()  # finish the static period
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preTrialPauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "preTrialPause"-------
for thisComponent in preTrialPauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_2.started', ISI_2.tStart)
thisExp.addData('ISI_2.stopped', ISI_2.tStop)

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [goodbye]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye* updates
    if goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye.frameNStart = frameN  # exact frame index
        goodbye.tStart = t  # local t and not account for scr refresh
        goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye, 'tStartRefresh')  # time at next scr refresh
        goodbye.setAutoDraw(True)
    if goodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goodbye.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            goodbye.tStop = t  # not accounting for scr refresh
            goodbye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(goodbye, 'tStopRefresh')  # time at next scr refresh
            goodbye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodbye.started', goodbye.tStartRefresh)
thisExp.addData('goodbye.stopped', goodbye.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
