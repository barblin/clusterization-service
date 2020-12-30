import json


class MinimumTreeResponse:
    def __init__(self, edges):
        self.data = []
        self.max_X = 0
        self.max_Y = 0

        for edge in edges:
            if self.max_X < edge.vertex1.coords[0]:
                self.max_X = edge.vertex1.coords[0]

            if self.max_X < edge.vertex2.coords[0]:
                self.max_X = edge.vertex2.coords[0]

            if self.max_Y < edge.vertex1.coords[1]:
                self.max_Y = edge.vertex1.coords[1]

            if self.max_Y < edge.vertex2.coords[1]:
                self.max_Y = edge.vertex2.coords[1]

            self.data.append((edge.vertex1.__dict__, edge.vertex2.__dict__))

    def jsonify(self):
        return json.dumps(self.__dict__)
