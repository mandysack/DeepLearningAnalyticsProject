# DeepLearningAnalyticsProject
Introduction project for Deep Learning Analytics
Mandy Sack 2019

# Objectives

The goal of this project is to use a twitter dataset to determine if the an account is a bot or not. 

# Information on the data:
The dataset used is caverlee-2011 from the website https://botometer.iuni.iu.edu/bot-repository/datasets.html 
Reference: Lee, Kyumin, Brian David Eoff, and James Caverlee. "Seven Months with the Devils: A Long-Term Study of Content Polluters on Twitter." ICWSM. 2011.

# Attribute Information:
The data has already seperated data by bot, referred to as a "Content Polluter", and a not bot referred to as a "Legitimate User".

There has been a column added to the datasets labeled "Bad User" to identify this attribute prior to merging the datasets.

Bad User:
1 - Content Polluter
0 - Legitimate User

# 5 Features:
NumberOfFollowings
NumberOfFollowers
NumberOfTweets
LengthOfScreenName
LengthOfDescriptionInUserProfile

3 non-numeric features we're removed during the data cleasing as they did not provide information that would assist in proper classification
UserID
CreatedAt
CollectedAt

# Environment Setup For Running Experiment

You will need python3 & anaconda to run this experiment. If you are going to run this without a GPU then you will want to modify the notebooks to only import tensorflow instead of tensorflow-gpu

Create an anaconda environment using the following commands:
$ conda create -n dla python=3.6 tensorflow-gpu numpy matplotlib pandas scipy 
$ conda activate dla

# Files Included In This Package:
README.md - This file
Deep Learning Project.ipynb - Notebook that will run the DLA project
DataExploration.ipynb - Notebook that shows some of the commands used for exploring the dataset
data/content_polluters_classified.csv - Provides content polluters twitter account information and is classified as a Bad User 
data/legitimate_users_classified.csv - Provides legitimate users twitter account information and is classified as a Non-Bad User
data/mergedData_classified.csv - Provides both content polluters & legitimate users twitter account information sorted by the CollectedAt column 
data/trainingData_classified.csv - Provides the mergedData that has removed the 3 non-numerical columns as well as randomized for training purposes
docs/social_honeypot_icwsm_2011.pdf - Documentation regarding the data
docs/SevenMonthswiththeDevilsStudy.pdf - White paper that used the Twitter data

