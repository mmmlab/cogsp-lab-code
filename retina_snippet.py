# Code snippet with example of what to do to correct for os-level scaling in
# "Retina" (MacOS) and other HiDPI displays.

import psychopy
from psychopy import visual, core
import pyglet

## 1. Get full display resolution (as reported by OS)
# note: code below assumes either single or twin monitor configuration
pyg_screen = pyglet.canvas.Display().get_default_screen()
pyg_width = pyg_screen.width
pyg_height = pyg_screen.height

## 2. Create fullscreen Psychopy window and get actual hardware resolution
win = visual.Window(monitor='testMonitor',color='black',allowGUI=True,\
    units='pix',size=(pyg_width,pyg_height),fullscr=True)
win_width,win_height = win.size

## 3. Compute the ratio of os_width to win_width to determine whether we're
#     using a HiDPI display (i.e., one with pixel scaling).
px_ratio = win_width/pyg_width
is_retina = px_ratio > 1.0

## 4. Report results
print('Results:')
print('\t... OS-reported display resolution is: %d x %d'%(pyg_width,pyg_height))
print('\t... detected hardware resolution is: %d x %d'%(win_width,win_height))
print('\t... pixel scaling is %2.0f%%'%(px_ratio*100.0))
if is_retina:
    print('You are using a retina display.')
else:
    print('You are NOT using a retina display.')

## 5. Exit the program
core.quit()