'''
Load_Time_Data

Contains loading functions for each file type. Execute load into pandas and timing for each filetype.


Methods
    execute_load(file_types=['.json', '.py', '.pickle'], base_name='test')
    *returns dictionary {filetype(str), dict_load_time(float), pandas_load_time(float)}

'''
import time
import pickle
import pandas as pd
import json
import sys

timer_iterations = 100

def time_function(function):
    def wrapper(**kwargs):
        total_time = 0
        for _ in range(timer_iterations):
            t0 = time.time()
            function(kwargs['path'])
            t1 = time.time()
            total_time += (t1-t0)
            delete_imported_data()
        return total_time/timer_iterations
    return wrapper

@time_function
def load_json_as_dictionary(path):
    with open(path, 'r') as file:
        data = json.load(file)

@time_function
def load_py_as_dictionary(path=None):
    from test import data

@time_function
def load_pickle_as_dictionary(path):
    with open(path, 'rb') as handle:
        data = pickle.load(handle)

@time_function
def load_json_as_dataframe(path):
    data = pd.read_json(path)

@time_function
def load_py_as_dataframe(path=None):
    from test import data
    data = pd.DataFrame(data)

@time_function
def load_pickle_as_dataframe(path=None):
    with open(path, 'rb') as handle:
        data = pd.DataFrame(pickle.load(handle))

def load_file(filepath, filetype, output_type):
    load_menu = {
        '.json': {'dataframe':load_json_as_dataframe, 'dictionary':load_json_as_dictionary},
        '.py': {'dataframe':load_py_as_dataframe, 'dictionary':load_py_as_dictionary},
        '.pickle': {'dataframe':load_pickle_as_dataframe, 'dictionary':load_pickle_as_dictionary},
    }

    loader = load_menu[filetype][output_type]
    return loader(path=filepath)

def delete_imported_data():
    try:
        del sys.modules['test']
    except:
        return


if __name__ == "__main__":
    # load_pickle_as_dictionary(path='test.pickle')
    # load_json_as_dictionary(path='test.json')
    load_py_as_dictionary(path='test.py')
    # load_pickle_as_dataframe(path='test.pickle')
    # load_json_as_dataframe(path='test.json')
    # load_py_as_dataframe(path='test.py')