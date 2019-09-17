# Data Storage Experiment for Python Native Frameworks

A generative exploration of loading time for datasets of varying complexity across single-file storage types.

## Background

JSON similarity to python's dictionary data model got me wondering why we need JSON at all in python native frameworks such as Django or Flask.  A dictionary object can be imported.  In fact "import data" seems particulary pthonic to me.  This experiment first seeks to generate JSON, .py, and pickled dictionary files of various lenghts and complexity.  Second, the program loads the data into two data types used in data science and application development, a Pandas dataframe and python dictionary.

## Usage

python run.py

## Parameters

**Nest depth parameters** contain min, max, and stepsize for how deep an object to create.

**Records Per Nest Level Parameters** contain min, max, and stepsize for how wide each level should be.

## Next Steps

Refactoring the code to run faster is important.  Bottleneck exploration and potentially using stored data to generate the files instead of the faker library might be useful.

Analyzing the data:  Data collection is underway!  If you'd like to contribute, please let me know.

As a part of analyzing output, ensuring that the program is working as expected.

Contact me on [Twitter @vincebrandon](https://twitter.com/vincebrandon)
or through my site at [vincebrand.com](https://vincebrand.com)