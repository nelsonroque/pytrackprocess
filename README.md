# pyEye | Python module
## A python module to simplify eye-tracking data-processing

Python script to pre-process Eyelink ASCII files and extract data in csv format between two sentinel flags

# Features
- extract single trial of data<br>
- extract all trials of data<br>
- extract blinks only<br>
- extract fixations only<br>
- extract saccades only<br>

# Usage
- See <i>usage.py</i> for details on function calls and data paths

# Example Functions
-         pyeye.reports.trial.single(data_path,user_file_info,"start_baseline_1","stop_baseline_1","BASELINE_1",".csv")
pyeye.reports.trial.single(data_path,user_file_info,"start_baseline_2","stop_baseline_2","BASELINE_2",".csv")
pyeye.reports.trial.multiple(data_path,user_file_info,"start_trial",'stop_trial',"EXP",".csv")
pyeye.reports.event.blink(data_path,user_file_info,'R',"start_trial",'stop_trial',".csv")
pyeye.reports.event.fixation(data_path,user_file_info,'R',"start_trial",'stop_trial',".csv")
pyeye.reports.event.saccade(data_path,user_file_info,'R',"start_trial",'stop_trial',".csv")
-
