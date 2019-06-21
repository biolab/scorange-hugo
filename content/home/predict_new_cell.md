+++
title = "Predict New Cell Types Based on Marker Genes"
image = "/images/Population-Prediction.png"
learnMore = true
thumbnailImagePosition = "left"
weight = 20
excerpt = "Build classifiers to identify the cell type of each subpopulation. Use classifier on new data samples to predict cell types and focus on interesting cell type populations."
+++

Batch effect removal, machine learning, cell-embedding, and transfer learning -- these are all techniques useful in the classification of new cells, and scOrange has them all. While this section of the documentation is in writing and will be updated at the end of June 2019, we here reveal one cool feature of scOrange: automatic annotation of cells groups based on marker genes. We will continue to write up this section by pointing out how this and t-SNE based embedding of new cells can be used for cell classification that is immune to batch effects.

{{% figure src="/images/features/annotator.png"  %}}



