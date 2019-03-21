+++
draft = false
type = "blog"
image = "/blog_img/2018-10-23/genova.jpg"
thumbImage = "/blog_img/2018-10-23/poster_NETTAB_A1-thumb.png"
date = "2019-03-20"
title = "Clustering Cells in Mouse Pancreas"
hardLineBreak = true 
categories = ["conference", "FAIR", "reproducibility"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Clustering Cells in Mouse Pancreas" 
longExcerpt = "Clustering Cells in Mouse Pancreas - reproducing a study" 
+++

Single cell data can be used to identify and separate individual cell types from bulk samples. 
In this blog we will look at pancreatic cells from two mouse strains (Baron <i>et al.</i>, 2017, GEO accession: 
<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84133">GSE84133</a>), 
cluster them according to their cell type and identify marker genes for each subpopulation of cells. 

{{% figure src="/blog_img/2019-03-20/Blog_1.1.png" width="95%" height="95%" %}}
\
\


Firstly we need to load, order and nominalise our data. To achieve this, we use Load Data widget followed by Gene Name Matcher and Create Class widget which enables us the use the cell types as characterised by Baron et al as a control of our clustering. We normalise the data using Single Cell Preprocess.

{{% figure src="/blog_img/2019-03-20/Blog_1.2.1.png" width="95%" height="95%" %}}
\
\

Once the data has been normalised, we utilize the Louvain Clustering widget to cluster our cells. We adjust the resolution so that the clustering produces 13 clusters since this is the number of cell types described in mouse pancreas in literature. 

{% figure src="/blog_img/2019-03-20/Blog_1.3.png" width="95%" height="95%" %}}
\
\

We check the accuracy of clustering with box plot and t-SNE where we use Groups that we crated with Create Class widget in the previous step to colour cells. 

{% figure src="/blog_img/2019-03-20/tSNE_misi.png" width="95%" height="95%" %}}
\
\

The only thing we still need to do now, is to identify the marker genes. There is no specific widget in scOrange to accomplish this task so we will use similar steps as were used in the article by Baron et al. to find 3 most significant markers for each cluster and create a heatmap with them. 

{% figure src="/blog_img/2019-03-20/Blog_1.4.png" width="95%" height="95%" %}}
\
\

The best way to approach this is to firstly run a Cluster Analysis widget and transfer gene score data produced by it into a new data table. Secondly, we transfer the data for one cluster into a new data table where we organise it by the descending statistic score in order to identify top 3 most significant genes in this cluster. 

{% figure src="/blog_img/2019-03-20/Blog_1.5.png" width="95%" height="95%" %}}
\
\
We use Select Columns widget to extract marker genes for heatmap. To do this we manually search for the genes in Available Variables and transfer our marker genes into the features section. 

{% figure src="/blog_img/2019-03-20/Blog_1.6.png" width="95%" height="95%" %}}
\
\

Finaly we use selected genes to create the heatmap.
{% figure src="/blog_img/2019-03-20/heatmap_misi.png" width="95%" height="95%" %}}
\
\

*References*

Wilkinson, Mark D., et al. "The FAIR Guiding Principles for scientific data management and stewardship." Scientific data 3 (2016).
