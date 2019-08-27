#!/usr/bin/env python
# coding: utf-8

# # Deep Learning Project

# Developed by: Mandy Sack
# August 2019
# 

# In[1]:


import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import sklearn
import sys
import tensorflow as tf
from sklearn.model_selection import train_test_split


# In[2]:


# import the data
# first, verify you have the files in the correct location
print(os.path.isdir("data"))
dataDir = "data/"

print(os.path.isfile("data/content_polluters.csv"))
print(os.path.isfile("data/legitimate_users.csv"))

bDcolnames=['UserID','CreatedAt','CollectedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets','LengthOfScreenName','LengthOfDescriptionInUserProfile','BadUser'] 
badData = pd.read_csv(dataDir+"content_polluters.csv", names=bDcolnames)

nDcolnames=['UserID','CreatedAt','CollectedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets','LengthOfScreenName','LengthOfDescriptionInUserProfile','BadUser']
normalData = pd.read_csv(dataDir+"legitimate_users.csv", names=nDcolnames)

#TODO: make this configurable to enable your own data to be passed in 


# In[3]:


print(badData.head(3))
print(normalData.head(3))


# In[4]:


# merge the data together based on CollectedAt colum & save to file
mergedData = pd.concat([badData,normalData])
mergedData.sort_values(by=['CollectedAt'], inplace=True)
mergedData.to_csv(dataDir+"mergedData_classified.csv")
mergedData


# In[5]:


# Remove nonnumeric columns
mergedData.drop("CreatedAt", axis=1, inplace=True)
mergedData.drop("CollectedAt", axis=1, inplace=True)
mergedData.drop("UserID", axis=1, inplace=True)
mergedData.head(3)


# In[6]:


column_names = list(mergedData.columns)
# features are the attributes of the data 
features = column_names[:-1]
# label is to be predicted
labels = column_names[-1] 


# In[7]:


# The data needs to be split into a training set and a test set
# To use 80/20, set the training size to .8
training_set_size_portion = .8

# Keep track of the accuracy score
accuracy_score = 0

# The DNN has hidden units, set the spec for them here
hidden_units_spec = [10,20,10]
n_classes_spec = 2

# Define the temp directory for keeping the model and checkpoints
tmp_dir_spec = "data/model"

# The number of training steps
steps_spec = 100

# The number of epochs
epochs_spec = 5
#1500 got essentially the same amount but took exponentially longer


# In[8]:


# Randomize dataset & save to file
randomized_data = mergedData.sample(frac=1)
mergedData.to_csv(dataDir+"trainingData_classified.csv")


# In[9]:


total_records = len(randomized_data)
training_set_size = int(total_records * training_set_size_portion)
test_set_size = total_records = training_set_size


# In[10]:


# Build the training features and labels
training_features = randomized_data.head(training_set_size)[features].copy()
training_labels = randomized_data.head(training_set_size)[labels].copy()
print(training_features.head())
print(training_labels.head())


# In[11]:


# Build the testing features and labels
testing_features = randomized_data.tail(test_set_size)[features].copy()
testing_labels = randomized_data.tail(test_set_size)[labels].copy()


# In[12]:


feature_columns = [tf.feature_column.numeric_column(key) for key in features]


# In[13]:


classifier = tf.estimator.DNNClassifier( feature_columns=feature_columns, hidden_units=hidden_units_spec,  n_classes=n_classes_spec, model_dir=tmp_dir_spec)


# In[14]:


# Define the training input function
train_input_fn = tf.estimator.inputs.pandas_input_fn( x=training_features, y=training_labels, num_epochs=epochs_spec, shuffle=True)


# In[15]:


# Train the model using the classifer.
classifier.train(input_fn=train_input_fn, steps=steps_spec)


# In[16]:


# Define the test input function
test_input_fn = tf.estimator.inputs.pandas_input_fn( x=testing_features, y=testing_labels, num_epochs=epochs_spec, shuffle=False)


# In[17]:


# Evaluate accuracy
accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
print("Accuracy = {}".format(accuracy_score))


# In[18]:


# Create a prediction set --
# this is a list of input features that you want to classify
# Using a "known" Bad User to see if it classifies correctly
prediction_set = pd.DataFrame({'NumberOfFollowings':[12848], 'NumberOfFollowers':[12933], 'NumberOfTweets':[2315],'LengthOfScreenName':[5],'LengthOfDescriptionInUserProfile':[63]})


# In[19]:


predict_input_fn = tf.estimator.inputs.pandas_input_fn( x=prediction_set, num_epochs=1, shuffle=False)


# In[20]:


# Get a list of the predictions
predictions = list(classifier.predict(input_fn=predict_input_fn))


# In[21]:


predicted_classes = [p["classes"] for p in predictions] 
results=np.concatenate(predicted_classes) 
print(results)

