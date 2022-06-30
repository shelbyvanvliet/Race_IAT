#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Jun 30 10:40:31 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'IAT'  # from the Builder filename that created this script
expInfo = {'gender': '', 'age': '', 'participant': ''}
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
    originPath='/Users/Anzu/ImplicitAssociationTest/IAT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
# Dependencies
import itertools  # for flattening lists of lists into lists
import random
import math  # for math.ceil() rounding up

# Import stimuli exemplars
exemplars_filename = 'stimuli.xlsx'
exemplars = data.importConditions(exemplars_filename)# Import stimuli exemplars

# Determine rows of examplars (i.e., max number of rows)
"""
This method creates a fully counterbalanced presentation of exemplars when there are 5
of them, but it will not present each one an equal number of times it the n diverges from 5.
"""
n_exemplars = len(exemplars)
list_multiplier = int(math.ceil(10/n_exemplars))  # math.ceil() rounds up. 10 is the derived from way block lengths are calculated. Admittedly, this comment doensn't adequately document why it's ten. Honestly, I have to work it out of my fingers every time and can't explain it.

# Trial generation function
def generate_trials(trial_type_column, multiplier):
    """Generate a shuffled list of stimuli exemplars from a column in an excel stimuli file""" 
    a = dict()  # declare a dict to be populated
    for i in range(len(exemplars)):
        a[i] = [exemplars[i][trial_type_column]] * multiplier  # populate the dict from vertical reads of the conditions
    a = a.values()  # extract only values (and not keys) from the list of dicts
    a = list(itertools.chain(*a))  # flatten the list of dicts into a list
    random.shuffle(a)  # shuffle this list, so that it can be drawn from by the trials
    return a

# declare trial rows (not sure if necessary, but can't be bothered to removed and test)
trial_rows = ""

# set block order based on participant code
participantNumber = int(expInfo['participant'])
if (participantNumber % 2) == 1: 
    block_order = 1
elif (participantNumber % 2) == 0:
    block_order = 2
else:
    print("****condition file error: please enter a numeric participant code****")

instructionsBox = visual.TextStim(win=win, name='instructionsBox',
    text='',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructionsKey = keyboard.Keyboard()
leftCategoryLabel_2 = visual.TextStim(win=win, name='leftCategoryLabel_2',
    text='',
    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rightCategoryLabel_2 = visual.TextStim(win=win, name='rightCategoryLabel_2',
    text='',
    font='Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
leftAttributeLabel_2 = visual.TextStim(win=win, name='leftAttributeLabel_2',
    text='',
    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None, ori=0, 
    color=[-1, 1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
rightAttributeLabel_2 = visual.TextStim(win=win, name='rightAttributeLabel_2',
    text='',
    font='Arial',
    pos=[.6, 0.55], height=0.1, wrapWidth=None, ori=0, 
    color=[-1, 1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
orLeft_2 = visual.TextStim(win=win, name='orLeft_2',
    text='',
    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
orRight_2 = visual.TextStim(win=win, name='orRight_2',
    text='',
    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
#declare accuracy feedback message variable
msg=""
stimulusImageBox = visual.ImageStim(
    win=win,
    name='stimulusImageBox', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.6,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
stimulusTextBox = visual.TextStim(win=win, name='stimulusTextBox',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
requiredResponse = keyboard.Keyboard()
feedbackResponse = keyboard.Keyboard()
feedback = visual.TextStim(win=win, name='feedback',
    text='',
    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
leftCategoryLabel = visual.TextStim(win=win, name='leftCategoryLabel',
    text='',
    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rightCategoryLabel = visual.TextStim(win=win, name='rightCategoryLabel',
    text='',
    font='Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
leftAttributeLabel = visual.TextStim(win=win, name='leftAttributeLabel',
    text='',
    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None, ori=0, 
    color=[-1, 1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
rightAttributeLabel = visual.TextStim(win=win, name='rightAttributeLabel',
    text='',
    font='Arial',
    pos=[.6, 0.55], height=0.1, wrapWidth=None, ori=0, 
    color=[-1, 1, -1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
orLeft = visual.TextStim(win=win, name='orLeft',
    text='',
    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
orRight = visual.TextStim(win=win, name='orRight',
    text='',
    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "end"
endClock = core.Clock()
endBox = visual.TextStim(win=win, name='endBox',
    text='End of the task',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    # set the block length and the rows to pull from based on the current block 
    # this layout follows Nosek et al. 2007, "The Implicit Association Test at age 7: A methodological and conceptual review"
    if blocks.thisN == 0:
        trial_rows = "0:2" 
        n_block_repeats = 10   #2*10 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 1:
        trial_rows = "2:4" 
        n_block_repeats = 10   #2*10 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 2:
        trial_rows = "0:4" 
        n_block_repeats = 5   #4*5 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 3:
        trial_rows = "0:4" 
        n_block_repeats = 10   #4*10 = 40 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 4:
        trial_rows = "0:2" 
        n_block_repeats = 20   #2*20 = 40 trials
        modified_list_multiplier = list_multiplier * 2  # because this block has a different trials:categories ratio
    elif blocks.thisN == 5:
        trial_rows = "0:4" 
        n_block_repeats = 5   #4*5 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 6:
        trial_rows = "0:4" 
        n_block_repeats = 10   #4*10 = 40 trials
        modified_list_multiplier = list_multiplier
    
    # Generate list of stimuli for the block
    text_trial_type_1_trials = generate_trials('text_trial_type_1_exemplars', modified_list_multiplier)  # function and variable determined at begin exp.
    text_trial_type_2_trials = generate_trials('text_trial_type_2_exemplars', modified_list_multiplier)
    text_trial_type_3_trials = generate_trials('text_trial_type_3_exemplars', modified_list_multiplier)
    text_trial_type_4_trials = generate_trials('text_trial_type_4_exemplars', modified_list_multiplier)
    img_trial_type_1_trials = generate_trials('img_trial_type_1_exemplars', modified_list_multiplier)
    img_trial_type_2_trials = generate_trials('img_trial_type_2_exemplars', modified_list_multiplier)
    img_trial_type_3_trials = generate_trials('img_trial_type_3_exemplars', modified_list_multiplier)
    img_trial_type_4_trials = generate_trials('img_trial_type_4_exemplars', modified_list_multiplier)
    
    # set category and attribute labels based on the block order and current block
    if block_order == 1 and blocks.thisN <= 3:
        leftCategory = categoryA
        rightCategory = categoryB
    elif block_order == 1 and blocks.thisN > 3:
        leftCategory = categoryB
        rightCategory = categoryA
    elif block_order == 2 and blocks.thisN <= 3:
        leftCategory = categoryB
        rightCategory = categoryA
    elif block_order == 2 and blocks.thisN > 3:
        leftCategory = categoryA
        rightCategory = categoryB
    instructionsBox.setText(instructions)
    instructionsKey.keys = []
    instructionsKey.rt = []
    _instructionsKey_allKeys = []
    leftCategoryLabel_2.setText(leftCategory)
    rightCategoryLabel_2.setText(rightCategory)
    leftAttributeLabel_2.setText(leftAttribute)
    rightAttributeLabel_2.setText(rightAttribute)
    orLeft_2.setText(orStimulus)
    orRight_2.setText(orStimulus)
    # keep track of which components have finished
    instructionComponents = [instructionsBox, instructionsKey, leftCategoryLabel_2, rightCategoryLabel_2, leftAttributeLabel_2, rightAttributeLabel_2, orLeft_2, orRight_2]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction"-------
    while continueRoutine:
        # get current time
        t = instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if instructionsBox.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.tStart = t  # local t and not account for scr refresh
            instructionsBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsBox, 'tStartRefresh')  # time at next scr refresh
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        waitOnFlip = False
        if instructionsKey.status == NOT_STARTED and tThisFlip >= 2.75-frameTolerance:
            # keep track of start time/frame for later
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.tStart = t  # local t and not account for scr refresh
            instructionsKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsKey, 'tStartRefresh')  # time at next scr refresh
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructionsKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructionsKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructionsKey.status == STARTED and not waitOnFlip:
            theseKeys = instructionsKey.getKeys(keyList=['e', 'i'], waitRelease=False)
            _instructionsKey_allKeys.extend(theseKeys)
            if len(_instructionsKey_allKeys):
                instructionsKey.keys = _instructionsKey_allKeys[-1].name  # just the last key pressed
                instructionsKey.rt = _instructionsKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *leftCategoryLabel_2* updates
        if leftCategoryLabel_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            leftCategoryLabel_2.frameNStart = frameN  # exact frame index
            leftCategoryLabel_2.tStart = t  # local t and not account for scr refresh
            leftCategoryLabel_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftCategoryLabel_2, 'tStartRefresh')  # time at next scr refresh
            leftCategoryLabel_2.setAutoDraw(True)
        
        # *rightCategoryLabel_2* updates
        if rightCategoryLabel_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            rightCategoryLabel_2.frameNStart = frameN  # exact frame index
            rightCategoryLabel_2.tStart = t  # local t and not account for scr refresh
            rightCategoryLabel_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightCategoryLabel_2, 'tStartRefresh')  # time at next scr refresh
            rightCategoryLabel_2.setAutoDraw(True)
        
        # *leftAttributeLabel_2* updates
        if leftAttributeLabel_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            leftAttributeLabel_2.frameNStart = frameN  # exact frame index
            leftAttributeLabel_2.tStart = t  # local t and not account for scr refresh
            leftAttributeLabel_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftAttributeLabel_2, 'tStartRefresh')  # time at next scr refresh
            leftAttributeLabel_2.setAutoDraw(True)
        
        # *rightAttributeLabel_2* updates
        if rightAttributeLabel_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            rightAttributeLabel_2.frameNStart = frameN  # exact frame index
            rightAttributeLabel_2.tStart = t  # local t and not account for scr refresh
            rightAttributeLabel_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightAttributeLabel_2, 'tStartRefresh')  # time at next scr refresh
            rightAttributeLabel_2.setAutoDraw(True)
        
        # *orLeft_2* updates
        if orLeft_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            orLeft_2.frameNStart = frameN  # exact frame index
            orLeft_2.tStart = t  # local t and not account for scr refresh
            orLeft_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orLeft_2, 'tStartRefresh')  # time at next scr refresh
            orLeft_2.setAutoDraw(True)
        
        # *orRight_2* updates
        if orRight_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            orRight_2.frameNStart = frameN  # exact frame index
            orRight_2.tStart = t  # local t and not account for scr refresh
            orRight_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orRight_2, 'tStartRefresh')  # time at next scr refresh
            orRight_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('instructionsBox.started', instructionsBox.tStartRefresh)
    blocks.addData('instructionsBox.stopped', instructionsBox.tStopRefresh)
    blocks.addData('leftCategoryLabel_2.started', leftCategoryLabel_2.tStartRefresh)
    blocks.addData('leftCategoryLabel_2.stopped', leftCategoryLabel_2.tStopRefresh)
    blocks.addData('rightCategoryLabel_2.started', rightCategoryLabel_2.tStartRefresh)
    blocks.addData('rightCategoryLabel_2.stopped', rightCategoryLabel_2.tStopRefresh)
    blocks.addData('leftAttributeLabel_2.started', leftAttributeLabel_2.tStartRefresh)
    blocks.addData('leftAttributeLabel_2.stopped', leftAttributeLabel_2.tStopRefresh)
    blocks.addData('rightAttributeLabel_2.started', rightAttributeLabel_2.tStartRefresh)
    blocks.addData('rightAttributeLabel_2.stopped', rightAttributeLabel_2.tStopRefresh)
    blocks.addData('orLeft_2.started', orLeft_2.tStartRefresh)
    blocks.addData('orLeft_2.stopped', orLeft_2.tStopRefresh)
    blocks.addData('orRight_2.started', orRight_2.tStartRefresh)
    blocks.addData('orRight_2.stopped', orRight_2.tStopRefresh)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=n_block_repeats, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('block_layout.xlsx', selection=trial_rows),
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
        # update component parameters for each repeat
        # choose a random exemplar from the appropriate trial type list
        if trial_type == 1:
            text_stimulus = text_trial_type_1_trials.pop()
            image_stimulus = img_trial_type_1_trials.pop()
        elif trial_type == 2:
            text_stimulus = text_trial_type_2_trials.pop()
            image_stimulus = img_trial_type_2_trials.pop()
        elif trial_type == 3:
            text_stimulus = text_trial_type_3_trials.pop()
            image_stimulus = img_trial_type_3_trials.pop()
        elif trial_type == 4:
            text_stimulus = text_trial_type_4_trials.pop()
            image_stimulus = img_trial_type_4_trials.pop()
        
        # set stimulus colors based on trial type
        if trial_type == 1 or trial_type == 2:
             stimulusColor = [1, 1, 1]
        elif trial_type >2:
             stimulusColor = [-1, 1, -1]
        
        # set required and feedback responses
        # attributes are invariate across blocks so can be determined based on trial type only
        if trial_type == 3: #pos
            requiredAllowed = "i"
            requiredCorrect = "i"
            feedbackAllowed = "e"
            feedbackCorrect = "e"
        elif trial_type == 4: #neg
            requiredAllowed = "e"
            requiredCorrect = "e"
            feedbackAllowed = "i"
            feedbackCorrect = "i"
        # categories depend on block order, current block and trial type
        if block_order == 1: 
            if blocks.thisN <= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
                elif trial_type == 2: #insects
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
            elif blocks.thisN >= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
                elif trial_type == 2: #insects
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
        elif block_order == 2: 
            if blocks.thisN <= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
                elif trial_type == 2: #insects
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
            elif blocks.thisN >= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
                elif trial_type == 2: #insects
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
        stimulusImageBox.setImage(image_stimulus)
        stimulusTextBox.setColor(stimulusColor, colorSpace='rgb')
        stimulusTextBox.setText(text_stimulus)
        requiredResponse.keys = []
        requiredResponse.rt = []
        _requiredResponse_allKeys = []
        feedbackResponse.keys = []
        feedbackResponse.rt = []
        _feedbackResponse_allKeys = []
        leftCategoryLabel.setText(leftCategory)
        rightCategoryLabel.setText(rightCategory)
        leftAttributeLabel.setText(leftAttribute)
        rightAttributeLabel.setText(rightAttribute)
        orLeft.setText(orStimulus)
        orRight.setText(orStimulus)
        # keep track of which components have finished
        trialComponents = [stimulusImageBox, stimulusTextBox, requiredResponse, feedbackResponse, feedback, leftCategoryLabel, rightCategoryLabel, leftAttributeLabel, rightAttributeLabel, orLeft, orRight]
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
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if len(feedbackResponse.keys)<1:
                msg=""
            else:
                msg="X"
            
            # *stimulusImageBox* updates
            if stimulusImageBox.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                stimulusImageBox.frameNStart = frameN  # exact frame index
                stimulusImageBox.tStart = t  # local t and not account for scr refresh
                stimulusImageBox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulusImageBox, 'tStartRefresh')  # time at next scr refresh
                stimulusImageBox.setAutoDraw(True)
            
            # *stimulusTextBox* updates
            if stimulusTextBox.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                stimulusTextBox.frameNStart = frameN  # exact frame index
                stimulusTextBox.tStart = t  # local t and not account for scr refresh
                stimulusTextBox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulusTextBox, 'tStartRefresh')  # time at next scr refresh
                stimulusTextBox.setAutoDraw(True)
            
            # *requiredResponse* updates
            waitOnFlip = False
            if requiredResponse.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                requiredResponse.frameNStart = frameN  # exact frame index
                requiredResponse.tStart = t  # local t and not account for scr refresh
                requiredResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(requiredResponse, 'tStartRefresh')  # time at next scr refresh
                requiredResponse.status = STARTED
                # AllowedKeys looks like a variable named `requiredAllowed`
                if not type(requiredAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(requiredAllowed, str):
                        logging.error('AllowedKeys variable `requiredAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in requiredAllowed:
                        requiredAllowed = (requiredAllowed,)
                    else:
                        requiredAllowed = eval(requiredAllowed)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(requiredResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(requiredResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if requiredResponse.status == STARTED and not waitOnFlip:
                theseKeys = requiredResponse.getKeys(keyList=list(requiredAllowed), waitRelease=False)
                _requiredResponse_allKeys.extend(theseKeys)
                if len(_requiredResponse_allKeys):
                    requiredResponse.keys = _requiredResponse_allKeys[0].name  # just the first key pressed
                    requiredResponse.rt = _requiredResponse_allKeys[0].rt
                    # was this correct?
                    if (requiredResponse.keys == str(requiredCorrect )) or (requiredResponse.keys == requiredCorrect ):
                        requiredResponse.corr = 1
                    else:
                        requiredResponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *feedbackResponse* updates
            waitOnFlip = False
            if feedbackResponse.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                feedbackResponse.frameNStart = frameN  # exact frame index
                feedbackResponse.tStart = t  # local t and not account for scr refresh
                feedbackResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackResponse, 'tStartRefresh')  # time at next scr refresh
                feedbackResponse.status = STARTED
                # AllowedKeys looks like a variable named `feedbackAllowed`
                if not type(feedbackAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedbackAllowed, str):
                        logging.error('AllowedKeys variable `feedbackAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedbackAllowed:
                        feedbackAllowed = (feedbackAllowed,)
                    else:
                        feedbackAllowed = eval(feedbackAllowed)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(feedbackResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(feedbackResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if feedbackResponse.status == STARTED and not waitOnFlip:
                theseKeys = feedbackResponse.getKeys(keyList=list(feedbackAllowed), waitRelease=False)
                _feedbackResponse_allKeys.extend(theseKeys)
                if len(_feedbackResponse_allKeys):
                    feedbackResponse.keys = _feedbackResponse_allKeys[0].name  # just the first key pressed
                    feedbackResponse.rt = _feedbackResponse_allKeys[0].rt
                    # was this correct?
                    if (feedbackResponse.keys == str(feedbackCorrect )) or (feedbackResponse.keys == feedbackCorrect ):
                        feedbackResponse.corr = 1
                    else:
                        feedbackResponse.corr = 0
            
            # *feedback* updates
            if feedback.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                feedback.frameNStart = frameN  # exact frame index
                feedback.tStart = t  # local t and not account for scr refresh
                feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
                feedback.setAutoDraw(True)
            if feedback.status == STARTED:  # only update if drawing
                feedback.setText(msg, log=False)
            
            # *leftCategoryLabel* updates
            if leftCategoryLabel.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                leftCategoryLabel.frameNStart = frameN  # exact frame index
                leftCategoryLabel.tStart = t  # local t and not account for scr refresh
                leftCategoryLabel.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftCategoryLabel, 'tStartRefresh')  # time at next scr refresh
                leftCategoryLabel.setAutoDraw(True)
            
            # *rightCategoryLabel* updates
            if rightCategoryLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightCategoryLabel.frameNStart = frameN  # exact frame index
                rightCategoryLabel.tStart = t  # local t and not account for scr refresh
                rightCategoryLabel.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightCategoryLabel, 'tStartRefresh')  # time at next scr refresh
                rightCategoryLabel.setAutoDraw(True)
            
            # *leftAttributeLabel* updates
            if leftAttributeLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftAttributeLabel.frameNStart = frameN  # exact frame index
                leftAttributeLabel.tStart = t  # local t and not account for scr refresh
                leftAttributeLabel.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftAttributeLabel, 'tStartRefresh')  # time at next scr refresh
                leftAttributeLabel.setAutoDraw(True)
            
            # *rightAttributeLabel* updates
            if rightAttributeLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightAttributeLabel.frameNStart = frameN  # exact frame index
                rightAttributeLabel.tStart = t  # local t and not account for scr refresh
                rightAttributeLabel.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightAttributeLabel, 'tStartRefresh')  # time at next scr refresh
                rightAttributeLabel.setAutoDraw(True)
            
            # *orLeft* updates
            if orLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                orLeft.frameNStart = frameN  # exact frame index
                orLeft.tStart = t  # local t and not account for scr refresh
                orLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(orLeft, 'tStartRefresh')  # time at next scr refresh
                orLeft.setAutoDraw(True)
            
            # *orRight* updates
            if orRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                orRight.frameNStart = frameN  # exact frame index
                orRight.tStart = t  # local t and not account for scr refresh
                orRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(orRight, 'tStartRefresh')  # time at next scr refresh
                orRight.setAutoDraw(True)
            
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
        trials.addData('stimulusImageBox.started', stimulusImageBox.tStartRefresh)
        trials.addData('stimulusImageBox.stopped', stimulusImageBox.tStopRefresh)
        trials.addData('stimulusTextBox.started', stimulusTextBox.tStartRefresh)
        trials.addData('stimulusTextBox.stopped', stimulusTextBox.tStopRefresh)
        # check responses
        if requiredResponse.keys in ['', [], None]:  # No response was made
            requiredResponse.keys = None
            # was no response the correct answer?!
            if str(requiredCorrect ).lower() == 'none':
               requiredResponse.corr = 1;  # correct non-response
            else:
               requiredResponse.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('requiredResponse.keys',requiredResponse.keys)
        trials.addData('requiredResponse.corr', requiredResponse.corr)
        if requiredResponse.keys != None:  # we had a response
            trials.addData('requiredResponse.rt', requiredResponse.rt)
        trials.addData('requiredResponse.started', requiredResponse.tStartRefresh)
        trials.addData('requiredResponse.stopped', requiredResponse.tStopRefresh)
        # check responses
        if feedbackResponse.keys in ['', [], None]:  # No response was made
            feedbackResponse.keys = None
            # was no response the correct answer?!
            if str(feedbackCorrect ).lower() == 'none':
               feedbackResponse.corr = 1;  # correct non-response
            else:
               feedbackResponse.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('feedbackResponse.keys',feedbackResponse.keys)
        trials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            trials.addData('feedbackResponse.rt', feedbackResponse.rt)
        trials.addData('feedbackResponse.started', feedbackResponse.tStartRefresh)
        trials.addData('feedbackResponse.stopped', feedbackResponse.tStopRefresh)
        trials.addData('feedback.started', feedback.tStartRefresh)
        trials.addData('feedback.stopped', feedback.tStopRefresh)
        trials.addData('leftCategoryLabel.started', leftCategoryLabel.tStartRefresh)
        trials.addData('leftCategoryLabel.stopped', leftCategoryLabel.tStopRefresh)
        trials.addData('rightCategoryLabel.started', rightCategoryLabel.tStartRefresh)
        trials.addData('rightCategoryLabel.stopped', rightCategoryLabel.tStopRefresh)
        trials.addData('leftAttributeLabel.started', leftAttributeLabel.tStartRefresh)
        trials.addData('leftAttributeLabel.stopped', leftAttributeLabel.tStopRefresh)
        trials.addData('rightAttributeLabel.started', rightAttributeLabel.tStartRefresh)
        trials.addData('rightAttributeLabel.stopped', rightAttributeLabel.tStopRefresh)
        trials.addData('orLeft.started', orLeft.tStartRefresh)
        trials.addData('orLeft.stopped', orLeft.tStopRefresh)
        trials.addData('orRight.started', orRight.tStartRefresh)
        trials.addData('orRight.stopped', orRight.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed n_block_repeats repeats of 'trials'
    
# completed 1 repeats of 'blocks'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.750000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [endBox]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endBox* updates
    if endBox.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
        # keep track of start time/frame for later
        endBox.frameNStart = frameN  # exact frame index
        endBox.tStart = t  # local t and not account for scr refresh
        endBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endBox, 'tStartRefresh')  # time at next scr refresh
        endBox.setAutoDraw(True)
    if endBox.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endBox.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            endBox.tStop = t  # not accounting for scr refresh
            endBox.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endBox, 'tStopRefresh')  # time at next scr refresh
            endBox.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endBox.started', endBox.tStartRefresh)
thisExp.addData('endBox.stopped', endBox.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
