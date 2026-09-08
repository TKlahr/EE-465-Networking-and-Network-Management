#!/bin/bash

score=0    # Starts score at 0
#----------
echo "Question 1: What is 2*2?" # Ask question 1
read answer    # Store user input

if [ "$answer" = "4" ]; then    # Check if user has correct answer
    echo "Correct!"
    score=$((score + 1))    # Add 1 to score because user is correct
else
    echo "Wrong! The correct answer is 4."    # User is wrong and tell them correct answer
fi    # Close if statement
#----------
echo "Question 2: What is 2^2?" # Ask question 2
read answer    # New input overrides old input

if [ "$answer" = "4" ]; then    # Check if user has correct answer
    echo "Correct!"
    score=$((score + 1))    # Add 1 to score because user is correct
else
    echo "Wrong! The correct answer is 4."    # User is wrong and tell them correct answer
fi    # Close if statement
#-----------
echo "Question 3: What is 2!?" # Ask question 3
read answer    # New input overrides old input

if [ "$answer" = "2" ]; then    # Check if user has correct answer
    echo "Correct!"
    score=$((score + 1))    # Add 1 to score because user is correct
else
    echo "Wrong! The correct answer is 2."    # User is wrong and tell them correct answer
fi    # Close if statement
#----------
quizdate=$(date)
echo "You took this quiz on $quizdate."
echo "Your score is $score our of 3."
