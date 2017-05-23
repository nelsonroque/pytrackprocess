'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PYTRACKPRO (v.0) #
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
# ----------------------------------------------------------------------
# libraries
import time
import glob
# ----------------------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# define function to read all data (at the frame level, between two MSG flags)
# vars: frame, x, y, pupil
# ----------------------------------------------------------------------
def readWindowBetweenFlags(data_path,user_file,startFlag,endFlag,section,filestring,inType,outType):
    start_time = time.time()

    # define eyetracking messages to ignore
    TRACK_MSGS = ['SSACC','ESACC','SFIX','EFIX','SBLINK','EBLINK','END','MSG']

    # while the asc file has data to read
    input_filename = (data_path+user_file+inType)
    output_filename = (data_path+user_file+"_"+filestring+outType)

    # open output file
    df = open((output_filename),'a')

    # open the input file for reading
    with open(input_filename,'r') as f:
        # read each line
        for line in f:
            # get line where baseline starts (pre or post)
            if(startFlag in line):
                SECTION = section
                break
        for line in f:
            # get line where baseline ends (pre or post)
            if(endFlag in line):
                break
            else:
                # get eye movements/pupil until end of baseline, #ignorind eyetracking messages
                if not any(x in line for x in TRACK_MSGS):
                    line = line.replace(' ', '')
                    line_data = line.split("\t")
                    FRAME = line_data[0]
                    X_COORD = line_data[1]
                    Y_COORD = line_data[2]
                    PUPIL_SIZE = line_data[3]
                    TRIAL_DATA = [SECTION,FRAME,X_COORD,Y_COORD,PUPIL_SIZE]
                    df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("SESSION TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# function to batch process participants with your custom batch functions
# using/extending PYTRACKPRO utility functions
# see extractSamples_Experiment_PUPILCAPTURE for an example
# ----------------------------------------------------------------------
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
        extractSamples_Experiment_PUPILCAPTURE(data_path,user_file_info)

        # -----------------------------------------------
        # -----------------------------------------------

        # get elapsed time for participant processing
        elapsed = time.time() - start_time

        # print processing msg for each participant
        print("PARTICIPANT TOTAL PROCESSING TIME:",elapsed,"seconds")

    # get elapsed time for full batch processing
    process_elapsed_time = time.time() - process_time
    print("BATCH TOTAL PROCESSING TIME:",elapsed,"seconds")
# ----------------------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# extract samples for baseline period for a single participant (could be used in batch (see below, USAGE))
# ----------------------------------------------------------------------
def extractSamples_Experiment_PUPILCAPTURE(data_path,user_file):
    # process both baseline events
    readWindowBetweenFlags(data_path,user_file,"start_baseline_1","stop_baseline_1","BASELINE_1","B1",".asc",".csv")
    readWindowBetweenFlags(data_path,user_file,"start_baseline_2","stop_baseline_2","BASELINE_2","B2",".asc",".csv")
# [END_FUNCTION] -------------------------------------------------------

# ==========================--------------------------------------------
# BULK USAGE OF PYTRACKPRO
# ==========================--------------------------------------------

# create filename
data_path = 'data/'

# glob search construction
glob_search = data_path + "*.asc"

custom_batch(data_path,glob_search)
