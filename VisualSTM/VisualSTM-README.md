# Visual Short Term Memory

## Synopsis

This is based on a relatively-easy to read article that is in the resources file. It’s a good opportunity for students to practice reading scientific articles. 

This is based on work that shows that the more objects we have to remember, the less good we are at remembering them all. 

There are two different tasks included in this folder
    - The first task `VisualSTM.py` is a difference detection task in which the 
    observer must simply indicate whether there was or wasn't a change 
    (in orientation, color, or __) in the display.
    - The second task is a variation of the first that turns it into a 
    *discrimination* task. In this case, the experimenter changes the orientation 
    difference by which a bar changes between the probe (first) and test (second)
    displays, and the observer must report in what direction the perturbed bar
    was rotated. This modified version of the experiment shows that we aren’t as 
    good at remembering small differences when there are a lot of objects that 
    might change.

The statistics can either be simple - just plotting the means - or complicated - run an actual ANOVA - so it can be done at any time during the semester. 

## To Do:
1. The experiment opens a small window, it should be made full screen.
2. The individual elements can (and often do) appear at the very edges of the 
display window. This needs to be changed. A buffer should be added to limit element
positions.
3. There are no introductory responses, nor any indication of the response key
mapping. These need to be added.

----notes in MacOS
-seems to work
-fixation point?
