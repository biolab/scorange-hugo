+++
draft = false
type = "blog"
image = "/blog_img/2019-03-29/"
thumbImage = "/blog_img/2019-03-29/"
date = "2019-06-06"
title = "Identification of Cell Populations in Healthy Bone Marrow"
hardLineBreak = true 
categories = ["marker genes", "tSNE", "box plot"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = " " 
longExcerpt = " " 
+++


The data from<a href= “https://www.sciencedirect.com/science/article/pii/S0092867419300947”> Galen  <i> et al.</i></a> in available in the GEO database under the accession number <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116256”>GSE116256</a>. We will be using the data from only one healthy patient <a href= “https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588000”> BM4 </a> and its <a href= https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588001> annotation file </a> since this is by far the biggest nonenriched sample from a healthy individual in this dataset. 
<br>

<!-- popravi tage, naslovno sliko, povzetke,...-->
<!-- dodaj uvod-->

After loading the data and matching the genes in the dataset to those in databases, we filter out all the genes that appear in less than 10 cells. Besides the usual normalisation, we select 5000 most variable genes. 
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial1.PNG" width="45%" height="45%" %}}
\
\
Since the relationships between the cell clusters is important for this analysis, we use Hierarhical Clustering widget to cluster the data. Firstly, we calculate the distances between the cells and then cluster them with top N set to 15, since we know from the literature that we are looking for 15 cell types. 
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial2.PNG" width="75%" height="75%" %}}
\
\
<!--mogoče še izpostavi, kako lahko vidiš na grafu, kako so povezane gruče med sabo-->
We can tackle the identification of the clusters using two different approaches. The first is by identifying the most significant genes in each cluster as described in one of our previous <a href= “https://singlecell.biolab.si/blog/pancreas/ “> blogs</a> and assuming cell types according to marker genes’ functions, the other is using the <a href= https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3588001> annotation file </a> provided by <a href= “https://www.sciencedirect.com/science/article/pii/S0092867419300947”> Galen  <i> et al.</i></a>.
\
\
{{% figure src="/blog_img/2019-06-06/workflow_partial3.PNG" width="85%" height="85%" %}}
\
\
But before we take a closer look at either of the alternatives, let us take a look at the distribution of the clusters using the Box Plot widget. 
\
\
{{% figure src="/blog_img/2019-06-06/boxplot.png" width="95%" height="95%" %}}
\
\
C4 and C5 are the biggest clusters. This information might come in handy when we try to identify them.
<br>

What we have also already done in this workflow is identified markers for each cluster with the help of Data Tables (explained in detail in <a href= “https://singlecell.biolab.si/blog/pancreas/“> this blog</a>). With these markers we can classify clusters. For example, <i>CD3D</i> is the most significant gene in cluster 4. It encodes T-cell surface glycoprotein CD3. Similarly <i>MS4A1</i> in the cluster 3 encodes B-lymphocyte antigen CD20.
<br>

Next, we can look at how our clusters match up with the markers for cell types found in the article. A straightforward way to do this is to visualise it with Heat Map widget. We have to use Select Columns widget before it to only display the markers.
<!-- CCl5 je npr. marker za CTL in NK (clustra C1 in C2), CD3G pa večinoma za CTL, torej so C2 CTL. ALi naj raje cel heatmap ven vržem?-->
\
\
{{% figure src="/blog_img/2019-06-06/heatmap_theirmarkers.png" width="95%" height="95%" %}}
\
\
Now that we have matched clusters with cell types, we can use Edit Domain widget to change annotations of the clusters. 
\
\
{{% figure src="/blog_img/2019-06-06/editdomain.PNG" width="95%" height="95%" %}}
\
\
Additionally, we can merge the annotation file provided by Galen  <i> et al.</i></a> with our data and display both bell classifications on t-SNE projection simultaneously. 
<!-- kako moraš spremeniti anno file, da ga bere-->
\
\
{{% figure src="/blog_img/2019-06-06/workflow_final.PNG" width="95%" height="95%" %}}
\
\
\
\
{{% figure src="/blog_img/2019-06-06/tSNE.png" width="95%" height="95%" %}}
\
\


<!-- ali naj še na roko dopišem, kaj so preostale skupine?-->

<!-- dodaj zaključek-->

*References* 
\
Petropoulos, S., Edsgärd, D., Reinius <i>et al.</i> (2016). <a href=”https://www.cell.com/fulltext/S0092-8674(16)30280-X”>Single-Cell RNA-Seq Reveals Lineage and X Chromosome Dynamics in Human Preimplantation Embryos.</a> <i>Cell</i>, 165(4), 1012–1026.
<!-- popravi-->