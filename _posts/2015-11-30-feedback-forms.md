---
title: "An Analysis of Course Feedback Forms"
date: 2015-11-30
tags: [Machine Learning, Neural Networks]
header:
  image: "../images/feedback/feedback.jpg"
  excerpt: "Machine Learning, Classification, Data Science"
---
An analysis of course feedback forms to predict the instructor, students attendance and number of repeats for that course.  

## Data

The data is a collection of course feedback forms from a group of 5820 students, along with the attendance, number of repeats, and the difficulty level of the course for which the feedback has been submitted.  

The data has four sets of classes that it can be classified into –

- Instructor (1, 2, 3)
- No. of repeats (1, 2, 3)
- Attendance (0, 1, 2, 3, 4)
- Difficulty (1, 2, 3, 4, 5)

There are 28 features in all, each one being a rating on a scale of 1 to 5 of some aspect of the course or the instructor.  

I tried feeding the features into a neural network, and based on the feedback of a random student I tried to predict –  
- the number of repeats
- the attendance of a student
- the instructor

## Neural network

I used a two-layer feed-forward network, with sigmoid hidden and softmax output neurons. This can classify vectors arbitrarily well, given that there are enough neurons in its hidden layer.  

## Predicting the number of repeats
I first trained the network to predict the no. of repeats. I got a very high accuracy of ~80%. On closer observation, I found that due to the highly biased distribution of the data points in one class (0 repeats), the network predicted almost every point as belonging to that class.
![](/images/feedback/bar-1.PNG)  

![](/images/feedback/mat-1.PNG)

## Predicting the attendance
I then tried to train the network to predict the attendance. The attendance histogram had a better distribution than the previous case. But, I only managed to get an accuracy of about 37% with the validation data. This probably happened because the number of possible classes increased to 5.
![](/images/feedback/bar-2.PNG)  

![](/images/feedback/mat-2.PNG)

## Predicting the instructor
Finally, I trained the network to predict the instructor for a given set of feedback values. There were only 3 instructors, and the distribution looked like this.
![](/images/feedback/bar-3.PNG)  

![](/images/feedback/mat-3.PNG)

### Varying the number of neurons to increase prediction accuracy  
With 10 neurons in the hidden layer, I obtained an accuracy of 59% for the validation data. Similarly, for 5 and 20 neurons in the hidden layer, I got accuracies of 62.4% and 62.8% respectively.

### Varying the number of iterations for better performance
At the 37th iteration, I obtained the best validation performance.  

![](/images/feedback/validation.PNG)
