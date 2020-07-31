---
title: "Harry Potter's Invisibility Cloak"
date: 2020-07-15
tags: [OpenCV]
header:
  image: "/images/ds.jpg"
  excerpt: "Computer Vision"
---

Take any blue cloth and be invisible.

## Why this project
As a child, I always wanted to have magical powers. I came across someone on my linkedIn that did this project. I had to get myself an invisibility cloak too.

## How it Works
#### Finding HSV thresholds
I convert the image captured by the webcam to an [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV) image. I then set up scrollbars where I can vary the Hue, Saturation and Value to find the thresholds that detect only one color - the color of the cloak.
#### Setting up masks
I then set up masks that separate out the cloak from the rest of the picture on screen.
#### The trick to Invisibility
When webcam first starts, we capture an image of the background where the subject will be standing. When the cloak appears on screen, we superimpose the background image on the webcam display. And Voila!

## Code

[Here](https://github.com/akhilayaragoppa/akhilayaragoppa.github.io/blob/master/source_code/invisibilityCloak.py) is the code I wrote.
