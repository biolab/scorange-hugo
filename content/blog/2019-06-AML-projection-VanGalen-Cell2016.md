+++
draft = false
type = "blog"
image = "/blog_img/2019-06-14/cover.png"
thumbImage = "/blog_img/2019-06-14/cover-small.png"
date = "2019-06-14"
title = "Embedding New Cells onto an Existing t-SNE Projection"
hardLineBreak = true 
categories = ["Apply Domain", "tSNE", "embedding", "chemotherapy"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "We project single cell data from an AML patient undergoing chemotherapy onto a t-SNE of a healthy individual to analyse cell population changes in the course of treatment." 
longExcerpt = "We analyse cell population changes in the course of chemotherapy by recreating a part of a study from Galen et al. (Cell, 2019) and projecting single cell data set from an AML patient undergoing treatment onto a t-SNE of a healthy individual." 
+++

<i><b>Note:</b> This blog is in many ways a continuation of our previous blog <a href=" https://singlecell.biolab.si/blog/aml_identification/ "> Identification of Cell Populations in Healthy Bone Marrow </a>, therefore it is advisable to read it before tackling this one.</i>
<br>
<br>

Batch effects can be a real nuisance when producing t-SNE plots of multiple data sets. In today’s blog we will show how to bypass them in scOrange by projecting single cell data set from an AML patient onto a t-SNE of healthy individual's bone marrow cells clustered according to cell type we have generated in our previous <a href= ”https://singlecell.biolab.si/blog/aml_identification/”> blog</a>. 
<br>

We will be using the same data as in our <a href=" https://singlecell.biolab.si/blog/aml_identification/ ">previous blog</a> gathered by <a href= “https://www.sciencedirect.com/science/article/pii/S0092867419300947”> Galen  <i> et al.</i> (Cell, 2019) </a> which is available in the GEO database under the accession number <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256”>GSE116256</a>. More accurately, we will be using the data as we annotated it after clustering in the last blog. We need the annotated data from the healthy subject (<a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588000”>BM4</a>) and one AML patient (AML556) <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3587963"> before</a>, <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3587965">15 days after</a> and <a href= "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3587967"> 31 days after</a> undergoing chemotherapy. If you want to skip recreating the whole workflow from our previous blog, just use the Merge Data widget to merge the data from the healthy person with its <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588001“>annotation file</a>. If you followed the previous workflow, use the Save data widget after the Merge Data widget to export the annotated data.  
\
{{% figure src="/blog_img/2019-06-14/workflow-partial1.png" %}}
\
We have to load the data from the healthy individual and from the AML patient before the chemotherapy separately. Then run both datasets through the Genes widget, normalise it on counts per million and put it on a logarithmic scale in the Single Cell Preprocess widget. Now we make our primary t-SNE projection from the data of the healthy individual.
\
{{% figure src="/blog_img/2019-06-14/tSNE.png" %}}
\
Next, we use the t-SNE projection of the cells from the healthy individual as a template for assessing the cells from the AML patient by using the Apply domain widget.
\
{{% figure src="/blog_img/2019-06-14/workflow-partial2.png" %}}
\
Before we display the data, we have to merge it using the Concatenate widget where we select the append data source ID so that we can display this selection in the Scatter Plot widget. t-SNE is our primary data input and Apply Domain our template data input. 
\
{{% figure src="/blog_img/2019-06-14/workflow.png" %}}
\
Because we don’t want to reexecute t-SNE and run into problems with the batch effect in doing so, we use the Scatter Plot widget to display the data and set t-SNE-x and t-SNE-x as variables for the x and y axis. 
\
{{% figure src="/blog_img/2019-06-14/Day0.png" %}}
\
This is our projection of the single cell data from the AML patient before the chemotherapy onto t-SNE of the cells from a healthy person. The projected cells are displayed as grey crosses. By using the dataset sampled on 15<sup>th</sup> day after the patient has first undergone chemotherapy, we can explore how the therapy affects cell populations.   
\
{{% figure src="/blog_img/2019-06-14/Day15.png" %}}
\
Looking at the clustering pattern from our earlier <a href= ”https://singlecell.biolab.si/blog/aml_identification/”>blog</a>, we can conclude that the cells here are predominantly T and natural killer cells, which is consistent with clearance of the cells during the chemotherapy.
<br>

And how about a month after the chemotherapy?
\
{{% figure src="/blog_img/2019-06-14/Day31.png"  %}}
\
The hematopoietic stem cells have repopulated and, as we can see from the distribution of the grey points on the t-SNE representing cells from the patient, formed different cell types. 
<br>

In short, we have shown how to infer cell types with the help of t-SNE and a pre-existing reference data set with known cell types.
<br>
<br>

*References* 
\
Van Galen P, Hovestadt V, Wadsworth MH, <i>et al.</i> (2016). <a href=”https://www.sciencedirect.com/science/article/pii/S0092867419300947”>Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.</a> <i>Cell</i>, 176(6), 1265–1281.