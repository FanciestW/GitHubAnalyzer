1) Programming language analysis

   - [x] What was the most popular primary programming language during the time window in 2012 covered by the data set? You can judge popularity by determining the set of repositories accessed in the time window and determining what the primary language was for each one. Create a bar chart showing the top 10 languages.

   - [x] Determine the top 10 countries responsible for Github repos. The country owning a particular repository can be determined by noting which user owns the repo, then finding an event where this user is the actor, and looking up the actor's location. Many users may not have a specified location, so do as much analysis as you can based on the locations that are filled in. For each of these countries, determine the relative popularity of the 10 languages determined in part (a). Create a 3D bar chart showing this correlation of productive countries and programming languages.

2) Repo popularity analysis

   - [x] What was the most popular repo during the time window in 2012? You can judge popularity by the total number of events that have occurred on the timeline during the window. Create a list of the top 10.

   - [x] For the top 10 repos found in part (a), determine the relationship between the number of contributors to each repo with the number of watchers of the repo. Pick the maximum number of watchers recorded during the time window for the one value. To determine the contributors, count the number of users that were actors on the repo and subtract any whose only action was a watch event. Display this using a 2D scatter plot, using different colors for each repo's data.

   - [x] Track the keyword "security" in repo descriptions accessed during the time window in 2012. Graph a curve showing the number of repos related to security that were created in each of the years that records have been kept.

3) Development analysis

   - [x] For the time window in 2012, determine the time of day in which the most development activity occurs. Break the day into four 6-hour blocks and determine the number of development activities that occurred in each time block over the year. Create a simple histogram showing these results.

   - [x] Analyze the activity in part (a) further. Break down the type of development activities into the following categories: Create, Fork, Delete, Commit, Pull Request, Other. Create a stacked bar graph to show this information, where each bar is subdivided into portions for each of the activity types.

   - [x] Analyze the activity in part (a) further. Determine what quantity of the development activity was done by contributors in the USA vs. contributors in the rest of the world. Create a stacked bar graph showing this country developer breakdown. Again, you can omit development actions taken by users without a specified location.

   - [x] What is the most active development day of the week? Using the data gathered in part (a), create an animation that shows the development activity broken down by which day of the week it occurred on in a bar graph, where the contents of the bar graph change over the weeks of the time window (this will not be a long animation).

   - [x] For the most popular repo found in part (2.a) above, determine the time it has taken to resolve each issue in the repo that was opened during the time window. Display a histogram to show these issue handling times (pick some reasonable amount of time to represent an unresolved issue during the window).

Extra credit - perform another non-trivial analysis, perhaps one of the suggestions you made in your list of five tasks that was sent to me.

Properly comment your code and submit it here on Blackboard, along with the graphs and text that are the output of your program for all of the analyses above.
