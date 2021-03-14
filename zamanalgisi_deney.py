#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b12),
    on 2018_12_10_0102
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.0b12'
expName = 'zamanalgisi_deney'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\alia\\Desktop\\zamanalgisi_deney\\zamanalgisi_deney.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "alistirma_yonerge"
alistirma_yonergeClock = core.Clock()
abaslik = visual.TextStim(win=win, name='abaslik',
    text=u'ALI\u015eTIRMA Y\xd6NERGES\u0130',
    font=u'Arial',
    pos=(0, 0.7), height=0.07, wrapWidth=None, ori=0, 
    color=u'blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ayonerge = visual.TextStim(win=win, name='ayonerge',
    text=u"Deney boyunca ekran\u0131n ortas\u0131nda mavi bir perde g\xf6r\xfcnecektir. Bazen mavi perdenin sa\u011f taraf\u0131ndan bazen de sol taraf\u0131ndan siyah renkli bir kare perdeye do\u011fru hareket edecek, kimi zaman da sadece mavi perde g\xf6r\xfcnecektir. Daha sonra ekran\u0131n ortas\u0131nda art\u0131 i\u015fareti (+) belirecek, sonras\u0131nda ilk a\u015famada g\xf6rd\xfc\u011f\xfcn\xfcz uyar\u0131c\u0131 tekrar sunulacakt\u0131r. \n\nBu deneyde sizden istenen, ilk a\u015famada sadece mavi perdeyi g\xf6rd\xfcyseniz, ikinci sunumunda ilk sunumda ekranda kald\u0131\u011f\u0131 kadar s\xfcre ge\xe7ti\u011finde 'space' tu\u015funa basarak di\u011fer a\u015famaya ge\xe7menizdir.\n \n\u0130lk a\u015famada mavi perdeye do\u011fru sa\u011fdan veya soldan hareket eden siyah kare g\xf6rd\xfcyseniz, \u0130kinci a\u015famada siyah kare mavi perdenin arkas\u0131na girdikten sonra karenin sona ula\u015ft\u0131\u011f\u0131n\u0131 d\xfc\u015f\xfcnd\xfc\u011f\xfcn\xfcz anda 'space' tu\u015funa bas\u0131n\u0131z.\n\n\nHadi birka\xe7 al\u0131\u015ft\u0131rma yapal\u0131m!",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
devam = visual.TextStim(win=win, name='devam',
    text=u"                             Haz\u0131rsan\u0131z, \ndevam etmek i\xe7in 'Bo\u015fluk(space)' tu\u015funa bas\u0131n\u0131z.",
    font=u'Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "a_giris"
a_girisClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u"Haz\u0131r oldu\u011funda 'space' tu\u015funa bas",
    font=u'Arial',
    pos=(0, -0.9), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image=u'nokta.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "a_ilksunum"
a_ilksunumClock = core.Clock()

# Initialize components for Routine "a_araekran"
a_araekranClock = core.Clock()
a_artiresmi = visual.ImageStim(
    win=win, name='a_artiresmi',
    image=u'arti.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "a_uyaricisunum"
a_uyaricisunumClock = core.Clock()
a_perde = visual.ImageStim(
    win=win, name='a_perde',
    image=u'perde.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "a_bitis"
a_bitisClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=u'Al\u0131\u015ft\u0131rma uygulamas\u0131 sona erdi.',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "deney_yonerge"
deney_yonergeClock = core.Clock()
baslik = visual.TextStim(win=win, name='baslik',
    text=u'DENEY Y\xd6NERGES\u0130',
    font=u'Arial',
    pos=(0, 0.7), height=0.07, wrapWidth=None, ori=0, 
    color=u'blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
yonerge = visual.TextStim(win=win, name='yonerge',
    text=u"Deney boyunca ekran\u0131n ortas\u0131nda mavi bir perde g\xf6r\xfcnecektir. Bazen mavi perdenin sa\u011f taraf\u0131ndan bazen de sol taraf\u0131ndan siyah renkli bir kare perdeye do\u011fru hareket edecek, kimi zaman da sadece mavi perde g\xf6r\xfcnecektir. Daha sonra ekran\u0131n ortas\u0131nda art\u0131 i\u015fareti (+) belirecek, sonras\u0131nda ilk a\u015famada g\xf6rd\xfc\u011f\xfcn\xfcz uyar\u0131c\u0131 tekrar sunulacakt\u0131r. \n\nBu deneyde sizden istenen, ilk a\u015famada sadece mavi perdeyi g\xf6rd\xfcyseniz, ikinci sunumunda ilk sunumda ekranda kald\u0131\u011f\u0131 kadar s\xfcre ge\xe7ti\u011finde 'space' tu\u015funa basarak di\u011fer a\u015famaya ge\xe7menizdir.\n \n\u0130lk a\u015famada mavi perdeye do\u011fru sa\u011fdan veya soldan hareket eden siyah kare g\xf6rd\xfcyseniz, \u0130kinci a\u015famada siyah kare mavi perdenin arkas\u0131na girdikten sonra karenin sona ula\u015ft\u0131\u011f\u0131n\u0131 d\xfc\u015f\xfcnd\xfc\u011f\xfcn\xfcz anda 'space' tu\u015funa bas\u0131n\u0131z.\n\n\nHadi deneye ge\xe7elim!",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
hazirim = visual.TextStim(win=win, name='hazirim',
    text=u"                             Haz\u0131rsan\u0131z, \ndevam etmek i\xe7in 'Bo\u015fluk(space)' tu\u015funa bas\u0131n\u0131z.",
    font=u'Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "giris"
girisClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u"Haz\u0131r oldu\u011funda 'space' tu\u015funa bas",
    font=u'Arial',
    pos=(0, -0.9), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
nokta_ = visual.ImageStim(
    win=win, name='nokta_',
    image=u'nokta.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ilksunum"
ilksunumClock = core.Clock()

# Initialize components for Routine "araekran"
araekranClock = core.Clock()
artiresmi = visual.ImageStim(
    win=win, name='artiresmi',
    image=u'arti.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image = visual.ImageStim(
    win=win, name='image',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "uyarici_sunum"
uyarici_sunumClock = core.Clock()
perde = visual.ImageStim(
    win=win, name='perde',
    image=u'perde.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "bitir"
bitirClock = core.Clock()
finito = visual.TextStim(win=win, name='finito',
    text=u'      bitti :( \nte\u015fekk\xfcrler!',
    font=u'Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "alistirma_yonerge"-------
t = 0
alistirma_yonergeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
alistirma_yonergeComponents = [abaslik, ayonerge, devam, key_resp_5]
for thisComponent in alistirma_yonergeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "alistirma_yonerge"-------
while continueRoutine:
    # get current time
    t = alistirma_yonergeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *abaslik* updates
    if t >= 0.0 and abaslik.status == NOT_STARTED:
        # keep track of start time/frame for later
        abaslik.tStart = t
        abaslik.frameNStart = frameN  # exact frame index
        abaslik.setAutoDraw(True)
    
    # *ayonerge* updates
    if t >= 0.0 and ayonerge.status == NOT_STARTED:
        # keep track of start time/frame for later
        ayonerge.tStart = t
        ayonerge.frameNStart = frameN  # exact frame index
        ayonerge.setAutoDraw(True)
    
    # *devam* updates
    if t >= 1 and devam.status == NOT_STARTED:
        # keep track of start time/frame for later
        devam.tStart = t
        devam.frameNStart = frameN  # exact frame index
        devam.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
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
    for thisComponent in alistirma_yonergeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "alistirma_yonerge"-------
for thisComponent in alistirma_yonergeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "alistirma_yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
alistirma_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'alistirma.xlsx'),
    seed=None, name='alistirma_loop')
thisExp.addLoop(alistirma_loop)  # add the loop to the experiment
thisAlistirma_loop = alistirma_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAlistirma_loop.rgb)
if thisAlistirma_loop != None:
    for paramName in thisAlistirma_loop:
        exec('{} = thisAlistirma_loop[paramName]'.format(paramName))

for thisAlistirma_loop in alistirma_loop:
    currentLoop = alistirma_loop
    # abbreviate parameter names if possible (e.g. rgb = thisAlistirma_loop.rgb)
    if thisAlistirma_loop != None:
        for paramName in thisAlistirma_loop:
            exec('{} = thisAlistirma_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "a_giris"-------
    t = 0
    a_girisClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    a_girisComponents = [text, key_resp_6, image_2]
    for thisComponent in a_girisComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "a_giris"-------
    while continueRoutine:
        # get current time
        t = a_girisClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.2 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *image_2* updates
        if t >= 0.1 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_girisComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_giris"-------
    for thisComponent in a_girisComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "a_giris" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "a_ilksunum"-------
    t = 0
    a_ilksunumClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    a_ilkekran = visual.MovieStim3(
        win=win, name='a_ilkekran',
        noAudio = True,
        filename=alistirmalar,
        ori=0, pos=(0, 0), opacity=1,
        depth=0.0,
        )
    # keep track of which components have finished
    a_ilksunumComponents = [a_ilkekran]
    for thisComponent in a_ilksunumComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "a_ilksunum"-------
    while continueRoutine:
        # get current time
        t = a_ilksunumClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *a_ilkekran* updates
        if t >= 0.0 and a_ilkekran.status == NOT_STARTED:
            # keep track of start time/frame for later
            a_ilkekran.tStart = t
            a_ilkekran.frameNStart = frameN  # exact frame index
            a_ilkekran.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_ilksunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_ilksunum"-------
    for thisComponent in a_ilksunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "a_ilksunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "a_araekran"-------
    t = 0
    a_araekranClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    a_araekranComponents = [a_artiresmi, image_3]
    for thisComponent in a_araekranComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "a_araekran"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = a_araekranClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *a_artiresmi* updates
        if t >= 0.3 and a_artiresmi.status == NOT_STARTED:
            # keep track of start time/frame for later
            a_artiresmi.tStart = t
            a_artiresmi.frameNStart = frameN  # exact frame index
            a_artiresmi.setAutoDraw(True)
        frameRemains = 0.3 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if a_artiresmi.status == STARTED and t >= frameRemains:
            a_artiresmi.setAutoDraw(False)
        
        # *image_3* updates
        if t >= 0.3 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.3 + 1.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_araekranComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_araekran"-------
    for thisComponent in a_araekranComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "a_uyaricisunum"-------
    t = 0
    a_uyaricisunumClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    a_uyaricilar = visual.MovieStim3(
        win=win, name='a_uyaricilar',
        noAudio = True,
        filename=alistirmalar,
        ori=0, pos=(0, 0), opacity=1,
        depth=0.0,
        )
    a_tepki = event.BuilderKeyResponse()
    # keep track of which components have finished
    a_uyaricisunumComponents = [a_uyaricilar, a_perde, a_tepki]
    for thisComponent in a_uyaricisunumComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "a_uyaricisunum"-------
    while continueRoutine:
        # get current time
        t = a_uyaricisunumClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *a_uyaricilar* updates
        if t >= 0.0 and a_uyaricilar.status == NOT_STARTED:
            # keep track of start time/frame for later
            a_uyaricilar.tStart = t
            a_uyaricilar.frameNStart = frameN  # exact frame index
            a_uyaricilar.setAutoDraw(True)
        
        # *a_perde* updates
        if t >= 0.0 and a_perde.status == NOT_STARTED:
            # keep track of start time/frame for later
            a_perde.tStart = t
            a_perde.frameNStart = frameN  # exact frame index
            a_perde.setAutoDraw(True)
        
        # *a_tepki* updates
        if t >= 0.0 and a_tepki.status == NOT_STARTED:
            # keep track of start time/frame for later
            a_tepki.tStart = t
            a_tepki.frameNStart = frameN  # exact frame index
            a_tepki.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if a_tepki.status == STARTED:
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
        for thisComponent in a_uyaricisunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_uyaricisunum"-------
    for thisComponent in a_uyaricisunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "a_uyaricisunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'alistirma_loop'

# get names of stimulus parameters
if alistirma_loop.trialList in ([], [None], None):
    params = []
else:
    params = alistirma_loop.trialList[0].keys()
# save data for this loop
alistirma_loop.saveAsExcel(filename + '.xlsx', sheetName='alistirma_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
alistirma_loop.saveAsText(filename + 'alistirma_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "a_bitis"-------
t = 0
a_bitisClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
a_bitisComponents = [text_3, key_resp_7]
for thisComponent in a_bitisComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "a_bitis"-------
while continueRoutine:
    # get current time
    t = a_bitisClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
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
    for thisComponent in a_bitisComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "a_bitis"-------
for thisComponent in a_bitisComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "a_bitis" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "deney_yonerge"-------
t = 0
deney_yonergeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
deney_yonergeComponents = [baslik, yonerge, hazirim, key_resp_2]
for thisComponent in deney_yonergeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "deney_yonerge"-------
while continueRoutine:
    # get current time
    t = deney_yonergeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baslik* updates
    if t >= 0.0 and baslik.status == NOT_STARTED:
        # keep track of start time/frame for later
        baslik.tStart = t
        baslik.frameNStart = frameN  # exact frame index
        baslik.setAutoDraw(True)
    
    # *yonerge* updates
    if t >= 0.0 and yonerge.status == NOT_STARTED:
        # keep track of start time/frame for later
        yonerge.tStart = t
        yonerge.frameNStart = frameN  # exact frame index
        yonerge.setAutoDraw(True)
    
    # *hazirim* updates
    if t >= 1 and hazirim.status == NOT_STARTED:
        # keep track of start time/frame for later
        hazirim.tStart = t
        hazirim.frameNStart = frameN  # exact frame index
        hazirim.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
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
    for thisComponent in deney_yonergeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "deney_yonerge"-------
for thisComponent in deney_yonergeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "deney_yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
deney_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'uyaricilar.xlsx'),
    seed=None, name='deney_loop')
thisExp.addLoop(deney_loop)  # add the loop to the experiment
thisDeney_loop = deney_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDeney_loop.rgb)
if thisDeney_loop != None:
    for paramName in thisDeney_loop:
        exec('{} = thisDeney_loop[paramName]'.format(paramName))

for thisDeney_loop in deney_loop:
    currentLoop = deney_loop
    # abbreviate parameter names if possible (e.g. rgb = thisDeney_loop.rgb)
    if thisDeney_loop != None:
        for paramName in thisDeney_loop:
            exec('{} = thisDeney_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "giris"-------
    t = 0
    girisClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    girisComponents = [text_2, key_resp_4, nokta_]
    for thisComponent in girisComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "giris"-------
    while continueRoutine:
        # get current time
        t = girisClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.2 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *nokta_* updates
        if t >= 0.1 and nokta_.status == NOT_STARTED:
            # keep track of start time/frame for later
            nokta_.tStart = t
            nokta_.frameNStart = frameN  # exact frame index
            nokta_.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in girisComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "giris"-------
    for thisComponent in girisComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "giris" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ilksunum"-------
    t = 0
    ilksunumClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ilkekran = visual.MovieStim3(
        win=win, name='ilkekran',
        noAudio = True,
        filename=uyaricilar,
        ori=0, pos=(0, 0), opacity=1,
        depth=0.0,
        )
    # keep track of which components have finished
    ilksunumComponents = [ilkekran]
    for thisComponent in ilksunumComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ilksunum"-------
    while continueRoutine:
        # get current time
        t = ilksunumClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ilkekran* updates
        if t >= 0.0 and ilkekran.status == NOT_STARTED:
            # keep track of start time/frame for later
            ilkekran.tStart = t
            ilkekran.frameNStart = frameN  # exact frame index
            ilkekran.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ilksunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ilksunum"-------
    for thisComponent in ilksunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ilksunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "araekran"-------
    t = 0
    araekranClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    araekranComponents = [artiresmi, image]
    for thisComponent in araekranComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "araekran"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = araekranClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *artiresmi* updates
        if t >= 0.3 and artiresmi.status == NOT_STARTED:
            # keep track of start time/frame for later
            artiresmi.tStart = t
            artiresmi.frameNStart = frameN  # exact frame index
            artiresmi.setAutoDraw(True)
        frameRemains = 0.3 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if artiresmi.status == STARTED and t >= frameRemains:
            artiresmi.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.3 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.3 + 1.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in araekranComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "araekran"-------
    for thisComponent in araekranComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "uyarici_sunum"-------
    t = 0
    uyarici_sunumClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    uyarici_seti = visual.MovieStim3(
        win=win, name='uyarici_seti',
        noAudio = True,
        filename=uyaricilar,
        ori=0, pos=(0, 0), opacity=1,
        depth=0.0,
        )
    tepsi_suresi = event.BuilderKeyResponse()
    # keep track of which components have finished
    uyarici_sunumComponents = [uyarici_seti, perde, tepsi_suresi]
    for thisComponent in uyarici_sunumComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "uyarici_sunum"-------
    while continueRoutine:
        # get current time
        t = uyarici_sunumClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *uyarici_seti* updates
        if t >= 0.0 and uyarici_seti.status == NOT_STARTED:
            # keep track of start time/frame for later
            uyarici_seti.tStart = t
            uyarici_seti.frameNStart = frameN  # exact frame index
            uyarici_seti.setAutoDraw(True)
        
        # *perde* updates
        if t >= 0.0 and perde.status == NOT_STARTED:
            # keep track of start time/frame for later
            perde.tStart = t
            perde.frameNStart = frameN  # exact frame index
            perde.setAutoDraw(True)
        
        # *tepsi_suresi* updates
        if t >= 0.0 and tepsi_suresi.status == NOT_STARTED:
            # keep track of start time/frame for later
            tepsi_suresi.tStart = t
            tepsi_suresi.frameNStart = frameN  # exact frame index
            tepsi_suresi.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(tepsi_suresi.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if tepsi_suresi.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                tepsi_suresi.keys = theseKeys[-1]  # just the last key pressed
                tepsi_suresi.rt = tepsi_suresi.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in uyarici_sunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "uyarici_sunum"-------
    for thisComponent in uyarici_sunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if tepsi_suresi.keys in ['', [], None]:  # No response was made
        tepsi_suresi.keys=None
    deney_loop.addData('tepsi_suresi.keys',tepsi_suresi.keys)
    if tepsi_suresi.keys != None:  # we had a response
        deney_loop.addData('tepsi_suresi.rt', tepsi_suresi.rt)
    # the Routine "uyarici_sunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'deney_loop'

# get names of stimulus parameters
if deney_loop.trialList in ([], [None], None):
    params = []
else:
    params = deney_loop.trialList[0].keys()
# save data for this loop
deney_loop.saveAsExcel(filename + '.xlsx', sheetName='deney_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
deney_loop.saveAsText(filename + 'deney_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "bitir"-------
t = 0
bitirClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
bitirComponents = [finito, key_resp_3]
for thisComponent in bitirComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "bitir"-------
while continueRoutine:
    # get current time
    t = bitirClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finito* updates
    if t >= 0.0 and finito.status == NOT_STARTED:
        # keep track of start time/frame for later
        finito.tStart = t
        finito.frameNStart = frameN  # exact frame index
        finito.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
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
    for thisComponent in bitirComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bitir"-------
for thisComponent in bitirComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "bitir" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
