---
layout: post
title: "Classification of Songs - A Machine Learning Project"
date: 2019-11-19
header:
	image: "/images/header-msd.png"
	excerpt: "Machine Learning, Classification, Regression, Data Science"
---

#Dataset

The **Million Song Dataset** is a freely-available collection of audio features and metadata for a million contemporary popular music tracks. This project uses a [subset](http://millionsongdataset.com/pages/getting-dataset/#subset) of this dataset. The data contains 515,345 songs, each described by 90 features, and the year in which the song was released. The years range from 1922 to 2011.

#Exploratory Data Analysis

For simplicity, the number of classes is reduced from 90 to 9 by assigning a decade to each song, instead of year.

A histogram of the count of songs in each decade showed an unevenly distributed data:
[hist-unmodified](/images/hist-unmodified.png)

Changing the width of the classes resulted in a more evenly distributed graph as shown: (explain why you needed evenly distributed data)
[hist-modified](/images/hist-modified.png)

#Choosing Features
A feature can be chosen for classification, if it peaks at different places for different classes. For example, I chose 'Timbre average 1' as one of the classifiers as it peaked at various regions for Class 1 and Class 2 as shown in the below figure:
[hist-f1-c1-c2](/images/hist-f1-c1-c2.png)

##Principal Components
A scatter plot of the first two principal components looked something like this:
[scatter-pc](/images/scatter-pc.png)

Two important observations can be made from this plot:
1. There is a significant difference in the amount of data between the first few classes and the last couple of classes (it is obscured by pink).
2. The colors are all bundled together. Ideally, the different colors must be local to different regions on the plot, so that a more accurate decision can be made when predicting the class of some unknown data.

#Bayes' CLassification
The test data was first classified without reducing any dimensions (i.e., using all 90 features independently). An accuracy of 22% was obtained.

The 90 features were then projected in the direction of the 2 eigenvectors corresponding to the 2 highest eigenvalues. Classifying with the help of the 2 principal components returned an accuracy of around 50%. As this result seemed odd, the procedure was rechecked. 
This lead to a conclusion that the dataset has the **curse of dimesionality**. The problem is that when the dimensionality increases, the volume of the space increases so fast that the available data becomes sparse. So, a huge amount of data is required to support analysis in higher dimensions.

After modyfying class sizes to obtain a more evenly distributed data, the prediction accuracy was in fact lower (only about 35%). I do not have a plausible explanation for this. The decision boundary looks as below:
[decision-boundary](/images/dec-bound.png)
