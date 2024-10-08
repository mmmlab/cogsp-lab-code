#dividedattention_6.  
#E Kowler.  Aug 19, 2015
#Christina Asante March , 2017


#Based on Joseph, Chun & Nakayama (1997).Attentional requirements in a preattentive
#search task. Nature 387, 805-807.  dual-task format.  central and primary task:  monitor stream of letters for a targetletterw
#with different contrast.  Second task:  an array of 8 gabors will flash some time either slightly before or after the target letter.
#One gabor will be tilted.  Report direction of tilt and location in array of tilted grating.
#Joseph et al. report that performance is poor when grating flashes around the time of the target letter, indicating that even
#a "simple" early vision task (orientation identification) demands attention.

#Obtaining this result may depend on choice of parameters in the menu including Gabor contrast, letter contrast, and sizes.
#Also, Joseph et al. used a mask following the grating.  This has not been implemented here.

#Sept 21, 2015:  The target character is now a NUMERAL 
# March 2017 The experiment has been changed to only output a csv file, and the direction of tilt is no longer asked
#instead it is only the location of the grating

from psychopy import visual, core, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy, random, string, scipy
import csv
import os
import pyglet


global mywin
global grating
global fixation
global blankletter
global centraltext
global xecc,yecc
global savetilt

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


# # set up the menu for choice of conditions
# myDlg = gui.Dlg(title="Divided Attention",size=(1, 1))
# myDlg.addField('StudentID:','xx')
# myDlg.addField('SessionNumber:',1)
# myDlg.addField('NumberofTrials',3)
# myDlg.addField('Eccentricity (pix)',200)
# myDlg.addField('Grating contrast (0-1)',.5)
# myDlg.addField('Grating frequency',.06)
# myDlg.addField('Grating diameter(pix)',50)
# myDlg.addField('Letter contrast (0-1)', -.5)
# myDlg.addField('Letter height (pix)',30)
# myDlg.addField('Task(G,N,or B)', 'G')
# myDlg.show()

# set up the menu for choice of conditions
sessioninfo = {}
sessioninfo['StudentID'] = 'xx'
sessioninfo['SessionNumber'] = 1
sessioninfo['NumberofTrials'] = 3
sessioninfo['Eccentricity (pix)'] = 200
sessioninfo['Grating contrast (0-1)'] = 0.5
sessioninfo['Grating frequency'] = .06
sessioninfo['Grating diameter(pix)'] = 50
sessioninfo['Letter contrast'] =  -1
sessioninfo['Letter height (pix)'] = 30
sessioninfo['Task(G,N,or B)'] =  'G'

myDlg = gui.DlgFromDict(sessioninfo)
if myDlg.OK:
    pass
    #sessioninfo=myDlg.data
else:
    print('cancelled') #Changed from print 'cancelled' to print(cancelled)
        

#window
WWIDTH,WHEIGHT,PX_SCALE = get_display_info()
mywin = visual.Window(size=[WWIDTH,WHEIGHT], monitor="testMonitor", units="pix",fullscr=True,
        screen=0, allowGUI=True, allowStencil=False, 
        color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True)
#rgb=[-1,-1,-1] makes screen black
random.seed()  #initializes by reading the time

#read values from menu and put in variables
idn=sessioninfo['StudentID']
sessnumber=sessioninfo['SessionNumber']
ntrials=sessioninfo['NumberofTrials']
eccent=sessioninfo['Eccentricity (pix)']
gratingcontrast=sessioninfo['Grating contrast (0-1)']
gratingfreq=sessioninfo['Grating frequency']
gratingdiam=sessioninfo['Grating diameter(pix)']
lettercontrast=sessioninfo['Letter contrast']
letterheight=sessioninfo['Letter height (pix)']
instruction=sessioninfo['Task(G,N,or B)'].upper()


# #read values from menu and put in variables
# idn=sessioninfo[0]
# sessnumber=sessioninfo[1]
# ntrials=sessioninfo[2]
# eccent=sessioninfo[3]*PX_SCALE
# gratingcontrast=sessioninfo[4]
# gratingfreq=sessioninfo[5]
# gratingdiam=sessioninfo[6]*PX_SCALE
# lettercontrast=sessioninfo[7]
# letterheight=sessioninfo[8]*PX_SCALE
# instruction=sessioninfo[9]

print(instruction) #Changed from print instruction to print(instruction)

#filename
filename=''
filename='divAttTilt_'
filename+=instruction[0]+'_'
filename+=idn
filename+='_'+str(sessnumber)
filename+='_'+data.getDateStr()
print(filename) #Changed from print filename to print(filename)
datetime=data.getDateStr()


#initialize things
savetilt=0
eccentneg= eccent * (-1)
eccentdiag = eccent * .707
eccentnegdiag = eccentdiag * (-1)
xecc=[ eccent, eccentdiag, 0, eccentnegdiag, eccentneg, eccentnegdiag, 0, eccentdiag]
yecc=[ 0, eccentdiag, eccent, eccentdiag, 0, eccentnegdiag, eccentneg, eccentnegdiag ]
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'T', 'U', 'W','X', 'Y']
all_letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'T', 'U', 'W','X', 'Y','a','b','c','d','e','f','g','h','j','k','l','m','n','p','r','t','u','w','x','y']
numerals=['0', '1', '2', '3', '4' ,'5' ,'6', '7', '8', '9']
numeraltarget=[]
letter=[]
letterseq=[]
letterresp=[]
gratingtilt=[]
gratingseq=[]


numPresented = [] #Correct Response to the target numeral
numResponse=[] #response to the target numeral
numCorrect=[]
locResponse=[]
locPresented=[]
locCorrect=[]


timebetweenframes = .083 #.083 gives about 12 letters/s.Same as JosephChunNakayama.since we're not counting frames,won't be exact  
LETTER_DURATION = 0.033
BLANK_DURATION = 0.050
FEEDBACK_DURATION = 2.0
#timebetweenframes = .04
noisecontrast=.7
nletterstoshow=len(letters)

grating= visual.GratingStim(win=mywin, mask="gauss", units="pix", size=gratingdiam, pos=[xecc[0],yecc[0]], sf=[gratingfreq,0],contrast=gratingcontrast)
#fixation = visual.GratingStim(win=mywin, size=15, pos=[0,0], sf=0, rgb= 1,contrast=.5)
fixation = visual.Circle(win=mywin,radius=6,units='pix', pos=[0,0],fillColor='black',lineColor='black',interpolate=True)
blankletter=visual.GratingStim(win=mywin, size=30, pos=[0,0],sf=0, color=(1,1,1), colorSpace='rgb', contrast=0)
trialClock = core.Clock()
centraltext=visual.TextStim(win=mywin, text='B',pos=[0,0],color=(1,1,1), colorSpace='rgb',contrast=lettercontrast,height=letterheight)
noiseTexture = numpy.random.rand(128,128)*2.0-1 #from demo visual_noise.py
noisepatch=visual.GratingStim(win=mywin, tex=noiseTexture, mask="gauss", units="pix", size=gratingdiam, pos=[xecc[0],yecc[0]], contrast=noisecontrast)

data = [("Trial", "Location Response","Actual Location","Location Correct?", \
         "Numeral Response", "Actual Numeral","Numeral Correct?","Condition")]

def write_file(filename):

    for i in range(0, ntrials):
        data.append((i+1, locResponse[i], locPresented[i], locCorrect[i],\
                      numResponse[i], numPresented[i], numCorrect[i],instruction))
    # create data directory
    if not os.path.exists('data'):
        os.makedirs('data')
    # write data
    with open('data/%s.csv' %(filename), 'w',newline='',encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter=',' )
        writer.writerows(data)

def orderletters(letters):                              #randomly select letters for display
    nletterstoshow=len(letters)
    letterstoshow=[0]*nletterstoshow  #initialize
    for m in range(nletterstoshow):
        mindex=random.randint(1,len(letters))-1
        letterstoshow[m]=letters[mindex]
    return letterstoshow
    
def picktargetletter(nletterstoshow):       #which is the target letter?
    targetletter=random.randint(5,nletterstoshow-5)-1   #target letter should not be too early or late
    return targetletter

def picktargetnumeral(numerals):                   #pick numeral to show
    targetnumeral=random.randint(0,len(numerals)-1)
    return targetnumeral
    
def pickletterwithgrating(targetletter,nl):         #decide when gratings will appear
    endletter=targetletter + 3                      #grating can appear up to 4 letters after the target letter
    if endletter > nl -3:                           #be sure it's not too late
        endletter = nl -3
    letterwithgrating = random.randint(targetletter-1,endletter)
    return letterwithgrating
    
def picktiltedgrating():                            #pick which grating is tilted
    whichgrating=random.randint(1,len(xecc)) - 1
    return whichgrating

def showblank():
    centraltext.contrast=0
    grating.contrast=0
    centraltext.draw()
    grating.draw()
    mywin.flip()

def blankScreen():
    
    mywin.flip(clearBuffer=True)
    mywin.flip()


def drawGabors(letterindex,whichgrating,letterwithgrating,tiltdirection):
    for n in range(len(xecc)):     #yes, do all of them
        grating.pos=(xecc[n],yecc[n])       #location
        noisepatch.pos=(xecc[n],yecc[n])       #location
        grating.ori=0
        # decide grating tilt direction
        if n == whichgrating:                #tilted grating  
            grating.ori=15 * tiltdirection
        else:
            grating.ori=0
        # decide whether to show gratings
        if letterindex in (letterwithgrating,letterwithgrating+1):  #show gratings?
            grating.contrast=gratingcontrast
            grating.draw()
        elif letterindex in (letterwithgrating+2,letterwithgrating+3):
            noisepatch.draw()
        else:
            grating.contrast=0
            grating.draw()

#the routine below is showing the critical displays, the stream of central letters and the single display of a 8 gabors
def showcriticaldisplay(letterstoshow,targetletter,letterindex,whichgrating,letterwithgrating,tiltdirection):

    if letterindex == targetletter:
        centraltext.contrast= lettercontrast*(-1)   #ek took out * (-1) so all have same contrast now
    else:
        centraltext.contrast = lettercontrast
    
    centraltext.text=letterstoshow[letterindex]                 #see set up of centraltext above
    mywin.clearBuffer()
    centraltext.draw()   #draw central letter
    #this is where the gratings appear
    drawGabors(letterindex,whichgrating,letterwithgrating,tiltdirection)
    mywin.flip()
    core.wait(LETTER_DURATION)
    mywin.clearBuffer()
    drawGabors(letterindex,whichgrating,letterwithgrating,tiltdirection)
    mywin.flip()
    core.wait(BLANK_DURATION)

    
#this is for taking a response that includes a display of 8 numerals at each grating location
def displaysometextandlocations(texttodisplay):
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],color=(1,1,1), colorSpace='rgb',contrast=1,height=letterheight)
    for n in range(len(xecc)):
        ttd=repr(n)  #convert to string
        numberprompt=visual.TextStim(win=mywin,text=ttd,pos=[xecc[n],yecc[n]],color=(1,1,1), colorSpace='rgb',contrast=1,height=letterheight)
        numberprompt.draw()
    prompt.draw()
    mywin.flip()
#displays any text.  Use for response
def displaysometext(texttodisplay):
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],color=(1,1,1), colorSpace='rgb',contrast=1,height=letterheight,wrapWidth=800)
    prompt.draw()
    mywin.flip()
#get response
def getresponse():
    k = event.waitKeys()
    event.clearEvents()
    b=k[0]
    if b=='escape':  #option to get out
        mywin.close()
        core.quit()
    return b
   

if instruction[0] in ('G','g'):
    print("firstloop ", instruction[0])
    instructions = """
    For this version of the experiment, please watch the circles presented and 
    try to detect and remember the location of the target circle whose grating 
    tilt differs from the rest.
    """
elif instruction[0] in ('N','n'):
    print(instruction[0])
    instructions = """
    For this version of the experiment, please pay attention to the alphanumeric 
    characters shown at the center of the array. Your task will be to detect and
    report the unique number presented among the set of letters.
    """
else:
    print(instruction[0])
    instructions = """
    For this version of the experiment, you will need to carry out two simultaneous tasks:

    First, you will need to pay attention to the alphanumeric characters shown at 
    the center of the array and remember theunique number presented among the set of letters.

    Second, you will need to watch the circles presented and try to detect and 
    remember the location of the target circle whose grating tilt differs from the rest.
    """
msg = visual.TextStim(win=mywin, text=instructions,wrapWidth=800)
msg.draw()
mywin.flip()
#k = ['']
k = event.waitKeys()

    
    
    
    
    
#run all trials
for itrial in range (0,ntrials):
    print("trial", itrial + 1) #Changed from print "trial", itrial + 1 to print("trial",itrial + 1)
    texttodisplay= 'Press any key to start Trial %d' % (itrial+1) 
    msg = visual.TextStim(win=mywin, text=texttodisplay)
    msg.draw()
    mywin.flip()

    k = ['']
    k = event.waitKeys()
  
    core.wait(1)
    letterstoshow=orderletters(letters)                         #select letters randomly
    targetletter=picktargetletter(len(letterstoshow))           #pick which is the target (different contrast)
    targetnumeral=picktargetnumeral(numerals)                   #pick target numeral
    
    letterstoshow[targetletter]=targetnumeral                   #replace the letter with the numeral
    letterwithgrating=pickletterwithgrating(targetletter,len(letterstoshow))  #decide when the gratings will appear
    whichgrating=picktiltedgrating()                                            #decide which grating is tilted
    lettertimer=core.Clock()                                        #define a clock to time events in th e trial
    letterindex=0
    #print "letterwithgrating", letterwithgrating
    tiltdirection=random.randint(1,2) # 1=right, -1 left.  Pick tilt direction.. Amt of tilt is in showcriticaldisplay
    if tiltdirection == 2:
        tiltdirection = -1  #left
    
    # show fixation
    mywin.clearBuffer()
    fixation.draw()
    mywin.flip()
    core.wait(0.5)
    mywin.clearBuffer()
    mywin.flip()
    core.wait(0.5)

    for letterindex in range (len(letterstoshow)):  #display all the letters
        #wait a bit
        
        # while lettertimer.getTime() < timebetweenframes:  
        #     showblank()                         
        #show stuff here
        showcriticaldisplay(letterstoshow,targetletter,letterindex,whichgrating,letterwithgrating,tiltdirection)
       
        if event.getKeys(keyList=['escape','q']):  #option to get out
            mywin.close()
            core.quit()

    targetletterresponse=10   #0 is within numerals 
    utargetletterresponse='0'
    if instruction[0] not in ('G', 'g'): #if B or N
        displaysometext("target numeral")
        # wait for numeral response
        while targetletterresponse not in numerals:
            targetletterresponse=getresponse()
     #   print targetletterresponse    
    
       # utargetletterresponse=targetletterresponse.upper()
        utargetletterresponse=str(targetletterresponse)                   #no more upper case
        feedback='response ' + targetletterresponse + '   Answer was   ' + str(targetnumeral)
        # feedback='response ' + utargetletterresponse + '   Answer was ' + targetnumeral
        
        
        displaysometext(feedback)
        core.wait(FEEDBACK_DURATION)
        gloc=repr(whichgrating)
        numResponse.append(targetletterresponse)
        numPresented.append(targetnumeral) #appends the correct target numeral
        numCorrect.append(targetnumeral==int(targetletterresponse))             
        
        
        if instruction in ('N', 'n'):
            locResponse.append("N/A")
            locPresented.append("N/A")
            locCorrect.append("N/A")
    
    gratinglocationresponse=9
    gloc = repr(whichgrating)
    
    if instruction[0] not in ('N', 'n'): #if B or G ask the location of the grating   
        displaysometextandlocations("Target location? (0-7)")
        locs=['0','1','2','3','4','5','6','7']
        while gratinglocationresponse not in locs:
            gratinglocationresponse=getresponse()

        feedback= 'Location response: ' + gratinglocationresponse + '  Actual location: ' + gloc
        displaysometext(feedback)
        core.wait(FEEDBACK_DURATION)
        locPresented.append(int(gloc))
        locResponse.append(gratinglocationresponse)
        locCorrect.append(int(int(gloc)==int(gratinglocationresponse)))
        if instruction in ('G', 'g'):
            numResponse.append("N/A")
            numPresented.append("N/A")
            numCorrect.append("N/A")
            

    
   
   
   # if len(event.getKeys())>0: break
   # event.clearEvents()
    
    
   
write_file(filename)
mywin.close()
core.quit()
