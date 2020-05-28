# unit: pixels on the screen
from psychopy import visual, core, event, monitors,data
from psychopy import gui
from pyglet.window import key
import xlwt
import random
import math
s = False
global win
result=[]
def write_file(file,sq_contrast):
    global result
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(0, 0, "ExperimentName:%s"%name)
    sheet1.write(1, 0, "Student Initial:%s"%ID)
    sheet1.write(2, 0, "SessionNumber:%d"%session)
    sheet1.write(3, 0, "Trail#")
    sheet1.write(3, 1, "barContrast")
    sheet1.write(3, 2, "response")
    for i in range(0,len(result)):
        sheet1.write(i+4, 0, i+1)
        sheet1.write(i+4, 1, sq_contrast)
        sheet1.write(i+4, 2, result[i])
    file+='.xls'
    book.save(file) 
def show_rec(contrast):
    global win,result,showbox2
    square_len=210
    square_width=10
    square_color=[i*contrast for i in [255.0,255.0,255.0]] # contrast of the bars
    rm=10; # radius of motion
    r=square_len/2 # radium for the occluder
    # set square motion
    angular_speed=0.11 # angular speed, radian per second
    duration=3 # seconds
    # set square occluder shape,size,contrast
    occ_size=100
    occ_contrast=0.4
    # set circular background shape,size,contrast
    cir_size=80
    cir_contrast=occ_contrast
    # set aperture shape,loc, size,contrast
    aperture_height=40
    aperture_len=2*(r-occ_size/2)
    aperture_contrast=0.1
    #create stimuli: 1 square,4 apertures and 4 square occluders and 4 circular background
    # 4 occluders
    square_loc_initial=[0,0]
    occ_locsx=[r,r,-r,-r]
    occ_locsy=[r,-r,-r,r]
    occ1=visual.Rect(win,units='pix',fillColor=1,width=occ_size,height=occ_size,contrast=occ_contrast,pos=(occ_locsx[0],occ_locsy[0]));
    occ2=visual.Rect(win,units='pix',fillColor=1,width=occ_size,height=occ_size,contrast=occ_contrast,pos=(occ_locsx[1],occ_locsy[1]));
    occ3=visual.Rect(win,units='pix',fillColor=1,width=occ_size,height=occ_size,contrast=occ_contrast,pos=(occ_locsx[2],occ_locsy[2]));
    occ4=visual.Rect(win,units='pix',fillColor=1,width=occ_size,height=occ_size,contrast=occ_contrast,pos=(occ_locsx[3],occ_locsy[3]));
    # 4 circular background
    cir_locsx=occ_locsx
    cir_locsy=occ_locsy
    cir1=visual.Circle(win,units='pix',fillColor=1,radius=cir_size,contrast=cir_contrast,pos=(cir_locsx[0],cir_locsy[0]));
    cir2=visual.Circle(win,units='pix',fillColor=1,radius=cir_size,contrast=cir_contrast,pos=(cir_locsx[1],cir_locsy[1]));
    cir3=visual.Circle(win,units='pix',fillColor=1,radius=cir_size,contrast=cir_contrast,pos=(cir_locsx[2],cir_locsy[2]));
    cir4=visual.Circle(win,units='pix',fillColor=1,radius=cir_size,contrast=cir_contrast,pos=(cir_locsx[3],cir_locsy[3]));
    # 4 apertures
    aperture_locsx=[0,r,0,-r]
    aperture_locsy=[r,0,-r,0]
    apert1=visual.Rect(win,units='pix',lineColorSpace='rgb255',lineColor=[x*aperture_contrast for x in [255,255,255]],fillColorSpace='rgb255',fillColor=[x*aperture_contrast for x in [255,255,255]],contrast=aperture_contrast,width=aperture_len,height=aperture_height,pos=(aperture_locsx[0],aperture_locsy[0]))
    apert2=visual.Rect(win,units='pix',lineColorSpace='rgb255',lineColor=[x*aperture_contrast for x in [255,255,255]],fillColorSpace='rgb255',fillColor=[x*aperture_contrast for x in [255,255,255]],contrast=aperture_contrast,width=aperture_height,height=aperture_len,pos=(aperture_locsx[1],aperture_locsy[1]))
    apert3=visual.Rect(win,units='pix',lineColorSpace='rgb255',lineColor=[x*aperture_contrast for x in [255,255,255]],fillColorSpace='rgb255',fillColor=[x*aperture_contrast for x in [255,255,255]],contrast=aperture_contrast,width=aperture_len,height=aperture_height,pos=(aperture_locsx[2],aperture_locsy[2]))
    apert4=visual.Rect(win,units='pix',lineColorSpace='rgb255',lineColor=[x*aperture_contrast for x in [255,255,255]],fillColorSpace='rgb255',fillColor=[x*aperture_contrast for x in [255,255,255]],contrast=aperture_contrast,width=aperture_height,height=aperture_len,pos=(aperture_locsx[3],aperture_locsy[3]))
    # draw
    cir1.draw();cir2.draw(); cir3.draw(); cir4.draw();apert1.draw();apert2.draw();apert3.draw();apert4.draw();occ1.draw();occ2.draw(); occ3.draw(); occ4.draw();
    
    # show motion
    for i in range(0,200): # 200 frames
        # square_loc=(rm*math.cos(angular_speed*i)+square_loc_initial[0],rm*math.sin(angular_speed*i)+square_loc_initial[1]);
        square_loc=(rm*math.cos(angular_speed*i)+square_loc_initial[0],rm*math.sin(angular_speed*i)+square_loc_initial[1]);
        square=visual.Rect(win,units='pix',lineColorSpace='rgb255',lineColor=[255,255,255],opacity=1,lineWidth=square_width,width=square_len,height=square_len,contrast=square_contrast,pos=(square_loc));   
       # square.colorSpace='rgb'
        cir1.draw();cir2.draw(); cir3.draw(); cir4.draw();apert1.draw();apert2.draw();apert3.draw();apert4.draw();square.draw();occ1.draw();occ2.draw(); occ3.draw(); occ4.draw();
        if i==199:
            showbox2.draw()
        win.update();
        core.wait(duration/200)
    while True:
        keylist=event.waitKeys()
        if 'escape' in keylist:
            print 'exit by the users'
            result.append('NULL')
            mywin.close()
            core.quit()
            break 
        elif '1' in keylist:
            result.append(int(1))
            break
        elif '2' in keylist:
            result.append(int(2))
            break
        elif '3' in keylist:
            result.append(int(3))
            break
        else:
            # print 'incorrect key. ..Press 1 for incoherent, 2 for intermediate and 3 for coherent'
            cir1.draw();cir2.draw(); cir3.draw(); cir4.draw();apert1.draw();apert2.draw();apert3.draw();apert4.draw();square.draw();occ1.draw();occ2.draw(); occ3.draw(); occ4.draw();
            showbox2.setText('Incorrect key. Press 1 for incoherent, 2 for intermediate and 3 for coherent')
            showbox2.draw()
            win.update()
            continue
    
def show_instruction():
     global win
     instr=visual.SimpleImageStim(win, image='instruction.png', units='', pos=(0.0, 0.0), flipHoriz=False, flipVert=False, name=None, autoLog=None)
     instrStim = visual.BufferImageStim(win, stim = [instr])
     instrStim.draw()
     win.flip()
     while True:
        if len(event.getKeys())>0: break
     event.clearEvents()
# show GUI
myDlg = gui.Dlg(title="Motion Coherence Experiment:Aperture",size=(1, 1))
myDlg.addField('ExperimentName:','Effect of Aperture')
myDlg.addField('Student Initial:','xh')
myDlg.addField('SessionNumber:',001)
myDlg.addField('Contrast(from 0 to 1):',001)
myDlg.addField('NumberofTrials',5)
myDlg.show()
if myDlg.OK:
    thisInfo = myDlg.data
    name='Motion2'
    ID=thisInfo[1]
    session=thisInfo[2]
    contrast=thisInfo[3]
    trials=thisInfo[4]
    file=''
    file+=name
    # file+='_BarContrast'+str(contrast)
    file+='_'+ID
    file+='_Session'+str(session)
    file+='_'+data.getDateStr()
    print file
    keyState=key.KeyStateHandler()
    win = visual.Window( monitor="testMonitor", units="pix",allowGUI=True,fullscr=False)
    win.winHandle.push_handlers(keyState)
    show_instruction()
    # instruction between trials
    showbox1=visual.TextStim(win,
                        font='Arial',
                        height=0.09,
                        # font_color=[0,0,0],
                        # dpi=72,
                        # size=(1.8,0.6),
                        pos=(0.0,0), 
                        units='norm',
                        alignHoriz='center',
                        alignVert='center',
                        colorSpace='rgb255'
                        )
    global showbox2
    showbox2=visual.TextStim(win,
                        text='Response: 1 (incoherent), 2 (intermediate coherence), 3 (coherent)', 
                        font='Arial',
                        height=0.07,
                        # font_color=[0,0,0],
                        # dpi=72,
                        # size=(1.8,0.6),
                        pos=(0.0,-0.7), 
                        units='norm',
                        alignHoriz='center',
                        alignVert='center',
                        colorSpace='rgb255'
                        )
    square_contrast=contrast;  # temporary, can be changed for future use
    for x in range(0,trials):
        if s==True:
            break;
                # show instruction between trials
        showbox1.setText('Trial% .0f: Hit any key to see the display' %(x+1))
        showbox2.setText('Response: 1 (incoherent), 2 (intermediate coherence), 3 (coherent)')
        showbox1.draw()
        win.flip()
        # wait for user input
        while True:
            if len(event.getKeys())>0: break
        event.clearEvents()
        show_rec(square_contrast);
    write_file(file,contrast)
else:
    print 'user cancelled'

