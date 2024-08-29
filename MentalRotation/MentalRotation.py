#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), Sun Jan 31 14:44:46 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import pyglet
import os  # handy system and path functions

def get_display_info():
    """
    gets effective fullscreen resolution from the os and creates a temporary
    window to compute the native hardware resolution and to determine whether
    there is any pixel scaling (i.e., as in MacOS 'Retina' displays)

    returns a tuple consisting of: horizontal resolution, vertical resolution, 
    and pixel scaling factor
    """
    # 1. Get full display resolution (as reported by OS)
    # note: code below assumes either single or twin monitor configuration
    screen = pyglet.canvas.Display().get_default_screen()
    os_width = screen.width
    os_height = screen.height
    # 2. Create fullscreen Psychopy window and get actual hardware resolution
    testwin = visual.Window(monitor='testMonitor',color='black',allowGUI=True,\
        units='pix',size=(os_width,os_height),fullscr=True)
    hard_width,hard_height = testwin.size
    # 3. Compute the ratio of hard_width to os_width to determine whether we're
    #    using a HiDPI display (i.e., one with pixel scaling).
    pixel_scaling = hard_width/os_width
    # 4. Exit the window
    testwin.close()
    return os_width,os_height,pixel_scaling


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'MentalRot'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s_%s' %(expInfo['participant'],expInfo['session'],expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[1040, 800], fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# WWIDTH,WHEIGHT,PX_SCALE = get_display_info()
# win = visual.Window(monitor='testMonitor',color='black',allowGUI=True,
#         colorSpace='rgb',blendMode='avg', useFBO=True,units='height',
#         fullscr=True,size=(WWIDTH,WHEIGHT))

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Intructions_1"
Intructions_1Clock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text="Welcome. You will see two letters on the screen that have been rotated. For each pair of letters, indicate if they are mirror images of each other when they two letters are in their normal upright position. (Ignore the rotations.)\r\n\r\nPress 'm' if they are mirror images of each other. Press 'n' if they are the same (not mirror images).  \r\n\r\nPress the 'm' to continue.",    font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=.8,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Intructions_2"
Intructions_2Clock = core.Clock()
image_L_3 = visual.ImageStim(win=win, name='image_L_3',
    image='sin', mask='raisedCos',
    ori=1.0, pos=[-.25, .2], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_R_3 = visual.ImageStim(win=win, name='image_R_3',
    image='sin', mask='raisedCos',
    ori=1.0, pos=[0.25, .2], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text="Here, the letter on the right is a mirror image of the letter on the left. They would still be different after mentally rotating them to line up. So press 'm' (different). If they are the same, you would press 'n'.\r\n\r\nTry to respond as accurately as you can. Also try to be fast, but emphasize being accurate. Press 'n' to start.",    font='Arial',
    pos=[0, -.2], height=0.04, wrapWidth=1,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "pause_start"
pause_startClock = core.Clock()
mini_pause_2 = visual.TextStim(win=win, ori=0, name='mini_pause_2',
    text=' +',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()

image_L = visual.ImageStim(win=win, name='image_L',
    image='sin', mask='raisedCos',
    ori=1.0, pos=[-.25, 0], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_R = visual.ImageStim(win=win, name='image_R',
    image='sin', mask='raisedCos',
    ori=1.0, pos=[0.25, 0], size=[.3,.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
text = visual.TextStim(win=win, ori=0, name='text',
    text='\'m\' for "different"\r\n\'n\' for "same"',    font='Arial',
    pos=[0, -.3], height=0.03, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
data_string = 'angle,rt,corr\n'
trial_count = visual.TextStim(win=win, ori=0, name='trial_count',
    text='default text',    font='Arial',
    pos=[.4, -.4], height=0.03, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
mini_pause = visual.TextStim(win=win, ori=0, name='mini_pause',
    text=' ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "the_end"
the_endClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='The end.\r\n\r\nPress space to continue',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "plot_data"
plot_dataClock = core.Clock()
from matplotlib import pyplot
import pandas as pd

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Intructions_1"-------
t = 0
Intructions_1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
Intructions_1Components = []
Intructions_1Components.append(ISI_2)
Intructions_1Components.append(text_4)
Intructions_1Components.append(key_resp_4)
for thisComponent in Intructions_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intructions_1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intructions_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['m'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *ISI_2* period
    if t >= 0.0 and ISI_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_2.tStart = t  # underestimates by a little under one frame
        ISI_2.frameNStart = frameN  # exact frame index
        ISI_2.start(0.5)
    elif ISI_2.status == STARTED: #one frame should pass before updating params and completing
        ISI_2.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intructions_1"-------
for thisComponent in Intructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
# thisExp.addData('key_resp_4.keys',key_resp_4.keys)
# if key_resp_4.keys != None:  # we had a response
#     thisExp.addData('key_resp_4.rt', key_resp_4.rt)
# thisExp.nextEntry()
# the Routine "Intructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Intructions_2"-------
t = 0
Intructions_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
image_L_3.setOri(0)
image_L_3.setImage('FR.png')
image_R_3.setOri(-90)
image_R_3.setImage('F.png')
# keep track of which components have finished
Intructions_2Components = []
Intructions_2Components.append(key_resp_6)
Intructions_2Components.append(image_L_3)
Intructions_2Components.append(image_R_3)
Intructions_2Components.append(text_5)
for thisComponent in Intructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intructions_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['n'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_L_3* updates
    if t >= 0.0 and image_L_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_L_3.tStart = t  # underestimates by a little under one frame
        image_L_3.frameNStart = frameN  # exact frame index
        image_L_3.setAutoDraw(True)
    
    # *image_R_3* updates
    if t >= 0.0 and image_R_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_R_3.tStart = t  # underestimates by a little under one frame
        image_R_3.frameNStart = frameN  # exact frame index
        image_R_3.setAutoDraw(True)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intructions_2"-------
for thisComponent in Intructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pause_start"-------
t = 0
pause_startClock.reset()  # clock 
frameN = -1
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
pause_startComponents = []
pause_startComponents.append(mini_pause_2)
for thisComponent in pause_startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pause_start"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pause_startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mini_pause_2* updates
    if t >= 0.0 and mini_pause_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        mini_pause_2.tStart = t  # underestimates by a little under one frame
        mini_pause_2.frameNStart = frameN  # exact frame index
        mini_pause_2.setAutoDraw(True)
    if mini_pause_2.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
        mini_pause_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pause_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pause_start"-------
for thisComponent in pause_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=6, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('MentalRot.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial['rgb'])
if thisTrial != None:
    for paramName in thisTrial.keys():
        cmdString = "%s = thisTrial['%s']"%(paramName,paramName)
        exec(cmdString)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial['rgb'])
    if thisTrial != None:
        for paramName in thisTrial.keys():
            cmdString = "%s = thisTrial['%s']"%(paramName,paramName)
            exec(cmdString)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if same == 'n':
        limage = 'F.png'
        rimage = 'FR.png'
        if random() > .5:
           rimage, limage = limage, rimage
    else:
        limage = rimage = 'F.png'
        if random() > .5:
            limage = rimage = 'FR.png'
    Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response.status = NOT_STARTED
    image_L.setOri(leftori)
    image_L.setImage(limage)
    image_R.setOri(rightori)
    image_R.setImage(rimage)
    
    trial_count.setText(trials.thisN)
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(Response)
    TrialComponents.append(image_L)
    TrialComponents.append(image_R)
    TrialComponents.append(text)
    TrialComponents.append(trial_count)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Response* updates
        if t >= 0.0 and Response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response.tStart = t  # underestimates by a little under one frame
            Response.frameNStart = frameN  # exact frame index
            Response.status = STARTED
            # keyboard checking is just starting
            Response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Response.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Response.keys = theseKeys[-1]  # just the last key pressed
                Response.rt = Response.clock.getTime()
                # was this 'correct'?
                if (Response.keys == str(('n','m')[same=='n'])) or (Response.keys == ('n','m')[same=='n']):
                    Response.corr = 1
                else:
                    Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image_L* updates
        if t >= 0.0 and image_L.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_L.tStart = t  # underestimates by a little under one frame
            image_L.frameNStart = frameN  # exact frame index
            image_L.setAutoDraw(True)
        
        # *image_R* updates
        if t >= 0.0 and image_R.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_R.tStart = t  # underestimates by a little under one frame
            image_R.frameNStart = frameN  # exact frame index
            image_R.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        
        # *trial_count* updates
        if t >= 0.0 and trial_count.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_count.tStart = t  # underestimates by a little under one frame
            trial_count.frameNStart = frameN  # exact frame index
            trial_count.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
       Response.keys=None
       # was no response the correct answer?!
       if str(('n','m')[same=='n']).lower() == 'none': Response.corr = 1  # correct non-response
       else: Response.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Response.keys',Response.keys)
    trials.addData('Response.corr', Response.corr)
    if Response.keys != None:  # we had a response
        trials.addData('Response.rt', Response.rt)
    data_string += '%d,%.3f,%d\n' % (abs(angle), Response.rt, Response.corr)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pause"-------
    t = 0
    pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    if trials.thisN == 4 and expInfo['participant'] == 'JRG':    
        trials.finished = True
    # keep track of which components have finished
    pauseComponents = []
    pauseComponents.append(mini_pause)
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mini_pause* updates
        if t >= 0.0 and mini_pause.status == NOT_STARTED:
            # keep track of start time/frame for later
            mini_pause.tStart = t  # underestimates by a little under one frame
            mini_pause.frameNStart = frameN  # exact frame index
            mini_pause.setAutoDraw(True)
        if mini_pause.status == STARTED and t >= (0.0 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            mini_pause.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials'


#------Prepare to start Routine "the_end"-------
t = 0
the_endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
the_endComponents = []
the_endComponents.append(text_3)
the_endComponents.append(key_resp_2)
for thisComponent in the_endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "the_end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = the_endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "the_end"-------
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "the_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# #------Prepare to start Routine "plot_data"-------
# t = 0
# plot_dataClock.reset()  # clock 
# frameN = -1
# # update component parameters for each repeat
# def plotYX(yaxis, xaxis, description=''):
#     pyplot.grid(True)
#     pyplot.title(description)
#     pyplot.xlabel('Angle')
#     pyplot.ylabel('Response time (s)')
#     pyplot.xlim([0, 315])
#     #slope,inter = np.polyfit(xaxis[:5],yaxis[:5],1)
#     pyplot.plot(xaxis, yaxis) #, xaxis[:5], np.array(xaxis[:5]) * slope + inter)
#     pyplot.draw()
#     pyplot.show()

# temp_filename = 'data/mental_rotation_data.csv'
# with open(temp_filename, 'w') as fd:
#     fd.write(data_string)

# data = pd.read_csv(temp_filename)
# data = data[data['rt'] < 4]  # trim RT at 4 sec
# mrt = data.loc[:,'rt']
# correct = data.loc[:, 'corr']
# angle = data.loc[:, 'angle']

# dfsum = data.groupby('angle', as_index=False).mean()
# m = dfsum.loc[:, 'rt']
# a = dfsum.loc[:, 'angle']

# scored_data = zip(a, m)
# print('average time (sec) at each rotation:')
# print("  0  45  90  135 180 225 270 315")
# print("--> %s <--" % repr([round(i,3) for i in m]).strip('[]').replace(',', '  '))
# print("\n%% correct        : %2.2f" % (100 * correct.mean()))
# print("overall speed (s): %2.3", mrt.mean())

# plotYX(m, a)

# with open(temp_filename, 'a+') as fd:
#     fd.write('\n\n' + repr(scored_data))
# # keep track of which components have finished
# plot_dataComponents = []
# for thisComponent in plot_dataComponents:
#     if hasattr(thisComponent, 'status'):
#         thisComponent.status = NOT_STARTED

# #-------Start Routine "plot_data"-------
# continueRoutine = True
# while continueRoutine:
#     # get current time
#     t = plot_dataClock.getTime()
#     frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#     # update/draw components on each frame
    
    
#     # check if all components have finished
#     if not continueRoutine:  # a component has requested a forced-end of Routine
#         break
#     continueRoutine = False  # will revert to True if at least one component still running
#     for thisComponent in plot_dataComponents:
#         if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#             continueRoutine = True
#             break  # at least one component has not yet finished
    
#     # check for quit (the Esc key)
#     if endExpNow or event.getKeys(keyList=["escape"]):
#         core.quit()
    
#     # refresh the screen
#     if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#         win.flip()

# #-------Ending Routine "plot_data"-------
# for thisComponent in plot_dataComponents:
#     if hasattr(thisComponent, "setAutoDraw"):
#         thisComponent.setAutoDraw(False)

# # the Routine "plot_data" was not non-slip safe, so reset the non-slip timer
# routineTimer.reset()




win.close()
core.quit()
