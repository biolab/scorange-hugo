+++
draft = false
type = "blog"
image = ""
thumbImage = ""
date = "2019-04-23" 
title = "Subsets of exhausted CD8+  T cells" 
hardLineBreak = true 
categories = ["clustering", "marker genes", "tSNE", "immunology", "CD8+"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Identify subsets of exhausted CD8 <sup>+</sup> T cells during chronic viral infections and corresponding groups in T cells isolated from tumours." 
longExcerpt = "Identify subsets of exhausted CD8 <sup>+</sup> T cells during chronic viral infections and corresponding groups in T cells isolated from tumours." 
+++

<!--v naslovi ne dela nadnapisano-->

Nobel prize in medicine 2018 was awarded for the discovery of cancer therapy by inhibition of negative immune regulation. Since then the attempts to improve the results of the checkpoint blockade immunotherapy have highlighted the importance of understanding the heterogeneity of the cells. Here we will show how scOrange can be used in this expanding field of research by will reproducing the a part of the study by <a href="https://www.nature.com/articles/s41590-019-0312-6"> Miller <i>et al.</i></a> published in Nature Immunology this March.  

Namely, we will be comparing single cell expression profiles of T cells isolated from tumours (<b>TIL</b>) and from T cells during chronic viral infection with lymphocytic choriomeningitis virus (<b>LCMV</b>), to see whether the states of dysfunctional CD8<sup>+</sup> TILs are comparable to those of T cell exhaustion in LCMVs. 

Naturally, we first need to download data which was deposited on GEO database by Miller <i>et al.</i> in two supersets: <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122675"> GSE122675 </a>  - TIL superset and <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122712"> GSE122712 </a> - LCMV superset.

Make sure you download files in MTX format, each superset into a separate folder, and rename files into <i>matrix.mtx</i>, <i>genes.tvs</i> and <i>barcodes.tvs</i>, since this is the format automatically recognised by the Load Data widget in scOrange. 
\
\
{{% figure src="/blog_img/2019-04-23/workflow1.png" width="85%" height="85%" %}}
\
\
So, now we have both datasets and before we start clustering them, we have to name genes and normalise the data using Gene Name Matcher and Single Cell Preprocess widgets.   
\
\
{{% figure src="/blog_img/2019-04-23/subset2.png" width="95%" height="95%" %}}
\
\
After that we start by clustering the LCMV superset and later using the marker genes, we identify here for stem-like and terminally exhausted CD8<sup>+</sup> T cells, to see if we can classify the same groups in TIL superset. 
\
\
{{% figure src="/blog_img/2019-04-23/workflow2.png" width="95%" height="95%" %}}
\
\
We drive the data through the Louvain Clustering widget, where we set the resolution to 2,3 and k neighbours to 100 to elicit 6 clusters.

In order to identify our clusters and their marker genes we run the Cluster Analysis widget using the Mann-Whitney method since our data is not normally distributed. We set set the gene count to 200 to determine a higher number of the significant genes. 
\
\
{{% figure src="/blog_img/2019-04-23/subset6_cluster.png" width="95%" height="95%" %}}
\
\
Data Table widget helps us in displaying marker genes for selected clusters and ordering them by their statistic score. 

Accordingly, C1 cluster is identified as terminaly exausted T cells (<i>cd7</i>, <i>Cd160</i>, <i>Rgs1</i>), C2 as effector cells (<i>cd7</i>, <i>Cd160</i>, <i>Rgs1</i>), C3 are progenitor exhausted T cells (<i>Tcf 7</i>, <i>xcl</i>) and C4 proliferating cells (<i>cdc6</i>, <i>bub1</i>). Given the size and the genes that define the remaining two clusters, we can assume they are representative of contaminating naive T cells. <!--malo še razširi-->

t-SNE projection is created by the t-SNE widget.  
\
\
{{% figure src="/blog_img/2019-04-23/tSNElcmv.png" width="95%" height="95%" %}}
\
\
We use the same workflow to attain t-SNE projection for the TIL subset. 
\
\
{{% figure src="/blog_img/2019-04-23/tSNEtic.png" width="95%" height="95%" %}}
\
\
To test if LCMVs and TILs elicit analogous subsets of exhausted T cells, we use the marker genes we identified for both subgroups to colour and size t-SNE projections. <!--dodaj še sliko za to?-->

The marker gene for terminally exhausted T-cell was identified as <i>cd7</i> by <a href="https://www.nature.com/articles/s41590-019-0312-6">Miller <i>et al.</i> </a> and us.
\
\
{{% figure src="/blog_img/2019-04-23/tSNEcd7.png" width="95%" height="95%" %}}
{{% figure src="/blog_img/2019-04-23/tSNE1cd7.png" width="95%" height="95%" %}}
\
\
Similarly, we both identified <i>tcf7</i> as the marker gene for progenitor exhausted T cells.
\
\
{{% figure src="/blog_img/2019-04-23/tSNETcf7.png" width="95%" height="95%" %}}
{{% figure src="/blog_img/2019-04-23/tSNE1Tcf7.png" width="95%" height="95%" %}}
\
\
As we can see, both of the genes predominantly colour different clusters in TIL and LCMV subsets.
<!--dodaj še naš gen in zaključek?-->
\
\
\

*References* 
\
Miller C.M., Sen D.R, Abosy R.A., <i>et al.</i> Subsets of Exhausted CD8+ T Cells Differentially Mediate Tumor Control and Respond to Checkpoint Blockade. <i>Nat Immunol.</i> 2019; 20:326–336. doi:<a href="https://www.nature.com/articles/s41590-019-0312-6">10.1038/s41590-019-0312-6 </a>