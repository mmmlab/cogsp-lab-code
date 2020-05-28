#visual_estm
#J Rubinstein   Oct 8, 2015
#based on.  
#E Kowler.  Aug 19, 2015
# updated C Aitkin to work with Apple Catalina OS Feb 25 2020

from psychopy import visual, core, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy, random, string, scipy
import csv
#import xlwt

global mywin
global grating
global fixation
global blankletter
global centraltext
global xecc,yecc
global savetilt



# set up the menu for choice of conditions
myDlg = gui.Dlg(title="Visual Short Term Memory",size=(1, 1))
myDlg.addField('Initials:','xx')
myDlg.addField('SessionNumber:',1)
myDlg.addField('NumberofTrials',40)
myDlg.addField('Time between Display 1 and 2', 1000)
myDlg.addField('Bar length', 100)
myDlg.addField('Bar width', 15)
myDlg.addField('Task (C,O,or E)')
myDlg.show()
if myDlg.OK:
    sessioninfo=myDlg.data
else:
    print('cancelled') #Changed from print 'cancelled' to print('cancelled')
        

#window
mywin = visual.Window([800,600], monitor="testMonitor", units="pix")
#rgb=[-1,-1,-1] makes screen black
random.seed()  #initializes by reading the time


#read values from menu and put in variables
idn=sessioninfo[0]
sessnumber=sessioninfo[1]
ntrials=sessioninfo[2] 
pause=sessioninfo[3]
barlength=sessioninfo[4]
barwidth=sessioninfo[5]
task=sessioninfo[6]

actual = []
response = []
nbarstostore=[]
taskstore=[]
print(task) #Changed from print task to print(task)

#filename
filename=''
filename='visstm_'
filename+=task[0]+'_'
filename+=idn
filename+='_'+str(sessnumber)
filename+='_'+data.getDateStr()
print(filename) #Changed from print filename to print(filename)
datetime=data.getDateStr()


#initialize things
displaytime = .25
#(seconds)
#possible x positions of bars...4 choices
barxpos = [-320, -160, 160, 320]
#possible y positions of bars...4 choices
barypos = [-240, -120, 120, 240]
barlocations = []

for x in barxpos:
    for y in barypos:
        barlocations.append([x,y])
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White']
orientation = [0, 45, 90, 135]
nbars = [2, 4, 6, 8]

dataFileWrite = [("Trial",
"Task",
"N objects",
"Actual",
"Response",
)]
#write  file with results
def write_file(filename):
    
    for i in range (0, ntrials): 
        dataFileWrite.append((i+1, taskstore[i],nbarstostore[i],actual[i],response[i]))

    with open('%s.csv' %(filename), 'w') as fp:
        writer = csv.writer(fp, delimiter=',' )
        writer.writerows(dataFileWrite)



def choosebars(nbars_trial):                              #randomly select bars for display
    alreadyloc = []
    bars=[0]*nbars_trial  #initialize
    print(nbars_trial) #Changed from print nbars_trial to print(nbars_trial)
    for b in range(nbars_trial):
   #     print b
   #     print bars
        barcolor = random.choice(colors)
        barori = random.choice(orientation)
        barloc = random.choice(barlocations)
        while barloc in alreadyloc:
            #check if there's already a bar at this location
            barloc = random.choice(barlocations)
        alreadyloc.append(barloc)
    #    print barlocations
    #    print barloc
        bars[b] = visual.Rect(mywin, width = barwidth, height = barlength)
        bars[b].pos = barloc
        bars[b].fillColor=barcolor
        bars[b].lineColor = barcolor
        bars[b].ori=barori
    z = [b.pos for b in bars]
    r = [b.fillColor for b in bars]
 #   print z
 #   print r
    return bars


        #core.wait(.5)  #uncomment to slow down for debugging
    
#show the display with the bars
def showdisplay(display, bars, diff):
    thistask='s' #default.  will change if display 2 and different
    if display == 2:
        #is second display
        if diff:
            #this display will be different
            d = random.randint(0, len(bars)-1)
            if task.lower() == 'e':
                #either...randomly choose color or orientation
                thistask = random.choice(['c','o'])
            else:
                thistask = task.lower()
            if thistask == 'c':
                prevcolor = bars[d].fillColor
                while prevcolor == bars[d].fillColor: #won't be the same color
                    newcolor = random.choice(colors)
                    bars[d].fillColor = newcolor
                    bars[d].lineColor = newcolor
            elif  thistask == 'o':
                prevori = bars[d].ori
                while prevori == bars[d].ori: #won't be the same orientation
                    bars[d].ori = random.choice(orientation)

    for b in range(len(bars)):
        bars[b].draw()
    
    mywin.flip()
    
    core.wait(displaytime)
    return thistask
   #return bars
#displays any text.  Use for response

def blankscreen():
    
    mywin.flip(clearBuffer=True)
    mywin.flip()
 #   print pause/1000.0
    core.wait(pause/1000.0)

def displaysometext(texttodisplay):
    prompt=visual.TextStim(win=mywin, text=texttodisplay,pos=[0,0],rgb=1,contrast=1)
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
   
   
#run all trials
for itrial in range (0,ntrials):
    print("trial", itrial + 1) #Changed print "trial", itrial + 1 to print("trial", itrial + 1)
    texttodisplay='Trial ' + repr(itrial+1) + '  Press key' 
    msg = visual.TextStim(win=mywin, text=texttodisplay)
    msg.draw()
    mywin.flip()

    k = ['']
    k = event.waitKeys()
  
    core.wait(1)
    nbarsnow=random.choice(nbars)
#    barstoshow=choosebars(random.choice(nbars)) #    
    barstoshow=choosebars(nbarsnow)
    lettertimer=core.Clock()                        #define a clock to time events in th e trial
    
    diff = bool(random.getrandbits(1))
    #randomly choose if this display will be different or the same
    
    #display displays
    thistask=showdisplay(1, barstoshow, diff)
    blankscreen()
    thistask=showdisplay(2, barstoshow, diff)
    
            
   #Trial over.  Take responses and give feedback         
    
    sdresponse=0
    utargetletterresponse='0'

    displaysometext("same or different?")
    
    while sdresponse not in ['s', 'd']:
        sdresponse=getresponse()
    responsediff = 0
    if sdresponse == 'd':
        sdtext = 'different'
    else:
        sdtext = 'same'
    response.append(sdresponse)
    if diff:
        actualtxt = 'different'
        actual.append('d')
    else:
        actualtxt = 'same'
        actual.append('s')
    feedback='response: ' + sdtext + '   Answer was: ' + actualtxt
#    if responsediff == diff:
#        feedback = 'Correct!'
#    else:
#        feedback = 'Incorrect...'
#    
    displaysometext(feedback)
    core.wait(2)
    
    
    
    #store trial dataFile
    
    nbarstostore.append(nbarsnow)
 #   print 'nbars', nbarstostore
    taskstore.append(str(thistask))
    
   
   # if len(event.getKeys())>0: break
   # event.clearEvents()
    
    
   
write_file(filename)
mywin.close()
core.quit()