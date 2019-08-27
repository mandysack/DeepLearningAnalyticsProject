# DeepLearningAnalyticsProject
Introduction project for Deep Learning Analytics <br>
Mandy Sack 2019<br>

# Objectives

The goal of this project is to use a twitter dataset to determine if the an account is a bot or not. 

# Information on the data:
The dataset used is caverlee-2011 from the website https://botometer.iuni.iu.edu/bot-repository/datasets.html <br>
Reference: Lee, Kyumin, Brian David Eoff, and James Caverlee. "Seven Months with the Devils: A Long-Term Study of Content Polluters on Twitter." ICWSM. 2011.

# Attribute Information:
The data has already seperated data by bot, referred to as a "Content Polluter", and a not bot referred to as a "Legitimate User".

There has been a column added to the datasets labeled "Bad User" to identify this attribute prior to merging the datasets.

Bad User:
1 - Content Polluter
0 - Legitimate User

# 5 Features:
NumberOfFollowings <br>
NumberOfFollowers <br>
NumberOfTweets <br>
LengthOfScreenName <br>
LengthOfDescriptionInUserProfile <br>

3 non-numeric features we're removed during the data cleasing as they did not provide information that would assist in proper classification <br>
UserID <br>
CreatedAt <br>
CollectedAt <br>

# Environment Setup For Running Experiment

You will need python3 & anaconda to run this experiment. If you are going to run this without a GPU then you will want to modify the notebooks to only import tensorflow instead of tensorflow-gpu <br>

Create an anaconda environment using the following commands: <br>
$ conda create -n dla python=3.6 tensorflow-gpu numpy matplotlib pandas scipy  <br>
$ conda activate dla <br>

# Files Included In This Package:
README.md - This file <br>
Deep Learning Project.ipynb - Notebook that will run the DLA project <br>
DataExploration.ipynb - Notebook that shows some of the commands used for exploring the dataset <br>
data/content_polluters_classified.csv - Provides content polluters twitter account information and is classified as a Bad User  <br>
data/legitimate_users_classified.csv - Provides legitimate users twitter account information and is classified as a Non-Bad User <br>
data/mergedData_classified.csv - Provides both content polluters & legitimate users twitter account information sorted by the CollectedAt column  <br>
data/trainingData_classified.csv - Provides the mergedData that has removed the 3 non-numerical columns as well as randomized for training purposes <br>
docs/social_honeypot_icwsm_2011.pdf - Documentation regarding the data <br>
docs/SevenMonthswiththeDevilsStudy.pdf - White paper that used the Twitter data <br>

