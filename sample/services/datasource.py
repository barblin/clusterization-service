import pandas as pd
from sample.models.plots import ScatterPlot
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
source_location = dir_path + '/../../ressources/syntheticData/'
default_file = 'waveData_5.csv'

cached_files = {}


def files():
    return os.listdir(source_location)


def load():
    return load_file(default_file)


def load_scatter_plot(filename):
    data = load_file(filename)
    return ScatterPlot(data, data['labels'])


def data_without_labels(df):
    modified = df.copy()
    del modified['labels']
    return modified.to_numpy()


def load_file(filename):
    if filename in cached_files.keys():
        return cached_files[filename]

    col_names = ['feat-1', 'feat-2', 'labels']
    data = pd.read_csv(source_location + filename, names=col_names)
    # col_names.remove('index')
    # data = data[col_names]
    data = data.astype({'labels': 'int32'})

    cached_files[filename] = data

    return cached_files[filename]
