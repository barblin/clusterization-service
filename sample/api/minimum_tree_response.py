import json


class MinimumTreeResponse:
    def __init__(self, edges):
        self.data = []
        self.max_X = 0
        self.max_Y = 0

        for edge in edges:
            if self.max_X < edge.point1[0]:
                self.max_X = edge.point1[0]

            if self.max_X < edge.point2[0]:
                self.max_X = edge.point2[0]

            if self.max_Y < edge.point1[1]:
                self.max_Y = edge.point1[1]

            if self.max_Y < edge.point2[1]:
                self.max_Y = edge.point2[1]

            self.data.append((edge.point1, edge.point2))

    def jsonify(self):
        return json.dumps(self.__dict__)