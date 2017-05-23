# libraries
import time

# define function to read baseline data
def readBaseline(user_file,startFlag,endFlag,section,filestring,inType,outType):
    start_time = time.time()

    # define eyetracking messages to ignore
    TRACK_MSGS = ['SSACC','ESACC','SFIX','EFIX','SBLINK','EBLINK','END']

    # while the asc file has data to read
    input_filename = (user_file+inType)
    output_filename = (user_file+"_"+filestring+outType)

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
                    #Y_COORD = line_data[2]
                    #PUPIL_SIZE = line_data[3]
                    #TRIAL_DATA = [SECTION,FRAME,X_COORD,Y_COORD,PUPIL_SIZE]
                    #df.write(",".join(TRIAL_DATA)+"\n")

    df.close()
    elapsed = time.time() - start_time
    print(elapsed, " seconds")
# [END_FUNCTION] -------------------------------------------------------

# for each participant
# create filename
user_file = 'sub_2015'

readBaseline(user_file,"start_baseline_1","stop_baseline_1","BASELINE_1","B1",".asc",".csv")
readBaseline(user_file,"start_baseline_2","stop_baseline_2","BASELINE_2","B2",".asc",".csv")
