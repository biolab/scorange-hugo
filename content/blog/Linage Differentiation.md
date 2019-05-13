+++
draft = false
type = "blog"
image = ""
thumbImage = ""
date = "2019-05-10"
title = "Pinpointing Linage Differentiation in Human Preimplantation Embryotic Cells"
hardLineBreak = true 
categories = ["PCA", "tSNE", "differentiation", "embryo", "linage", "clustering"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Combine clustering and time component to pinpoint the time of trophectoderm (TE) and inner cell mass (ICM) differentiation in human preimplantation embryotic cells" 
longExcerpt = "Combine clustering and time component to pinpoint the time of trophectoderm (TE) and inner cell mass (ICM) differentiation in human preimplantation embryotic cells and recreate a part of study by Petropoulos et al. (Cell, 2016)" 
+++
<!--dodaj uvod-->
<!--dodaj cover sliki-->
<!--linkaj zadnji blog v prvi povedi-->
We will be using the same single cell data from human preimplantation embryos as in the last blog. The data was published by <a href=” https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Petropoulos <i> et al. </i> </a>and is deposited in ArrayExpress database under the accession number <a href=”https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-3929/”>E-MTAB-3929</a>. 
<br>

Naturally, we have to start by loading the data into Orange and pre-processing it using the familiar workflow with the following widgets: Load Data, Gene Name Matcher, Create Class to sort cells by sampling and of course Single Cell Preprocess to normalise the data and select 500 most variable genes.
\
\
{{% figure src="/blog_img/2019-05-10/workfow_embryos2nd_1.png" width="85%" height="85%" %}}
\
\
To show that cells expression changes with time, we cluster the cells using the Louvain Clustering widget with resolution set to 1.7 and k-neighbours to 100. t-SNE distinctly depicts 7 clusters. E4 and E5 samples are slightly divided, which is in accordance to the fact that Petropoulos <i>et al.</i> sampled those cells at two occasions 4-6 hours apart.
\
\
{{% figure src="/blog_img/2019-05-10/tSNE2.png" width="85%" height="85%" %}}
\
\
Another way to confirm that time play a crucial role in the cell segregation is by using the Principal Component Analysis (PCA) widget. 
\
\
{{% figure src="/blog_img/2019-05-10/workfow_embryos2nd_2.PNG" width="95%" height="95%" %}}
\
\
Scatter Plot widget reveals that cells are clearly aligned in the accordance with the time of development (embryonic day) when dimensionally reduced, meaning that time is one of the prevalent factors for segregation.
\
\
{{% figure src="/blog_img/2019-05-10/PCA.png" width="95%" height="95%" %}}
\
\
Additionally we can explore another strong segregating factor which takes place during E5 and causes scatter plot to distinctly change shape. Since this timeline corresponds with blastocoel formation, we could try scoring cells for trophectoderm (<b>TE</b>) and inner cell mass (<b>ICM</b>) gene markers and check whether this is the reason behind segregation of the cells on the scatter plot.  
<br>

Firstly we need to export genes into a new data table. In it we select <i>GATA2</i> and <i>GATA3</i> as markers for TE and <i>SOX2</i> plus <i>PDGFRA</i> for ICM cells and use them as gene input for Score Cells widget. 
\
\
{{% figure src="/blog_img/2019-05-10/workfow_embryos2nd_3.png" width="95%" height="95%" %}}
\
\
As the second input we need to select all the cells in a Data Table widget that contains normalised data. After that we cluster the cells using the similar settings as before (k-neighbours: 100, resolution: 1.6) to elicit 8 clusters (5 for each sampling day and three additional ones to separate E5, E5 and E7 to ICM and TE cells).
\
\
{{% figure src="/blog_img/2019-05-10/tSNE2_2.png" width="95%" height="95%" %}}
\
\
tSNE projection reveals that cells sampled on 5<sup>th</sup> (E5), 6<sup>th</sup> (E6) and 7<sup>th</sup> (E7) day separate into two different clusters.

<!--dopiši, kako natančneje ločiti ICM in TE, da se vidi tudi na grafu in naredi zaključek-->

*References* 
\
Petropoulos, S., Edsgärd, D., Reinius <i>et al.</i> (2016). <a href=”https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Single-Cell RNA-Seq Reveals Lineage and X Chromosome Dynamics in Human Preimplantation Embryos.</a> <i>Cell</i>, 165(4), 1012–1026.
