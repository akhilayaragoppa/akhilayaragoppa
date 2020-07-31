---
title: "Cosine distance between two documents"
date: 2019-12-10
category: "Algorithms"
header:
  image: "/images/abs.jpg"
---

A tiny python script that calculates the cosine distance between any two documents.

## What is cosine distance?

In simple terms, cosine distance gives an idea of the degree of dissimilarity between two sets of text documents. We do this by calculating the angle between them. Angle between two vectors is the angle formed by the word vectors in the two documents. A detailed explanation of the algorithm should make this clear.  

## Where can we see this being used?

There are several applications of cosine distance algorithm.

* Implementing a search engine
* Testing for plagiarism
* Natural Language Processing

## Algorithm

Steps:
1. Parse the given document to find all the words present in the document
2. Calculate frequencies of each word. Consider this a multi-dimensional vector (the number of dimensions of the vector being the number of unique words in the document)
3. Calculate the angle between these two vectors

## Inputs

The code takes two file names as input, between which you intend to calculate the angle.

## Output

The final output is the angle (in radians) between the two documents.

## Source code

The source code with the entire implementation can be found [here](https://github.com/akhilayaragoppa/akhilayaragoppa.github.io/blob/master/source_code/document-distance.py)
