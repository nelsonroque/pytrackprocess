'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PYTRACKPRO (v.0.1) #
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ASSUMPTIONS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
- YOU HAVE IMPLEMENTED MSG EVENTS IN YOUR EXPERIMENT
    - SPECIFICALLY A UNIQUE START AND END EVENT MESSAGE (i.e. trial_1_start, trial_1_end)
    - VIA EXPERIMENT BUILDER, OPENSESAME, PSYCHOPY, ETC
- ASSUMES SR RESEARCH EYELINK-1000 DATAFILES (EDF) HAVE BEEN CONVERTED TO ASC files
    - EYELINK PROVIDES AN EDF2ASC UTILITY FOR THIS

# PLANS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
- IMPLEMENT AS MODULE
- CLEAN UP FUNCTION NAMES
- SHORTEN FUNCTION CALLS
- IMPLEMENT READING OF CONFIG FILE FOR TRIAL VARS TO LOOK FOR
'''
import pytrack.getSingleWindowReport
import pytrack.getFixationReport
import pytrack.getSaccadeReport
import pytrack.getBlinkReport
import pytrack.getTrialReport
