#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 28, 2020, at 23:36
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
expName = 'MoralCognition'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\melchi\\Documents\\CourseMaterials\\CogSPLabs\\LabCodeFiles\\MoralCognition\\MoralCognition_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruct = visual.TextStim(win=win, name='Instruct',
    text='You will be presented with a series of narratives about random bystanders. \n\nFor each narrative, once you are finished reading the story, press spacebar to bring up the response pages. \n\nYou will first be asked to rate whether one of the bystander\'s possible actions is morally acceptable or not. Click "Y" for Yes or "N" for No. \n\nIn addition, you will be asked to rate how morally acceptable the bystander\'s action is from 1 to 7: 1 being completely acceptable to 7 completely unacceptable. Type in the number, and then click on the box with your number in it. \n\nThe next trial will start automatically after you click on the box.\n\nPress space once you finish reading these instructions.',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
forceend_instruct = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
storytime = visual.TextStim(win=win, name='storytime',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
forceend_storytime = keyboard.Keyboard()

# Initialize components for Routine "intentq"
intentqClock = core.Clock()
deonticjudgment = visual.TextStim(win=win, name='deonticjudgment',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
YESORNO = visual.TextStim(win=win, name='YESORNO',
    text='default text',
    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
djresp = keyboard.Keyboard()

# Initialize components for Routine "Likert_Scale"
Likert_ScaleClock = core.Clock()
LikertScaleText = visual.TextStim(win=win, name='LikertScaleText',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
forceend_instruct.keys = []
forceend_instruct.rt = []
_forceend_instruct_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Instruct, forceend_instruct]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct* updates
    if Instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct.frameNStart = frameN  # exact frame index
        Instruct.tStart = t  # local t and not account for scr refresh
        Instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct, 'tStartRefresh')  # time at next scr refresh
        Instruct.setAutoDraw(True)
    if Instruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instruct.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            Instruct.tStop = t  # not accounting for scr refresh
            Instruct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instruct, 'tStopRefresh')  # time at next scr refresh
            Instruct.setAutoDraw(False)
    
    # *forceend_instruct* updates
    waitOnFlip = False
    if forceend_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        forceend_instruct.frameNStart = frameN  # exact frame index
        forceend_instruct.tStart = t  # local t and not account for scr refresh
        forceend_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(forceend_instruct, 'tStartRefresh')  # time at next scr refresh
        forceend_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(forceend_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(forceend_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if forceend_instruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > forceend_instruct.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            forceend_instruct.tStop = t  # not accounting for scr refresh
            forceend_instruct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(forceend_instruct, 'tStopRefresh')  # time at next scr refresh
            forceend_instruct.status = FINISHED
    if forceend_instruct.status == STARTED and not waitOnFlip:
        theseKeys = forceend_instruct.getKeys(keyList=['space'], waitRelease=False)
        _forceend_instruct_allKeys.extend(theseKeys)
        if len(_forceend_instruct_allKeys):
            forceend_instruct.keys = _forceend_instruct_allKeys[-1].name  # just the last key pressed
            forceend_instruct.rt = _forceend_instruct_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct.started', Instruct.tStartRefresh)
thisExp.addData('Instruct.stopped', Instruct.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mc_conditions.xlsx'),
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
    routineTimer.add(122.000000)
    # update component parameters for each repeat
    storytime.setText(intentstory)
    forceend_storytime.keys = []
    forceend_storytime.rt = []
    _forceend_storytime_allKeys = []
    # keep track of which components have finished
    trialComponents = [ISI, fixation, storytime, forceend_storytime]
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
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *storytime* updates
        if storytime.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            storytime.frameNStart = frameN  # exact frame index
            storytime.tStart = t  # local t and not account for scr refresh
            storytime.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(storytime, 'tStartRefresh')  # time at next scr refresh
            storytime.setAutoDraw(True)
        if storytime.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > storytime.tStartRefresh + 120.0-frameTolerance:
                # keep track of stop time/frame for later
                storytime.tStop = t  # not accounting for scr refresh
                storytime.frameNStop = frameN  # exact frame index
                win.timeOnFlip(storytime, 'tStopRefresh')  # time at next scr refresh
                storytime.setAutoDraw(False)
        
        # *forceend_storytime* updates
        waitOnFlip = False
        if forceend_storytime.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            forceend_storytime.frameNStart = frameN  # exact frame index
            forceend_storytime.tStart = t  # local t and not account for scr refresh
            forceend_storytime.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forceend_storytime, 'tStartRefresh')  # time at next scr refresh
            forceend_storytime.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(forceend_storytime.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(forceend_storytime.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if forceend_storytime.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > forceend_storytime.tStartRefresh + 120.0-frameTolerance:
                # keep track of stop time/frame for later
                forceend_storytime.tStop = t  # not accounting for scr refresh
                forceend_storytime.frameNStop = frameN  # exact frame index
                win.timeOnFlip(forceend_storytime, 'tStopRefresh')  # time at next scr refresh
                forceend_storytime.status = FINISHED
        if forceend_storytime.status == STARTED and not waitOnFlip:
            theseKeys = forceend_storytime.getKeys(keyList=['space'], waitRelease=False)
            _forceend_storytime_allKeys.extend(theseKeys)
            if len(_forceend_storytime_allKeys):
                forceend_storytime.keys = _forceend_storytime_allKeys[-1].name  # just the last key pressed
                forceend_storytime.rt = _forceend_storytime_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
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
    trials.addData('ISI.started', ISI.tStart)
    trials.addData('ISI.stopped', ISI.tStop)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    trials.addData('storytime.started', storytime.tStartRefresh)
    trials.addData('storytime.stopped', storytime.tStopRefresh)
    
    # ------Prepare to start Routine "intentq"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    deonticjudgment.setText(djquestion)
    YESORNO.setText('YES (Y)\t\t\tNO (N)')
    djresp.keys = []
    djresp.rt = []
    _djresp_allKeys = []
    # keep track of which components have finished
    intentqComponents = [deonticjudgment, YESORNO, djresp]
    for thisComponent in intentqComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intentqClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "intentq"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intentqClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intentqClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *deonticjudgment* updates
        if deonticjudgment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deonticjudgment.frameNStart = frameN  # exact frame index
            deonticjudgment.tStart = t  # local t and not account for scr refresh
            deonticjudgment.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deonticjudgment, 'tStartRefresh')  # time at next scr refresh
            deonticjudgment.setAutoDraw(True)
        if deonticjudgment.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > deonticjudgment.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                deonticjudgment.tStop = t  # not accounting for scr refresh
                deonticjudgment.frameNStop = frameN  # exact frame index
                win.timeOnFlip(deonticjudgment, 'tStopRefresh')  # time at next scr refresh
                deonticjudgment.setAutoDraw(False)
        
        # *YESORNO* updates
        if YESORNO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YESORNO.frameNStart = frameN  # exact frame index
            YESORNO.tStart = t  # local t and not account for scr refresh
            YESORNO.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YESORNO, 'tStartRefresh')  # time at next scr refresh
            YESORNO.setAutoDraw(True)
        if YESORNO.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > YESORNO.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                YESORNO.tStop = t  # not accounting for scr refresh
                YESORNO.frameNStop = frameN  # exact frame index
                win.timeOnFlip(YESORNO, 'tStopRefresh')  # time at next scr refresh
                YESORNO.setAutoDraw(False)
        
        # *djresp* updates
        waitOnFlip = False
        if djresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            djresp.frameNStart = frameN  # exact frame index
            djresp.tStart = t  # local t and not account for scr refresh
            djresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(djresp, 'tStartRefresh')  # time at next scr refresh
            djresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(djresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(djresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if djresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > djresp.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                djresp.tStop = t  # not accounting for scr refresh
                djresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(djresp, 'tStopRefresh')  # time at next scr refresh
                djresp.status = FINISHED
        if djresp.status == STARTED and not waitOnFlip:
            theseKeys = djresp.getKeys(keyList=['y', 'n'], waitRelease=False)
            _djresp_allKeys.extend(theseKeys)
            if len(_djresp_allKeys):
                djresp.keys = _djresp_allKeys[-1].name  # just the last key pressed
                djresp.rt = _djresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intentqComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intentq"-------
    for thisComponent in intentqComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('deonticjudgment.started', deonticjudgment.tStartRefresh)
    trials.addData('deonticjudgment.stopped', deonticjudgment.tStopRefresh)
    trials.addData('YESORNO.started', YESORNO.tStartRefresh)
    trials.addData('YESORNO.stopped', YESORNO.tStopRefresh)
    # check responses
    if djresp.keys in ['', [], None]:  # No response was made
        djresp.keys = None
    trials.addData('djresp.keys',djresp.keys)
    if djresp.keys != None:  # we had a response
        trials.addData('djresp.rt', djresp.rt)
    trials.addData('djresp.started', djresp.tStartRefresh)
    trials.addData('djresp.stopped', djresp.tStopRefresh)
    
    # ------Prepare to start Routine "Likert_Scale"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    LikertScaleText.setText('To what extent is this action morally acceptable?\r\n1 being completely acceptable to 7 being completely unacceptable.\r\n\r\nClick the number to rate acceptability, then click the number below to confirm your response.\r\n')
    rating.reset()
    # keep track of which components have finished
    Likert_ScaleComponents = [LikertScaleText, rating]
    for thisComponent in Likert_ScaleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Likert_ScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Likert_Scale"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Likert_ScaleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Likert_ScaleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LikertScaleText* updates
        if LikertScaleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LikertScaleText.frameNStart = frameN  # exact frame index
            LikertScaleText.tStart = t  # local t and not account for scr refresh
            LikertScaleText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LikertScaleText, 'tStartRefresh')  # time at next scr refresh
            LikertScaleText.setAutoDraw(True)
        if LikertScaleText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LikertScaleText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                LikertScaleText.tStop = t  # not accounting for scr refresh
                LikertScaleText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LikertScaleText, 'tStopRefresh')  # time at next scr refresh
                LikertScaleText.setAutoDraw(False)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Likert_ScaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Likert_Scale"-------
    for thisComponent in Likert_ScaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('LikertScaleText.started', LikertScaleText.tStartRefresh)
    trials.addData('LikertScaleText.stopped', LikertScaleText.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.started', rating.tStart)
    trials.addData('rating.stopped', rating.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


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
