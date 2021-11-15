# Music Genre Classifier

## Objective

The objective of this project is to learn about approaches to classification of music genres. 
The main method explored in this project is the K-nearest neighbours (KNN).

K-nearest neighbours is popularly used for regression and classification. The predictions on the data points are based
on a similarity score, which is computed based on how far the points are from one another.

## Background
The first step of the music genre classifier would be to extract features and component from the provided audio files 
(whether it be for training or classification).


## Develop

A Makefile is included in the repository for ease of use.

To run the training dataset:
```bash
make train
```

To run the classifier on a specific file:
```bash
make run
```

