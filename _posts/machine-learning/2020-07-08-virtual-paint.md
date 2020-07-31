---
title: "Virtual Paint"
date: 2020-07-08
tags: [OpenCV]
header:
  image: "/images/ds.jpg"
  excerpt: "Computer Vision"
---

Hover a marker in the air in front of the camera to paint on the screen.

## Why this project
Fascinated by the field of computer vision, I sought to learn more about it. I learnt some basics of the library of OpenCV in python. In an effort to apply the skills learnt to a project and learn more along the way, I chose this project.

## How it Works
#### Finding HSV thresholds
I convert the image captured by the webcam to an [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV) image. I then set up scrollbars where I can vary the Hue, Saturation and Value to find the thresholds that detect only one color.
#### Setting up masks
I then set up masks that separate out each color from the rest of the picture on screen.
#### Painting in the air
As I move a colored marker, I draw on the image with the same color as the marker. This created the effect of a virtual marker.

## Code

[Here](#) is the code I wrote.
