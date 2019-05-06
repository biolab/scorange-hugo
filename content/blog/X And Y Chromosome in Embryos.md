+++
draft = false
type = "blog"
image = "" <!--dodaj slike-->
thumbImage = ""
date = "2019-05-06" 
title = "X And Y Chromosome Expression in Human Preimplantation Embryos" 
hardLineBreak = true 
categories = ["clustering", "karyotype", "t-SNE", "Y Chromosome", "Embryo"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Determine karyotype of the samples from single cell data and cluster cells in a preimplantation embryo." 
longExcerpt = "Using the single cell data from Petropoulos et al. (Cell, 2016) we determine the karyotype (XY,XX) of the cells in a preimplantation embryo and cluster them to examine their development." 
+++
<!--dodaj uvod-->
The data we need for this example is deposited in ArrayExpress database under the accession number <a href=”https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-3929/”> E-MTAB-3929 </a>. This single cell data was collected from human preimplantation embryos at different timepoints.
We import the data into Orange using The Load Data widget, followed by Gene Name Matcher widget. Employing Create Class widget helps us to classificate cells based on the sampling day.
\
\
{{% figure src="/blog_img/2019-05-06/createclass.png" width="95%" height="95%" %}}
\
\
\
\
{{% figure src="/blog_img/2019-05-06/workflow_embryo_partial.PNG" width="95%" height="95%" %}}
\
\
We are now ready to dive into a more demanding task of separating cells based on their biological sex. In order to do that, we need to score cells based on X- and Y-linked genes. We shall start with the Y-linked genes. Firstly, we connect a new Data Table widget from the data we normalised so far and use it as the first input for the Score Cell widget. As the second input, we select Y-linked genes (<i>AMELY , DAZ1, Ddx3y, EIF1AY, KDM5D, PCDH11Y, RBMY1A1, RPS4Y1, RPS4Y2, SRY , TSPY1, USP9Y, UTY, ZFY</i>) in a separate Data Table widget. 
\
\
{{% figure src="/blog_img/2019-05-06/workflow_embryo_partial2.PNG" width="95%" height="95%" %}}
\
\
Distribution widget is the most fitting way to depict out results. 
\
\
{{% figure src="/blog_img/2019-05-06/chrY_distribution.png" width="95%" height="95%" %}}
\
\
Observing the outcome, we can quickly deduce that the bar on the far left is representative of the cells with the XX karyotype and the rest represent cells from male embryos. 
<br>
To check weather Y-linked genes are ubiquitously expressed at all stages of preimplantation embryos, we foremost have to elect the cells with XY karyotype.  We utilise the Data Table widget and sort the cells according to their score for Y-linked genes. Judging from the distribution, a good cut off mark for the XY cells seems to lie between 0,3 and 0,5, therefore we select 0,4. The Box Plot widget reveals an increase between E3 (day 3) and E4 (day 4). 
\
\
{{% figure src="/blog_img/2019-05-06/chrY_male_box.png" width="95%" height="95%" %}}
\
\
As demonstrated by <a href=” https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Petropoulos <i> et al. </i> </a> this is due to incomplete zygotic genome activation at E3, since cells at this stage still contain lingering maternal transcripts.
\
\
{{% figure src="/blog_img/2019-05-06/workflow_embryo.png" width="95%" height="95%" %}}
\
\
To show that cells expression changes with time, we cluster them using the Louvain Clustering widget with resolution set to 2.0 and k-neighbours to 100. tSNE distinctly depicts 7 clusters. E4 and E5 samples are divided in two clusters which is in accordance to the fact that Petropoulos <i> et al. </i> sampled those cells at two occasions 4-6 hours apart.
\
\
{{% figure src="/blog_img/2019-05-06/tSNE1.png" width="95%" height="95%" %}}
\
\

<!--dodaj zaključek-->