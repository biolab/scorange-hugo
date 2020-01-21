+++
draft = false
type = "blog"
image = "/blog_img/2019-08-19/cover.png" 
thumbImage = "/blog_img/2019-08-19/cover-small.png"
frontPageImage = "/blog_img/2019-08-19/cover-small.png"
date = "2019-08-19" 
title = "Automatic Embedding of New Cells Onto an Existing Landscape" 
hardLineBreak = true 
categories = ["Annotator", "embedding", "new widget", "t-SNE"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Learn how to quickly embed new cells onto an existing tSNE projection using the new widget the Annotator" 
longExcerpt = "Learn how to quickly embed new cells onto an existing tSNE projection using the new widget the Annotator on the dataset of a healthy individual and AML patient undergoing chemotherapy gathered by Van Galen et al. (Cell, 2016)" 
+++

<i><b>Note:</b> This blog deals with the same topic as our blog <a href="https://singlecell.biolab.si/blog/2019-06-aml-projection-vangalen-cell2016/"> Embedding New Cells onto an Existing t-SNE Projection</a>, but uses a new widget the Annotator in doing so, therefore it is advisable to run through it first and get some background from it. </i>
<br>
<br>
<br>

In our <a href="https://singlecell.biolab.si/blog/2019-08-automatic-annotation-Baron-CellSyst2016/"> previous blog</a> we looked at the new Annotator widget and how it can be used to effortlessly group and identify cell types in your dataset. Here we will explore another feature of the same widget: the embedding of the new cells onto and existing tSNE projection.
<br>

We will be using the data gathered by <a href= "https://www.sciencedirect.com/science/article/pii/S0092867419300947"> Galen  <i> et al.</i> (Cell, 2019) </a> which is available in our datasets, so you do not have to be concerned with downloading and importing it.
<br>

Essentially, we will go through the same process as in blog <a href="https://singlecell.biolab.si/blog/2019-06-aml-projection-vangalen-cell2016/"> Embedding New Cells onto an Existing t-SNE Projection</a>, but thanks to the new widget it will take us considerably less effort and time. 
\
\
{{% figure src="/blog_img/2019-08-19/workflow-partial.PNG" %}}
\
Firstly, we need to load our datasets and pre-process them. We will be using the Healthy human bone marrow as our primary and the AML patient bone marrow day 0 as our secondary dataset. Find the mentioned datasets in two separate Single Cell Datasets widgets, annotate the genes with the Genes widget, filter them and use the Single Cell Preprocess widget to normalise the samples on counts per million and put them on a logarithmic scale. Make a t-SNE projection from the Healthy human bone marrow dataset. 
\
\
{{% figure src="/blog_img/2019-08-19/workflow-full.PNG" %}}
\
Use the t-SNE as reference data input to the Annotator widget and AML patient dataset as the secondary data input.
\
{{% figure src="/blog_img/2019-08-19/tSNE.png" %}}
\
Since this projection would be much easier to analyse if it also displayed cell types, we add the Marker Genes widget to our workflow to annotate the cell groups. 
\
{{% figure src="/blog_img/2019-08-19/tSNEd0.png" %}}
\
Now this is much easier to interpret. The sample from the AML patient seems to contain most of the cell types present in a healthy donor.
<br>

There are two more datasets significant for this case in our database that we can explore. One of the AML patient right after undergoing therapy and other of the same patient recovering from the treatment. Let us take a look at how they match up to the healthy sample by simply changing our datasets in the Single Cell Datasets widget that leads up to the Annotator widget as secondary data input.
<br>

The effect of chemotherapy in the sample AML patient bone marrow day 15 is well noticeable. Cell clearance has taken place and the cells here are predominantly T cells. 
\
{{% figure src="/blog_img/2019-08-19/tSNEd15.png" %}}
\
Sample taken on the 31<sup>st</sup> day shows that the patient has recovered and the hematopoietic stem cells have repopulated.
\
{{% figure src="/blog_img/2019-08-19/tSNEd31.png" %}}
\
As we can see, comparing to the effort in our blog <a href="https://singlecell.biolab.si/blog/2019-06-aml-projection-vangalen-cell2016/"> Embedding New Cells onto an Existing t-SNE Projection</a>, the Annotator widget really does simplify the embedding of the new cells onto and an existing tSNE projection.
<br>
<br>


<i>References:</i>

Van Galen P, Hovestadt V, Wadsworth MH, <i>et al.</i> (2016). <a href="https://www.sciencedirect.com/science/article/pii/S0092867419300947">Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.</a> <i>Cell</i>, 176(6), 1265–1281.
