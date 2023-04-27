# Project Documentation

Written by Jeevan Ng

# Source Control Repository 

# Code Style Guide 

# List of Features

This terminal application will allow a user to create their own plant watering schedule for three different frequencies; weekly, fortnightly and monthly. 

It will use file handling to create a json file which will hold information that the user enters. Python will read and write this file as information is updated.

## Feature #1 

This feature will allow the user to add information to the schedule. This feature will take the following data as input from the user; 

- Name of plant 
- Frequency of watering (weekly, fortnightly or monthly) 
- When the plant was last watered (days)
- Amount of water needed

Error handling will be used to ensure that the user will not be able to enter anything other than what is desired by the application. E.g. Data type of integer for "When the plant was last watered (days)"

## Feature 2 

The user will be able to remove a plant from the schedule. It will get an input from the user and ask them to type which plant they wish to remove. 

e.g
```python
remove_plant = input("Please type which plant you wish to remove from the schedule: ")
``` 

## Feature 3 
View which plants need watering today. 

This feature will display the current day using the built-in datetime library in Python and list which plants need to be watered.

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

## Feature 4

Mark plant as watered. This feature will enable the user to let the program know which plant has been watered so that it does not show up as needing watering until required.

This feature will reset the variable "When was the plant last watered (days)", and assign it a new date which will be equal to the date they marked as watered. 

This means that if the user misses a watering one of their plants for a couple of days, whenever they mark as watered, it will then take the weekly, fortnightly or monthly schedule from that date. This is much better logic than assigning plants to be watered on a certain day, and printing out the list according to that day. 

For example, if a user assigns a plant to the schedule that needs to be watered every week. If they forgot to water their plant for 3 days, and then mark as complete. If we assigned it a weekday, it would show as needing to be watered 4 days later. However, if we assign the date/time, whenever they mark it as complete, it will then show up as being watered 7 days later. One week. 

## Feature 5
This feature will allow the user to view the entire list of plants they have added to the schedule and show when they were all last watered. 

## Feature 6
This feature will allow the user to exit the program. 

```python
print("Exiting program. Thank you.")
```

# Implementation Plan

Trello 

# Design Help Documentation 

