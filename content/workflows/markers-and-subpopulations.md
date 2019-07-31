+++
title= "Marker Genes and Subpopulations"
# the aspect ratio of images should match 460 : 280
images =  ["/workflow_images/markers-and-subpopulations.png", 
           "/workflow_images/marked-tsne.png", 
           "/workflow_images/table-with-cell-scores.png"]
type = "workflows"
blog =  ""
video = "https://www.youtube.com/watch?v=-xB3Jga1dC0"
download = "markers-and-subpopulations.ows"
tags = ["Marker Genes", "t-SNE"]
weight = 70
+++

This workflow uses Score Cell and Marker Genes widget to score the cells according to the expression of selected markers. Scored cells can be passed to, say, t-SNE visualization, where any change of a selection of marker genes will automatically trigger the update in t-SNE to identify an associated subpopulation of cells.
