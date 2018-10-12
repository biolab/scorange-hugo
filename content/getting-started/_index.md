+++
title = "Getting started"
url = "/getting-started/"
listing = true
+++


### Download and Install
{{< link_new url="/download/" name="Download">}} Orange distribution package and run the
installation file on your local computer. {{< link_new url="http://biolab.github.io/datafusion-installation-guide/" name="Here">}} is a step-by-step installation guide, that we recommend you to follow.

### Run

Locate Orange program icon. It is probably on your desktop (Win, Linux) or in the Applications folder (Mac).
Double click on the icon to run Orange.
\
![Orange Icon](/getting_started/orange-icon.png__210x10000_q95.jpg)
                      

### Welcome to Orange
At the start, Orange opens a welcome screen. From here you can create new data mining workflows or browse through the ones
you have already created. If you are running Orange for the first time, start by clicking on the Tutorial icon to
browse through tutorial workflows.
![welcome.png](/getting_started/welcome-screen.png)
                        

### Tutorials

From the tutorials window, select any of the preloaded data mining workflows. Here, we will choose the one with
hierarchical clustering.

![tutorials.png](/getting_started/hierarchical-clustering.png)
                        
Selected tutorial will open in Orange canvas. In Orange, data mining workflows consist of computational
components called widgets. Widgets do all the work and exchange information. They can communicate through channels.
In the workflow below, the File widget sends its data to the Data Table widget and Distance widget, which, in turn,
communicates the computed distances to two other widgets in the workflow.

![hierarhical-clustering-workflow.png](/getting_started/hierarchical-clustering-tutorial.png)

Any data mining starts with the data. In our hierarchical clustering schema, the File widget reads the data from the
file on your computer and sends the data to other widgets.

![file-widget-icon.png](/getting_started/file-widget.png)
                  
Double click on the File widget icon to open it. Select "Browse documentation data sets..." and from the list of
pre-installed data files choose iris.tab.
![file-widget.png](/getting_started/browse-documentiation-data-sets.png)

The File widget will now read the [the famous data set on
150 Iris flowers](http://en.wikipedia.org/wiki/Iris_flower_data_set) and send it to the workflow. The changes will propagate through the workflow updating its
widgets. Close the window of the File widget and double click on the Data Table widget to open it. This displays
the data that we have just read.

![data-table.png](/getting_started/data-table-iris.png)

Open and close other widgets to see what they do. In this workflow, the most interesting widget is Hierarchical
Clustering that displays clustering results. Scroll through the dendrogram - the tree-based rendering of the
clustering - to check if the algorithm correctly identified the three species of Iris.

![hierarhical-clustering.png](/getting_started/hierarchical-clustering-dendrogram.png)

You may now open other tutorials (from the Help menu choose Tutorials). Or create a workflow of your own.

### Your Own Workflow

We first need to start with an empty canvas. Click on New in Orange's welcome screen, or, if Orange is already
running, choose New from the File menu.

We will explore the data on passengers of the HMS Titanic and develop a model to predict the probability of survival
based on the passenger's traveling class, gender and age. Let us start by placing the File and Data Table widgets on the
canvas.

![canvas-titanic.png](/getting_started/linking-widgets.png)

We would like the File widget to read the data and send it to the Data Table for inspection. We need to connect
these two widgets to establish a communication between them. Click on the dashed line besides the File
widget and drag the line to the Data Table.

![file-data-table-connection.png](/getting_started/linking-widgets2.png)

To load the data, open the File widget (double click on its icon), select "Browse documentation data sets" from the
Data File box and choose titanic.tab.

![titanic-file.png](/getting_started/loading-data.png)
                       
The widget automatically transferred the loaded data to all the connected widgets. Check this by opening the Data
Table widget.

![titanic-data-table.png](/getting_started/data-table-titanic.png)

Our aim is to inspect survival probabilities for the passengers of Titanic by age, sex and status. Place Sieve
Diagram on the canvas and connect it to the File widget.

![titanic-nbc-workflow.png](/getting_started/titanic-workflow.png)

Double click on the Sieve Diagram widget to visualize actual survival probabilites against expected ones. Play with attribute
combinations to get the best visualization. Here's a hint: sex and status will give you the most interesting results.

![titanic-nomogram.png](/getting_started/titanic-workflow-sievediagram.png)
                      
The lowest survival probability is estimated for adult males traveling in the third class and the highest for females from
the first class. How about the crew? Who had the higest probability of survival? Hover over the diagram to see the information.
                        
You have now learned how to place widgets on the canvas, connect them to make workflows, read the data and visualize it. 
Consider exploring other widgets and their combinations, or load some data of
your own and see how Orange can help you in the analysis.
                       