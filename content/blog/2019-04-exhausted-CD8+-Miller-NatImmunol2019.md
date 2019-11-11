+++
draft = false
type = "blog"
image = "/blog_img/2019-04-23/header-cd8.png"
thumbImage = "/blog_img/2019-04-23/header-cd8-small.png"
frontPageImage = "/blog_img/2019-04-23/header-cd8-small.png"
date = "2019-04-23" 
title = "Subsets of Exhausted CD8+ T Cells" 
hardLineBreak = true 
categories = ["clustering", "marker genes", "t-SNE", "immunology", "CD8+", "checkpoint blockade"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Identify subsets of exhausted CD8 <sup>+</sup> T cells during chronic viral infections and corresponding groups in T cells isolated from tumours." 
longExcerpt = "We reproduce a part of the study by Miller et al. (Nature Immunology, 2019) through identifying subsets of exhausted CD8+ T cells during chronic viral infections and corresponding groups in T cells isolated from tumours" 
+++


The Nobel prize in medicine 2018 was awarded for the discovery of cancer therapy by inhibition of negative immune regulation. Since then the attempts to improve the results of the checkpoint blockade immunotherapy have highlighted the importance of understanding the heterogeneity of the cells. Here we will show how scOrange can be used in this expanding field of research by reproducing a part of the study by <a href="https://www.nature.com/articles/s41590-019-0312-6"> Miller <i>et al.</i></a> published in Nature Immunology this March.  

Namely, we will be comparing single cell expression profiles of T cells isolated from tumours (<b>TIL</b>) and from T cells during chronic viral infection with lymphocytic choriomeningitis virus (<b>LCMV</b>), to see whether the states of dysfunctional CD8<sup>+</sup> TILs are comparable to those of T cell exhaustion in LCMVs. 

Naturally, we first need to download data which was deposited on the GEO database by Miller <i>et al.</i> in two supersets: <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122675"> GSE122675 </a>  - TIL superset and <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122712"> GSE122712 </a> - LCMV superset. Alternatively, you can avoiding having to download data from the GEO database by using the Single Cell Datasets widget to load the Tumor infiltrating CD8+ and the CD8+ in chronic viral infection datasets.

Make sure you download files in MTX format, each superset into a separate folder, and rename files into <i>matrix.mtx</i>, <i>genes.tvs</i> and <i>barcodes.tvs</i>, since this is the format automatically recognised by the Load Data widget in scOrange. 
\
{{% figure src="/blog_img/2019-04-23/workflow1.PNG" %}}
\
So, now we have both datasets and before we start clustering them, we have to name genes and normalise the data using Genes and Single Cell Preprocess widgets.   
\
{{% figure src="/blog_img/2019-04-23/subset2.PNG" %}}
\
After that we start by clustering the LCMV superset and later, using the marker genes, we identify here, for stem-like and terminally exhausted CD8<sup>+</sup> T cells, to see if we can classify the same groups in TIL superset. 
\
{{% figure src="/blog_img/2019-04-23/workflow2.PNG" %}}
\
We drive the data through the Louvain Clustering widget, where we set the resolution to 2,3 and k neighbours to 100 to elicit 6 clusters.

In order to identify our clusters and their marker genes we run the Cluster Analysis widget using the Mann-Whitney method since our data is not normally distributed. We set set the gene count to 200 to determine a higher number of the significant genes. 
\
{{% figure src="/blog_img/2019-04-23/subset6-cluster.PNG" %}}
\
Data Table widget helps us in displaying marker genes for selected clusters and ordering them by their statistic score. 

Accordingly, C1 cluster is identified as containing terminally exhausted  T cells (<i>Cd7</i>, <i>Cd160</i>, <i>Rgs1</i>), C2 as effector cells (<i>Cd7</i>, <i>Cd160</i>, <i>Rgs1</i>), C3 are progenitor exhausted T cells (<i>Tcf 7</i>, <i>Xcl</i>) and C4 proliferating cells (<i>Cdc6</i>, <i>Bub1</i>). Given the size and the genes that define the remaining two clusters, we can assume they are representative of contaminating naive T cells. 

t-SNE projection is created with the t-SNE widget.  
\
{{% figure src="/blog_img/2019-04-23/tSNElcmv.png" %}}
\
We use the same workflow to attain t-SNE projection for the TIL subset, but this time we set the resolution to 1,4 in Louvain Clustering widget to elicit 8 clusters.

\
{{% figure src="/blog_img/2019-04-23/workflow3.PNG" %}}
\
{{% figure src="/blog_img/2019-04-23/tSNEtil.png" %}}
\
To test if LCMVs and TILs elicit analogous subsets of exhausted T cells, we use the marker genes we identified for both subgroups in previous steps colour and size cells in t-SNE projections. 

One of the marker genes for terminally exhausted T-cell we have identified is <i>Cd7</i>. The same gene was singled out by <a href="https://www.nature.com/articles/s41590-019-0312-6">Miller <i>et al.</i> </a> as well. So, let's take a look at how it applies on TIL (left) and LCMV (right) datasets. In both projections the cells associated with the selected gene seem to be predominantly located in specific clusters. 
\
{{% figure src="/blog_img/2019-04-23/tSNEcd7.png" %}}
\
Similarly we both identified <i>Tcf7</i> as the marker gene for progenitor exhausted T cells and occurrence of it is in different clusters of T cells isolated from mousses chronically infected with LCMB than the occurrence of <i>Cd7</i>, but the arrangement of its significance in T cells isolated from tumours is not noticeably divergent.
\
{{% figure src="/blog_img/2019-04-23/tSNETcf7.png" %}}
\
Because of that we decided to seek out another marker gene for progenitor exhausted T cells which is predominantly significant in different clusters in TIL and LCMV subsets. One of the highest scoring genes for C3 cluster in LCMV superset is <i>Xcl1</i> and tSNE projections reveal much better distinguishment in TIL subset as <i>Tcf7</i>.
\
{{% figure src="/blog_img/2019-04-23/tSNExcl1.png" %}}
\
We have demonstrated that scOrange is applicable to the single cell data from studies in the field of immunotherapy. The marker genes singled out here could help identify and better target progenitor exhausted T cells to reinvigorate their response to tumour cells with anti-PD-1 therapy.
\

*References* 
\
Miller CM, Sen DR, Abosy RA <i>et al.</i> (2019) <a href="https://www.nature.com/articles/s41590-019-0312-6">Subsets of Exhausted CD8+ T Cells Differentially Mediate Tumor Control and Respond to Checkpoint Blockade.</a> <i>Nat Immunol.</i> 20:326–336.