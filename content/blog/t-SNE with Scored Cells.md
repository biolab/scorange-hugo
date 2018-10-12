+++
draft = false
type = "blog"
image = "/blog_img/2018-10-03/t-SNE-with-Scored-Cells.png"
thumbImage = "/blog_img/2018-10-03/t-SNE-with-Scored-Cells.thumb.png"
date = "2018-10-03"
title = "t-SNE with Scored Cells"
weight = 1
hardLineBreak = true 
categories = ["clustering", "data mining", "genomics"]
excerpt = "We can find highly expressed cells with Score Cells widget and display the cell map in t-SNE."
joinLines = false
author = "Ajda Pretnar"
+++

scOrange can help you find interesting groups of cells. Let us first load the Bone marrow mononuclear cells with AML data from the Single Cell Datasets widget. The data contains gene expressions in bone marrow mononuclear cells from a patient with acute myeloid leukemia (AML) and two healthy donors used as controls. We can first observe the data in a Data Table.
\
\

{{% figure src="/blog_img/2018-10-03/AML-datatable.png" %}}
\
\

Then we can load the marker genes to find highly expressed genes in the original data. The organism we are working with here is human. Then we can select a set of marker genes from the list. Let us go with S100A9, which contains genes for calcium binding protein A9.
\
\

{{% figure src="/blog_img/2018-10-03/Marker-Genes-S100A9.png" width="60%" height="60%" %}}
\
\

Now, connect first the Single Cell Datasets to Score Cells and then the Marker Genes widget. Score Cells will match gene names and score genes with the maximum expression level from the reference data.
\
\

{{% figure src="/blog_img/2018-10-03/Score-Cells1.png" width="40%" height="40%" %}}
\
\

Finally, we can observe the results in a t-SNE visualization. t-SNE projects multidimensional data in a 2D space by their probability function. We get nice clusters of data. But what is even better is that we can color them by the score! Let us set color and size to Score attribute. Yellow cells are those that have high expression for the select gene markers.
\
\

{{% figure src="/blog_img/2018-10-03/t-SNE-score.png" %}}
\
\

Keep the Marker Genes widget open, select a different set of genes and observe the result in t-SNE.
\
\

{{% figure src="/blog_img/2018-10-03/final-workflow-blog1.png" width="60%" height="60%" %}}
\
