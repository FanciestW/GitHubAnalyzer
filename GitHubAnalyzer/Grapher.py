import matplotlib.pyplot as plt

class Grapher:

    def __init__(self):
        pass

    def top_bar_chart(self, x_labels, data, y_label, title):
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