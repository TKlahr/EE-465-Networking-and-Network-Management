#!/bin/bash

score=0    # Starts score at 0

echo "Question 1: What is 2*2?" # Ask question 1
read answer    # Store user input

if [ "$answer" = "4" ]; then    # Check if user has correct answer
    echo "Correct!"
    score=$((score + 1))    # Add 1 to score because user is correct
else
    echo "Wrong! The correct answer is 4."    # User is wrong and tell them correct answer
fi    # Close if statement
