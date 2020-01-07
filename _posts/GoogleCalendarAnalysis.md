
# Extracting events from Google Calendar for Data Analysis

I wrote a python script to extract events from my google calendar using the 
Google Calendar API.
* Inputs: Start date, number of days (n)
* Output: A csv file with events for n days and related information.
This can be directly imported as a DataFrame using pandas, for 
further analysis and visualization.

## Motivation

I am always looking for ways to maximise my productivity. The goal is to 
get done as much as I want to, while being careful not to reach the point of burnout.  

I recently came across this idea of scheduling every minute of your day using a 
calendar. This method worked surprisingly well and helped me very easily achieve 
my daily goals. I have been using the google calendar to track my daily activities. 
It occurred to me that I could track and monitor my progress by visualizing how I 
spent the last few days/weeks.

## What the code does

### Querying data from Calendar API
Each task I schedule in my day is an event. I first extract the event resources 
by calling the google calendar APIs. Some useful information on how various items 
in the calendar are stored, is provided in the [official documentation](https://developers.google.com/calendar/concepts).

### Ordering and segregating data
I segregate the events belonging to each day from the start date (configurable).
For each event I obtain: 
* Name of the event.
* The category of the event. Each category has a different color assigned to it.
* The date and time of start of the event.
* The duration of the event.

### Saving data into a csv
I create tables with all the above mentioned data. I save these into a csv file.
The csv file is created such that it can directly be imported into pandas as a DataFrame for further analysis.


## Calendar (Input)

This is what my calendar looked like in the last week.

![calendar](../images/g-calendar.png)

## Extracted Data (Output)

The extracted data from google calendar has the following columns:
- Day
- Event name
- Start datetime
- Event duration
- Category (Color in calendar)

A sample of the extracted data is shown below:
![Excel](../images/g-csv.png)

## What to do with the extracted csv

After importing the csv into a data frame, I can plot various graphs (histograms, pie charts, etc.) 
indicating the amount of time spent in various activites and monitor how I utilize my time. 

I shall be putting up another post with the complete analysis of this data. I will 
probably implement some ideas from habit tracking apps to extract useful 
information and implications of this data.

## Source Code

The source code for this project is in python. Source code can be found [here](https://github.com/akhilayaragoppa/akhilayaragoppa.github.io/blob/master/source_code/google-calendar.py).