# libraries
import time
import glob

# define function to read baseline data
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

def extract_BaselineSamples(data_path,user_file):
    start_time = time.time()
    readWindowBetweenFlags(data_path,user_file,"start_baseline_1","stop_baseline_1","BASELINE_1","B1",".asc",".csv")
    readWindowBetweenFlags(data_path,user_file,"start_baseline_2","stop_baseline_2","BASELINE_2","B2",".asc",".csv")
    elapsed = time.time() - start_time
    print("PARTICIPANT TOTAL PROCESSING TIME:",elapsed,"seconds")
# [END_FUNCTION] -------------------------------------------------------

# for each participant
# create filename
data_path = 'data/'

# glob search construction
glob_search = data_path + "*.asc"

def bulk

# search for all asc files
for name in glob.glob(glob_search):
    filename = name
    user_file_info = name.split("data\\")[1].split(".asc")[0]

    # process participant
    extract_BaselineSamples(data_path,user_file_info)
