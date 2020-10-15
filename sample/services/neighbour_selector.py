from sklearn.neighbors import NearestNeighbors
from sample.models.NeighbourData import NeighbourData

columns = ['feat-1', 'feat-2']


def execute(data):
    # 4) Get nearest neighbor indices
    k_nn = 200
    df_nbh = data[columns].copy()

    nbh_model = NearestNeighbors(algorithm='ball_tree', metric='minkowski',
                                 metric_params=None, leaf_size=30, p=2, n_jobs=-1)
    nbh_model.fit(df_nbh)
    nbh_distances, nbh_indices = nbh_model.kneighbors(df_nbh, k_nn, return_distance=True)

    return NeighbourData(data, nbh_distances, df_nbh, nbh_model)
