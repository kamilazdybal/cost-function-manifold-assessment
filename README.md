# Cost function for low-dimensional manifold topology assessment

This repository contains Jupyter notebooks associated with the publication:

> K. Zdybał, E. Armstrong, J.C. Sutherland, A. Parente - Cost function for low-dimensional manifold topology assessment.

## Reproducing paper results

To reproduce the results included in the original publication (and in the supplementary material), several Python libraries are required. Mainly, the [PCAfold](https://pcafold.readthedocs.io/en/latest/index.html) library contains the implementation of the cost function. It also introduces several functions and algorithms used throughout the work. The installation instructions can be found in the linked documentation page.

Below is a full list of required libraries:

```
numpy
pandas
copy
time
random
pickle
csv
ast
PCAfold
tensorflow
keras
sklearn
dml
umap
scipy
plotly
matplotlib
```

Random seed `100` is used throughout this work.

#### [Cost function assessment of swiss roll data projections](code/)

#### [Cost function application to categorical data](code/)
