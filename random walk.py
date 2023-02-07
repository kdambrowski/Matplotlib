
import matplotlib.pyplot as plt
from random import choice


class RandomWalk:

    def __init__(self,num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def random_walk(self):
        while len(self.x_values)<self.num_points:

            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)


if __name__ == '__main__':
    rw = RandomWalk()
    rw.random_walk()

    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(18, 7), dpi=(126))
    points = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Reds, edgecolor='black', s=10)
    ax.scatter(0,0, c='orange', s=20, label= 'Start of x and y axes')
    ax.scatter(rw.x_values[1], rw.y_values[1], c='blue', s=20, label= 'first step')
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c='green', s=20, label= 'last step')
    ax.set_title('random walk', fontsize=23)
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(True)


    plt.legend()
    plt.show()
