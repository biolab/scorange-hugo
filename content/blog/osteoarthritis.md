+++
draft = false
type = "blog"
image = "/blog_img/2019-06-28/"
thumbImage = "/blog_img/2019-06-28/"
date = "2019-06-21"
title = "Profiling Human Osteoarthritis Cartilage Chondrocytes"
hardLineBreak = true 
categories = ["PCA", "osteoarthritis", "scatter plot"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "" 
longExcerpt = "" 
+++

<!-- dodaj cover slike, kratek in dolg povzetek, uvod, popravi slike in datum-->

\
\
{{% figure src="/blog_img/2019-06-28/workflow_partial1.PNG" width="60%" height="60%" %}}
\
\
Processing of the data downloaded from the GEO database (accession number: <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE104782”>GSE104782</a>) will be a bit longer than usual this time.  We start by eliminating the batch effect, since we don't want the differences between the 32 individuals sampled in this study to interfere with our analysis of gene expression. After that we use Genes widget to match gene names in the data to their IDs and Create Class widget to mark cells based on the stage of osteoarthritis as microscopically diagnosed by Ji <i>et al.</i> (S0 = normal articular cartilage, S4=exposed subchondral bone). 
\
\
{{% figure src="/blog_img/2019-06-28/createclass.PNG" width="60%" height="60%" %}}
\
\
Continuing with Single Cell Preprocess widget, we select 500 most variable genes, logarithmize and normalise the data. In the PCA widget we select 4 components, that together cover 37% of the variance. 
\
\
{{% figure src="/blog_img/2019-06-28/workflow_partial2.PNG" width="70%" height="70%" %}}
\
\
Scatter Plot widget helps us identify the PC4 as the principal component with the strongest disease-stage progression. 
\
\
{{% figure src="/blog_img/2019-06-28/PCAplot.png" width="95%" height="95%" %}}
\
\
This means we can now use PC4 scoring to determine genes associated with osteoarthritis progression. Export components from PCA widget to Data Table widget. If you open the table, you will notice that genes are displayed in rows and principal components in columns. If we want to order genes by ascending or descending PC4 score, we need principal components in rows. We can simply achieve this by using the Transpose widget. Now we can order genes by PC4 scores by clicking the PC4 column.  
\
\
{{% figure src="/blog_img/2019-06-28/workflow_partial3.PNG" width="85%" height="85%" %}}
\
\
We notice that  genes with negative correlation for PC4 are mainly involved in extracellular matrix organisation and collagen metabolism (<i>PTGES</i>, <i>NPR3</i>, <i>ANGPTL1</i>, <i>POSTN</i>) and those with positive correlation (<i>IL1B</i>, <i>CHRDL2</i>, <i>CCl3</i>, <i>CXCL3</i>) in skeletal system development and cellular responses to stress.
\
\
{{% figure src="/blog_img/2019-06-28/workflow_full.PNG" width="95%" height="95%" %}}
\
\

\
\
{{% figure src="/blog_img/2019-06-28/PCgenes.png" width="95%" height="95%" %}}
\
\


<!--dokončaj besedilo, dodaj zaključek-->

*References* 
\

Ji Q, Zheng Y, Zhang G, <i>et al.</i> (2019) <a href= “https://ard.bmj.com/content/78/1/100.long”> Single-cell RNA-seq Analysis Reveals the Progression of Human Osteoarthritis.</a> <i> Annals of the Rheumatic Diseases</i>, 78(1), 100–110. 