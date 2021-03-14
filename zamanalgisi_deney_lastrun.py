#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Mart 14, 2021, at 21:59
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
psychopyVersion = '2021.1.3'
expName = 'zamanalgisi_deney'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='C:\\Users\\alia\\Desktop\\zamanalgisi_deney\\zamanalgisi_deney_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

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

# Initialize components for Routine "alistirma_yonerge"
alistirma_yonergeClock = core.Clock()
abaslik = visual.TextStim(win=win, name='abaslik',
    text='ALIŞTIRMA YÖNERGESİ',
    font='Arial',
    pos=(0, 0.7), height=0.07, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ayonerge = visual.TextStim(win=win, name='ayonerge',
    text='Alıştırma denemeleriyle başlayacağız.\n\nDeneme ekranın merkezinde bulunan bir artı işareti ile başlayacaktır.\nDaha sonra ekranın ortasında uyarıcı ya da uyarıcılar görünecektir.\n\nBu uyarıcılardan bir tanesi mavi bir perdedir, diğeri ise siyah bir karedir. \n\nBu uyarıcılar üç şekilde karşınıza çıkabilir:\n\n    1) Mavi perdenin sağ tarafından siyah renkli bir kare perdeye doğru hareket edecektir.\n    2) Mavi perdenin sol tarafından siyah renkli bir kare perdeye doğru hareket edecektir.\n    3) Sadece mavi perde görünecektir.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
devam = visual.TextStim(win=win, name='devam',
    text="                             Hazırsanız, \ndevam etmek için 'Boşluk(space)' tuşuna basınız.",
    font='Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "alistirma_yonerge2"
alistirma_yonerge2Clock = core.Clock()
abaslik2 = visual.TextStim(win=win, name='abaslik2',
    text=None,
    font='Arial',
    pos=(0, 0.7), height=0.07, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ayonerge2 = visual.TextStim(win=win, name='ayonerge2',
    text='Bu aşamada yapmanız gereken şey mavi perdeye doğru sağdan ya da soldan hareket eden siyah karenin mavi perdenin arkasına girdikten sonra perdenin sonuna ulaştığı süreyi aklınızda tutmaktır.\n\nDaha sonra ekranın ortasında artı işareti (+) belirecektir. Arkasından ilk aşamada gördüğünüz uyarıcılar aynı süreyle tekrar sunulacaktır.\n\nBu aşamada sizden beklenen, ilk aşamadaki uyarıcıların harekete geçme ve sona erme zamanlarını dikkate alarak uygun süreye karar vermek ve o anda “boşluk (space)” tuşuna basmaktır.\n\nHer bir denemede aynı uyarıcı ya da uyarıcılar iki kere karşınıza çıkmaktadır.\nBu deneyde en önemli olan nokta, ilk aşamada uyarıcı ya da uyarıcıların görülme süresini akılda tutarak (tahmin ederek) ikinci aşamada buna uygun tepki vermektir. \n\nİkinci aşamada siz tuşa basana kadar bir sonraki denemeye geçilmeyecektir.\nHerhangi bir sorunuz yok ise boşluk tuşuna basarak alıştırmaları başlatabilirsiniz.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
devam2 = visual.TextStim(win=win, name='devam2',
    text="                             Hazırsanız, \ndevam etmek için 'Boşluk(space)' tuşuna basınız.",
    font='Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "a_giris"
a_girisClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Hazır olduğunda 'boşluk' tuşuna bas",
    font='Arial',
    pos=(0, -0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='nokta.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "a_ilksunum"
a_ilksunumClock = core.Clock()

# Initialize components for Routine "a_araekran"
a_araekranClock = core.Clock()
a_artiresmi = visual.ImageStim(
    win=win,
    name='a_artiresmi', 
    image='arti.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "a_uyaricisunum"
a_uyaricisunumClock = core.Clock()
a_perde = visual.ImageStim(
    win=win,
    name='a_perde', 
    image='perde.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
a_tepki = keyboard.Keyboard()

# Initialize components for Routine "a_bitis"
a_bitisClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Alıştırma uygulaması sona erdi.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "deney_yonerge"
deney_yonergeClock = core.Clock()
baslik = visual.TextStim(win=win, name='baslik',
    text='DENEY YÖNERGESİ',
    font='Arial',
    pos=(0, 0.7), height=0.07, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
yonerge = visual.TextStim(win=win, name='yonerge',
    text="Deney boyunca ekranın ortasında mavi bir perde görünecektir. Bazen mavi perdenin sağ tarafından bazen de sol tarafından siyah renkli bir kare perdeye doğru hareket edecek, kimi zaman da sadece mavi perde görünecektir. Daha sonra ekranın ortasında artı işareti (+) belirecek, sonrasında ilk aşamada gördüğünüz uyarıcı tekrar sunulacaktır. \n\nBu deneyde sizden istenen, ilk aşamada sadece mavi perdeyi gördüyseniz, ikinci sunumunda ilk sunumda ekranda kaldığı kadar süre geçtiğinde 'space' tuşuna basarak diğer aşamaya geçmenizdir.\n \nİlk aşamada mavi perdeye doğru sağdan veya soldan hareket eden siyah kare gördüyseniz, İkinci aşamada siyah kare mavi perdenin arkasına girdikten sonra karenin sona ulaştığını düşündüğünüz anda 'space' tuşuna basınız.\n\n\nHadi deneye geçelim!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
hazirim = visual.TextStim(win=win, name='hazirim',
    text="                             Hazırsanız, \ndevam etmek için 'Boşluk(space)' tuşuna basınız.",
    font='Arial',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "giris"
girisClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="Hazır olduğunda 'boşluk' tuşuna bas",
    font='Arial',
    pos=(0, -0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
nokta_ = visual.ImageStim(
    win=win,
    name='nokta_', 
    image='nokta.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ilksunum"
ilksunumClock = core.Clock()

# Initialize components for Routine "araekran"
araekranClock = core.Clock()
artiresmi = visual.ImageStim(
    win=win,
    name='artiresmi', 
    image='arti.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "uyarici_sunum"
uyarici_sunumClock = core.Clock()
perde = visual.ImageStim(
    win=win,
    name='perde', 
    image='perde.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tepsi_suresi = keyboard.Keyboard()

# Initialize components for Routine "bitir"
bitirClock = core.Clock()
finito = visual.TextStim(win=win, name='finito',
    text='bitti :)',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
finito2 = visual.TextStim(win=win, name='finito2',
    text='\n\n\n\n\nkatılımınız için teşekkür ederiz!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "alistirma_yonerge"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
alistirma_yonergeComponents = [abaslik, ayonerge, devam, key_resp_5]
for thisComponent in alistirma_yonergeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
alistirma_yonergeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "alistirma_yonerge"-------
while continueRoutine:
    # get current time
    t = alistirma_yonergeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=alistirma_yonergeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *abaslik* updates
    if abaslik.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        abaslik.frameNStart = frameN  # exact frame index
        abaslik.tStart = t  # local t and not account for scr refresh
        abaslik.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(abaslik, 'tStartRefresh')  # time at next scr refresh
        abaslik.setAutoDraw(True)
    
    # *ayonerge* updates
    if ayonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ayonerge.frameNStart = frameN  # exact frame index
        ayonerge.tStart = t  # local t and not account for scr refresh
        ayonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ayonerge, 'tStartRefresh')  # time at next scr refresh
        ayonerge.setAutoDraw(True)
    
    # *devam* updates
    if devam.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        devam.frameNStart = frameN  # exact frame index
        devam.tStart = t  # local t and not account for scr refresh
        devam.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(devam, 'tStartRefresh')  # time at next scr refresh
        devam.setAutoDraw(True)
    
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
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in alistirma_yonergeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "alistirma_yonerge"-------
for thisComponent in alistirma_yonergeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('abaslik.started', abaslik.tStartRefresh)
thisExp.addData('abaslik.stopped', abaslik.tStopRefresh)
thisExp.addData('ayonerge.started', ayonerge.tStartRefresh)
thisExp.addData('ayonerge.stopped', ayonerge.tStopRefresh)
thisExp.addData('devam.started', devam.tStartRefresh)
thisExp.addData('devam.stopped', devam.tStopRefresh)
# the Routine "alistirma_yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "alistirma_yonerge2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
alistirma_yonerge2Components = [abaslik2, ayonerge2, devam2, key_resp_8]
for thisComponent in alistirma_yonerge2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
alistirma_yonerge2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "alistirma_yonerge2"-------
while continueRoutine:
    # get current time
    t = alistirma_yonerge2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=alistirma_yonerge2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *abaslik2* updates
    if abaslik2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        abaslik2.frameNStart = frameN  # exact frame index
        abaslik2.tStart = t  # local t and not account for scr refresh
        abaslik2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(abaslik2, 'tStartRefresh')  # time at next scr refresh
        abaslik2.setAutoDraw(True)
    
    # *ayonerge2* updates
    if ayonerge2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ayonerge2.frameNStart = frameN  # exact frame index
        ayonerge2.tStart = t  # local t and not account for scr refresh
        ayonerge2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ayonerge2, 'tStartRefresh')  # time at next scr refresh
        ayonerge2.setAutoDraw(True)
    
    # *devam2* updates
    if devam2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        devam2.frameNStart = frameN  # exact frame index
        devam2.tStart = t  # local t and not account for scr refresh
        devam2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(devam2, 'tStartRefresh')  # time at next scr refresh
        devam2.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in alistirma_yonerge2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "alistirma_yonerge2"-------
for thisComponent in alistirma_yonerge2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('abaslik2.started', abaslik2.tStartRefresh)
thisExp.addData('abaslik2.stopped', abaslik2.tStopRefresh)
thisExp.addData('ayonerge2.started', ayonerge2.tStartRefresh)
thisExp.addData('ayonerge2.stopped', ayonerge2.tStopRefresh)
thisExp.addData('devam2.started', devam2.tStartRefresh)
thisExp.addData('devam2.stopped', devam2.tStopRefresh)
# the Routine "alistirma_yonerge2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
alistirma_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('alistirma.xlsx'),
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
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    a_girisComponents = [text, key_resp_6, image_2]
    for thisComponent in a_girisComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    a_girisClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "a_giris"-------
    while continueRoutine:
        # get current time
        t = a_girisClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=a_girisClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
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
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_girisComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_giris"-------
    for thisComponent in a_girisComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    alistirma_loop.addData('text.started', text.tStartRefresh)
    alistirma_loop.addData('text.stopped', text.tStopRefresh)
    alistirma_loop.addData('image_2.started', image_2.tStartRefresh)
    alistirma_loop.addData('image_2.stopped', image_2.tStopRefresh)
    # the Routine "a_giris" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "a_ilksunum"-------
    continueRoutine = True
    # update component parameters for each repeat
    a_ilkekran = visual.MovieStim3(
        win=win, name='a_ilkekran',
        noAudio = True,
        filename=alistirmalar,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        depth=0.0,
        )
    # keep track of which components have finished
    a_ilksunumComponents = [a_ilkekran]
    for thisComponent in a_ilksunumComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    a_ilksunumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "a_ilksunum"-------
    while continueRoutine:
        # get current time
        t = a_ilksunumClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=a_ilksunumClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *a_ilkekran* updates
        if a_ilkekran.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            a_ilkekran.frameNStart = frameN  # exact frame index
            a_ilkekran.tStart = t  # local t and not account for scr refresh
            a_ilkekran.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_ilkekran, 'tStartRefresh')  # time at next scr refresh
            a_ilkekran.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_ilksunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_ilksunum"-------
    for thisComponent in a_ilksunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    a_ilkekran.stop()
    # the Routine "a_ilksunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "a_araekran"-------
    continueRoutine = True
    routineTimer.add(1.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    a_araekranComponents = [a_artiresmi, image_3]
    for thisComponent in a_araekranComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    a_araekranClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "a_araekran"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = a_araekranClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=a_araekranClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *a_artiresmi* updates
        if a_artiresmi.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            a_artiresmi.frameNStart = frameN  # exact frame index
            a_artiresmi.tStart = t  # local t and not account for scr refresh
            a_artiresmi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_artiresmi, 'tStartRefresh')  # time at next scr refresh
            a_artiresmi.setAutoDraw(True)
        if a_artiresmi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_artiresmi.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                a_artiresmi.tStop = t  # not accounting for scr refresh
                a_artiresmi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_artiresmi, 'tStopRefresh')  # time at next scr refresh
                a_artiresmi.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 1.1-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_araekranComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_araekran"-------
    for thisComponent in a_araekranComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    alistirma_loop.addData('a_artiresmi.started', a_artiresmi.tStartRefresh)
    alistirma_loop.addData('a_artiresmi.stopped', a_artiresmi.tStopRefresh)
    alistirma_loop.addData('image_3.started', image_3.tStartRefresh)
    alistirma_loop.addData('image_3.stopped', image_3.tStopRefresh)
    
    # ------Prepare to start Routine "a_uyaricisunum"-------
    continueRoutine = True
    # update component parameters for each repeat
    a_uyaricilar = visual.MovieStim3(
        win=win, name='a_uyaricilar',
        noAudio = True,
        filename=alistirmalar,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        depth=0.0,
        )
    a_tepki.keys = []
    a_tepki.rt = []
    _a_tepki_allKeys = []
    # keep track of which components have finished
    a_uyaricisunumComponents = [a_uyaricilar, a_perde, a_tepki]
    for thisComponent in a_uyaricisunumComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    a_uyaricisunumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "a_uyaricisunum"-------
    while continueRoutine:
        # get current time
        t = a_uyaricisunumClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=a_uyaricisunumClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *a_uyaricilar* updates
        if a_uyaricilar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            a_uyaricilar.frameNStart = frameN  # exact frame index
            a_uyaricilar.tStart = t  # local t and not account for scr refresh
            a_uyaricilar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_uyaricilar, 'tStartRefresh')  # time at next scr refresh
            a_uyaricilar.setAutoDraw(True)
        
        # *a_perde* updates
        if a_perde.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            a_perde.frameNStart = frameN  # exact frame index
            a_perde.tStart = t  # local t and not account for scr refresh
            a_perde.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_perde, 'tStartRefresh')  # time at next scr refresh
            a_perde.setAutoDraw(True)
        
        # *a_tepki* updates
        waitOnFlip = False
        if a_tepki.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            a_tepki.frameNStart = frameN  # exact frame index
            a_tepki.tStart = t  # local t and not account for scr refresh
            a_tepki.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_tepki, 'tStartRefresh')  # time at next scr refresh
            a_tepki.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(a_tepki.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(a_tepki.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if a_tepki.status == STARTED and not waitOnFlip:
            theseKeys = a_tepki.getKeys(keyList=['space'], waitRelease=False)
            _a_tepki_allKeys.extend(theseKeys)
            if len(_a_tepki_allKeys):
                a_tepki.keys = _a_tepki_allKeys[-1].name  # just the last key pressed
                a_tepki.rt = _a_tepki_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in a_uyaricisunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "a_uyaricisunum"-------
    for thisComponent in a_uyaricisunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    a_uyaricilar.stop()
    alistirma_loop.addData('a_perde.started', a_perde.tStartRefresh)
    alistirma_loop.addData('a_perde.stopped', a_perde.tStopRefresh)
    # the Routine "a_uyaricisunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'alistirma_loop'


# ------Prepare to start Routine "a_bitis"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
a_bitisComponents = [text_3, key_resp_7]
for thisComponent in a_bitisComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
a_bitisClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "a_bitis"-------
while continueRoutine:
    # get current time
    t = a_bitisClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=a_bitisClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
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
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in a_bitisComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "a_bitis"-------
for thisComponent in a_bitisComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "a_bitis" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "deney_yonerge"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
deney_yonergeComponents = [baslik, yonerge, hazirim, key_resp_2]
for thisComponent in deney_yonergeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
deney_yonergeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "deney_yonerge"-------
while continueRoutine:
    # get current time
    t = deney_yonergeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=deney_yonergeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baslik* updates
    if baslik.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        baslik.frameNStart = frameN  # exact frame index
        baslik.tStart = t  # local t and not account for scr refresh
        baslik.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(baslik, 'tStartRefresh')  # time at next scr refresh
        baslik.setAutoDraw(True)
    
    # *yonerge* updates
    if yonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        yonerge.frameNStart = frameN  # exact frame index
        yonerge.tStart = t  # local t and not account for scr refresh
        yonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(yonerge, 'tStartRefresh')  # time at next scr refresh
        yonerge.setAutoDraw(True)
    
    # *hazirim* updates
    if hazirim.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        hazirim.frameNStart = frameN  # exact frame index
        hazirim.tStart = t  # local t and not account for scr refresh
        hazirim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hazirim, 'tStartRefresh')  # time at next scr refresh
        hazirim.setAutoDraw(True)
    
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in deney_yonergeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "deney_yonerge"-------
for thisComponent in deney_yonergeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('baslik.started', baslik.tStartRefresh)
thisExp.addData('baslik.stopped', baslik.tStopRefresh)
thisExp.addData('yonerge.started', yonerge.tStartRefresh)
thisExp.addData('yonerge.stopped', yonerge.tStopRefresh)
thisExp.addData('hazirim.started', hazirim.tStartRefresh)
thisExp.addData('hazirim.stopped', hazirim.tStopRefresh)
# the Routine "deney_yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
deney_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('uyaricilar.xlsx'),
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
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    girisComponents = [text_2, key_resp_4, nokta_]
    for thisComponent in girisComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    girisClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "giris"-------
    while continueRoutine:
        # get current time
        t = girisClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=girisClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
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
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *nokta_* updates
        if nokta_.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            nokta_.frameNStart = frameN  # exact frame index
            nokta_.tStart = t  # local t and not account for scr refresh
            nokta_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nokta_, 'tStartRefresh')  # time at next scr refresh
            nokta_.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in girisComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "giris"-------
    for thisComponent in girisComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    deney_loop.addData('text_2.started', text_2.tStartRefresh)
    deney_loop.addData('text_2.stopped', text_2.tStopRefresh)
    deney_loop.addData('nokta_.started', nokta_.tStartRefresh)
    deney_loop.addData('nokta_.stopped', nokta_.tStopRefresh)
    # the Routine "giris" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ilksunum"-------
    continueRoutine = True
    # update component parameters for each repeat
    ilkekran = visual.MovieStim3(
        win=win, name='ilkekran',
        noAudio = True,
        filename=uyaricilar,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        depth=0.0,
        )
    # keep track of which components have finished
    ilksunumComponents = [ilkekran]
    for thisComponent in ilksunumComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ilksunumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ilksunum"-------
    while continueRoutine:
        # get current time
        t = ilksunumClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ilksunumClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ilkekran* updates
        if ilkekran.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ilkekran.frameNStart = frameN  # exact frame index
            ilkekran.tStart = t  # local t and not account for scr refresh
            ilkekran.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ilkekran, 'tStartRefresh')  # time at next scr refresh
            ilkekran.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ilksunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ilksunum"-------
    for thisComponent in ilksunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ilkekran.stop()
    # the Routine "ilksunum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "araekran"-------
    continueRoutine = True
    routineTimer.add(1.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    araekranComponents = [artiresmi, image]
    for thisComponent in araekranComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    araekranClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "araekran"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = araekranClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=araekranClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *artiresmi* updates
        if artiresmi.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            artiresmi.frameNStart = frameN  # exact frame index
            artiresmi.tStart = t  # local t and not account for scr refresh
            artiresmi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artiresmi, 'tStartRefresh')  # time at next scr refresh
            artiresmi.setAutoDraw(True)
        if artiresmi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > artiresmi.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                artiresmi.tStop = t  # not accounting for scr refresh
                artiresmi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(artiresmi, 'tStopRefresh')  # time at next scr refresh
                artiresmi.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 1.1-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in araekranComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "araekran"-------
    for thisComponent in araekranComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    deney_loop.addData('artiresmi.started', artiresmi.tStartRefresh)
    deney_loop.addData('artiresmi.stopped', artiresmi.tStopRefresh)
    deney_loop.addData('image.started', image.tStartRefresh)
    deney_loop.addData('image.stopped', image.tStopRefresh)
    
    # ------Prepare to start Routine "uyarici_sunum"-------
    continueRoutine = True
    # update component parameters for each repeat
    uyarici_seti = visual.MovieStim3(
        win=win, name='uyarici_seti',
        noAudio = True,
        filename=uyaricilar,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        depth=0.0,
        )
    tepsi_suresi.keys = []
    tepsi_suresi.rt = []
    _tepsi_suresi_allKeys = []
    # keep track of which components have finished
    uyarici_sunumComponents = [uyarici_seti, perde, tepsi_suresi]
    for thisComponent in uyarici_sunumComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    uyarici_sunumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "uyarici_sunum"-------
    while continueRoutine:
        # get current time
        t = uyarici_sunumClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=uyarici_sunumClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *uyarici_seti* updates
        if uyarici_seti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            uyarici_seti.frameNStart = frameN  # exact frame index
            uyarici_seti.tStart = t  # local t and not account for scr refresh
            uyarici_seti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(uyarici_seti, 'tStartRefresh')  # time at next scr refresh
            uyarici_seti.setAutoDraw(True)
        
        # *perde* updates
        if perde.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            perde.frameNStart = frameN  # exact frame index
            perde.tStart = t  # local t and not account for scr refresh
            perde.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(perde, 'tStartRefresh')  # time at next scr refresh
            perde.setAutoDraw(True)
        
        # *tepsi_suresi* updates
        waitOnFlip = False
        if tepsi_suresi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tepsi_suresi.frameNStart = frameN  # exact frame index
            tepsi_suresi.tStart = t  # local t and not account for scr refresh
            tepsi_suresi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tepsi_suresi, 'tStartRefresh')  # time at next scr refresh
            tepsi_suresi.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(tepsi_suresi.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(tepsi_suresi.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if tepsi_suresi.status == STARTED and not waitOnFlip:
            theseKeys = tepsi_suresi.getKeys(keyList=['space'], waitRelease=False)
            _tepsi_suresi_allKeys.extend(theseKeys)
            if len(_tepsi_suresi_allKeys):
                tepsi_suresi.keys = _tepsi_suresi_allKeys[-1].name  # just the last key pressed
                tepsi_suresi.rt = _tepsi_suresi_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in uyarici_sunumComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "uyarici_sunum"-------
    for thisComponent in uyarici_sunumComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    uyarici_seti.stop()
    deney_loop.addData('perde.started', perde.tStartRefresh)
    deney_loop.addData('perde.stopped', perde.tStopRefresh)
    # check responses
    if tepsi_suresi.keys in ['', [], None]:  # No response was made
        tepsi_suresi.keys = None
    deney_loop.addData('tepsi_suresi.keys',tepsi_suresi.keys)
    if tepsi_suresi.keys != None:  # we had a response
        deney_loop.addData('tepsi_suresi.rt', tepsi_suresi.rt)
    deney_loop.addData('tepsi_suresi.started', tepsi_suresi.tStartRefresh)
    deney_loop.addData('tepsi_suresi.stopped', tepsi_suresi.tStopRefresh)
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
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
bitirComponents = [finito, key_resp_3, finito2]
for thisComponent in bitirComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
bitirClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bitir"-------
while continueRoutine:
    # get current time
    t = bitirClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=bitirClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finito* updates
    if finito.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finito.frameNStart = frameN  # exact frame index
        finito.tStart = t  # local t and not account for scr refresh
        finito.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finito, 'tStartRefresh')  # time at next scr refresh
        finito.setAutoDraw(True)
    
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
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *finito2* updates
    if finito2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finito2.frameNStart = frameN  # exact frame index
        finito2.tStart = t  # local t and not account for scr refresh
        finito2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finito2, 'tStartRefresh')  # time at next scr refresh
        finito2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in bitirComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bitir"-------
for thisComponent in bitirComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finito.started', finito.tStartRefresh)
thisExp.addData('finito.stopped', finito.tStopRefresh)
thisExp.addData('finito2.started', finito2.tStartRefresh)
thisExp.addData('finito2.stopped', finito2.tStopRefresh)
# the Routine "bitir" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
