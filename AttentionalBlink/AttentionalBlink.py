#Attentional Blink
#Asante April 2017
#The Attentional Blink Experiment was designed to present a series of stimuli and have the user find two images. The first will 
#always come before the second, however due to the Attentional Blink that happens in memory after finding the first image, keeps
#the user from consciously finding the 2nd image.
import psychopy
# set preference for audio sound engine
psychopy.prefs.hardware['audioLib'] = ['PTB', 'pyo','pygame']
from psychopy import visual, core, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy, random, string, scipy
import csv

global mywin
global grating
global fixation
global blankletter
global centraltext
global xecc,yecc
global savetilt

# set up the menu for choice of conditions
myDlg = gui.Dlg(title="Attentional Blink",size=(1, 1))
myDlg.addField('Initials:','xx')
myDlg.addField('SessionNumber:',1)
myDlg.addField('NumberofTrials',15)
myDlg.show()
if myDlg.OK:
    sessioninfo=myDlg.data
else:
    print('cancelled') #Changed this from print 'cancelled' to print('cancelled')
#****************************************************** MENU VALUES ***********************************************************************************************
idn=sessioninfo[0] # Sets idn equal to initials
sessnumber=sessioninfo[1] #sets equal to Session nummber
ntrials=sessioninfo[2] #sets n trial equal to number of trials

#******************************************************* VARIABLES ************************************************************************************************
beforeWhite = []      #number of letters prior to white letter
targetLetter = []     #letter that is in white
containSet = []       #whether there was an X or not
afterWhite = []       #how many letters after the white one the X came up
respX = []            # if they responded whether there was an x or not
respTarget = []       #Response as to what the target letter was

withXSet = []
initialSet = []
xSet = []
noXSet = []
# ********************************************************CSV FILE**********************************************************************
#filename
filename=''
filename='Attentional Blink'
filename+=idn
filename+='_'+str(sessnumber)
filename+='_'+data.getDateStr()
print(filename) #Changed from print filename to print(filename)
datetime=data.getDateStr()

#window #
mywin = visual.Window(size=(1920, 1080),fullscr=True,screen=0,\
    monitor="testMonitor",units="pix",color = (0,0,0))
#rgb=[-1,-1,-1] makes screen black
random.seed()  #initializes by reading the time


data = [("Trial", 
"Letters Prior to Target",
"Loc of X after Target",
"Target Letter", 
"Target Letter Resp",
"X Present", 
"X Present Response", 
)]

def write_file(filename):
    for i in range(0, ntrials):
        data.append((i+1, beforeWhite[i], afterWhite[i], targetLetter[i], respTarget[i], containSet[i], respX[i]))
    with open('%s.csv' %(filename), 'w') as fp:
        writer = csv.writer(fp, delimiter=',' )
        writer.writerows(data)

def getResponse():
    k = event.waitKeys()
    event.clearEvents()
    b=k[0]
    if b=='escape':  #option to get out
        mywin.close()
        core.quit()
    return b

def blankScreen(): 
    mywin.flip(clearBuffer=True)
    mywin.flip()
 #   print pause/1000.0  

def displaysometext(texttodisplay):
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],rgb=2,contrast=1)
    prompt.draw()
    mywin.flip()

#write excel file with results

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'G', 'H', 'I', 'J', 'K', 'L', \
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'Y', 'Z']


def chooseNumOfLett(): 
    #chooses the number of random black letters that show up before white 
    numOfLetters = random.randint(7, 15)
    beforeWhite.append(numOfLetters)
    return numOfLetters

def chooseLett():
    lett = random.choice(letters)
    return lett
    

def showDisplay(trialType):
    x = chooseNumOfLett()   
    beforeWhite.append(x)
    print("1")
    if trialType == 1:
        containSet.append("1")
    else:
        containSet.append("0")

    for i in range(x-1):    #appends letters to the first set
        blackLett = chooseLett()
        while blackLett in initialSet:
            blackLett = chooseLett()
        initialSet.append(blackLett)
     
    for i in range(8):
        xLett = chooseLett()
        while xLett in xSet:
            xLett = chooseLett()
        xSet.append(xLett)
      
    for i in range(8):
        noXLett = chooseLett()
        while noXLett in noXSet:
            noXLett = chooseLett()
        noXSet.append(noXLett)
    print("2")
    xLoc = random.randint(0,7)
    xSet[xLoc] = 'X'
    
    if trialType != 1:
        afterWhite.append("No X Present")
        
    else:
        afterWhite.append(xLoc + 1)

    whiteLett = chooseLett()
    
    while whiteLett in xSet:
        whiteLett = chooseLett()
    
    targetLetter.append(whiteLett)
    
    if trialType == 1: #second set has x
        
        for  i in range(len(initialSet)):
            lettSett = visual.TextStim(win=mywin, text=initialSet[i], color = 'Black', pos = (0,0), height = 100) 
            lettSett.draw()                                                      #draw (actually, writes to a buffer)
            mywin.flip()
            core.wait(.015)
            blankScreen()
            core.wait(.085) 
        
        whiteLetter = visual.TextStim(win=mywin, text=whiteLett, color = 'White', pos = (0,0), height = 100) 
        whiteLetter.draw()                                                      #draw (actually, writes to a buffer)
        mywin.flip()
        core.wait(.015)
        blankScreen()
        core.wait(.085)
        
        for  i in range(len(xSet)):
            hasX = visual.TextStim(win=mywin, text=xSet[i], color = 'Black', pos = (0,0), height = 100) 
            hasX.draw()                                                      #draw (actually, writes to a buffer)
            mywin.flip()
            core.wait(.015)
            blankScreen()
            core.wait(.085)            
    if trialType == 2:   #second set doesnt have x  
        
        for  i in range(len(initialSet)):
            lettSett = visual.TextStim(win=mywin, text=initialSet[i], color = 'Black', pos = (0,0), height = 100) 
            lettSett.draw()                                                      #draw (actually, writes to a buffer)
            mywin.flip()
            core.wait(.015)
            blankScreen()
            core.wait(.085)        
        
        whiteLetter = visual.TextStim(win=mywin, text=whiteLett, color = 'White', pos = (0,0), height = 100) 
        whiteLetter.draw()                                                      #draw (actually, writes to a buffer)
        mywin.flip()
        core.wait(.015)
        blankScreen()
        core.wait(.085)            
        
        for  i in range(len(noXSet)):
            setWithoutX = visual.TextStim(win=mywin, text=noXSet[i], color = 'Black', pos = (0,0), height = 100) 
            setWithoutX.draw()                                                      #draw (actually, writes to a buffer)
            mywin.flip()
            core.wait(.015)
            blankScreen()
            core.wait(.085)
#**********************************************EXPERIMENT BEGINS*************************************************************
#------------------------------------------------Instructions----------------------------------------------------------------- 
block_instruction_text = """
A series of letters will be shown. You have two tasks:\n
(1) Within the series is a white letter. Find
and identify the letter.\n
(2) After this letter appears another series of letters will be shown, and you 
will need to determine whether this second sequence contains an X. \n
Following the complete presentation of the letter sequence will be asked to 
report which letter was in white and whether there was an X. \n
Press SPACEBAR to start the experiment.
"""

winWidth,winHeight = mywin.size

block_instructions = visual.TextStim(win=mywin,text=block_instruction_text,\
    color='White',pos=(0,0),alignText='left',wrapWidth=800,height=40) 
block_instructions.draw()                   #draw (actually, writes to a buffer)
mywin.flip()
# listen for keypress
keypress = None
while keypress != 'space':
    keypress = getResponse()
    print(keypress)

blankScreen()
#-------------------------------------------------Trial Loop-------------------------------------------------------------------
for i in range(ntrials):
    if i != 0:
        del xSet[:]
        del noXSet[:]
        del initialSet[:]
    
    rand = random.randint(0, 1)
    if rand  <  0.5:
        trialType = 1 
    else:
        trialType = 2      
#-----------------------------------------------Letters Shown------------------------------------------------------------------
    press_key_text = "Press SPACEBAR to start the trial."
    press_key = visual.TextStim(win=mywin, text= press_key_text, color = 'White', pos = (0,130), height = 30)
    press_key.draw() 
        
    cross = "+"
    crossImg = visual.TextStim(win=mywin, text=cross, color = 'Black', pos = (0,0), height = 80) 
    crossImg.draw()                                                      #draw (actually, writes to a buffer)
    mywin.flip()

    # listen for keypress
    keypress = None
    while keypress != 'space':
        keypress = getResponse()
        print(keypress)
    # present the next trial
    core.wait(.5)
    blankScreen()
    showDisplay(trialType)
    blankScreen()
        
#-----------------------------------------------Target Letter--------------------------------------------------------------------        
    letter_query_text = "Which letter was white? Press the corresponding letter on the keyboard"
    letter_query = visual.TextStim(win=mywin,text=letter_query_text,\
        color='White',pos=(0,130),height=30)
    letter_query.draw() 
    mywin.flip()    
    # listen for keypress response
    valid_responses = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keypress = None
    keypress = getResponse().upper()
    while keypress not in valid_responses:
        keypress = getResponse()
    # save the observer's response
    respTarget.append(keypress)
    blankScreen()    
#-----------------------------------------------x----------------------------------------------------------------    
    x_query_text = "Was there an x in this trial? Press 'n' for no and 'y' for yes"
    x_query= visual.TextStim(win=mywin, text= x_query_text,color='White',\
        pos=(0,150),height=30) 
    x_query.draw() 
    mywin.flip()
    # listen for keypress response
    keypress = None
    keypress = getResponse().upper()
    while keypress not in ['Y', 'N']:
        keypress = getResponse()
    # save the observer's response
    x_response = 1 if keypress=='Y' else 0
    respX.append(str(x_response)) 
    blankScreen()
#--------------------------------------------------End------------------------------------------------------------------    
nextTrial = "Press any key to exit the program"
nxt = visual.TextStim(win=mywin, text=nextTrial, color = 'Black', pos = (0, 90), height = 30) 
nxt.draw()                                                     
mywin.flip()
keypress = getResponse()   
    
write_file(filename)  
mywin.close()
core.quit()
    
    
    
    
    
    
    