+++
draft = false
type = "blog"
image = "/blog_img/2019-05-06/cover_embryo.png" 
thumbImage = "/blog_img/2019-05-06/cover_embryo.png"
date = "2019-05-06" 
title = "X And Y Chromosome Expression in Human Preimplantation Embryos" 
hardLineBreak = true 
categories = ["clustering", "karyotype", "Y chromosome", "embryo", "distribution"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "Determine karyotype (XY, XX) of the samples from single cell data and observe the time of activation of Y chromosome in a preimplantation embryo." 
longExcerpt = "Using the single cell data from Petropoulos et al. (Cell, 2016) we determine the karyotype (XY, XX) of the cells and inspect the time of activation of Y chromosome in a preimplantation embryo." 
+++
We have already demonstrated how to identify cell types using marker genes in our previous <a href= "https://singlecell.biolab.si/blog/marker-genes/">blog</a>. Today we will apply the same principle to determine the biological sex of human preimplantation embryos sampled by <a href= ”https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Petropoulos <i> et al. </i> </a> (Cell, 2016) and examine the time of Y chromosome activation. 
<br>

The data we need for this example is deposited in ArrayExpress database under the accession number <a href=”https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-3929/”> E-MTAB-3929 </a>. This single cell data was collected from human preimplantation embryos at different timepoints.
We import the data into Orange using The Load Data widget, followed by Gene Name Matcher widget. Employing Create Class widget helps us to classificate cells based on the sampling day.
\
\
{{% figure src="/blog_img/2019-05-06/createclass_workflow.png" width="95%" height="95%" %}}
\
\
We are now ready to dive into a more demanding task of separating cells based on their biological sex. In order to do that, we need to score cells based on X- and Y-linked genes. We shall start with the Y-linked genes. Firstly, we connect a new Data Table widget from the data we normalised so far and use it as the first input for the Score Cell widget. As the second input, we select Y-linked genes (<i>AMELY , DAZ1, Ddx3y, EIF1AY, KDM5D, PCDH11Y, RBMY1A1, RPS4Y1, RPS4Y2, SRY , TSPY1, USP9Y, UTY, ZFY</i>) in a separate Data Table widget. 
\
\
{{% figure src="/blog_img/2019-05-06/workflow_embryo_partial2.PNG" width="95%" height="95%" %}}
\
\
Distribution widget is the most fitting way to depict the scores. 
\
\
{{% figure src="/blog_img/2019-05-06/chrY_distribution.png" width="75%" height="75%" %}}
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
{{% figure src="/blog_img/2019-05-06/workfow_embryos.PNG" width="95%" height="95%" %}}
\
\
Additionally, we can check expression of X-linked genes to exclude any cells with too low overall expression profiles and asses the possibility of X0 karyotype. We aproach this the same way as before; by selecting X-linked genes (<i>AMELX, DDX3X, EIF1AX,KDM5C, PCDH11X, RPS4X, SOX3, USP9X, UTX</i>) in a separate Data Table and scoring cells with them. 
\
\
{{% figure src="/blog_img/2019-05-06/chrX_distribution.png" width="75%" height="75%" %}}
\
\
Some of the cells seem to have suspiciously low expression of X chromosome. Most probably the reason behind this observation is that one of the embryos in this dataset has been identified as having XO karyotype by <a href= ”https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Petropoulos <i> et al.</i> </a>.
<br>

So, today we have showed how scOrange can be used to sort cells by karyotype and study time of activation of chromosomes in inhuman preimplantation embryos. 

*References* 
\
Miller CM, Sen DR, Abosy RA <i>et al.</i> (2019) <a href="https://www.nature.com/articles/s41590-019-0312-6">Subsets of Exhausted CD8+ T Cells Differentially Mediate Tumor Control and Respond to Checkpoint Blockade.</a> <i>Nat Immunol.</i> 20:326–336.

Petropoulos, S., Edsgärd, D., Reinius <i>et al.</i> (2016). <a href=”https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Single-Cell RNA-Seq Reveals Lineage and X Chromosome Dynamics in Human Preimplantation Embryos.</a> <i>Cell</i>, 165(4), 1012–1026. 