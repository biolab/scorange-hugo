+++
draft = false
type = "blog"
image = "/blog_img/2019-06-14/"
thumbImage = "/blog_img/2019-06-14/"
date = "2019-06-10"
title = "Projecting a New Set of Data onto t-SNE Without Reexecuting It"
hardLineBreak = true 
categories = ["Apply Domain", "tSNE", "projection", "chemotherapy"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "We project single cell data from an AML patient undergoing chemotherapy onto a t-SNE of a healthy individual to analyse cell population changes in the course of treatment." 
longExcerpt = "We analyse cell population changes in the course of chemotherapy by recreating a part of a study from Galen et al. (Cell, 2019) and projecting single cell data set from an AML patient undergoing treatment onto a t-SNE of a healthy individual." 
+++

<!-- dodaj cover slike, spremeni datum na 14-->
Batch effect can be a real nuisance when trying to project a new dataset onto an already existing t-SNE projection. With today’s blog we will show how to bypass it in scOrange by projecting single cell data set from an AML patient onto a t-SNE clustered according to cell type we have generated in our previous <a href= ”https://singlecell.biolab.si/blog/aml_identification/”> blog</a>. 
<br>

Once again we will be using the data gathered by <a href= “https://www.sciencedirect.com/science/article/pii/S0092867419300947”> Galen  <i> et al.</i> (Cell, 2019) </a> which is available in the GEO database under the accession number <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256”>GSE116256</a>. We need the data from a healthy person (<a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588000”>BM4</a>) and one AML patient (AML556) <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3587963"> before</a>, <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3587965">15 days after</a> and <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3587967"> 31 days after</a> undergoing chemotherapy. 
\
\
{{% figure src="/blog_img/2019-06-14/workflow_partial1.PNG" width="60%" height="60%" %}}
\
\
We have to load the data from the healthy individual and from the AML patient before the chemotherapy separately. Then run both datasets through the Genes widget, normalise it on counts per million and put it on a logarithmic scale in the Single Cell Preprocess widget. Now we make our primary t-SNE projection from the data of the healthy individual.
\
\
{{% figure src="/blog_img/2019-06-14/workflow_partial2.PNG" width="70%" height="70%" %}}
\
\
Next, we use the t-SNE projection of the cells from the healthy individual as a template for assessing the cells from the AML patient by using the Apply domain widget.
<!--ali obstaja kakšna bolj primerna beseda kot assess v tem primeru?-->
\
\
{{% figure src="/blog_img/2019-06-14/workflow.PNG" width="95%" height="95%" %}}
\
\
Before we display the data, we have to merge it using the Concatenate widget where we select the append data source ID so that we can display this selection in the Scatter Plot widget. t-SNE is our primary data input and Apply Domain our template data input. 
<br>

Because we don’t want to reexecute t-SNE and run into problems with the batch effect in doing so, we use the Scatter Plot widget to display the data and set t-SNE-x and t-SNE-x as variables for the x and y axis. 
\
\
{{% figure src="/blog_img/2019-06-14/Day0.png" width="95%" height="95%" %}}
\
\
This is our projection of the single cell data from the AML patient before the chemotherapy onto t-SNE of the cells from a healthy person. By using the dataset sampled 15<sup>th</sup> day after the patient has first undergone chemotherapy, we can explore how the therapy affects cell populations.   
\
\
{{% figure src="/blog_img/2019-06-14/Day15.png" width="95%" height="95%" %}}
\
\
Looking at the clustering pattern from our earlier <a href= ”https://singlecell.biolab.si/blog/aml_identification/”>blog</a>, we can conclude that the cells here are predominantly T and natural killer cells, which is consistent with clearance of the cells during the chemotherapy.
<br>

And how about a month after the chemotherapy?
\
\
{{% figure src="/blog_img/2019-06-14/Day31.png" width="95%" height="95%" %}}
\
\
The hematopoietic stem cells have repopulated and, as we can see from the distribution of the grey points on the t-SNE representing cells from the patient, formed different cell types. 
<br>
<!--dodaj zaključek-->
*References* 
\
Van Galen P, Hovestadt V, Wadsworth MH, <i>et al.</i> (2016). <a href=”https://www.sciencedirect.com/science/article/pii/S0092867419300947”>Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.</a> <i>Cell</i>, 176(6), 1265–1281.