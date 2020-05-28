#VSTM2.
#Christina  June 2016
#Based on Bays&Hussain(2008) Science.  321, 851-854.
#Each trial: two displays.  Orientation (tilt) of one item in second display is different from 
#corresponding item.  Independent variable: delta-tilt.  Chosen randomly from array of 5 with
#center value = zero.  
#If task is too hard, make delta tilts larger.


#based on VSTM, J Rubinstein   Oct 8, 2015
#based on.  
#E Kowler.  Aug 19, 2015


from psychopy import visual, core, gui, data, event, sound
from psychopy.tools.filetools import fromFile, toFile
import time, numpy, random, string, scipy
import xlwt

global mywin
global grating
global fixation
global blankletter
global centraltext
global xecc,yecc
global savetilt



# set up the menu for choice of conditions
myDlg = gui.Dlg(title="Visual Short Term Memdory",size=(1, 1))
myDlg.addField('Initials:','xx')
myDlg.addField('SessionNumber:',1)
myDlg.addField('NumberofTrials',10)
myDlg.addField('Time between Display 1 and 2', 1000)
#myDlg.addField('Task (C,O,or E)')
myDlg.show()
if myDlg.OK:
    sessioninfo=myDlg.data
else:
    print 'cancelled'
        

#window
mywin = visual.Window([800,600], monitor="testMonitor", units="pix")
#rgb=[-1,-1,-1] makes screen black
random.seed()  #initializes by reading the time


#read values from menu and put in variables
idn=sessioninfo[0] # Sets idn equal to initials
sessnumber=sessioninfo[1] #sets equal to Session nummber
ntrials=sessioninfo[2] #sets n trial equal to number of trials
pause=sessioninfo[3]#sets equal to Time between display one and two
#task=sessioninfo[4] #Task C O E

actual = []
response = []
nbarstostore=[]
taskstore=[]
tiltchange = []
#print task

#filename
filename=''
filename='visstm2_'
#filename+=task[0]+'_' #adds Task C O E _
filename+=idn
filename+='_'+str(sessnumber)
filename+='_'+data.getDateStr()
print filename
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
nbars = [2, 4, 6]                   #displays will be either 2 4 or 6 bars
barlength = 100  #used to be 50
barwidth = 15  #used to be 10
delta_tilt = [-20, -10, 0, 10, 20]  #change these to adjust task difficulty

#write excel file with results
def write_file(filename):
    
    #write stuff at beginning
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(0, 0, "Visual Short Term Memory")
    sheet1.write(1, 0, "Subject:%s"%idn)     
    sheet1.write(2, 0, "SessionNumber:%d"%sessnumber)
    #sheet1.write(3, 0, "Task:%s" %task)
    sheet1.write(4, 0, "Inter-display time:%d" %pause)
    #column labels
    sheet1.write(11, 0, "Trial")
 #   sheet1.write(11, 1, "Task")  #dont need.  relevant to VSTM1
    sheet1.write(11, 1, "N objects")
 #   sheet1.write(11, 3, "Actual")  #dont need
    sheet1.write(11, 2, "Response")
    sheet1.write(11,3,"Delta Tilt")

#below is info for each trial

    for i in range (0, ntrials): 
        sheet1.write(i+12, 0, i+1)                      # trial
      #  sheet1.write(i+12, 1, taskstore[i])             # task
        sheet1.write(i+12, 1, nbarstostore[i])          # how many bars were on the screen
     #   sheet1.write(i+12, 3, actual[i - 1])            # the correct answer
        sheet1.write(i+12, 2, response[i])              # the users response (SHOULD BE EXPRESSES AS -1 IF CCW and 1 IF CW)
        sheet1.write(i+12, 3, tiltchange[i])            # Array of the correct delta_tilt values for display 2 (CW OR CCW)
        #sheet1.write(i+12, 3, d)    #same or different?
        
        
    filename+='.xls'
    book.save(filename)
# SAVE USERS RESPONSE AS SPECIFIC VALUE

def choosebars(nbars_trial):                              #randomly select bars for display
    alreadyloc = []
    bars=[0]*nbars_trial  #initialize
    print nbars_trial
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
        bars[b] = visual.Rect(mywin, width = barwidth, height = barlength) #bars is the display of bars
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


def showdisplay(display, bars): #diff):
    global critical_item
    global critical_ori
    
    thistask='s' #default.  will change if display 2 and different
    
    
    critical_item = random.choice(bars) #chooses a random bar and assigns it to critical item
    prevori = critical_item.ori                  #Prevori is display 1 orientation
    
    if display == 2:
        critical_ori = random.choice(delta_tilt) #critical_ori is assigned to delta_tilt
        critical_item.ori = critical_ori + prevori #The degree tilt is added to the previous orientation of the critical item
        
   
    
    for b in range(len(bars)):
        bars[b].draw()  #draw in buffer
    
    mywin.flip() #flip buffer to display
    
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
    print "trial", itrial + 1
    texttodisplay='Trial ' + repr(itrial+1) + '  Press key'     #to display trial number
    msg = visual.TextStim(win=mywin, text=texttodisplay)        #for displaying trial number
    msg.draw()                                                      #draw (actually, writes to a buffer)
    mywin.flip()                                                    #flip = display now

    k = ['']
    k = event.waitKeys()                                        #psychopy function. wait for button press
  
    core.wait(1)
    nbarsnow=random.choice(nbars)                           #choos how many bars
#    barstoshow=choosebars(random.choice(nbars)) #    
    barstoshow=choosebars(nbarsnow)                 #choosebars is a function.  see above
    lettertimer=core.Clock()                        #define a clock to time events in th e trial
    
    #diff = bool(random.getrandbits(1))
    #randomly choose if this display will be different or the same
    
    #display displays
    thistask=showdisplay(1, barstoshow)#, diff)               #showdisplay is a function see above
    
    blankscreen()
    
    thistask=showdisplay(2, barstoshow)#, diff)
    
    tiltchange.append(critical_ori)
   
   #Trial over.  Take responses and give feedback         
    
    sdresponse=0
    utargetletterresponse='0'

    displaysometext("clockwise (press 'M') or counterclockwise (press 'Z')?")  #function, above
    
    while sdresponse not in ['m','z']:
        sdresponse=getresponse()    #function, above
        #responsediff = 0
    
    if sdresponse == 'm':    #checks if its going clockwise
        sdtext = 'clockwise'
        response.append(1)
    else:
       sdtext = 'counterclockwise'
       response.append(-1)
       
       
    
    
    
    
    
    
    if critical_ori < 0:
        actualtxt = 'counterclockwise' #What the user sees
        actual.append('CCW')                   #Actual List response
        
    else:
        actualtxt = 'clockwise'
        actual.append('CW')
    
    
    
    #if diff:
    #    actualtxt = 'different'
    #   actual.append('d')
    #else:
    #   actualtxt = 'same'
    #   actual.append('s')"""
    
    
    feedback='response: ' + sdtext + '   Answer was: ' + actualtxt + ' ' + str(critical_ori)
    


#   if responsediff == diff:
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
    
    #letter.append(str(target))
    #letter.append(letterstoshow[targetletter])
#    print letter
#    letterseq.append(targetletter+1)
#    print letterseq
#    letterresp.append(targetletterresponse)
#    print letterresp
#    gratingtilt.append(tilt)
#    print gratingtilt
#    gratingseq.append(letterwithgrating+1)
#    print gratingseq
#    gratinglocation.append(int(gloc))
#    print gratinglocation
#    gratingTresponse.append(ugratingtiltresponse)
#    print gratingTresponse
#    gratinglocresponse.append(int(gratinglocationresponse))
#    print gratinglocresponse
#    
   
   
   # if len(event.getKeys())>0: break
   # event.clearEvents()
    
    
   
write_file(filename)
mywin.close()
core.quit()