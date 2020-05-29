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
