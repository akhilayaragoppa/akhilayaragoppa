---
title: "Classification of Songs - Million Song Dataset"
date: 2019-11-19
tags: [Machine Learning, Bayesian Classification]
header:
  image: "../images/songs.jpg"
  excerpt: "Machine Learning, Classification, Data Science"
---

## Dataset

The **Million Song Dataset** is a freely-available collection of audio features and metadata for a million contemporary popular music tracks. This project uses a [subset](http://millionsongdataset.com/pages/getting-dataset/#subset) of this dataset. The data contains 515,345 songs, each described by 90 features, and the year in which the song was released. The years range from 1922 to 2011.

## Exploratory Data Analysis

For simplicity, the number of classes is reduced from 90 to 9 by assigning a decade to each song, instead of year.
A histogram of the count of songs in each decade showed an unevenly distributed data:
<img src="{{ site.url}}{{ site.baseurl }}/images/hist-unmodified.PNG" alt="Hist-unmodified">

In an attempt to obtain a more evenly distributed data, the width of the classes was altered, thus resulting in a distribution as shown below:
![hist-modified](/images/hist-modified.PNG)

## Choosing Features
A feature can be chosen for classification, if it peaks at different places for different classes. For example, I chose 'Timbre average 1' as one of the classifiers as it peaked at various regions for Class 1 and Class 2 as shown in the below figure:
![hist-f1-c1-c2](/images/hist-f1-c1-c2.PNG)

### Principal Components
A scatter plot of the first two principal components looked something like this:
![scatter-pc](/images/scatter-pc.PNG)

Two important observations can be made from this plot:
1. There is a significant difference in the amount of data between the first few classes and the last couple of classes (it is obscured by pink).
2. The colors are all bundled together. Ideally, the different colors must be local to different regions on the plot, so that a more accurate decision can be made when predicting the class of some unknown data.

## Bayes' Classification
The test data was first classified without reducing any dimensions (i.e., using all 90 features independently). An accuracy of 22% was obtained.

The 90 features were then projected in the direction of the 2 eigenvectors corresponding to the 2 highest eigenvalues. Classifying with the help of the 2 principal components returned an accuracy of around 50%. As this result seemed odd, the procedure was rechecked.
This lead to a conclusion that the dataset has the **curse of dimesionality**. The problem is that when the dimensionality increases, the volume of the space increases so fast that the available data becomes sparse. So, a huge amount of data is required to support analysis in higher dimensions.

After modyfying class sizes to obtain a more evenly distributed data, the prediction accuracy was in fact lower (only about 35%). I do not have a plausible explanation for this. The decision boundary looks as below:
![decision-boundary](/images/dec-bound.PNG)

## Implementation
The MATLAB code written to perform the above analysis:
```matlab
raw = load('YearPredictionMSD.txt');
data = raw(:,2:91);
%Separate data for train and test as given in website
%separate class info from data
trainingData = data(1:463715,:);
class_traingData = raw(1:463715,1);
r_class_train = ClassReduce(class_traingData);
testingData = data(463716:515345,:);
class_testingData = raw(463716:515345,1);
r_class_test = ClassReduce(class_testingData);

%histogram of two features
figure,hist(trainingData(:,1));
figure,hist(trainingData(:,13));

% find 2 principle components(PC)
coeff = pca(data);
coeff = coeff(:,1:2);
%figure, mesh(coeff);

% finding data representation along PC
mu = mean(trainingData);
lowrep_trainingData = zeros(size(trainingData,1),2);
for i = 1:size(trainingData,1)
    lowrep_trainingData(i,:) = (trainingData(i,:)- mu) * coeff;
end
dim_cov = cov(lowrep_trainingData);

mu = mean(testingData);
lowrep_testingData = zeros(size(testingData,1),2);
for i = 1:size(testingData,1)
    lowrep_testingData(i,:) = (testingData(i,:)- mu) * coeff;
end

model = NaiveBayes.fit(trainingData,r_class_train);
test_op = predict(model,testingData);
result = ((test_op- r_class_test) == 0);
acuracy = sum(result)/size(result,1);

model2 = NaiveBayes.fit(lowrep_trainingData,r_class_train);
test_op1 = predict(model2,lowrep_testingData);
result1 = ((test_op1- r_class_test) == 0);
acuracy1 = sum(result1)/size(result1,1);
```
