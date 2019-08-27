# DeepLearningAnalyticsProject
Introduction project for Deep Learning Analytics
Mandy Sack 2019

# Objectives

The goal of this project is to use a twitter dataset to determine if the an account is a bot or not. 

1) Can we properly identify as a "bot" or "not"?
2) Stretch objective if time allows: Can we create a "bot", and have it properly classified given the datasets?


# Information on the data:
The dataset used is caverlee-2011 from the website https://botometer.iuni.iu.edu/bot-repository/datasets.html 
Reference: Lee, Kyumin, Brian David Eoff, and James Caverlee. "Seven Months with the Devils: A Long-Term Study of Content Polluters on Twitter." ICWSM. 2011.

# Attribute Information:
The data has already seperated data by bot, referred to as a "Content Polluter", and a not bot referred to as a "Legitimate User".

There has been a column added to both datasets labeled "Bad User" to identify this attribute prior to merging the datasets.

Bad User:
1 - Content Polluter
0 - Legitimate User

# 8 Features:
UserID
CreatedAt
CollectedAt
NumberOfFollowings
NumberOfFollowers
NumberOfTweets
LengthOfScreenName
LengthOfDescriptionInUserProfile

# Environment Setup
Create an anaconda environment using the following commands:
conda create -n dla python=3.6 tensorflow-gpu numpy matplotlib pandas scipy
conda activate dla
