from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class Grapher:

    def __init__(self):
        pass

    def top_bar_chart(self, x_labels, data, y_label, title):
        """
            Graphs a top N bar graph with labels.

            Parameters
            ----------
            x_labels: list[str]
                A list of labels to discribe each graphed data on the x label axis.
            data: list[int]
                Y values for each corresponding x value from x_labels.
            y_label: str
                The y label string to describe what is bring plotted.
            title: str
                The title of the graph.
        """
        fig, ax = plt.subplots()
        ax.bar(x_labels, data, align='edge')
        for i, n in enumerate(data):
            s = str(int(n))
            ax.text(i, n + 10, s)
        ax.set_ylabel(y_label)
        plt.tight_layout()
        plt.title(title)
        plt.show()
        return fig

    def top_country_langs(self, countries, langs):
        fig = plt.figure()
        ax = Axes3D(fig)
        x = np.arange(10)
        y = np.arange(1, 11)
        x_mesh, y_mesh = np.meshgrid(x, y)
        x, y = x_mesh.ravel(), y_mesh.ravel()
        z = np.zeros(len(x))
        dx = np.ones(len(x)) * 0.5
        dy = np.ones(len(x)) * 0.5
        dz = np.arange(100)
        lang_rank = np.transpose([arr[1] for arr in langs]).ravel()
        ax.bar3d(x, y, z, dx, dy, lang_rank, shade=True)
        ax.set_xlabel('Top Countries')
        ax.set_xticks(x)
        ax.set_xticklabels(countries)
        ax.set_ylabel('Top Languages')
        ax.set_yticks(y)
        ax.set_zlabel('Repo Count')
        plt.tight_layout()
        plt.title('Top Locations and Their Top Languages')
        plt.show()

    def watcher_contributor_scatter(self, data, repo_names):
        x = [watchers[0] for watchers in data]
        y = [contributors[1] for contributors in data]
        plt.scatter(x, y)
        plt.show()
        