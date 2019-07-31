+++
draft = false
type = "blog"
image = "/blog_img/2019-03-20/cover.png"
thumbImage = "/blog_img/2019-03-20/cover.png"
frontPageImage = "/blog_img/2019-03-20/cover.png"
date = "2019-03-29"
title = "Clustering Cells in Mouse Pancreas"
hardLineBreak = true 
categories = ["clustering", "marker genes", "t-SNE", "heatmap"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Learn how to cluster cells and identify marker genes for clusters" 
longExcerpt = "To reproduce a part of a study by Baron et al. (Cell Systems, 2016), we cluster mouse pancreatic cells and identify marker genes for each type of the cells."
+++

Single cell data can be used to identify and separate individual cell types from bulk samples. 
In this blog we will look at pancreatic cells from two mouse strains (<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5228327/">Baron <i>et al.</i></a>, 2017, GEO accession: <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84133">GSE84133</a>), 
cluster them according to their cell type and identify marker genes for each subpopulation of cells. 

\
{{% figure src="/blog_img/2019-03-20/blog-1-1-1.png" %}}
\
{{% figure src="/blog_img/2019-03-20/blog-1-1-2.png" %}}
\

Firstly we need to load, order and nominalise our data. To achieve this, we use the Load Data widget followed by the Genes (don't forget to set organism to <i>Mus Musculus</i>) and the Create Class widget, which enables us the use the cell types as characterised by <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5228327/">Baron <i>et al.</i></a> as a control of our clustering. We normalise the data using the Single Cell Preprocess widget. Alternatively you can use Single Cell Datasets widget and load the Pancreas cells in mouse dataset with it.  

\
{{% figure src="/blog_img/2019-03-20/blog-1-2-1.png" %}}
\

Once the data has been normalised, we utilize the Louvain Clustering widget to cluster our cells. We adjust the resolution so that the clustering produces 13 clusters since this is the number of cell types described in mouse pancreas in literature. 

\
{{% figure src="/blog_img/2019-03-20/blog-1-3-1.png" %}}
\
{{% figure src="/blog_img/2019-03-20/blog-1-3-2.png" %}}
\

We check the accuracy of clustering with box plot and t-SNE where we use Groups that we crated with the Create Class widget in the previous step to colour cells. 
\
{{% figure src="/blog_img/2019-03-20/tSNE-mouse.png" %}}
\

The only thing we still need to do now, is to identify the marker genes. There is no specific widget in scOrange to accomplish this task, so we will use similar steps as were used in the article by <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5228327/">Baron <i>et al.</i></a> to find the three most significant markers for each cluster and create a heatmap with them. 
\
{{% figure src="/blog_img/2019-03-20/workflow-1-4.PNG" %}}
\

The best way to approach this is to firstly run a Cluster Analysis widget. We can see that Orange already recognises some of the gene clusters associated with different groups of cells. For example, T cell receptor complex genes correlate with T cells.
<br> 
<br> 
Secondly, we transfer the <b>gene score data</b> produced by the widget into a new data table. Then we transfer the data for one cluster into a new data table where we organise it by the descending statistic score in order to identify top three most significant genes in this cluster. 
<br> 
<br> 
After we have identified all the marker genes, we select and save them using the Save Data widget for additional processing, which will be further explored in the next blog. 
\
{{% figure src="/blog_img/2019-03-20/blog-1-5.png" %}}
\

We use Select Columns widget to extract marker genes for heatmap. To do this, we manually search for the genes in Available Variables and transfer our marker genes into the features section. 
\
{{% figure src="/blog_img/2019-03-20/blog-1-6.png" %}}
\

Finally, we use selected genes to create the heatmap. From it we can identify cell clusters by looking at the functions of the marker genes. Alpha cells are most strongly correlated with <i>GCG</i> encoding glucagon, beta cells with <i>INS1</i> and <i>INS2</i> encoding insulin, delta cells with <i>SST</i> encoding somatostatin, gamma cells with <i>PPY</i> encoding pancreatic polypeptide.
<br> <br> Using this principle we can cluster large bulks of cells to different cell type identities by identifying their marker genes and maping cell clusters according to functional roles of their marker genes.
\
{{% figure src="/blog_img/2019-03-20/heatmap-mouse.png" %}}
\

*References*

Baron M., Veres A., Wolock S.L., <i>et al.</i> A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas Reveals Inter- and Intra-cell Population Structure. <i>Cell Syst.</i> 2016;3(4):346–360.e4. doi:10.1016/j.cels.2016.08.011