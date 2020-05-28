from psychopy import visual, core, event, data
from psychopy import gui
# from win32api import GetSystemMetrics
from pyglet.window import key
import xlwt
import random
s = False
result=[]
def write_file(file,length,mueller):
    global result
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(0, 0, "ExperimentName:%s"%name)
    sheet1.write(1, 0, "SubjectID:%s"%ID)
    sheet1.write(2, 0, "SessionNumber:%d"%session)
    sheet1.write(3, 0, "Trial#")
    sheet1.write(3, 1, "StandardLength")
    sheet1.write(3, 2, "Mueller-Lyer?")
    sheet1.write(3, 3, "ComparisionLength")
    for i in range(0,len(result)):
        sheet1.write(i+4, 0, i+1)
        sheet1.write(i+4, 1, length)
        sheet1.write(i+4, 2, mueller)
        sheet1.write(i+4, 3, result[i])
    file+='.xls'
    book.save(file)
def show_normal(length):
    jetter=random.uniform(-0.05, 0.05)
    global win
    global textbox
    winWidth = 1000
    s_length=length/(winWidth/2.00)
    c_length=random.uniform(length*0.8,length*1.2)/(winWidth/2.00)
    s_line = visual.ShapeStim(win, vertices= [[-s_length+jetter,0], [0+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    c_line = visual.ShapeStim(win, vertices= [[0+jetter,0], [c_length+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    l_line = visual.ShapeStim(win, vertices= [[-s_length+jetter,-0.05], [-s_length+jetter,0.05]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    m_line = visual.ShapeStim(win, vertices= [[0+jetter,-0.05], [0+jetter,0.05]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    r_line = visual.ShapeStim(win, vertices= [[c_length+jetter,-0.05], [c_length+jetter,0.05]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    textbox.setText('This is trial %s\nThe left line is the standard, and the right line is the comparison.\nPress J to INCREASE the comparison by 10 pixels\nPress F to DECREASE the comparison by 10 pixels.\nPress H to INCREASE the comparison by 1 pixel\nPress G to DECREASE the comparison by 1 pixel.\nPress Q when done with this trial.\nPress Esc to end the session early'%str(x+1))
    textbox.draw()
    s_line.draw()
    c_line.draw()
    m_line.draw()
    l_line.draw()
    r_line.draw()
    win.flip()
    while True:
        keylist=event.getKeys()
        if 'q' in keylist:
            global result
            result.append(int(c_length*(winWidth/2)))
            print 'insert new length to c_length list'
            break 
        elif keyState[key.J]:
            if c_length<1:
                c_length=c_length+1/(winWidth/2.00)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line.setVertices([[c_length+jetter,-0.05],[c_length+jetter,0.05]])
            textbox.draw()
            s_line.draw()
            m_line.draw()
            c_line.draw()
            l_line.draw()
            r_line.draw()
            win.flip()
        elif keyState[key.H]:
            if c_length<1:
                c_length=c_length+0.1/(winWidth/2.00)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line.setVertices([[c_length+jetter,-0.05],[c_length+jetter,0.05]])
            textbox.draw()
            s_line.draw()
            m_line.draw()
            c_line.draw()
            l_line.draw()
            r_line.draw()
            win.flip()
        elif keyState[key.F]:
            if c_length>0.002:
                c_length=c_length-1/(winWidth/2.00)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line.setVertices([[c_length+jetter,-0.05],[c_length+jetter,0.05]])
            textbox.draw()
            s_line.draw()
            m_line.draw()
            c_line.draw()
            l_line.draw()
            r_line.draw()
            win.flip()
        elif keyState[key.G]:
            if c_length>0.0002:
                c_length=c_length-0.1/(winWidth/2.00)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line.setVertices([[c_length+jetter,-0.05],[c_length+jetter,0.05]])
            textbox.draw()
            s_line.draw()
            m_line.draw()
            c_line.draw()
            l_line.draw()
            r_line.draw()
            win.flip()
        elif 'escape'in keylist:
            print 'set escape signal'
            global s
            s=True
            break
        else:
            pass

def show_mueller(length):
    jetter=random.uniform(-0.05, 0.05)
    global win
    global textbox
    winWidth = 1000
    s_length=length/(winWidth/2.0)
    c_length=random.uniform(length*0.8,length*1.2)/(winWidth/2.0)
    s_line = visual.ShapeStim(win, vertices= [[-s_length+jetter,0], [0+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    c_line = visual.ShapeStim(win, vertices= [[0+jetter,0], [c_length+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    l_line_1 = visual.ShapeStim(win, vertices= [[-s_length+jetter-0.05,0.05], [-s_length+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    l_line_2 = visual.ShapeStim(win, vertices= [[-s_length+jetter,0], [-s_length+jetter-0.05,-0.05]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    m_line_1 = visual.ShapeStim(win, vertices= [[0+jetter+0.05,0.05], [0+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    m_line_2 = visual.ShapeStim(win, vertices= [[0+jetter,0], [0+jetter+0.05,-0.05]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    r_line_1 = visual.ShapeStim(win, vertices= [[c_length+jetter-0.05,-0.05], [c_length+jetter,0]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    r_line_2 = visual.ShapeStim(win, vertices= [[c_length+jetter,0], [c_length+jetter-0.05,0.05]],
    lineColor=[-1,-1,-1],fillColor=None, lineWidth=2, autoLog=False)
    textbox.setText('This is trial %s\nThe left line is the standard, and the right line is the comparison.\nPress J to INCREASE the comparison by 10 pixels\nPress F to DECREASE the comparison by 10 pixels.\nPress H to INCREASE the comparison by 1 pixel\nPress G to DECREASE the comparison by 1 pixel.\nPress Q when done with this trial.\nPress Esc to end the session early'%str(x+1))
    textbox.draw()
    s_line.draw()
    c_line.draw()
    m_line_1.draw()
    l_line_1.draw()
    r_line_1.draw()
    m_line_2.draw()
    l_line_2.draw()
    r_line_2.draw()
    win.flip()
    while True:
        keylist=event.getKeys()
        if 'q'in keylist:
            global result
            result.append(int(c_length*(winWidth/2.0)))
            print 'insert new length to c_length list'
            break 
        elif keyState[key.J]:
            if c_length<1:
                c_length=c_length+1/(winWidth/2.0)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line_1.setVertices([[c_length+jetter-0.05,-0.05], [c_length+jetter,0]])
            r_line_2.setVertices([[c_length+jetter,0], [c_length+jetter-0.05,0.05]])
            textbox.draw()
            s_line.draw()
            c_line.draw()
            m_line_1.draw()
            l_line_1.draw()
            r_line_1.draw()
            m_line_2.draw()
            l_line_2.draw()
            r_line_2.draw()
            win.flip()
        elif keyState[key.H]:
            if c_length<1:
                c_length=c_length+0.1/(winWidth/2.0)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line_1.setVertices([[c_length+jetter-0.05,-0.05], [c_length+jetter,0]])
            r_line_2.setVertices([[c_length+jetter,0], [c_length+jetter-0.05,0.05]])
            textbox.draw()
            s_line.draw()
            c_line.draw()
            m_line_1.draw()
            l_line_1.draw()
            r_line_1.draw()
            m_line_2.draw()
            l_line_2.draw()
            r_line_2.draw()
            win.flip()
        elif keyState[key.F]:
            if c_length>0.002:
                c_length=c_length-1/(winWidth/2.0)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line_1.setVertices([[c_length+jetter-0.05,-0.05], [c_length+jetter,0]])
            r_line_2.setVertices([[c_length+jetter,0], [c_length+jetter-0.05,0.05]])
            textbox.draw()
            s_line.draw()
            c_line.draw()
            m_line_1.draw()
            l_line_1.draw()
            r_line_1.draw()
            m_line_2.draw()
            l_line_2.draw()
            r_line_2.draw()
            win.flip()
        elif keyState[key.G]:
            if c_length>0.0002:
                c_length=c_length-0.1/(winWidth/2.0)
            c_line.setVertices([[0+jetter,0],[c_length+jetter,0]])
            r_line_1.setVertices([[c_length+jetter-0.05,-0.05], [c_length+jetter,0]])
            r_line_2.setVertices([[c_length+jetter,0], [c_length+jetter-0.05,0.05]])
            textbox.draw()
            s_line.draw()
            c_line.draw()
            m_line_1.draw()
            l_line_1.draw()
            r_line_1.draw()
            m_line_2.draw()
            l_line_2.draw()
            r_line_2.draw()
            win.flip()
        elif 'escape'in keylist:
            print 'set escape signal'
            global s
            s=True
            break
        else:
            pass
def show_instruction():
    global win
    global textbox
    
    showbox=visual.TextStim(win,
                         text='PRESS ANY KEY TO START', 
                         font='Courier New',
                         #font_size=50,
                         color=[0,0,0],
                         #dpi=72,
                         #size=(1.8,0.6),
                         pos=(0.0,-0.4), 
                         units='norm',
                         #grid_horz_justification='center',
                         #grid_vert_justification='center',
                         alignHoriz='center', 
                         alignVert='center',
                         colorSpace='rgb255'
                         )
    showbox.height = 0.15
    showbox.wrapWidth = 2
    showbox.draw()
    textbox.draw()
    win.flip()
    while True:
        if len(event.getKeys())>0: break
    event.clearEvents()
myDlg = gui.Dlg(title="Line Length",size=(1, 1))
myDlg.addField('ExperimentName:','LINE')
myDlg.addField('SubjectID:','xx')
myDlg.addField('SessionNumber:',1)
myDlg.addField('StandardLineLength(in pixels):',200)
myDlg.addField('NumberofTrials',30)
myDlg.addField('Mueller-Lyer(N;Y)')
myDlg.show()
if myDlg.OK:  # then the user pressed OK
    thisInfo = myDlg.data
    name=thisInfo[0]
    ID=thisInfo[1]
    session=thisInfo[2]
    length=thisInfo[3]
    trials=thisInfo[4]
    mueller=thisInfo[5]
    
    
    
    file=''
    file+=name
    file+='_'
    file+=ID
    file+='_'
    file+=str(session)
    file+='_'+data.getDateStr()

    print file
    keyState=key.KeyStateHandler()
    global x
    x = 0
    win = visual.Window([800,600],monitor='Monitor',allowGUI=True,fullscr=False)
    textbox=visual.TextStim(win,
                         text='The left line is the standard, and the right line is the comparison.\nPress J to INCREASE the comparison by 10 pixels\nPress F to DECREASE the comparison by 10 pixels.\nPress H to INCREASE the comparison by 1 pixel\nPress G to DECREASE the comparison by 1 pixel.\nPress Q when done with this trial.\nPress Esc to end the session early', 
                         font='Courier New',
                         #font_size=15,
                         color=[0,0,0],
                         #dpi=72,
                         #size=(1.8,0.4),
                         pos=(0.0,0.4), 
                         units='norm',
                         #grid_horz_justification='center',
                         #grid_vert_justification='center',
                         alignHoriz='center', 
                         alignVert='center',
                         colorSpace='rgb255'
                         )
    textbox.height = (0.05)
    textbox.wrapWidth = 2
    win.winHandle.push_handlers(keyState)
    show_instruction()
    while x < trials :
        if s==True:
            break;
        if mueller=='N':
            show_normal(length)
        elif mueller=='n':
            show_normal(length)
        elif mueller=='Y':
            show_mueller(length)
        elif mueller=='y':
            show_mueller(length)
        else:
            show_normal(length)
        x = x + 1
    write_file(file,length,mueller)
else:
    print 'user cancelled'