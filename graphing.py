import numpy as np
import matplotlib.pyplot as plt


def create_scatter_plot(file_name):
    f = open(file_name, 'r')
    seperated = map(lambda x: x.split(','), f.read().split('\n')[1:-1])
    names = map(lambda x: x[0], seperated)
    y = map(lambda x: float(x[1]), seperated)
    x = map(lambda x: float(x[2]), seperated)
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('std_dev')
    ax.set_ylabel('mean_points')

    fig.savefig('%s_plot.png' % file_name)

    # for i, txt in enumerate(names):
    #     ax.annotate(txt, (x[i],y[i]))


if __name__ == '__main__':
    create_scatter_plot('nfl_player_variance_2014.csv')
