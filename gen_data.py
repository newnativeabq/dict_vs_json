import random
from faker import Faker
from faker.providers import geo
import json
import pickle
import os
import multiprocessing


class FakeDataGenerator():
    def __init__(self, nest_depth=1, records_per_level = 100):
        self.nest_depth = nest_depth
        self.records_per_level = records_per_level
        self.fake = init_faker()
        self.faker_menu = {
            'tag':
                [
                    'self.fake.name()',
                    'self.fake.color_name()',
                ],
            'data':
                [
                    'self.fake.address()',
                    'self.fake.location_on_land()',
                    'self.fake.sentences(nb=2, ext_word_list=None)',
                ],
        }

    def __repr__(self):
        return 'FakeDataGenerator ({}, {})'.format(self.nest_depth, self.records_per_level)

    def __len__(self):
        return self.nest_depth * self.records_per_level

    def build_fake_data(self):
        self.__cache = {}
        for i in range(self.records_per_level):
            self.__cache[i] = self.build_record()
        return self.__cache

    def build_record(self):
        record = {}
        j = 0
        for i in range(self.nest_depth):
            j += 1
            if j >= i:
                record[self.get_value('tag')] = self.get_value('data')
            else:
                record[self.get_value('tag')] = self.build_record()
        return record

    def get_value(self, type):
        self.fake.seed(random.randint(1,100))
        return eval(
            random.choice(self.faker_menu[type])
        )


def init_faker():
    faker = Faker()
    faker.add_provider(geo)
    return faker

def build_json(data, filename):
    assert type(data) == dict, "data to write not in python dict format"
    full_filename = filename+'.json'
    try:
        with open(full_filename, 'w') as file:
            json.dump(data, file)
            message = '.json file created successfully at {}'.format(os.path.join(os.getcwd(), full_filename))
            # print(message)
            return message
    except:
        raise

def build_dict(data, filename):
    assert type(data) == dict, "data to write not in python dict format"
    full_filename = filename+'.py'
    try:
        with open(full_filename, 'w') as file:
            file.write('data='+str(data))
            message = '.py file created successfully at {}'.format(os.path.join(os.getcwd(), full_filename))
            # print(message)
            return message
    except:
        raise

def build_pickle(data, filename):
    assert type(data) == dict, "data to write not in python dict format"
    full_filename = filename+'.pickle'
    try:
        with open(full_filename, 'wb') as file:
            pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
            message = '.pickle file created successfully at {}'.format(os.path.join(os.getcwd(), full_filename))
            # print(message)
            return message
    except:
        raise

def generate_fake_data_files(nest_level, records_per_level):
    new_gen = FakeDataGenerator(nest_level, records_per_level)
    fake_data = new_gen.build_fake_data()
    json_process = multiprocessing.Process(target=build_json, args=(fake_data, 'test',))
    py_process = multiprocessing.Process(target=build_dict, args=(fake_data, 'test',))
    pickle_process = multiprocessing.Process(target=build_pickle, args=(fake_data, 'test',))
    json_process.start()
    py_process.start()
    pickle_process.start()
    json_process.join()
    py_process.join()
    pickle_process.join()


if __name__ == "__main__":
    generate_fake_data_files(2, 2)


