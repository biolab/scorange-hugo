+++
draft = false
type = "blog"
image = "/blog_img/2019-03-20/cover.png"
thumbImage = "/blog_img/2019-03-20/cover.png"
date = "2019-03-20"
title = "Clustering Cells in Mouse Pancreas"
hardLineBreak = true 
categories = ["clustering", "marker genes", "tSNE", "heatmap"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Learn how to cluster cells and identify marker genes for clusters" 
longExcerpt = "Clustering Cells in Mouse Pancreas - reproducing a study" 
+++

Single cell data can be used to identify and separate individual cell types from bulk samples. 
In this blog we will look at pancreatic cells from two mouse strains (Baron <i>et al.</i>, 2017, GEO accession: 
<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84133">GSE84133</a>), 
cluster them according to their cell type and identify marker genes for each subpopulation of cells. 

{{% figure src="/blog_img/2019-03-20/Blog_1.1.png" width="95%" height="95%" %}}
\
\


Firstly we need to load, order and nominalise our data. To achieve this, we use Load Data widget followed by Gene Name Matcher and Create Class widget which enables us the use the cell types as characterised by <i>Baron et al.</i> as a control of our clustering. We normalise the data using Single Cell Preprocess.

{{% figure src="/blog_img/2019-03-20/Blog_1.2.1.png" width="95%" height="95%" %}}
\
\

Once the data has been normalised, we utilize the Louvain Clustering widget to cluster our cells. We adjust the resolution so that the clustering produces 13 clusters since this is the number of cell types described in mouse pancreas in literature. 

{{% figure src="/blog_img/2019-03-20/Blog_1.3.png" width="95%" height="95%" %}}
\
\

We check the accuracy of clustering with box plot and t-SNE where we use Groups that we crated with Create Class widget in the previous step to colour cells. 

{{% figure src="/blog_img/2019-03-20/tSNE_misi.png" width="95%" height="95%" %}}
\
\

The only thing we still need to do now, is to identify the marker genes. There is no specific widget in scOrange to accomplish this task so we will use similar steps as were used in the article by Baron et al. to find 3 most significant markers for each cluster and create a heatmap with them. 

{{% figure src="/blog_img/2019-03-20/Workflow_1.4.PNG" width="95%" height="95%" %}}
\
\

The best way to approach this is to firstly run a Cluster Analysis widget. We can see that Orange already recognises some of the gene clusters associated with different groups of cells. For example, T cell receptor complex genes correlate with T cells.
<br>Secondly, we transfer <b>gene score data</b> produced by the widget into a new data table. Then we transfer the data for one cluster into a new data table where we organise it by the descending statistic score in order to identify top 3 most significant genes in this cluster. 

{{% figure src="/blog_img/2019-03-20/Blog_1.5.png" width="95%" height="95%" %}}
\
\

We use Select Columns widget to extract marker genes for heatmap. To do this we manually search for the genes in Available Variables and transfer our marker genes into the features section. 

{{% figure src="/blog_img/2019-03-20/Blog_1.6.png" width="95%" height="95%" %}}
\
\

Finally, we use selected genes to create the heatmap. From it we can identify cell clusters by looking at the functions of the marker genes.  From it we can indentfy cell clussters by looking at the functions of the marker genes. Alpha cells are most strongly correlated with <i>GCG</i> encoding glucagon, beta cells with <i>INS1</i> and <i>INS2</i> encoding insulin, delta cells with <i>SST</i> encoding somatostatin, gamma cells with <i>PPY</i> encoding pancreatic polypeptide.
<br> Using this principle we can cluster large bulks of cells to different cell type identities by identifying their marker genes and maping cell clusters according to functional roles of their marker genes.

{{% figure src="/blog_img/2019-03-20/heatmap_misi.png" width="95%" height="95%" %}}
\
\

*References*

Baron, Maayan <i>et al.</i> “A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas Reveals Inter- and Intra-cell Population Structure” Cell systems vol. 3,4 (2016): 346-360.e4. 
