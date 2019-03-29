+++
draft = false
type = "blog"
image = ""
thumbImage = ""
date = "2019-03-29"
title = "Importing and using your own marker genes"
hardLineBreak = true 
categories = ["conference", "FAIR", "reproducibility"]
joinLines = false
author = "Iva Černoša"
shortExcerpt = "If you ever felt limited by Marker Gene widget, here you can discover how to bypass it" 
longExcerpt = "If you ever felt limited by Marker Gene widget, here you can discover how to bypass it" 
+++

<i><b>Note:</b> This blog heavily references and uses the data we identified in our previous blog <a href="">Clustering Cells in Mouse Pancreas</a>, therefore it is advisable for everyone less experienced with scOrange to read it before tackling this one.</i>
<br>
<br>
Orange already has a build-in widget with marker genes but what if your marker genes are not in included its library? Well, there is no reason to give up, with only a few extra steps you can easily import our own. 

{{% figure src="/blog_img/2019-03-29/marker_1.png" width="95%" height="95%" %}}
\
\
As usual, we first need to import our data. We are using the data from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5228327/">Baron <i>et al.</i></a> (GEO accession: GSE84133). We import and normalise our data using Load Data, Gene Name Matcher and Single Cell Preprocess widgets (a detailed description of these steps is available in our previous blog Clustering Cells in Mouse Pancreas).
<br>
<br>
Now we import our marker genes using File widget. Here we are using the marker genes for we identified and saved in the last steps of our earlier blog. Marker genes can be formatted in a simple table. In case your data does not include Entrez IDs for your genes, you have to process them with the Gene Name Matcher widget first, so that Orange assigns them Entrez IDs and can later match them to the genes in the data you are analysing.  

{{% figure src="/blog_img/2019-03-29/marker_2.png" width="95%" height="95%" %}}
\
\
To connect out marker genes and our data, we use Score Cells widget and make sure we correctly mark our input data. Marker genes should be attached as genes and our data as data. 

{{% figure src="/blog_img/2019-03-29/marker_3.png" width="95%" height="95%" %}}
\
\
Orange has now scored cells based on our markers. To visualise this, we use t-SNE and colour cells based on Cell Score with it. Since yellow coloured cells in this graph represent cells that score higher for selected genes and we selected the markers for beta cells in in the previous step, these are more likely to be beta cells. 

{{% figure src="/blog_img/2019-03-29/marker_4.png" width="95%" height="95%" %}}
\
\
*References*

