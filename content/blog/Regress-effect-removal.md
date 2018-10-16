+++
draft = false
type = "blog"
image = "/blog_img/2018-10-04/regressing-batch-effect.png"
thumbImage = "/blog_img/2018-10-04/regressing-batch-effect.thumb.png"
date = "2018-10-03"
title = "Regressing Out Cell-Cycle Effects"
weight = 2
hardLineBreak = true 
categories = ["batch effect", "PCA"]
joinLines = false
author = "Ajda Pretnar"
shortExcerpt = "Calculate cell-cycle phase scores based on canonical markers, and regress these out of the data during pre-processing."
longExcerpt = "Calculate cell-cycle phase scores based on canonical markers, and regress these out of the data during pre-processing."
+++

scOrange can remove cell-cycle effects from the data. We will work with *mouse haematopoietic stem and progrenitor cell differentiation* data from the Single Cell Datasets. It is always good to observe it in a Data Table.
\
\

{{% figure src="/blog_img/2018-10-03/mouse-datatable.png" %}}
\
\

First, we need to normalize the data using the counts-per-million reads (CPM) from the Single Cell Preprocess widget.
\
\

{{% figure src="/blog_img/2018-10-04/preprocessing1.png" width="40%" height="40%" %}}
\
\

Then, pass the data through the first Score Cells widget and provide S phase markers from Tirosh et. al (2016) that we have loaded with Marker Genes widget. We will repeat the same procedure with the second Score Cells and another Marker Genes widget, this time using the G2M phase markers. Now, we have the data with two additional meta columns containing marker gene scores.
\
\

{{% figure src="/blog_img/2018-10-04/t-SNE-selection.png" %}}
\
\

In the second preprocessing phase we will select highly variable genes, log-normalize them and scale the expression data to the upper bound of 10.
\
\

{{% figure src="/blog_img/2018-10-04/preprocessing2.png" %}}
\
\

Now for the fun part. We will draw a PCA plot using the first two PCA components. Select two components in PCA widget and pass the data to two Scatter Plots, one for S phase and one for G2M phase.
\
\

{{% figure src="/blog_img/2018-10-04/scatterplots1.png" caption="The final workflow." width="60%" height="60%" %}}
\
\
In the second branch we will use Batch Effect Removal, which can eliminate the cell cycle-associated variance and obtain corrected expression values. If we repeat the same procedure as above, with PCA and two Scatter Plots, we can see how cells of the same cycle phase are much less clustered.
\
