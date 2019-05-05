import matplotlib.pyplot as plt

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

    def top_3d_bar(self, x_labels, xdata, ydata, title):
        pass
