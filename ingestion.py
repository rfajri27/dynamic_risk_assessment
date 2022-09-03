import pandas as pd
import numpy as np
import glob
import os
import json
from datetime import datetime




#############Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']



#############Function for data ingestion
def merge_multiple_dataframe():
    #check for datasets, compile them together, and write to an output file
    csv_files = glob.glob("%s/*.csv" % input_folder_path)

    df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)

    df.drop_duplicates(inplace=True)

    df.to_csv("%s/finaldata.csv" % output_folder_path, index=False)

    with open(os.path.join(output_folder_path, "ingestedfiles.txt"), "w") as report_file:
        for line in csv_files:
            report_file.write(line + "\n")



if __name__ == '__main__':
    merge_multiple_dataframe()
