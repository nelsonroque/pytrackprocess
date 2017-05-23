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

# FUTURE DIRECTIONS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
- IMPLEMENT READING OF CONFIG FILE FOR TRIAL VARS TO LOOK FOR
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# FUNCTIONS
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# [START_FUNCTION] -----------------------------------------------------
# for each trial, extract blinks, and blink duration with frames (for labelling tracking data)
def blink(data_path,user_file,eyeTracked,startFlag,endFlag,outType):
    import time
    import glob

    start_time = time.time()

    # define eyetracking messages to ignore
    EVENT_SENTINEL = ['EBLINK']
    SEARCH_MSG = (EVENT_SENTINEL[0]+eyeTracked)
    TRACK_MSGS = ['END','MSG']

    filestring = 'BLINK'

    # while the asc file has data to read
    input_filename = (data_path+user_file+'.asc')
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
                        if any(x in line for x in EVENT_SENTINEL):
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            START_FRAME = line_data[0].split(SEARCH_MSG)[1]
                            END_FRAME = line_data[1]
                            BLINK_DURATION = line_data[2].rstrip("\n")
                            TRIAL_DATA = [str(TRIAL),START_FRAME,END_FRAME,BLINK_DURATION]
                            df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(BLINK REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------


# [START_FUNCTION] -----------------------------------------------------
# for each trial, extract blinks, and blink duration with frames (for labelling tracking data)
def fixation(data_path,user_file,eyeTracked,startFlag,endFlag,outType):
    import time
    import glob
    start_time = time.time()

    # define eyetracking messages to ignore
    EVENT_SENTINEL = ['EFIX']
    SEARCH_MSG = (EVENT_SENTINEL[0]+eyeTracked)
    TRACK_MSGS = ['END','MSG']

    filestring = 'FIXATION'

    # while the asc file has data to read
    input_filename = (data_path+user_file+'.asc')
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
                        if any(x in line for x in EVENT_SENTINEL):
                            #print(line)
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            #print(line_data)
                            START_FRAME = line_data[0].split(SEARCH_MSG)[1]
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
def saccade(data_path,user_file,eyeTracked,startFlag,endFlag,outType):
    import time
    import glob
    start_time = time.time()

    # define eyetracking messages to ignore
    EVENT_SENTINEL = ['ESACC']
    SEARCH_MSG = (EVENT_SENTINEL[0]+eyeTracked)
    TRACK_MSGS = ['END','MSG']

    filestring = 'SACCADE'

    # while the asc file has data to read
    input_filename = (data_path+user_file+'.asc')
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
                        if any(x in line for x in EVENT_SENTINEL):
                            #print(line)
                            myline = line.replace(' ', '')
                            line_data = myline.split("\t")
                            #print(line_data)
                            START_FRAME = line_data[0].split(SEARCH_MSG)[1]
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
