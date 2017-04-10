import math

import Cluster
import Point

from Lab_1 import Combination


class Utils:

    @staticmethod
    def point_dist(a, b):
        result = math.sqrt(math.pow(a.get_x() - b.get_x(), 2) + math.pow(a.get_y() - b.get_y(), 2))
        # print(result)
        return result

    @staticmethod
    def delete_cluster(field):
        for cluster in field.get_clusters():
            if cluster.get_points_count() < field.get_min_cluster_points():
                for point in cluster.points:
                    field.get_points().remove(point)
                field.get_clusters().remove(cluster)

    @staticmethod
    def spread_points(field):
        if len(field.get_clusters()) == 0:
            cluster = Cluster.Cluster()
            cluster.get_points().extend(field.get_points())
            field.get_clusters().append(cluster)
        else:
            for cluster in field.get_clusters():
                cluster.get_points().clear()
            for point in field.get_points():
                min_dist = Utils.point_dist(point, field.get_clusters()[0].get_center())
                cluster_count = 0

                for i in range(len(field.get_clusters())):
                    current_dist = Utils.point_dist(point, field.get_clusters()[i].get_center())
                    if current_dist < min_dist:
                        min_dist = current_dist
                        cluster_count = i

                field.get_clusters()[cluster_count].get_points().append(point)

    @staticmethod
    def calc_cluster_center(field):
        for cluster in field.get_clusters():
            center = Point.Point()
            for point in cluster.get_points():
                center += point
            center = center/cluster.get_points_count()
            cluster.set_center(center)

    @staticmethod
    def calc_avarage_dists(field):
        for cluster in field.get_clusters():
            total_dist = 0
            for point in cluster.get_points():
                total_dist += Utils.point_dist(point, cluster.get_center())
            cluster.set_avarage_distance(total_dist/cluster.get_points_count())

    @staticmethod
    def calc_avarage_dist(field):
        total_dist = 0
        for cluster in field.get_clusters():
            total_dist += cluster.get_avarage_distance() * cluster.get_points_count()
        field.set_avarage_dist(total_dist/field.get_points_count())

    @staticmethod
    def calc_sigma(field):
        for cluster in field.get_clusters():
            total_delta_x = 0
            total_delta_y = 0
            for point in cluster.get_points():
                total_delta_x += math.pow(point.get_x() - cluster.get_center().get_x(), 2)
                total_delta_y += math.pow(point.get_y() - cluster.get_center().get_y(), 2)
            cluster.set_sigma_x(math.sqrt(total_delta_x / cluster.get_points_count()))
            cluster.set_sigma_y(math.sqrt(total_delta_y / cluster.get_points_count()))

    @staticmethod
    def calc_max_sigma(field):
        for cluster in field.get_clusters():
            if cluster.get_sigma_x() > cluster.get_sigma_y():
                cluster.set_sigma_max(cluster.get_sigma_x())
                cluster.set_sigma_max_component("X")
            else:
                cluster.set_sigma_max(cluster.get_sigma_y())
                cluster.set_sigma_max_component("Y")

    @staticmethod
    def divide_clusters(field, cluster):
        plus = Cluster.Cluster()
        minus = Cluster.Cluster()
        plus.set_center(Point.Point())
        minus.set_center(Point.Point())
        gamma = 0.5

        if cluster.get_sigma_max_component() == "X":
            plus.get_center().set_x(cluster.get_center().get_x() + cluster.get_sigma_max() * gamma)
            minus.get_center().set_x(cluster.get_center().get_x() - cluster.get_sigma_max() * gamma)
            plus.get_center().set_y(cluster.get_center().get_y())
            minus.get_center().set_y(cluster.get_center().get_y())

        else:
            plus.get_center().set_y(cluster.get_center().get_y() + cluster.get_sigma_max() * gamma)
            minus.get_center().set_y(cluster.get_center().get_y() - cluster.get_sigma_max() * gamma)
            plus.get_center().set_x(cluster.get_center().get_x())
            minus.get_center().set_x(cluster.get_center().get_x())

        field.get_clusters().remove(cluster)
        field.get_clusters().append(plus)
        field.get_clusters().append(minus)

    @staticmethod
    def calc_cluster_dists(field):
        distances = []
        for i in range(len(field.get_clusters())-1):
            for j in range(i + 1, len(field.get_clusters())):
                dist = Utils.point_dist(field.get_clusters()[i].get_center(), field.get_clusters()[j].get_center())
                if dist < field.get_density():
                    distances.append(Combination.Combination(field.get_clusters()[i], field.get_clusters()[j], dist))
        field.set_cluster_dists(distances)

    @staticmethod
    def filter_cluster_dists(field):
        sorted(field.get_cluster_dists(), key=lambda k: k.get_dist())
        for i in range(field.get_density(), len(field.get_cluster_dists())):
            field.get_cluster_dists().remove(i)

    @staticmethod
    def combine_clusters(field):
        forbitten = [Cluster.Cluster()]
        for combination in field.get_cluster_dists():
            if combination.get_first() in forbitten or combination.get_second() in forbitten:
                continue
            else:
                result = Cluster.Cluster()
                result.set_center(Point.Point())
                first_size = combination.get_first().get_points_count()
                second_size = combination.get_second().get_points_count()
                first_x = combination.get_first().get_center().get_x()
                first_y = combination.get_first().get_center().get_y()
                second_x = combination.get_second().get_center().get_x()
                second_y = combination.get_second().get_center().get_y()
                result.get_center().set_x((first_x * first_size + second_x * second_size) / (first_size + second_size))
                result.get_center().set_y((first_y * first_size + second_y * second_size) / (first_size + second_size))
                field.get_clusters().append(result)
                field.get_clusters().remove(combination.get_first())
                field.get_clusters().remove(combination.get_second())


