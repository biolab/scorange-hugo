+++
draft = false
type = "blog"
image = ""
thumbImage = ""
date = "2019-04-23"
title = "Subsets of exhausted CD8<sup>+</sup>  T cells"
hardLineBreak = true 
categories = ["clustering", "marker genes", "tSNE", "heatmap"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Learn how to cluster cells and identify marker genes for clusters" 
longExcerpt = "Identifying subsets of exhausted CD8 <sup>+</sup> T cells during chronic viral infections and corresponding groups in T cells isolated from tumours." 
+++

Today we will reproduce first part of the study by <a href="https://www.nature.com/articles/s41590-019-0312-6"> Miller <i>et al.</i></a> published in Nature Immunology this March.  
\
\
<br>
Naturally, we first need to download data which was deposited on GEO data base in two supersets: GSE122675 <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122675”> and GSE122712 <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122712”>.
Make sure you download files in MTX format, each superset into a separate folder, and rename files into <i>matrix.mtx</i>, <i>genes.tvs</i> and <i>barcodes.tvs</i>, since this is the format automatically recognised by the Load Data widget in scOrange. 
\
\
{{% figure src="/blog_img/2019-04-22/workflow1.png" width="85%" height="85%" %}}
\
\

So, now we have two datasets. One is a single cell expression profile of T cells isolated from tumours (<b>TIL</b>), the other is a profile of T cells during chronic viral infection with LCMV (<b>LCMV</b>) and before we start clustering them, we have to name genes and normalise the data using Gene Name Matcher and Single Cell Preprocess widgets.  
<br>
\
\
{{% figure src="/blog_img/2019-03-20/subset2.png" width="95%" height="95%" %}}
\
\
We will start by clustering the LCMV superset and later use the markers for stem-like and terminally exhausted CD8<Sup>+</Sup> T cells, we identify here, to see if we can classify the same groups in TIL superset. 

 
\
\

\
\

*References* <!--dopiši pravi vir 

Baron M., Veres A., Wolock S.L., <i>et al.</i> A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas Reveals Inter- and Intra-cell Population Structure. <i>Cell Syst.</i> 2016;3(4):346–360.e4. doi:10.1016/j.cels.2016.08.011--> 