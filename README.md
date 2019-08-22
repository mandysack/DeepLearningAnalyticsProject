# DeepLearningAnalyticsProject
Introduction project for Deep Learning Analytics

The goal of this project is to use a twitter dataset to determine if the an account is a bot or not. 

The dataset used is caverlee-2011 from the website https://botometer.iuni.iu.edu/bot-repository/datasets.html 
Reference: Lee, Kyumin, Brian David Eoff, and James Caverlee. "Seven Months with the Devils: A Long-Term Study of Content Polluters on Twitter." ICWSM. 2011.

Here's the breakdown of the data:

Attribute Information:
The data has already seperated data by bot, referred to as a "Content Polluter", and a not bot referred to as a "Legitimate User".

There has been a column added to both datasets labeled "Bad User" to identify this attribute prior to merging the datasets.

Bad User:
1 - Content Polluter
0 - Legitimate User

8 Features:
UserID
CreatedAt
CollectedAt
NumberOfFollowings
NumberOfFollowers
NumberOfTweets
LengthOfScreenName
LengthOfDescriptionInUserProfile