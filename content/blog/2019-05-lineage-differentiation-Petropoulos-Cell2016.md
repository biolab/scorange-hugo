+++
draft = false
type = "blog"
image = "/blog_img/2019-05-10/linage-cover.png"
thumbImage = "/blog_img/2019-05-10/linage-cover-small.png"
frontPageImage = "/blog_img/2019-04-23/header-cd8-small.png"
date = "2019-05-10"
title = "Pinpointing Lineage Differentiation in Human Preimplantation Embryotic Cells"
hardLineBreak = true 
categories = ["PCA", "tSNE", "differentiation", "embryo", "lineage", "clustering", "scatter plot"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Combine clustering and time component to pinpoint the time of trophectoderm (TE) and inner cell mass (ICM) differentiation in human preimplantation embryotic cells" 
longExcerpt = "Combine clustering and time component to pinpoint the time of trophectoderm (TE) and inner cell mass (ICM) differentiation in human preimplantation embryotic cells and recreate a part of study by Petropoulos et al. (Cell, 2016)" 
+++
Embryonic development has been well studied in mouse models but our knowledge of this process in the human embryo is rudimentary. Here we will take a closer look at the trophectoderm and the inner cell mass maturation during the first 7 days of human development to help with the assessment of the degree of conservation between the mouse and human blastocyst formation.

We will be using the same single cell data from human preimplantation embryos as in the previous <a href="https://singlecell.biolab.si/blog/2019-07-xy-emryos-petropoulos-cell2017/">blog</a>. The data was published by <a href="https://www.cell.com/fulltext/S0092-8674(16)30280-X">Petropoulos <i> et al. </i> </a>and is deposited in ArrayExpress database under the accession number <a href="https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-3929/">E-MTAB-3929</a>. 
<br>

Naturally, we have to start by loading the data into Orange and pre-processing it using the familiar workflow with the following widgets: Load Data, Genes, Create Class to sort the cells by sampling day and of course Single Cell Preprocess to normalise the data and select the 500 most variable genes. Alternatively, you can load the human preimplantation embryos dataset using Single Cell Datasets widget.  
\
{{% figure src="/blog_img/2019-05-10/workfow-linage-1.png" %}}
\
To show that the cells' expression changes with time, we cluster the cells using the Louvain Clustering widget with resolution set to 1.7 and k-neighbours to 100. t-SNE distinctly depicts 7 clusters. E4 and E5 samples are slightly divided, which complies with the fact that Petropoulos <i>et al.</i> sampled those cells at two occasions 4-6 hours apart.
\
{{% figure src="/blog_img/2019-05-10/tSNE2.png" %}}
\
Another way to confirm that time plays a crucial role in the cell segregation is by using the Principal Component Analysis (PCA) widget. 
\
{{% figure src="/blog_img/2019-05-10/workfow-linage-2.PNG" %}}
\
Scatter Plot widget reveals that cells are clearly aligned in the accordance with the time of development (embryonic day) when dimensionally reduced, meaning that time is one of the prevalent factors for segregation.
\
{{% figure src="/blog_img/2019-05-10/PCA.png" %}}
\
Additionally, we can explore another strong segregating factor which takes place during E5 and causes scatter plot to distinctly change shape. Since this timeline corresponds with blastocoel formation, we could try scoring the cells for trophectoderm (<b>TE</b>) and inner cell mass (<b>ICM</b>) gene markers and check whether this is the reason behind segregation of the cells on the scatter plot.  
<br>
Firstly we need to export genes into a new data table. In it we select <i>GATA2</i> and <i>GATA3</i> as the markers for TE and <i>SOX2</i> plus <i>PDGFRA</i> for ICM cells and use them as gene input for the Score Cells widget. 
\
{{% figure src="/blog_img/2019-05-10/workfow-linage-3.png" %}}
\
As the second input we need to select all the cells in a Data Table widget that contains normalised data. After that we cluster the cells using the similar settings as before (k-neighbours: 100, resolution: 1.6) to elicit 8 clusters (5 for each sampling day and three additional ones to separate E5, E6 and E7 to ICM and TE cells).
\
{{% figure src="/blog_img/2019-05-10/tSNE2-2.png" %}}
\
tSNE projection reveals that the cells sampled on 5<sup>th</sup> (E5), 6<sup>th</sup> (E6) and 7<sup>th</sup> (E7) day separate into two different clusters, but is not considerably different form tSNE that is not preceded by the Score Cells widget that takes into account the TE and ICM marker genes.
<br>

We could try running two Score Cells widgets consecutively; first scoring cells as TE (<i>GATA2</i>, <i>GATA3</i>), the second scoring cells as ICM (<i>SOX2</i>, <i>PDGFRA</i>). Additional benefit of this approach is that we will turn cell scores into two variables and consequently be able to display them on the scatter plot.
\
{{% figure src="/blog_img/2019-05-10/workfow-linage-full.PNG" %}}
\
We can now appoint TE and ICM scores on the X and Y axis of a scatter plot.
\
{{% figure src="/blog_img/2019-05-10/linage-scatter-plot.png" %}}
\
Observing which cells score high for TE and ICM markers, we can see that cells really do enter blastocoel formation on the 5<sup>th</sup> day. 
<br>

To illustrate that even more evidently, we cluster (k-neighbours: 100, resolution: 1.6) and display them with the t-SNE widget. We set ICM score as a sizing factor. The lineage differentiation is well visible in the projection since about half of the cells in E5, E6 and E7 diplay higher scores for ICM. 
\
{{% figure src="/blog_img/2019-05-10/tSNE2-3.png" %}}
\
By combining principal component analyses (PCA) with clustering this analysis of human preimplantation embryos indeed revealed that the segregation into TE and ICM lineages occurs at E5. 
<br>

*References* 
\
Petropoulos, S., Edsgärd, D., Reinius <i>et al.</i> (2016). <a href="https://www.cell.com/fulltext/S0092-8674(16)30280-X">Single-Cell RNA-Seq Reveals Lineage and X Chromosome Dynamics in Human Preimplantation Embryos.</a> <i>Cell</i>, 165(4), 1012–1026.
