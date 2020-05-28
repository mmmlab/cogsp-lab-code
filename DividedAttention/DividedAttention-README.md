# Divided attention

## Synopsis

This exercise shows the difficulty of divided attention. 

This can be done early in the semester, as students can do a simple t-test (see below) to analyze data, or later in the semester as there are so many variations already available.

The exercise has the student choose one of three tasks: identifying a number in a stream of letters presented at fixation, identifying which gabor patch flashed in the periphery is a different orientation, or both. 

There is a variation that uses color instead of tilt. If by chance you have a student who is interested in how people would do at identifying the direction of the tilt, we have that program already written. 


The t-test can be done if students run series of sessions of one task (make sure it’s the same one!) and the same number of sessions of the dual task. 

Later in the semester, students can pick among the variety of menu options and see what makes a task harder. A number of students in previous semesters have used this as their “original” project.

## To Do:

1. Check whether this should be full-screen. The current versions of 
`DividedAttention-Color.py` and `DividedAttention-Tilt.py` both open in small windows.
2. Fix deprecation warning for use of RGB arguments (replace with `color` and 
`colorSpace` arguments instead). These currently work but may fail in a future version of Psychopy.
3. Change to use PTB sound engine as preferred audio engine (not critical).
4. Potentially change to use openpyxl interface to output data in similar format
as original version of experiment (`dividedattention.py`) did with xlwt.