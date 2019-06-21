+++
title = "Discover New Marker Genes that Distinguish Cell Types"
image = "/images/Biomarkers.png"
learnMore = true
video = "lb-x36xqJ-E?start=6"
thumbnailImagePosition = "right"
weight = -20
excerpt = "Identify signature genes for each subpopulation using multiple methods. Use gene ontology enrichment to explore the biological meaning and identify cell types."
+++

In scOrange, we can find a cluster of cells and then characterize it with a set of differentially expressed genes. If there is a cell type that is prevailing in out cluster, this technique can be used to find candidates for gene markers.

In other words, we can consider a data set, score cells with a set of known markers, select a subset of cells that express these markers, find genes that are differentially expressed between selected and all other cells, and analyze these genes using, say, gene ontology to perhaps find an ontology term and corresponding genes of our liking. We can use the following workflow for this task.

{{% figure src="/images/features/diff-express-workflow.png"  %}}

Ok, this was fast. Let us go through this workflow step-by-step, and in the process learn how to define a set of our own markers.

## Cells Expressing Custom Set of Marker Genes

For an example, we will here explore the cells from bone marrow mononuclear cells that are readily available from scOrange's Single Cell Datasets widget. We would like to identify the group of B lymphocytes, or B cells, and perhaps some other types of cells. A conventient list of markers from those cells can come from a [CD Marker Handbook](https://www.bdbiosciences.com/documents/cd_marker_handbook.pdf); we can use to compile a short list of marker genes in Excel:

{{% figure src="/images/features/markers-excel.png"  %}}

In scOrange, we load the Excel file, use Gene widget to translate the common gene names into NCBI's Entrez ID and letting Orange know that these genes are human. Next, we use data table to display marker genes and cell types, and to select a subset of marker genes.

{{% figure src="/images/features/genes-table.png"  %}}

We selected the marker gene for B cells, and use Score Cells to score the cells accoding to the mean expression of selected marker genes. Turns out that there is a cluster of cells in t-SNE visualization that express this marker. Nice! We select these cells, and we are now ready to characterize them with differentially expressed genes.

## Differentially Expressed Genes

We can characterize cells that have been selected in t-SNE by producing a table with all the data that includes additional feature telling scOrange if the cell was selected or not. Note that by defaul, t-SNE would output only selected data items, and to change this we need to rewire the link between t-SNE and Differential Expression widget by double clicking on the corresponding link, removing the default "Selected Data" to "Data" connection and connecting the "Data" output of t-SNE to the input of differential expression widget.

{{% figure src="/images/features/t-sne-send-all-data.png"  %}}

Differential Expression widget displays the distribution of statistics accross genes. Here, we chose that we will score the genes by t statistics that compares their expression in selected group of cells and cells outside the selection. 

{{% figure src="/images/features/differential-expression.png"  %}}

We are interested for the genes in the tail of this distribution, but before giving out their names, let us see if they share any common annotations in the Gene Ontology.

## Gene Ontology Analysis

The ninety-four differentially expressed genes share a number of annotations from Gene Ontology. Most of them are related to immune process. No wonder: we have selected the cells expressing B lympocyte marker that are expected to be part of the human immune system.

{{% figure src="/images/features/gene-ontology.png"  %}}

## Finding New Markers

From Gene Ontology, we can select any interesting term and then check its corresponding genes in the Genes widget. We did so for the genes from immune cell process.

{{% figure src="/images/features/b-cell-putative-markers.png"  %}}

Among these genes is also CD79a, a known marker for the B cells. Oh, what a joy, we just rediscovered it. Here is a corresponding section from a [CD Marker Handbook](https://www.bdbiosciences.com/documents/cd_marker_handbook.pdf) that confirms our result.

{{% figure src="/images/features/cd-marker-handbook-on-cd79a.png"  %}}

The marker that we found has already been known, but this only encourage us to use the same procedure on some other data with more unknowns and differentially expressed genes that have not been characterized yet.

