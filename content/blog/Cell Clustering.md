+++
draft = false
type = "blog"
image = "/blog_img/2018-10-04/cell-clustering.png"
thumbImage = "/blog_img/2018-10-04/cell-clustering.thumb.png"
date = "2018-10-03"
title = "Cell Clustering"
weight = 2
hardLineBreak = true 
categories = ["clustering", "data mining", "genomics"]
joinLines = false
author = "Ajda Pretnar"
shortExcerpt = "Use Louvain clustering to find cell grousp and visualize cell landscape in a t-SNE projection."
longExcerpt = "Use Louvain clustering to find cell grousp and visualize cell landscape in a t-SNE projection."
+++

Louvain Clustering is a nice clustering method that detects communities in a network of nearest neighbours. We will use this on an example of *Bone marrow mononuclear cells with AML* data, that we have retrived with the Single Cell Datasets widget. First, let us observe the data in a Data Table.
\
\

{{% figure src="/blog_img/2018-10-03/AML-datatable.png" %}}
\
\

Now, let us pass the data through Louvain Clustering. We used the default 25 principal components and euclidean distance to determine communities. Louvain Clustering will append an additional column with information of community of each cell.
\
\

{{% figure src="/blog_img/2018-10-04/Louvain-clustering.png" width="40%" height="40%" %}}
\
\

We can observe the results of clustering in a cell landscape, that we plot with the t-SNE widget. Cells get nicely clustered with t-SNE and the clusters also correspond with the Louvain clustering. Great!
\
\

{{% figure src="/blog_img/2018-10-04/t-SNE-selection.png" %}}
\
\

Finally, we can observe the distribution of cell types in a Box Plot. Let us select a group of cells from the t-SNE plot and send it to Box Plot. The group we have selected contains mostly healty cells. This means health cells have a distinct expression profile.
\
\

{{% figure src="/blog_img/2018-10-04/box-plot.png" %}}
\
\
{{% figure src="/blog_img/2018-10-04/final-workflow2.png" caption="The final workflow." width="60%" height="60%" %}}
\
\
