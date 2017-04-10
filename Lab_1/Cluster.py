from Lab_1 import Point


class Cluster:

    def __init__(self):
        self.points = []
        self.center = Point.Point(0, 0)
        self.avarageDistance = 0
        self.sigmaX = 0
        self.sigmaY = 0
        self.MaxSigma = 0
        self.MaxSigmaComponent = 0

    def get_center(self):
        return self.center

    def set_center(self, center):
        self.center = center

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def get_points_count(self):
        return len(self.points)

    def set_avarage_distance(self, distance):
        self.avarageDistance = distance

    def get_avarage_distance(self):
        return self.avarageDistance

    def set_sigma_max(self, max_sigma):
        self.MaxSigma = max_sigma

    def get_sigma_max(self):
        return self.MaxSigma

    def get_sigma_x(self):
        return self.sigmaX

    def set_sigma_x(self, sigma_x):
        self.sigmaX = sigma_x

    def get_sigma_y(self):
        return self.sigmaY

    def set_sigma_y(self, sigma_y):
        self.sigmaY = sigma_y

    def get_sigma_max_component(self):
        return self.MaxSigmaComponent

    def set_sigma_max_component(self, component):
        self.MaxSigmaComponent = component

    def __str__(self):
        result = "========= Cluster =========\n"
        result += "Cluster centre: " + self.center.__str__() + '\n'
        result += "Cluster points: \n" + self.points.__str__() + '\n'
        return result
