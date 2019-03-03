+++
title= "Cell cycle phase prediction (transfer learning)"
image =  "/workflow_images/clustering.png"
type = "workflows"
blog =  ""
video = ""
download = "cell-cycle-phase-prediction.ows"
tags = []
weight = 20
+++


Here, we introduce a transfer learning scenario. We have two data sets of cells, potentially measured with different protocols or assays. The difference in methods is expected to be the main source of variation, occluding signal of interest.&#10;&#10;The goal is to infer a model - using the first data set - to classify each cell into one of the 3 cell cycle stages.  &#10;Then, using the inferred model, we can transfer the information to the second data set - predict the phases of the cell cycle. As all cells are labelled with known cell cycle phases, we can evaluate the performance of our model with common metrics.&#10;&#10;The workflow includes: Loading, gene filtering and preprocessing, data set alignment, visualization and performance evaluation.