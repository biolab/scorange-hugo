+++
title = "Discover New Marker Genes that Distinguish Cell Types"
image = "/images/Biomarkers.png"
learnMore = true
video = "lb-x36xqJ-E?start=6"
thumbnailImagePosition = "right"
weight = -20
excerpt = "Identify signature genes for each subpopulation using multiple methods. Use gene ontology enrichment to explore the biological meaning and identify cell types."
+++




Orange is all about data visualizations that help to uncover hidden data patterns, provide intuition behind data analysis procedures or support communication between data scientists and domain experts. Visualization widgets include scatter plot, box plot and histogram, and model-specific visualizations like dendrogram, silhouette plot, and tree visualizations, just to mention a few. Many other visualizations are available in add-ons and include visualizations of networks, word clouds, geographical maps, and more.

We take care to make Orange visualizations interactive: you can select data points from a scatter plot, a node in the tree, a branch in the dendrogram. Any such interaction will instruct visualization to send out a data subset that corresponds to the selected part of visualization. Consider the combination of a scatter plot and classification tree below. Scatter plot shows all the data, but highlights the data subset that corresponds to the selected node in the classification tree.


## Great Visualizations

Orange includes many standard visualizations. Scatter plot is great for visualizing correlations between pair of attributes, box plot for displaying basic statistics, heat map to provide an overview across entire data set, and projection plots like MDS for plotting the multinomial data in two dimensions.

{{% figure src="/images/tree-selection-scatterplot.png"  %}}


## Exploratory Data Analysis

Interactive visualizations enable exploratory data analysis. One can select interesting data subsets directly from plots, graphs and data tables and mine them in them downstream widgets. For example, select a cluster from the dendrogram of hierarchical clustering and map it to a 2D data presentation in the MDS plot. Or check their values of in the data table. Or observe the spread of its feature values in a box plot. Open all these windows at once and see how the changes in your selection affect other widgets. Or, for another example, cross-validate logistic regression on a data set and map some of the misclassifications to the two-dimensional projection. It is easy to turn Orange into a tool where domain experts can explore their data even if they lack insights in underlying statistics or machine learning.
