class ClusterFilters:
    def __init__(self, num_clusters,
                 wasser_error,
                 vars_from,
                 vars_until,
                 vars_step_size):
        if num_clusters is None:
            self.num_clusters = 6
        else:
            self.num_clusters = int(num_clusters)

        if wasser_error is None:
            self.wasser_error = 0
        else:
            self.wasser_error = float(wasser_error)

        if vars_from is None:
            self.vars_from = 0
        else:
            self.vars_from = float(vars_from)

        if vars_until is None:
            self.vars_until = 0
        else:
            self.vars_until = float(vars_until)

        if vars_step_size is None:
            self.vars_step_size = 0
        else:
            self.vars_step_size = float(vars_step_size)
