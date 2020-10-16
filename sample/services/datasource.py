import pandas as pd
from sample.models.plots import ScatterPlot
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
source_location = dir_path + '/../../ressources/syntheticData/'
default_file = 'waveData_5.csv'


def files():
    return os.listdir(source_location)


def load():
    return load_file(default_file)


def load_scatter_plot(filename):
    data = load_file(filename)
    return ScatterPlot(data, data['labels'])


def load_file(filename):
    col_names = ['feat-1', 'feat-2', 'labels']
    data = pd.read_csv(source_location + filename, names=col_names)
    # col_names.remove('index')
    # data = data[col_names]
    data = data.astype({'labels': 'int32'})
    print(data.shape)
    return data
