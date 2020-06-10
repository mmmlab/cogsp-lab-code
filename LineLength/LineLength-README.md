# Line Length

## Synopsis

Line Length is usually done as the first exercise. It’s the easiest to run, the 
most well-established (i.e. fewest possible bugs), and introduces students to a 
really important and basic fact about human sensation. It’s usually run in 
Cognition as well as it is easy and well-established.

## To Do:

1. The code is overly complex, making it inefficient and error-prone. It looks 
like the original author did a lot of cut-and-pasting. It should be refactored, 
as can be simplified substantially. In particular,
    - separate the drawing of the stimulus elements from the specification of 
    their parameters (i.e., in a separate function)
    - separate the boolean logic and user input handling from the drawing of the
    stimuli
    - abstract away repetitive and redundant code
2. The code generates a small window rather than a fullscreen view. This should
be fixed.
3. A variety of warnings need to be addressed, including:
    - TextStim.alignVert is deprecated (use anchorVert)
    - TextStim.alignHoriz is deprecated (use alignText and anchorHoriz)
    - Missing monitor specification
4. Ideally, the size of the standard should be randomized within a block, but
that could make the analysis a bit more complicated for a first project.
5. The starting position of the 

In MacOS-
does not work. Errors:

## Running: /Users/mphan/Desktop/302_306/cogsp-lab-code-master/LineLength/LineLength.py ##
LINE_xx_1_2020_Jun_10_1039
450.7643     WARNING     Monitor specification not found. Creating a temporary one...
451.5561     WARNING     TextStim.alignVert is deprecated. Use the anchorVert attribute instead
451.5561     WARNING     TextStim.alignHoriz is deprecated. Use alignText and anchorHoriz attributes instead
451.7031     WARNING     TextStim.alignVert is deprecated. Use the anchorVert attribute instead
451.7031     WARNING     TextStim.alignHoriz is deprecated. Use alignText and anchorHoriz attributes instead
2020-06-10 10:32:16.261 python[36231:15218990] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to (null)
Traceback (most recent call last):
  File "/Users/mphan/Desktop/302_306/cogsp-lab-code-master/LineLength/LineLength.py", line 325, in <module>
    show_normal(length)
  File "/Users/mphan/Desktop/302_306/cogsp-lab-code-master/LineLength/LineLength.py", line 57, in show_normal
    s_line.draw()
  File "/Applications/PsychoPy3.app/Contents/Resources/lib/python3.6/psychopy/visual/shape.py", line 594, in draw
    GL.glVertexPointer(2, GL.GL_DOUBLE, 0, self._borderPix.ctypes)
  File "/Applications/PsychoPy3.app/Contents/Resources/lib/python3.6/psychopy/visual/basevisual.py", line 492, in _borderPix
    self._updateVertices()
  File "/Applications/PsychoPy3.app/Contents/Resources/lib/python3.6/psychopy/visual/basevisual.py", line 520, in _updateVertices
    win=self.win, units=self.units)
  File "/Applications/PsychoPy3.app/Contents/Resources/lib/python3.6/psychopy/tools/monitorunittools.py", line 95, in convertToPix
    return unit2pixFunc(vertices, pos, win)
  File "/Applications/PsychoPy3.app/Contents/Resources/lib/python3.6/psychopy/tools/monitorunittools.py", line 38, in _deg2pix
    return deg2pix(pos + vertices, win.monitor)
  File "/Applications/PsychoPy3.app/Contents/Resources/lib/python3.6/psychopy/tools/monitorunittools.py", line 249, in deg2pix
    raise ValueError(msg % monitor.name)
ValueError: Monitor Monitor has no known size in pixels (SEE MONITOR CENTER)
##### Experiment ended. #####

