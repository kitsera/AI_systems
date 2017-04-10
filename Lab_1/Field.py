class Field:

    def __init__(self, points, k=4, Qn=1, Qs=1, Qc=3, l=1):
        self.points = points
        self.clusters = []
        self.max_clusters = k
        self.min_cluster_points = Qn
        self.deviation = Qs
        self.density = Qc
        self.max_combined_pairs = l
        self.avarage_dist = 0
        self.cluster_dists = []

    def get_max_clusters(self):
        return self.max_clusters

    def get_min_cluster_points(self):
        return self.min_cluster_points

    def get_deviation(self):
        return self.deviation

    def get_density(self):
        return self.density

    def set_density(self, density):
        self.density = density

    def get_max_combined_pairs(self):
        return self.max_combined_pairs

    def get_points(self):
        return self.points

    def get_points_count(self):
        return len(self.points)

    def get_clusters(self):
        return self.clusters

    def set_avarage_dist(self, dist):
        self.avarage_dist = dist

    def get_avarage_dist(self):
        return self.avarage_dist

    def set_cluster_dists(self, dist):
        self.cluster_dists = dist

    def get_cluster_dists(self):
        return self.cluster_dists

    def show(self):
        for cluster in self.get_clusters():
            print(cluster)
