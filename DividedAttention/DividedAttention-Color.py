#dividedattention_6.  
#E Kowler.  Aug 19, 2015
# C Asante March 6, 2017

#Based on Joseph, Chun & Nakayama (1997).Attentional requirements in a preattentive
#search task. Nature 387, 805-807.  dual-task format.  central and primary task:  monitor stream of letters for a targetletterw
#with different contrast.  Second task:  an array of 8 gabors will flash some time either slightly before or after the target letter.
#One gabor will be tilted.  Report direction of tilt and location in array of tilted grating.
#Joseph et al. report that performance is poor when grating flashes around the time of the target letter, indicating that even
#a "simple" early vision task (orientation identification) demands attention.

#Obtaining this result may depend on choice of parameters in the menu including Gabor contrast, letter contrast, and sizes.
#Also, Joseph et al. used a mask following the grating.  This has not been implemented here.

#Sept 21, 2015:  The target character is now a NUMERAL 
#March 6, 2017: Getting rid of tilt aspect of divided attention and instead turning it into colords instead of grating bars  

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


# set up the menu for choice of conditions
myDlg = gui.Dlg(title="Divided Attention",size=(1, 1))
myDlg.addField('StudentID:','xx')
myDlg.addField('SessionNumber:',1)
myDlg.addField('NumberofTrials',5)
myDlg.addField('Eccentricity (pix)',200)
#myDlg.addField('Grating contrast (0-1)',.5)
#myDlg.addField('Grating frequency',.06)
myDlg.addField('Grating diameter(pix)',50)
myDlg.addField('Letter contrast (0-1)', -.5)
myDlg.addField('Letter height (pix)',30)
myDlg.addField('Task(G,N,or B)', 'G')
myDlg.show()
if myDlg.OK:
    sessioninfo=myDlg.data
else:
    print('cancelled') #Changed from print 'cancelled' to print('cancelled')
        

#window
WWIDTH,WHEIGHT,PX_SCALE = get_display_info()
mywin = visual.Window(size=[WWIDTH,WHEIGHT], monitor="testMonitor", units="pix",fullscr=True,
        screen=0, allowGUI=True, allowStencil=False, 
        color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True)
#rgb=[-1,-1,-1] makes screen black
random.seed()  #initiali4zes by reading the time


#read values from menu and put in variables
idn=sessioninfo[0]
sessnumber=sessioninfo[1]
ntrials=sessioninfo[2]
eccent=sessioninfo[3]*PX_SCALE
#gratingcontrast=sessioninfo[4]
#gratingfreq=sessioninfo[5]
circleSize=sessioninfo[4]*PX_SCALE
lettercontrast=sessioninfo[5]
letterheight=sessioninfo[6]*PX_SCALE
instruction=sessioninfo[7]

print(instruction) #Changed from print instruction to print(instruction)

#filename
filename=''
filename='divattn_'
filename+=instruction[0]+'_'
filename+=idn
filename+='_'+str(sessnumber)
filename+='_'+data.getDateStr()
print(filename) #Changed form print filename to print(filename)
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



corrLocation=[]             #List of Correct color location

userResponse=[]             #List of user Responses on the Location of the different colored circle


timebetweenframes = .083 #.083 gives about 12 letters/s.Same as JosephChunNakayama.since we're not counting frames,won't be exact  
#timebetweenframes = .04
noisecontrast=.7
nletterstoshow=len(letters)

#grating= visual.GratingStim(win=mywin, mask="gauss", units="pix", size=gratingdiam, pos=[xecc[0],yecc[0]], sf=[gratingfreq,0],contrast=gratingcontrast)

rad = circleSize / 2
colorDiff = '#3373FF' #A slightly lighter shade of blue
mainColor = '#3346FF' #Blue
circle = visual.Circle(mywin,radius = rad, edges = 32)
#fixation = visual.GratingStim(win=mywin, size=15, pos=[0,0], sf=0, rgb= 1,contrast=.5)
blankletter=visual.GratingStim(win=mywin, size=30, pos=[0,0],sf=0, rgb=1, contrast=0)
trialClock = core.Clock()
centraltext=visual.TextStim(win=mywin, text='B',pos=[0,0],rgb=1,contrast=lettercontrast,height=letterheight)
#noiseTexture = scipy.random.rand(128,128)*2.0-1 #from demo visual_noise.py
#noisepatch=visual.GratingStim(win=mywin, tex=noiseTexture, mask="gauss", units="pix", size=gratingdiam, pos=[xecc[0],yecc[0]], contrast=noisecontrast)




#write excel file with results

data = [("Trial", "User Response","Correct Location")]

def write_file(filename):
    for i in range(0, ntrials):
        data.append((i+1, userResponse[i], corrLocation[i]))
    # create data directory
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/%s.csv' %(filename), 'w') as fp:
        writer = csv.writer(fp, delimiter=',' )
        writer.writerows(data)

#delimiter=','

#    sheet1 = book.add_sheet("Sheet 1")
#    sheet1.write(0, 0, "Divided Attention")
#    sheet1.write(1, 0, "Subject:%s"%idn)     
#    sheet1.write(2, 0, "SessionNumber:%d"%sessnumber)
#    sheet1.write(3, 0, "Instruction:%s" %instruction)
#    sheet1.wdrite(4, 0, "Eccentricity:%d" %eccent)
#    sheet1.write(5, 0, "GratingContrast:%f"%gratingcontrast)
#    sheet1.write(6, 0, "Frequency(c/pix):%f"%gratingfreq)
#    sheet1.write(7, 0, "GratingDiam(pix):%d"%gratingdiam)
#    sheet1.write(8, 0, "LetterContrast: %f"%lettercontrast)
#    sheet1.write(9, 0, "LetterHeight(pix):%d"%letterheight)
#    #column labels
#    sheet1.write(11, 0, "Trial")
#    sheet1.write(11, 1, "N:Seq")
#    sheet1.write(11, 2, "G:Seq")
#    sheet1.write(11, 3, "N")
#    sheet1.write(11, 4, "N:Resp")
#    sheet1.write(11, 5, "G:Tilt")
#    sheet1.write(11, 6, "G:TResp")
#    sheet1.write(11, 7, "G:Loc")
#    shee`t1.write(11, 8, "G:LResp")
#below is info for each trial

#    for i in range (0, ntrials):
#        sheet1.write(i+12, 0, i+1)          #trial
#        sheet1.write(i+12, 1, letterseq[i]) #sequential position of numeral
#        sheet1.write(i+12, 2, gratingseq[i])#sequential position of grating
#        sheet1.write(i+12, 3, letter[i])    #numeral
#        sheet1.write(i+12, 4, letterresp[i]) #numeral response
#        sheet1.write(i+12, 5, gratingtilt[i]) #grating tilt
#        sheet1.write(i+12, 6, gratingTresponse[i])  #grating tilt response
#        sheet1.write(i+12, 7, gratinglocation[i])       #grating location
#        sheet1.write(i+12, 8, gratinglocresponse[i])    #grating location response
        
#    filename+='.xls'
#    book.save(filename)



def orderletters(letters):                              #randomly select letters for display
    nletterstoshow=len(letters)
    letterstoshow=[0]*nletterstoshow  #initialize
    for m in range(nletterstoshow):
        mindex=random.randint(1,len(letters))-1
        letterstoshow[m]=letters[mindex]
    return letterstoshow
    
def picktargetletter(nletterstoshow):                  #which is the target letter?
    targetletter=random.randint(5,nletterstoshow-5)-1   #target letter should not be too early or late
    return targetletter

def picktargetnumeral(numerals):                   #pick numeral to show
    targetnumeral=random.randint(0,len(numerals)-1)
    return targetnumeral
    
def pickletterwithgrating(targetletter,nl):         #decide when colored circles will appear
    endletter=targetletter + 3                      #grating can appear up to 4 letters after the target letter
    if endletter > nl -3:                           #be sure it's not too late
        endletter = nl -3
    letterwithgrating = random.randint(targetletter-1,endletter)
    return letterwithgrating
    
def pickColoredCircle():                            #pick which grating is tilted
    whichCircle=random.randint(1,len(xecc)) - 1
    return whichCircle

def showblank():
    centraltext.contrast=0
    #grating.contrast=0
    centraltext.draw()
    #circle.draw()
    mywin.flip()
    
    
#the routine below is showing the critical displays, the stream of central letters and the single display of a 8 gabors


#get rid of everything that has to do with the grating and instead turn it into referencing the lighter shade of the color 





def showcriticaldisplay(letterstoshow,targetletter,letterindex,whichCircle,letterwithgrating,tiltdirection):
    
    centraltext.text=letterstoshow[letterindex]                 #see set up of centraltext above
    if letterindex == targetletter:
        centraltext.contrast= lettercontrast   #ek took out * (-1) so all have same contrast now
    else:
        centraltext.contrast = lettercontrast
    centraltext.draw()   #draw central letter
    for n in range (len(xecc)):     #yes, do all of them
        circle.pos=(xecc[n],yecc[n])       #location
        #noisepatch.pos=(xecc[n],yecc[n])       #location
        #grating.ori=0
        if n == whichCircle:                
            circle.fillColor = colorDiff
            circle.lineColor = colorDiff
        else:
            circle.fillColor = mainColor
            circle.lineColor = mainColor
        if letterindex==letterwithgrating:  #show gratings?
            circle.contrast= .5  
        else:
            circle.contrast=0
        circle.draw()
    mywin.flip()
    core.wait(.02)

        #core.wait(.5)  #uncomment to slow down for debugging
    
#this is for taking a response that includes a display of 8 numerals at each grating location
def displaysometextandlocations(texttodisplay):
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],rgb=1,contrast=1,height=letterheight)
    for n in range(len(xecc)):
        ttd=repr(n)  #convert to string
        numberprompt=visual.TextStim(win=mywin,text=ttd,pos=[xecc[n],yecc[n]],rgb=1,contrast=1,height=letterheight)
        numberprompt.draw()
    prompt.draw()
    mywin.flip()
#displays any text.  Use for response
def displaysometext(texttodisplay):
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],rgb=1,contrast=1,height=letterheight,wrapWidth=800)
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
    try to detect and remember the location of the target circle whose color
    differs from the rest.
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
    remember the location of the target circle whose color differs from the rest.
    """
msg = visual.TextStim(win=mywin, text=instructions,wrapWidth=800)
msg.draw()
mywin.flip()
#k = ['']
k = event.waitKeys()
   
   
#run all trials
for itrial in range (0,ntrials):
    print("trial", itrial + 1) #Changed from print "trial", itrial + 1 to print("trial", itrial + 1)
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
    
    whichCircle=pickColoredCircle()                                            #decide which grating is tilted
    
    lettertimer=core.Clock()                                        #define a clock to time events in th e trial
    
    letterindex=0
    
    #print "letterwithgrating", letterwithgrating
    # 1=right, -1 left.  Pick tilt direction.. Amt of tilt is in showcriticaldisplay
    #if tiltdirection == 2:
    #    tiltdirection = -1  #left
    
    
    for letterindex in range (len(letterstoshow)):  #display all the letters
        #wait a bit
        
        while lettertimer.getTime() < timebetweenframes:  
            showblank()                         
        #show stuff here
        showcriticaldisplay(letterstoshow,targetletter,letterindex,whichCircle,letterwithgrating,colorDiff)
        lettertimer.reset()  #reset timer for next wait
       
        if event.getKeys(keyList=['escape','q']):  #option to get out
            mywin.close()
            core.quit()
            
   #Trial over.  Take responses and give feedback         
    
    targetletterresponse=0
    utargetletterresponse='0'
    if instruction[0] not in ('G', 'g'):
        displaysometext("target numeral")
        
        while targetletterresponse not in numerals:
            targetletterresponse=getresponse()
     #   print targetletterresponse    
       # utargetletterresponse=targetletterresponse.upper()
        utargetletterresponse=str(targetletterresponse)                   #no more upper case
        feedback='response ' + targetletterresponse + '   Answer was   ' + str(targetnumeral)
        # feedback='response ' + utargetletterresponse + '   Answer was ' + targetnumeral
        displaysometext(feedback)
        core.wait(1)
    
    #print "tiltdirection", tiltdirection
    #set up variables for data file writing
    gratingtiltresponse=0
    ugratingtiltresponse='0'
    #if tiltdirection < 0:
    #    tilt= 'L'
    #elif tiltdirection > 0:
    #    tilt='R'
    gloc=repr(whichCircle)
    gratinglocationresponse=9
    if instruction[0] not in ('N', 'n'):
        #displaysometext("grating tilt, type L or R ")
        #while gratingtiltresponse not in ['l', 'r', 'L', 'R']:
        #    gratingtiltresponse=getresponse()
        #    ugratingtiltresponse=gratingtiltresponse.upper()
        displaysometextandlocations("Target location? (0-7)")
        locs=['0','1','2','3','4','5','6','7']
        while gratinglocationresponse not in locs:
            gratinglocationresponse=getresponse()
      #  gloc=repr(whichgrating)            
       # feedback = 'tilt response ' + ugratingtiltresponse + '    Tilt=' + tilt + '\n' \
        feedback = 'Location response =  ' + gratinglocationresponse + '  Actual location=' + gloc
      
        displaysometext(feedback)
        core.wait(3)
  
    #store trial dataFile
    #letter.append(letterstoshow[targetletter])
    #letter.append(str(targetnumeral))
    #print letter
   # letterseq.append(targetletter+1)
    #print letterseq
    #    letterresp.append(targetletterresponse)
    #print letterresp
   # gratingtilt.append(tilt)
    #print gratingtilt
   # gratingseq.append(letterwithgrating+1)
    #print gratingseq
    corrLocation.append(int(gloc))
    #print gratinglocation
   # gratingTresponse.append(ugratingtiltresponse)
    #print gratingTresponse
    userResponse.append(int(gratinglocationresponse))
    #print gratinglocresponse
    
   
   
   # if len(event.getKeys())>0: break
   # event.clearEvents()
    
    
   
write_file(filename)
mywin.close()
core.quit()
