import os

import pandas as pd

from sample.config.config import resources
from sample.models.plots import ScatterPlot

default_file = 'waveData_5.csv'
col_feat_1 = 'feat-1'
col_feat_2 = 'feat-2'
col_labels = 'labels'

cached_files = {}


def list_files():
    return os.listdir(resources())


def load():
    return load_file(default_file)


def load_scatter_plot(filename):
    data = load_file(filename)
    return ScatterPlot(data, data['labels'])


def data_without_labels(df):
    modified = df[[col_feat_1, col_feat_2]]
    return modified.to_numpy()


def load_file(filename):
    if filename in cached_files.keys():
        return cached_files[filename]

    col_names = [col_feat_1, col_feat_2, col_labels]
    data = pd.read_csv(resources() + filename, names=col_names)
    data = data.astype({col_labels: 'int32'})

    cached_files[filename] = data

    return cached_files[filename]
