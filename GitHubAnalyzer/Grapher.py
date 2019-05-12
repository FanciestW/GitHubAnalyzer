from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import re

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

            Returns
            -------
            pyplot.Figure
                The py plot figure
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
        """
            Graphs the top countries and their top languages.

            Parameters
            ----------
            countries: list(str)
                A list of strings containing country names.
            
            Returns
            -------
            pyplot.figure
                A figure for includes the graph of the top country languages.

            Returns
            -------
            pyplot.Figure
                The py plot figure
        """
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
        return fig

    def watcher_contributor_scatter(self, data, repo_names):
        """
            Plots a scatter graph to compare watchers and contributors.

            Parameters
            ----------
            data: list(tuple)
                A list of tuples containing watcher and contributor data.
            repo_names: list(str)
                A list of repository names that correspond with each data point.
        """
        x = [watchers[0] for watchers in data]
        y = [contributors[1] for contributors in data]
        names = [re.sub('^((http[s]?:\/\/(www.)?)?github.com\/)', '', i, flags=re.IGNORECASE) for i in repo_names]
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
                  'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        plt.scatter(x, y, c=colors)
        patches = [mpatches.Patch(color=colors[i], label=names[i]) for i in np.arange(len(names))]
        plt.legend(handles=patches)
        plt.xlabel("# of Watchers")
        plt.ylabel("# of Contributors")
        plt.title("Top 10 Repos: Watchers vs Contributors")
        plt.show()

    def repoYearLine(self, years_data, title):
        """
            Graphs a line graph of repository creation over time.

            Parameters
            ----------
            years_data: list(tuple)
                A list of tuples where each tuple contains a year and repo count.
            title: str
                The title of the graph
            
            Returns
            -------
            pyplot.Figure
                The py plot figure
        """
        years = [int(y[0]) for y in years_data]
        year_counts = [int(y[1]) for y in years_data]
        year_range = np.arange(min(years), max(years)+1).tolist()
        data = list()
        for y in year_range:
            if y in years:
                data.append(year_counts[years.index(y)])
            else:
                data.append(0)
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set_xticks(np.arange(len(year_range)))
        ax.set_xticklabels(year_range)
        plt.title = title
        plt.tight_layout()
        plt.show()
        return fig

    def activityHist(self, data, xlabels):
        """
            A histogram of activity during certain times of the day.

            Parameters
            ----------
            data: list(int)
                Value of each histogram bin.
            xlabels: list(str)
                List of bin values that label the times of the day.

            Returns
            -------
            pyplot.Figure
                The py plot figure
        """
        fig, ax = plt.subplots()
        ax.hist(np.arange(len(xlabels)), np.arange(len(xlabels) + 1) - 0.5, weights=data, edgecolor='black')
        ax.set_xticks(np.arange(len(xlabels)))
        ax.set_xticklabels(xlabels)
        ax.set(xticks=range(len(xlabels)), xlim=[-1, len(xlabels)])
        ax.set_ylabel('Activity Counts')
        plt.title('Time of Day Activity Histogram')
        plt.show()
        return fig

    def activityTypesBar(self, data, xlabels, ylabels):
        """
            Graphs a stacked bar graph of activity type in each time period.

            Parameters
            ----------
            data: list(list(int))
                A list of list of integers that represent the activity data.
            xlabels: list(str)
                List of bin values that label the times of the day.
            ylabels: list(str)
                List of strings describing the event types in order.
        """
        fig, ax = plt.subplots()
        bars = list()
        for i in range(len(data)):
            if i == 0:
                bar = ax.bar(np.arange(len(xlabels)), data[i])
                bars.append(bar)
            else:
                bar = ax.bar(np.arange(len(xlabels)), data[i], bottom=data[i-1])
                bars.append(bar)
        ax.set_xticks(np.arange(len(xlabels)))
        ax.set_xticklabels(xlabels)
        ax.set(xticks=range(len(xlabels)), xlim=[-1, len(xlabels)])
        ax.set_ylabel('Activity Counts')
        plt.legend(tuple(bars), tuple(ylabels))
        plt.title('Time of Day Activity Types')
        plt.show()
    