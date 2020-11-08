from flask import request

from sample.models.cluster_filters import ClusterFilters


def extract_query_params():
    return ClusterFilters(request.args.get('numClusters'),
                          request.args.get('wasserError'),
                          request.args.get('remOutliers'),
                          request.args.get('stdvMultiplier'),
                          request.args.get('normalizeNeighDist'))
