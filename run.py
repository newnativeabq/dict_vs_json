'''
Run data collection

Sample various nesting levels and length and get timing information.
'''

import gen_data
from gen_data import generate_fake_data_files
import file_info
from file_info import FileInfo
import pandas as pd
import numpy as np
from progress import progress


def export_data(dataframe):
    dataframe.to_csv('/mnt/cluster_share/lambda_school/4.portfolioprojects/dict_vs_json/run_data.csv')

if __name__ == "__main__":
    count = 0
    max_level_size = 500000
    min_level_size = 5000
    level_step = 5000

    max_nest_size = 5
    min_nest_size = 1
    nest_step = 1

    total_generations = int((max_level_size-min_level_size)/level_step) \
                             * int((max_nest_size-min_nest_size)/nest_step)

    nest_sizes = np.arange(min_nest_size, max_nest_size, nest_step)
    level_sizes = np.arange(min_level_size, max_level_size, level_step)

    columns = ['file_type', 'output_type', 'size', 'load_time', 'nest_level', 'records_per_level']
    df = pd.DataFrame(columns=columns)

    for nest_level in nest_sizes:
        for records_per_level in level_sizes:
            progress(count=count, total=total_generations, status='Running Data Collection')

            generate_fake_data_files(nest_level=nest_level, records_per_level=records_per_level)
            file_handler = FileInfo()
            file_handler.get_file_info()
            df2 = pd.DataFrame(file_handler.file_info)
            df2['nest_level'] = nest_level
            df2['records_per_level'] = records_per_level
            df = df.append(df2, ignore_index=True, sort=True)

            count += 1

    print(len(df))
    export_data(df)
