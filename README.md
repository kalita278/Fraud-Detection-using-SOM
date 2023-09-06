# Fraud-Detection-using-SOM


**DATA CLEANING:**

Created a single file with all the relevant variables and perform the necessary data quality checks and cleaning. In data cleaning, checked for the missing values/unexpected values in the dataset and there is no missing value in the dataset. Make sure that the data types of the variables are appropriate as required for our analysis (Here, converted all the categorical variable data types to category and continuous variable data types to int or float).


**DATA PREPROCESSING:**

Here, scaled the variable using MinMax scaler.

**SOM:**

Trained the som using minisom library and visualize the result to findout the outlier, i.e the the customer who have done fraud.


**HYBRID MODEL TO PREDICT FRAUD:**

Here build an ANN model with 2 hiddenlayer which can predict the fraud customer.

**MODEL DEPLOYMENT:**

Created a web app using pickle (used to save and load the model) and streamlit (used o create the web app) to predict the fraud customer. (refer to "fraud detection web app.py" file)
