from flask import request

from sample.models.filters.cluster_filters import ClusterFilters


def extract_query_params():
    return ClusterFilters(request.args.get('numClusters'),
                          request.args.get('wasserError'),
                          request.args.get('varsFrom'),
                          request.args.get('varsUntil'),
                          request.args.get('varsStepSize'))
