+++
draft = false
type = "blog"
image = "/blog_img/2019-07-28/coverphoto.png"
thumbImage = "/blog_img/2019-07-28/coverphoto-small.png"
frontPageImage = "/blog_img/2019-07-28/coverphoto-small.png"
date = "2019-07-28"
title = "Profiling Human Osteoarthritis Cartilage Chondrocytes"
hardLineBreak = true 
categories = ["PCA", "osteoarthritis", "scatter plot", "GO Browser"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Identify the genes affiliated with osteoarthritis progression in the cartilage data gathered by Ji Q et al. (Annals of the Rheumatic Diseases, 2019)" 
longExcerpt = "Identify the genes affiliated with osteoarthritis progression in the cartilage data gathered by Ji Q et al. (Annals of the Rheumatic Diseases, 2019) to shed a light on predicting clinical outcomes of the patients" 
+++

Osteoarthritis is one of the most costly and common chronic conditions. A better understanding of genetical background and expression changes during osteoarthritis progression could help with diagnosis and predictions of treatment outcomes, therefore, in his short blog, we will take a look at the genes affiliated with osteoarthritis progression.
\
{{% figure src="/blog_img/2019-07-28/workflow-partial1.PNG" %}}
\
Processing of the data downloaded from the GEO database (accession number: <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE104782">GSE104782</a>) will be a bit longer than usual this time.  We start by eliminating the batch effect, since we don't want the differences between the 32 individuals sampled in this study to interfere with our analysis of gene expression. After that we use Genes widget to match gene names in the data to their IDs and Create Class widget to mark cells based on the stage of osteoarthritis as microscopically diagnosed by Ji <i>et al.</i> (S0 = normal articular cartilage, S4=exposed subchondral bone). 
\
{{% figure src="/blog_img/2019-07-28/createclass.PNG" %}}
\
Continuing with Single Cell Preprocess widget, we select 500 most variable genes, logarithmize and normalise the data. In the PCA widget we select 4 components, that together cover 37% of the variance. 
\
{{% figure src="/blog_img/2019-07-28/workflow-partial2.PNG" %}}
\
Scatter Plot widget helps us identify the PC4 as the principal component with the strongest disease-stage progression. 
\
{{% figure src="/blog_img/2019-07-28/PCAplot.png" %}}
\
This means we can now use PC4 scoring to determine genes associated with osteoarthritis progression. Export components from PCA widget to Data Table widget. If you open the table, you will notice that genes are displayed in rows and principal components in columns. If we want to order genes by ascending or descending PC4 score, we need principal components in rows. We can simply achieve this by using the Transpose widget. Now we can order genes by PC4 scores by clicking the PC4 column.  
\
{{% figure src="/blog_img/2019-07-28/workflow-partial3.PNG" %}}
\
We can now take a look at genes with negative correlation for PC4 (<i>PTGES</i>, <i>NPR3</i>, <i>ANGPTL1</i>, <i>POSTN</i>) and those with positive correlation (<i>IL1B</i>, <i>CHRDL2</i>, <i>CCl3</i>, <i>CXCL3</i>) and determine their biological role using GO Browser widget.

Since PCA widget overruns the gene annotations in our data, we have to run it trough Genes widget again, than display it with the Scatter Plot widget, manual select positively or negatively corelated genes on the plot and use it as an input for the GO Browser. 
\
{{% figure src="/blog_img/2019-07-28/workflow-full.PNG" %}}
\
Genes with positive correlation for PC4, as displayed on the image bellow, are mainly involved in skeletal system development (ossification) and cellular responses to stress (defense response, innate immune response) suggesting the early changes that occur during osteoarthritis pathogenesis and those with negative correlation for PC4 are mainly involved in extracellular matrix organisation (tissue development, animal organ morphogenesis) and collagen metabolism (skeletal system development, odontogenesis). This makes sense since metabolic pathways switch towards glycolysis during osteoarthritis progression and in doing so contribute to impaired extracellular matrix synthesis and anabolic processes. 
\
{{% figure src="/blog_img/2019-07-28/positivepathways.png" %}}
\
Now you see, just how quick and easy identifying, annotating and explaining the genes affiliated with a certain trait (osteoarthritis progression) is in scOrange.

*References* 
\

Ji Q, Zheng Y, Zhang G, <i>et al.</i> (2019) <a href= "https://ard.bmj.com/content/78/1/100.long"> Single-cell RNA-seq Analysis Reveals the Progression of Human Osteoarthritis.</a> <i> Annals of the Rheumatic Diseases</i>, 78(1), 100–110. 