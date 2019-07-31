+++
draft = false
type = "blog"
image = "/blog_img/2019-08-05/cover.png"
thumbImage = "/blog_img/2019-08-05/cover-small.png"
date = "2019-08-05"
title = "Automatic Cell Type Annotation"
hardLineBreak = true 
categories = ["Annotator", "Marker genes", "new widget", "tSNE"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Learn how to effortlessly group and identify cell types in your dataset with a new widget: the Annotator." 
longExcerpt = "Learn how to effortlessly group and identify cell types in your dataset with a new widget: the Annotator as demonstrated here on the data from human pancreas (Baron et al., Cell Syst 2016)." 
+++

<i><b>Note:</b> This blog deals with the same topic as our previous blog <a href=" https://singlecell.biolab.si/blog/pancreas/ "> Clustering Cells in Mouse Pancreas </a>, but uses a new widget the Annotator in doing so, therefore it is advisable to run through it first and get some background from it. </i>
<br>
<br>

We have some great news for you: do you still remember how many steps we took in (<a href="https://singlecell.biolab.si/blog/pancreas/">Clustering Cells in Mouse Pancreas blog</a>  to identify and group cell types? Well, the whole process just got much simpler with our new widget: the Annotator. 
<br>

Again, we will be looking at the single cell data from the pancreas (<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5228327/">Baron <i>et al.</i></a>, 2017, GEO accession: <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84133">GSE84133</a>), but this time we will be using the data from human donors. 
\
{{% figure src="/blog_img/2019-08-05/partialworkflow.png" %}}
\
You have two options here: download the data from the GEO database and import it into scOrange using the Load Data widget and annotate it with Genes widget or simply find it in Single Cell Datasets.
\
{{% figure src="/blog_img/2019-08-05/fullworkflow.png" %}}
Use the t-SNE widget for visualisation purposes and then drive all the data to the Annotator widget as reference data input. With the Marker Genes we can omit the trouble of finding the proper genes, just do not forget to select Human as your organism and fell free to select either of the databases currently available in the widget. 
\
{{% figure src="/blog_img/2019-08-05/annotator.png" %}}
\
In the Annotator widget select t-SNE-x and t-SNE-y as your axises, score cells based on marker expression and set Ɛ for DBSCAN to 3. 

<!--razloži Ɛ for DBSCAN -->
\
{{% figure src="/blog_img/2019-08-05/tSNE.png" %}}
\
See, it is that simple to annotate cell types. Now you are able to move towards analysing each cell type much faster. 


*References*

Baron M., Veres A., Wolock S.L., <i>et al.</i> <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5228327/">A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas Reveals Inter- and Intra-cell Population Structure. </a> Cell Syst. 2016;3(4):346–360.e4. 
