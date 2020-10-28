import json


class MinimumTreeResponse:
    def __init__(self, edges):
        self.data = []
        self.max_X = 0
        self.max_Y = 0

        for edge in edges:
            if self.max_X < edge.point1.coords[0]:
                self.max_X = edge.point1.coords[0]

            if self.max_X < edge.point2.coords[0]:
                self.max_X = edge.point2.coords[0]

            if self.max_Y < edge.point1.coords[1]:
                self.max_Y = edge.point1.coords[1]

            if self.max_Y < edge.point2.coords[1]:
                self.max_Y = edge.point2.coords[1]

            self.data.append((edge.point1.__dict__, edge.point2.__dict__))

    def jsonify(self):
        return json.dumps(self.__dict__)
