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
# define function to read all data (at the frame level, between two MSG flags)
# vars: frame, x, y, pupil
# ----------------------------------------------------------------------
def single(data_path,user_file,startFlag,endFlag,filestring,outType):
    import time
    import glob
    import re

    start_time = time.time()

    # define eyetracking messages to ignore
    TRACK_MSGS = ['SSACC','ESACC','SFIX','EFIX','SBLINK','EBLINK','END','MSG']

    # while the asc file has data to read
    input_filename = (data_path+user_file+".asc")
    output_filename = (data_path+user_file+"_"+filestring+outType)

    # open output file
    df = open((output_filename),'w')

    # open the input file for reading
    with open(input_filename,'r') as f:
        # read each line
        for line in f:
            # get line where baseline starts (pre or post)
            if(startFlag in line):
                SECTION = filestring
                break
        for line in f:
            # get line where baseline ends (pre or post)
            if(endFlag in line):
                break
            else:
                # get eye movements/pupil until end of baseline, #ignorind eyetracking messages
                if not any(x in line for x in TRACK_MSGS):
                    myline = line.replace('\n', ' ')
                    myline = myline.replace(' ', '')
                    line_data = myline.split("\t")
                    FRAME = line_data[0]
                    if re.match("^[0-9]+$",FRAME) is not None:
                        if(len(line_data) < 5):
                            #print(line_data)
                            #print(len(line_data))
                            print("TRACKING LOST")
                            #print(line_data)
                        else:
                            X_COORD = line_data[1]
                            if re.match("^\d+?\.\d+?$", X_COORD) is not None:
                                Y_COORD = line_data[2]
                                PUPIL_SIZE = line_data[3]
                                TRIAL_DATA = [str(SECTION),FRAME,X_COORD,Y_COORD,PUPIL_SIZE]
                                df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(GENERIC REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# [START_FUNCTION] -----------------------------------------------------
# define function to read all data (at the frame level, between two MSG flags)
# vars: frame, x, y, pupil
# ----------------------------------------------------------------------
def multiple(data_path,user_file,startFlag,endFlag,filestring,outType):
    import time
    import glob
    import re

    start_time = time.time()

    # define eyetracking messages to ignore
    TRACK_MSGS = ['SSACC','ESACC','SFIX','EFIX','SBLINK','EBLINK','END','MSG']

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
                        if not any(x in line for x in TRACK_MSGS):
                            myline = line.replace('\n', ' ')
                            myline = myline.replace(' ', '')
                            line_data = myline.split("\t")
                            FRAME = line_data[0]
                            if re.match("^[0-9]+$",FRAME) is not None:
                                if(len(line_data) < 5):
                                    #print(line_data)
                                    #print(len(line_data))
                                    print("TRACKING LOST")
                                    #print(line_data)
                                else:
                                    X_COORD = line_data[1]
                                    if re.match("^\d+?\.\d+?$", X_COORD) is not None:
                                        Y_COORD = line_data[2]
                                        PUPIL_SIZE = line_data[3]
                                        TRIAL_DATA = [str(SECTION),FRAME,X_COORD,Y_COORD,PUPIL_SIZE]
                                        df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print("(TRIAL SAMPLES REPORT) TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------
