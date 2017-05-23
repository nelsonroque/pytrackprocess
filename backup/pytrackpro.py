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
import time
import glob
# ----------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# FUNCTIONS
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
    df = open((output_filename),'w')

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
                    #print(line)
                    line_data = line.split("\t")
                    FRAME = line_data[0]
                    if(FRAME.isdigit()):
                        X_COORD = line_data[1]
                        Y_COORD = line_data[2]
                        PUPIL_SIZE = line_data[3]
                        TRIAL_DATA = [SECTION,FRAME,X_COORD,Y_COORD,PUPIL_SIZE]
                        df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(GENERIC REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# define function to read all data (at the frame level, between two MSG flags)
# vars: frame, x, y, pupil
# ----------------------------------------------------------------------
def getTrialSamples(data_path,user_file,startFlag,endFlag,filestring,inType,outType):
    start_time = time.time()

    # define eyetracking messages to ignore
    TRACK_MSGS = ['SSACC','ESACC','SFIX','EFIX','SBLINK','EBLINK','END','MSG']

    # while the asc file has data to read
    input_filename = (data_path+user_file+inType)
    output_filename = (data_path+user_file+"_"+filestring+outType)

    # open output file
    df = open((output_filename),'w')

    # start event counter
    TRIAL = 0

    # open the input file for reading
    with open(input_filename,'r') as f:
        # read each line
        # search for trial start
        SECTION='PREPARE'
        startFound=False
        for line in f:
            # get line where baseline starts (pre or post)
            if(startFlag in line):
                #print("Trial:",TRIAL)
                startFound = True
                SECTION=TRIAL
            else:
                if(endFlag in line):
                    startFound = False
                    TRIAL += 1
                else:
                    if(startFound):
                        if not any(x in line for x in TRACK_MSGS):
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            FRAME = line_data[0]
                            if(FRAME.isdigit()):
                                X_COORD = line_data[1]
                                Y_COORD = line_data[2]
                                PUPIL_SIZE = line_data[3]
                                TRIAL_DATA = [str(SECTION),FRAME,X_COORD,Y_COORD,PUPIL_SIZE]
                                df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(TRIAL SAMPLES REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# for each trial, extract blinks, and blink duration with frames (for labelling tracking data)
def getSaccadeReport(data_path,user_file,startFlag,endFlag,filestring,inType,outType):
    start_time = time.time()

    # define eyetracking messages to ignore
    BLINK_MSGS = ['ESACC']
    TRACK_MSGS = ['END','MSG']

    # while the asc file has data to read
    input_filename = (data_path+user_file+inType)
    output_filename = (data_path+user_file+"_"+filestring+outType)

    # open output file
    df = open((output_filename),'w')

    # start event counter
    TRIAL = 0

    # open the input file for reading
    with open(input_filename,'r') as f:
        # read each line
        # search for trial start
        SECTION='PREPARE'
        startFound=False
        for line in f:
            # get line where baseline starts (pre or post)
            if(startFlag in line):
                #print("Trial:",TRIAL)
                startFound = True
                SECTION=TRIAL
            else:
                if(endFlag in line):
                    startFound = False
                    TRIAL += 1
                else:
                    if(startFound):
                        if any(x in line for x in BLINK_MSGS):
                            #print(line)
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            #print(line_data)
                            START_FRAME = line_data[0].split('ESACCR')[1]
                            END_FRAME = line_data[1]
                            SACCADE_DURATION = line_data[2].rstrip("\n")
                            START_X = line_data[3].rstrip("\n")
                            START_Y = line_data[4].rstrip("\n")
                            END_X = line_data[5].rstrip("\n")
                            END_Y = line_data[6].rstrip("\n")
                            AMPLITUDE = line_data[7].rstrip("\n")
                            PEAK_VELOCITY = line_data[8].rstrip("\n")
                            TRIAL_DATA = [str(TRIAL),START_FRAME,END_FRAME,SACCADE_DURATION,START_X,START_Y,END_X,END_Y,AMPLITUDE,PEAK_VELOCITY]
                            #print(TRIAL_DATA)
                            df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(SACCADE REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# for each trial, extract blinks, and blink duration with frames (for labelling tracking data)
def getFixationReport(data_path,user_file,startFlag,endFlag,filestring,inType,outType):
    start_time = time.time()

    # define eyetracking messages to ignore
    BLINK_MSGS = ['EFIX']
    TRACK_MSGS = ['END','MSG']

    # while the asc file has data to read
    input_filename = (data_path+user_file+inType)
    output_filename = (data_path+user_file+"_"+filestring+outType)

    # open output file
    df = open((output_filename),'w')

    # start event counter
    TRIAL = 0

    # open the input file for reading
    with open(input_filename,'r') as f:
        # read each line
        # search for trial start
        SECTION='PREPARE'
        startFound=False
        for line in f:
            # get line where baseline starts (pre or post)
            if(startFlag in line):
                #print("Trial:",TRIAL)
                startFound = True
                SECTION=TRIAL
            else:
                if(endFlag in line):
                    startFound = False
                    TRIAL += 1
                else:
                    if(startFound):
                        if any(x in line for x in BLINK_MSGS):
                            #print(line)
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            #print(line_data)
                            START_FRAME = line_data[0].split('EFIXR')[1]
                            END_FRAME = line_data[1]
                            BLINK_DURATION = line_data[2].rstrip("\n")
                            AVG_X = line_data[3].rstrip("\n")
                            AVG_Y = line_data[4].rstrip("\n")
                            AVG_PUPIL = line_data[5].rstrip("\n")
                            TRIAL_DATA = [str(TRIAL),START_FRAME,END_FRAME,BLINK_DURATION,AVG_X,AVG_Y,AVG_PUPIL]
                            df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(FIXATION REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# for each trial, extract blinks, and blink duration with frames (for labelling tracking data)
def getBlinkReport(data_path,user_file,startFlag,endFlag,filestring,inType,outType):
    start_time = time.time()

    # define eyetracking messages to ignore
    BLINK_MSGS = ['EBLINK']
    TRACK_MSGS = ['END','MSG']

    # while the asc file has data to read
    input_filename = (data_path+user_file+inType)
    output_filename = (data_path+user_file+"_"+filestring+outType)

    # open output file
    df = open((output_filename),'w')

    # start event counter
    TRIAL = 0

    # open the input file for reading
    with open(input_filename,'r') as f:
        # read each line
        # search for trial start
        SECTION='PREPARE'
        startFound=False
        for line in f:
            # get line where baseline starts (pre or post)
            if(startFlag in line):
                #print("Trial:",TRIAL)
                startFound = True
                SECTION=TRIAL
            else:
                if(endFlag in line):
                    startFound = False
                    TRIAL += 1
                else:
                    if(startFound):
                        if any(x in line for x in BLINK_MSGS):
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            START_FRAME = line_data[0].split("EBLINKR")[1]
                            END_FRAME = line_data[1]
                            BLINK_DURATION = line_data[2].rstrip("\n")
                            TRIAL_DATA = [str(TRIAL),START_FRAME,END_FRAME,BLINK_DURATION]
                            df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(BLINK REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
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
        # process both baseline events
        readWindowBetweenFlags(data_path,user_file_info,"start_baseline_1","stop_baseline_1","BASELINE_1","B1",".asc",".csv")
        readWindowBetweenFlags(data_path,user_file_info,"start_baseline_2","stop_baseline_2","BASELINE_2","B2",".asc",".csv")
        getTrialSamples(data_path,user_file_info,"start_trial",'stop_trial',"EXP",".asc",".csv")
        getBlinkReport(data_path,user_file_info,"start_trial",'stop_trial',"BLINKS",".asc",".csv")
        getFixationReport(data_path,user_file_info,"start_trial",'stop_trial',"FIXATION",".asc",".csv")
        getSaccadeReport(data_path,user_file_info,"start_trial",'stop_trial',"SACCADE",".asc",".csv")

        # -----------------------------------------------
        # -----------------------------------------------

        # get elapsed time for participant processing
        elapsed = time.time() - start_time

        # print processing msg for each participant
        print("(PARTICIPANT REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")

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
