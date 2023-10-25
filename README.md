# Falcon9-launch-DS
Predicting if the Falcon 9 first stage will land successfully

# IBM Data Science Capstone Project - SpaceX

## Introduction

In this capstone, we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website, with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch. 

This capstone project course will give you a taste of what data scientists go through in real life when working with real datasets. You will assume the role of a Data Scientist working for a startup intending to compete with SpaceX, and in the process follow the Data Science methodology involving [data collection](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/Data%20Collection%20API.ipynb), [data wrangling](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/Data%20Wrangling.ipynb), [exploratory data analysis](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/EDA%20with%20SQL.ipynb), [data visualization](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/EDA%20with%20Data%20Visualization.ipynb), [model development](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/Machine%20Learning%20Prediction.ipynb), [model evaluation](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/Machine%20Learning%20Prediction.ipynb), and [reporting](https://github.com/chuksoo/IBM-Data-Science-Capstone-SpaceX/blob/main/Winning%20Space%20Race%20with%20Data%20Science.pdf) your results to stakeholders. You are tasked with predicting if the first stage of the SpaceX Falcon 9 rocket will land successfully. 
##Falcon 9 Launch Dataset
This dataset contains details on Falcon 9 launches conducted by SpaceX from 2010 to 2022. It includes over 100 launches with information such as launch dates, sites, outcomes, and payload data.

###Data
The data is provided as a CSV file with the following columns:

FlightNumber - Official SpaceX flight number for the mission
LaunchDate - Date of launch in mm/dd/yyyy format
LaunchSite - Launch site name (CCAFS, VAFB, KSC, STLS)
Payload - Payload name(s)
PayloadType - Payload type (Satellite, Dragon, Starlink, etc)
PayloadMass - Payload mass in kg
Orbit - Orbit name (LEO, GTO, ISS, etc)
Customer - Customer name(s)
LaunchOutcome - Launch outcome (Success, Failure, etc)
There are some issues with missing values and inconsistencies which need to be addressed. Please refer to the Issues section.

###Usage
This dataset can be used for visualizing launch trends over time, analyzing launch sites statistics, predicting payload mass for different orbits, and more.

Potential analyses:

Plots of launch frequency per year, launch outcomes over time
Summary tables of launch sites, payload types, customers
Payload mass regression model based on orbit type
Launch success rates by site and payload type

###Issues
Some known issues with the data:
Missing values need to be filled in for some columns
Some flight numbers, dates, outcomes need verification
Payload mass units need consistency checking
Additional metadata like booster versions would add value
Feel free to open issues or PRs to discuss fixes and enhancements for the dataset.

## Business Problem
SpaceX advertises Falcon 9 rocket launches on its website, with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if you can accurately predict the likelihood of the first stage rocket landing successfully, you can determine the cost of a launch. With the help of your Data Science findings and models, the competing startup you have been hired by can make more informed bids against SpaceX for a rocket launch. 

## Objective
- To apply data science toolkit and machine learning in order to accurately predict the likelihood of the first stage rocket landing successfully, and thus determine the cost of a launch.
- Explore the data in order to obtain more insight from the data.

## Business metric
Classification accuracy - number of correct prediction divided by the total number of prediction defined as:
$$Accuracy = \frac{TP+TN}{TP+FP+TN+FN}$$

## Deliverables
- Accurate predictive algorithms
- Business case report to stakeholders


![SpaceX Launch Records Dashboard](https://github.com/axiom19/Falcon9-launch-DS/blob/b9b2c26c35a1273d6a59b9136d95ea9255335390/Dash%20App%201.png)
<br>
![SpaceX Launch Records Dashboard 2](https://github.com/axiom19/Falcon9-launch-DS/blob/b9b2c26c35a1273d6a59b9136d95ea9255335390/Dash%20App2.png)

