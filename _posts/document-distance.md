---
title: "Plagiarism test for two documents"
date: 2019-12-22
header:
  image: "../images/docdist.jpg"
---

# Testing for plagiarism by calculating the angle between the two documents

In this project, I try to estimate the degree of dissimilarity between two documents by calculating the angle between them.  
When I say angle, I mean the angle between the vectors formed by calculating the frequencies of each word in the document. A more detailed explanation of the algorithm should make this clear.  

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

## Applications

There are several areas where this algorithm can be used. The area that I am particularly interested is, using this algorithm to implement a search engine. Although, implementing a search engine would involve everything right from web crawling, web scraping and then finally using document distance to find the most similar links to display when searched. And that is a project idea to work on in the next 1-2 months.
