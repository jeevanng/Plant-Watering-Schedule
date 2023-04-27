# Project Documentation

Written by Jeevan Ng

# Source Control Repository 

# Code Style Guide 

# List of Features

This terminal application will allow a user to create their own plant watering schedule for three different frequencies; weekly, fortnightly and monthly. 

It will use file handling to create a json file which will hold information that the user enters. Python will read and write this file as information is updated.

## Feature #1 - Add plant to schedule 

This feature will allow the user to add information to the schedule, such as plant name, frequency of watering (weekly, fortnightly or monthly), when the plant was last watered (in days) etc. 

Error handling will be used to ensure that the user will not be able to enter anything other than what is desired by the application. E.g. Data type of integer for "When the plant was last watered (days)"

## Feature #2 - Remove plant from schedule 

The user will be able to remove a plant from the schedule. 

## Feature #3 - View plants that need watering
View which plants need watering today. 

This feature will display the current day using the built-in datetime library in Python and list which plants need to be watered.

## Feature #4 - Mark plant as watered

Mark plant as watered. This feature will enable the user to let the program know which plant has been watered so that it does not show up as needing watering until required. 

## Feature #5 - View entire plant list 
This feature will allow the user to view the entire list of plants they have added to the schedule and show when they were all last watered. 

## Feature #6 - Exit program
This feature will allow the user to exit the program. 

# Implementation Plan

## Create .json file 

At the beginning of our program, we can check if a .json file exists, and if it does then we can proceed as normal. If not, then we can create one for the user. 

We can use a try, except block to check those conditions stated above. 

## Feature #1 - Add plant to schedule 

This feature will take input from the user to compile into the .json file, such as;

- Name of plant 
- Frequency of watering (weekly, fortnightly or monthly) 
- When the plant was last watered (days)
- Amount of water needed

## Feature #2 - Remove plant from schedule 

This feature will get an input from the user and ask them to type which plant they wish to remove. This would be used if the plant died, was given away or they propagated it into various pots. 

e.g
```python
remove_plant = input("Please type which plant you wish to remove from the schedule: ")
``` 

## Feature #3 - View plants that need watering

The terminal application will determine which plants to display with the following method;

The program will use the current date/time and subtract the value of the variable "When the plant was last watered (days)", which will be converted from days into a date time object. This should let us know how many days it has been since the plant was last watered. 

We can then give our program some logic and display the plants if they meet certain conditions, such as;

```python
if frequency == "weekly" and last_watered >= 7
    print(f"{plant}")

if frequency == "fortnightly" and last_watered >= 14
    print(f"{plant}")

if frequency == "monthly" and last_watered >= 30
    print (f"{plant}")
```
## Feature #4 - Mark plant as watered

This feature will reset the variable "When was the plant last watered (days)", and assign it a new date which will be equal to the date they marked as watered. 

This means that if the user misses a watering one of their plants for a couple of days, whenever they mark as watered, it will then take the weekly, fortnightly or monthly schedule from that date. This is much better logic than assigning plants to be watered on a certain day, and printing out the list according to that day. 

For example, if a user assigns a plant to the schedule that needs to be watered every week. If they forgot to water their plant for 3 days, and then mark as complete. If we assigned it a weekday, it would show as needing to be watered 4 days later. However, if we assign the date/time, whenever they mark it as complete, it will then show up as being watered 7 days later. One week.

## Feature #5 - View entire plant list 

For this feature, it can be implemented by looping through the entire .json file and printing out the "key" that we assign to the plant names, and print them all out. We can also print out when they were last watered. 

```python
print(f"{file_name[0]["name"]}, which was last watered  {file_name[1]["last_watered"]} days ago.")
```

## Feature #6 - Exit program

When the user enters a certain input, we can break out of the loop (program) and exit with a friendly message. 

```python
print("Thank you for using the plant watering schedule. See you next time")
```

## Project Management Platform

I have used Trello to track tasks, add deadlines, prioritise different features and add checklists for each feature.

Each card has a color to show how much resources in time it will roughly take. They also include colorblind feature mode. The colors are;

- Green (SMALL) 
    - 1-2 hours of effort:
- Orange (MEDIUM)
    - medium: 2-4 hours of effort
= Red (LARGE) 
    - large: 4-8 hours of effort

### Overview

![overview](./docs/overview.png)

### Create .json File 

![create](./docs/create_file.png)

### Feature #1 - Add plant to schedule 

![feature_1](./docs/feature_1.png)

### Feature #2 - Remove plant from schedule 

![feature_2](./docs/feature_2.png)

### Feature #3 - View plants that need watering

![feature_3](./docs/feature_3.png)

### Feature #4 - Mark plant as watered

![feature_4](./docs/feature_4.png)

### Feature #5 - View entire plant list 

![feature_5](./docs/feature_5.png)

### Feature #6 - Exit program

![feature_6](./docs/feature_6.png)

# Design Help Documentation 

