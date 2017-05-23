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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# LIBRARIES
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import pytrack
import time
import glob
# ----------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# FUNCTIONS
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def custom_batch(data_path,glob_search):
    # search for all asc files (for each participant)
    process_time = time.time()
    for name in glob.glob(glob_search):
        # split everything off except the participant identifier
        user_file_info = name.split("data\\")[1].split(".asc")[0]

        # get start time for participant processing
        start_time = time.time()

        # -----------------------------------------------
        # -----------------------------------------------
        # ATTENTION
        # -----------------------------------------------
        # -----------------------------------------------

        # MODIFY YOUR FUNCTION HERE FOR YOUR EXPERIMENT
        # process both baseline events
        pytrack.getSingleWindowReport.getSingleWindowReport(data_path,user_file_info,"start_baseline_1","stop_baseline_1","BASELINE_1","B1",".asc",".csv")
        pytrack.getSingleWindowReport.getSingleWindowReport(data_path,user_file_info,"start_baseline_2","stop_baseline_2","BASELINE_2","B2",".asc",".csv")
        pytrack.getTrialReport.getTrialReport(data_path,user_file_info,"start_trial",'stop_trial',"EXP",".asc",".csv")
        pytrack.getBlinkReport.getBlinkReport(data_path,user_file_info,"start_trial",'stop_trial',"BLINKS",".asc",".csv")
        pytrack.getFixationReport.getFixationReport(data_path,user_file_info,"start_trial",'stop_trial',"FIXATION",".asc",".csv")
        pytrack.getSaccadeReport.getSaccadeReport(data_path,user_file_info,"start_trial",'stop_trial',"SACCADE",".asc",".csv")

        # -----------------------------------------------
        # -----------------------------------------------

        # get elapsed time for participant processing
        elapsed = time.time() - start_time

        # print processing msg for each participant
        print("(PARTICIPANT REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
        print("----------------------")

    # get elapsed time for full batch processing
    process_elapsed_time = time.time() - process_time
    print("BATCH TOTAL PROCESSING TIME:",process_elapsed_time,"seconds")
# ----------------------------------------------------------------------

# ==========================--------------------------------------------
# BULK USAGE OF PYTRACKPRO
# ==========================--------------------------------------------

# create filename
data_path = 'data/'

# glob search construction
glob_search = data_path + "*.asc"

custom_batch(data_path,glob_search)
