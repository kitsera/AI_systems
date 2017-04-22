import Field
from Utils import *


class ISODATA:

    def __init__(self, points, iter, k, Qn, Qs, Qc, l):
        self.field = Field.Field(points, k, Qn, Qs, Qc, l)
        self.max_iterations = iter
        self.step_1(0)

    def step_1(self, l):
        for i in range(l, self.max_iterations):
            Utils.spread_points(self.field)
            Utils.delete_cluster(self.field)
            Utils.calc_cluster_center(self.field)
            Utils.calc_avarage_dists(self.field)
            Utils.calc_avarage_dist(self.field)

            iteration_end = i == self.max_iterations
            even_iteration = i % 2 == 0
            too_many_clusters = len(self.field.get_clusters()) >= 2 * self.field.get_max_clusters()
            too_few_clusters = len(self.field.get_clusters()) <= 0.5 * self.field.get_max_clusters()

            if iteration_end:
                self.field.set_density(0)
                Utils.calc_cluster_dists(self.field)
                Utils.filter_cluster_dists(self.field)
                Utils.combine_clusters(self.field)
                self.step_1(i + 1)

            elif even_iteration or too_many_clusters:
                Utils.calc_cluster_dists(self.field)
                Utils.filter_cluster_dists(self.field)
                Utils.combine_clusters(self.field)
                self.step_1(i + 1)

            elif too_few_clusters:
                Utils.calc_sigma(self.field)
                Utils.calc_max_sigma(self.field)
                size = len(self.field.get_clusters())

                for j in range(size):
                    cluster_too_big = self.field.get_clusters()[j].get_sigma_max() > self.field.get_deviation()
                    number_too_big = self.field.get_clusters()[j].get_points_count() > 2 * (self.field.get_min_cluster_points() + 1)
                    distance_too_big = self.field.get_clusters()[j].get_avarage_distance() > self.field.get_avarage_dist()

                    if cluster_too_big and distance_too_big and number_too_big:
                        Utils.divide_clusters(self.field, self.field.get_clusters()[j])
                        self.step_1(i + 1)
                    elif cluster_too_big and too_few_clusters:
                        Utils.divide_clusters(self.field, self.field.get_clusters()[j])
                        self.step_1(i + 1)
                Utils.calc_cluster_dists(self.field)
                Utils.filter_cluster_dists(self.field)
                Utils.combine_clusters(self.field)


    def get_field(self):
        return self.field

    def print_field(self):
        return self.field.show()