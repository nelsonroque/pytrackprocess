'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PYTRACKPRO (v.0.1) #
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# LIBRARIES
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import pyeye.reports.event
import pyeye.reports.trial
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

        # EXAMPLES OF ALL FUNCTION CALLS POSSIBLE AT THE MOMENT (FOR EACH PARTICIPANT)
        pyeye.reports.trial.single(data_path,user_file_info,"start_baseline_1","stop_baseline_1","BASELINE_1",".csv")
        pyeye.reports.trial.single(data_path,user_file_info,"start_baseline_2","stop_baseline_2","BASELINE_2",".csv")
        pyeye.reports.trial.multiple(data_path,user_file_info,"start_trial",'stop_trial',"EXP",".csv")
        pyeye.reports.event.blink(data_path,user_file_info,'R',"start_trial",'stop_trial',".csv")
        pyeye.reports.event.fixation(data_path,user_file_info,'R',"start_trial",'stop_trial',".csv")
        pyeye.reports.event.saccade(data_path,user_file_info,'R',"start_trial",'stop_trial',".csv")

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
