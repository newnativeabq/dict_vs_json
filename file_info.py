'''
File_Info

Create a file information object that has an update method that will fetch the following
    for each filetype specified in self.lookup_types:

    - size(in bytes)


Methods:

    get_file_info()
    * returns dictionary {type(str): size_in_bytes(int)}
'''
import os
import load_time_data
from load_time_data import load_file


class FileInfo():
    def __init__(self, name='test', **kwargs):
        self.base_name = name
        self.filetypes = [
            '.json',
            '.py',
            '.pickle',
        ]
        self.outputtypes = [
            'dataframe',
            'dictionary',
        ]
        self.get_file_info()

    def __repr__(self):
        return 'File information available for {} files.'.format(len(self.file_info))

    def get_file_info(self):
        self.file_info = []
        for filetype in self.filetypes:
            filepath = get_filepath(self.base_name, filetype)
            if file_exists(filepath):
                for output_type in self.outputtypes:
                    file_info_to_add = {
                        'file_type': filetype,
                        'output_type': output_type,
                        'size': os.path.getsize(filepath),
                        'load_time': load_file(
                                                filepath=filepath,
                                                filetype=filetype,
                                                output_type=output_type
                                                )
                    }
                    self.file_info.append(file_info_to_add)



def file_exists(path):
    return os.path.exists(path)

def get_filepath(base_name, file_type):
    return os.path.abspath(base_name+file_type)


if __name__ == "__main__":
    files = FileInfo()
    print(files.file_info)