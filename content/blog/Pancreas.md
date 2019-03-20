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
shortExcerpt = "scOrange's away trip to Genova." 
longExcerpt = "scOrange's away trip to Genova." 
+++

Single cell data can be used to identify and separate individual cell types from bulk samples. 
In this blog we will look at pancreatic cells from two mouse strains (Baron et al., 2017, GEO accession: 
<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84133">GSE84133</a>), 
cluster them according to their cell type and identify marker genes for each subpopulation of cells. 

{{% figure src="/blog_img/2019-03-20/Blog_1.1.png" width="95%" height="95%" %}}
\
\


Firstly we need to load, order and nominalise our data. To achieve this, we use Load Data widget followed by Gene Name Matcher and Create Class widget
 which enables us the use the cell types as characterised by Baron et al as a control of our clustering. We normalise the data using Single Cell Preprocess.

{{% figure src="/blog_img/2019-03-20/Blog_1.2.1.png" width="95%" height="95%" %}}
\
\



*References*

Wilkinson, Mark D., et al. "The FAIR Guiding Principles for scientific data management and stewardship." Scientific data 3 (2016).
