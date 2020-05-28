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

global mywin
global grating
global fixation
global blankletter
global centraltext
global xecc,yecc
global savetilt


# set up the menu for choice of conditions
myDlg = gui.Dlg(title="Divided Attention",size=(1, 1))
myDlg.addField('StudentID:','xx')
myDlg.addField('SessionNumber:',1)
myDlg.addField('NumberofTrials',3)
myDlg.addField('Eccentricity (pix)',200)
myDlg.addField('Grating contrast (0-1)',.5)
myDlg.addField('Grating frequency',.06)
myDlg.addField('Grating diameter(pix)',50)
myDlg.addField('Letter contrast (0-1)', -.5)
myDlg.addField('Letter height (pix)',30)
myDlg.addField('Task(G,N,or B)', 'G')
myDlg.show()
if myDlg.OK:
    sessioninfo=myDlg.data
else:
    print('cancelled') #Changed from print 'cancelled' to print(cancelled)
        

#window
mywin = visual.Window([800,600], monitor="testMonitor", units="pix")
#rgb=[-1,-1,-1] makes screen black
random.seed()  #initializes by reading the time


#read values from menu and put in variables
idn=sessioninfo[0]
sessnumber=sessioninfo[1]
ntrials=sessioninfo[2]
eccent=sessioninfo[3]
gratingcontrast=sessioninfo[4]
gratingfreq=sessioninfo[5]
gratingdiam=sessioninfo[6]
lettercontrast=sessioninfo[7]
letterheight=sessioninfo[8]
instruction=sessioninfo[9]

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


cTargetNums = [] #Correct Response to the target numeral
uTargetNums=[] #response to the target numeral
userResponse=[]
corrLocation=[]


timebetweenframes = .083 #.083 gives about 12 letters/s.Same as JosephChunNakayama.since we're not counting frames,won't be exact  
timebetweenframes = .04
noisecontrast=.7
nletterstoshow=len(letters)

grating= visual.GratingStim(win=mywin, mask="gauss", units="pix", size=gratingdiam, pos=[xecc[0],yecc[0]], sf=[gratingfreq,0],contrast=gratingcontrast)
fixation = visual.GratingStim(win=mywin, size=15, pos=[0,0], sf=0, rgb= 1,contrast=.5)
blankletter=visual.GratingStim(win=mywin, size=30, pos=[0,0],sf=0, rgb=1, contrast=0)
trialClock = core.Clock()
centraltext=visual.TextStim(win=mywin, text='B',pos=[0,0],rgb=1,contrast=lettercontrast,height=letterheight)
noiseTexture = scipy.random.rand(128,128)*2.0-1 #from demo visual_noise.py
noisepatch=visual.GratingStim(win=mywin, tex=noiseTexture, mask="gauss", units="pix", size=gratingdiam, pos=[xecc[0],yecc[0]], contrast=noisecontrast)

data = [("Trial", "User Response Location","Correct Location", "Numeral Response", "Correct Number")]

def write_file(filename):

    for i in range(0, ntrials):
        data.append((i+1, userResponse[i], corrLocation[i], uTargetNums[i], cTargetNums[i]))
    
    
    with open('%s.csv' %(filename), 'w') as fp:
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




#the routine below is showing the critical displays, the stream of central letters and the single display of a 8 gabors
def showcriticaldisplay(letterstoshow,targetletter,letterindex,whichgrating,letterwithgrating,tiltdirection):
    
    centraltext.text=letterstoshow[letterindex]                 #see set up of centraltext above
    if letterindex == targetletter:
        centraltext.contrast= lettercontrast   #ek took out * (-1) so all have same contrast now
    else:
        centraltext.contrast = lettercontrast
    centraltext.draw()   #draw central letter
    
    #this is where the gratings appear
    
    for n in range(len(xecc)):     #yes, do all of them
        grating.pos=(xecc[n],yecc[n])       #location
        noisepatch.pos=(xecc[n],yecc[n])       #location
        grating.ori=0
        if n == whichgrating:                #tilted grating  
            grating.ori=15 * tiltdirection
        else:
            grating.ori=0
        if letterindex==letterwithgrating:  #show gratings?
            grating.contrast=gratingcontrast
            
        else:
            grating.contrast=0
        for nframes in range(5):   #was 10
            if letterindex==letterwithgrating+1:
                noisepatch.draw()
            else:
                grating.draw()
    mywin.flip()
    core.wait(.02)

    blankScreen()
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
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],rgb=1,contrast=1,height=letterheight)
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
   

if instruction[0] == 'G' or 'g':
    print("firstloop ", instruction[0])
    instructions = "For the experiment x watch the circles presented and remember the location of the specific circle with a grating tilt different from the rest."
    msg = visual.TextStim(win=mywin, text=instructions)
    msg.draw()
    mywin.flip()    
    #k = ['']
    #k = event.waitKeys()
elif instruction[0] == 'N' or 'n':
    print(instruction[0])
    instructions = "For the 2 experiment pay attention to the letters shown and find the number presented in the set."
    msg = visual.TextStim(win=mywin, text=instructions)
    msg.draw()
    mywin.flip()
    #k = ['']
    #k = event.waitKeys()
else:
    instructions = "For the  3 experiment watch the circles presented and remember the location of the specific circle with a grating different from the rest. Also, remember the number in the series of letters."
    msg = visual.TextStim(win=mywin, text=instructions)
    msg.draw()
    mywin.flip()
    #k = ['']
    #k = event.waitKeys()

    
    
    
    
    
#run all trials
for itrial in range (0,ntrials):
    print("trial", itrial + 1) #Changed from print "trial", itrial + 1 to print("trial",itrial + 1)
    texttodisplay='Trial ' + repr(itrial+1) + '  Press key' 
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
    
    
    for letterindex in range (len(letterstoshow)):  #display all the letters
        #wait a bit
        
        while lettertimer.getTime() < timebetweenframes:  
            showblank()                         
        #show stuff here
        showcriticaldisplay(letterstoshow,targetletter,letterindex,whichgrating,letterwithgrating,tiltdirection)
        lettertimer.reset()  #reset timer for next wait
       
        if event.getKeys(keyList=['escape','q']):  #option to get out
            mywin.close()
            core.quit()

    targetletterresponse=10   #0 is within numerals 
    utargetletterresponse='0'
    if instruction[0] not in ('G', 'g'): #if B or N
        displaysometext("target numeral")
        
        while targetletterresponse not in numerals:
            targetletterresponse=getresponse()
     #   print targetletterresponse    
    
       # utargetletterresponse=targetletterresponse.upper()
        utargetletterresponse=str(targetletterresponse)                   #no more upper case
        feedback='response ' + targetletterresponse + '   Answer was   ' + str(targetnumeral)
        # feedback='response ' + utargetletterresponse + '   Answer was ' + targetnumeral
        
        
        displaysometext(feedback)
        core.wait(3)
        gloc=repr(whichgrating)
        uTargetNums.append(targetletterresponse)
        cTargetNums.append(targetnumeral) #appends the correct target numeral             
        
        
        if instruction in ('N', 'n'):
            userResponse.append("N/A")
            corrLocation.append("N/A")
    
    gratinglocationresponse=9
    gloc = repr(whichgrating)
    
    if instruction[0] not in ('N', 'n'): #if B or G ask the location of the grating 
        
        displaysometextandlocations("location(0-7)")
        
        locs=['0','1','2','3','4','5','6','7']
        while gratinglocationresponse not in locs:
            gratinglocationresponse=getresponse()
      #  gloc=repr(whichgrating)            
        feedback= 'Location response: ' + gratinglocationresponse + '  Location: ' + gloc
      
        displaysometext(feedback)
        core.wait(3)
        corrLocation.append(int(gloc))
        userResponse.append(gratinglocationresponse)
        
        
        if instruction in ('G', 'g'):
            uTargetNums.append("N/A")
            cTargetNums.append("N/A")
            

    
   
   
   # if len(event.getKeys())>0: break
   # event.clearEvents()
    
    
   
write_file(filename)
mywin.close()
core.quit()
