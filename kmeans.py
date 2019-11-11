"""
Designed and Created by Pourya Pooryeganeh
2018 Fall
"""
import numpy as np
import operator
import matplotlib.pyplot as plt
import matplotlib.cm as cm

r = lambda: np.random.randint(1, 100)

class Centroids:

    def __init__(self , pos):

        self.pos = pos
        self.points = []
        self.prev_points = []
        self.color = None

class KMeans:

    def __init__(self , n_centroids = 5):

        self.n_centroids = n_centroids
        self.centroids = []

        #generate initial centroids :

        for _ in range(n_centroids):
            self.centroids.append(Centroids(np.array([r() , r()])))

        #assign a color to each centroid

        colors = cm.rainbow(np.linspace(0, 1, len(self.centroids)))

        for i , c in enumerate(self.centroids):
            c.colors : colors[i]
        
    def sample_data(self , samples = 50):

        self.x = [[r() , r()] for _ in range(samples)]
        
    def assign_centroid(self , x):

        #return centroid closest to a point

        distances = {}

        for centroid in self.centroids:
            distances[centroid] = np.linalg.norm(centroid.pos - x)

        closest = min(distances.items() , key = operator.itemgetter(1))[0]
        return closest

    def _update_centroids(self , reset = True):

        for centroid in self.centroids:
            centroid.prev_points = centroid.points
            x_cor = [x[0] for x in centroid.points]
            y_cor = [y[1] for y in centroid.points]

            try :
                centroid.pos[0] = sum(x_cor)/len(x_cor)
                centroid.pos[1] = sum(y_cor)/len(y_cor)

            except :
                pass

            if reset :
                centroid.points = []

            
    def fit(self):

        """im the game"""

        self.n_iters = 0
        fit = False

        while not fit:

            for point in self.x:

                closest = self.assign_centroid(point)
                closest.points.append(point)

            if len([c for c in self.centroids if c.points == c.prev_points]) == self.n_centroids:
                fit = True
                self._update_centroids(reset = False)

            else:
                self._update_centroids()

            self.n_iters += 1

    def plot(self):

        for i , c in enumerate(self.centroids):

            plt.scatter(c.pos[0] , c.pos[1] , marker = 'o' , color = c.color , s = 75)
            x_cors = [x[0] for x in c.points]        
            y_cors = [y[1] for y in c.points]
            plt.scatter(x_cors , y_cors , marker = '.' , color = c.color)
        
        
        title = 'the game KMeans'
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(title)
        plt.show()



if __name__ == '__main__':

    km = KMeans(n_centroids = 5)
    km.sample_data()
    km.fit()
    km.plot()













