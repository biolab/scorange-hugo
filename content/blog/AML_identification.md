+++
draft = false
type = "blog"
image = "/blog_img/2019-06-06/coverphoto.png"
thumbImage = "/blog_img/2019-06-06/coverphoto_small.png"
date = "2019-06-06"
title = "Identification of Cell Populations in Healthy Bone Marrow"
hardLineBreak = true 
categories = ["marker genes", "tSNE", "box plot", "cell populations", "clustering"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Identify cell populations in healthy human bone marrow and take a look at the putative cell differentiation trajectories." 
longExcerpt = "We identify cell populations in a dataset of healthy human bone marrow cells from Galen et al. (Cell, 2019) and take a look at the putative cell differentiation trajectories." 
+++

In order to study diseases such as leukaemia on cell populations level, we first need to characterise a healthy bone marrow cell population. So in this blog we set out to do just that. 

The data from<a href="https://www.sciencedirect.com/science/article/pii/S0092867419300947"> Galen  <i> et al.</i>(Cell, 2019)</a> in available in the GEO database under the accession number <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256">GSE116256</a>. We will be using the data from only one healthy patient <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588000”> BM4 </a> and its <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588001"> annotation file </a> since this is by far the biggest nonenriched sample from a healthy individual in this dataset. 
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial1.PNG" width="40%" height="40%" %}}
\
\
After loading the data and matching the genes in the dataset to those in databases, we filter out all the genes that appear in less than 10 cells. Besides the usual normalisation, we select 5000 most variable genes. 
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial2.PNG" width="65%" height="65%" %}}
\
\
Since the relationships between the cell clusters is important for this analysis, we use Hierarhical Clustering and not Louvian Clustering widget to cluster the data. Firstly, we calculate the distances between the cells and then visually determine the number of clusters by dragging the vertical line over the graph.
\
\
{{% figure src="/blog_img/2019-06-06/clustering.png" width="95%" height="95%" %}}
\
\
We can tackle the identification of the clusters using two different approaches. The first is by identifying the most significant genes in each cluster as described in one of our previous <a href="https://singlecell.biolab.si/blog/pancreas/"> blogs</a> and assuming cell types according to marker genes’ functions, the other is using the <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588001"> annotation file </a> provided by <a href="https://www.sciencedirect.com/science/article/pii/S0092867419300947"> Galen  <i> et al.</i></a>.
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial3.PNG" width="85%" height="85%" %}}
\
\
But before we take a closer look at either of the alternatives, let us take a look at the distribution of the clusters using the Box Plot widget. 
\
\
{{% figure src="/blog_img/2019-06-06/boxplot.png" width="95%" height="95%" %}}
\
\
C2 is the biggest cluster. This information might come in handy when we try to identify them.
<br>

What we have also already done in this workflow, is identified markers for each cluster with the help of Data Tables (explained in detail in <a href="https://singlecell.biolab.si/blog/pancreas/"> this blog</a>). With these markers we can classify clusters. For example, <i>CD3D</i> is the most significant gene in cluster 4. It encodes T-cell surface glycoprotein CD3. Similarly <i>MS4A1</i> in the cluster 3 encodes B-lymphocyte antigen CD20.
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial4.PNG" width="95%" height="95%" %}}
\
\
In case we run into problems identifying genes with this approach, we can always use the Score Cells widget to classify cells using known gene markers. Select the genes for the desired cell type, which are conveniently available in Marker Genes widget, and then order them by score in a new Data Table widget. As we can see in this case, most of the highly scored cells for natural killer cell markers show up in C1. 
\
\
{{% figure src="/blog_img/2019-06-06/NKcells.png" width="95%" height="95%" %}}
\
\
Now that we have matched clusters with cell types, we can use Edit Domain widget to change annotations of the clusters. 
\
\
{{% figure src="/blog_img/2019-06-06/editdomain.PNG" width="80%" height="80%" %}}
\
\
Additionally, we can merge the annotation file provided by Galen  <i> et al.</i></a> with our data and display both cell classifications on t-SNE projection simultaneously. 
\
\
{{% figure src="/blog_img/2019-06-06/workflow_final.PNG" width="95%" height="95%" %}}
\
\
To make the annotation file readable to Orange, we need to rename it from <i>GSM3588001_BM4.anno.txt.gz</i> to <i>GSM3588001_BM4.anno.<b>tab</b>.gz</i>. After that we can load it and merge it with our data using Merge Data widget.
\
\
{{% figure src="/blog_img/2019-06-06/mergedata.PNG" width="75%" height="75%" %}}
\
\
Have you noticed that we did not use Cluster Analysis widget as our output for the data we are about to display using t-SNE? That is because it reduces the data and therefore negatively influences our t-SNE visualisation. 
<br>

Lets check how our clustering and cell identification compares to that of Galen  <i> et al.</i>.
\
\
{{% figure src="/blog_img/2019-06-06/tSNE.png" width="95%" height="95%" %}}
\
\
Apart from some mismatches along the putative cell differentiation trajectories (for example with Progenitor Monocytes and Monocytes), cell types overlap. 
<br>    

Thus we have achieved what we undertook; characterised human bone marrow cell population and displayed cell differentiation trajectories on t-SNE projection.

*References* 
\
Petropoulos, S., Edsgärd, D., Reinius <i>et al.</i> (2016). <a href="https://www.cell.com/fulltext/S0092-8674(16)30280-X">Single-Cell RNA-Seq Reveals Lineage and X Chromosome Dynamics in Human Preimplantation Embryos.</a> <i>Cell</i>, 165(4), 1012–1026.
<!-- popravi-->