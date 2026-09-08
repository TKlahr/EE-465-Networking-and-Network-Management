#!/bin/bash

echo "Please enter your name:"    # Ask user for name
read name    # store input in name

echo "Hello, $name! How old are you?"    # Ask user for age
read age    # Store input in age

currentyear=$(date +%Y)    # Displays just the year of current date on the system. Y=4, y=2
yearsleft=$((100-age))    # Calculates how many years until user is 100
hundredyear=$((currentyear + yearsleft))    # Calculates what year the user will turn 100

echo "$name, you will be 100 years old in the year $hundredyear."    # Tells the user what year they will turn 100
