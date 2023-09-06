# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:48:30 2023

@author: dell1
"""

import numpy as np
import pickle
import streamlit as st
import tensorflow as tf

loaded_model = tf.keras.models.load_model('Model/ann.hdf5')
loadel_model_scaled=pickle.load(open('Model/trained_model_scaled.sav', 'rb'))

def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

def pred_fraud(input_data):
    input_data_flat = flat(input_data)
    input_data_array = np.asarray([input_data_flat])
    input_data_scaled = loadel_model_scaled.transform(input_data_array)
    input_data_reshape = input_data_scaled.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    
    if prediction[0] > 0.5:
        return 'The customer is fraud'
    else:
        return 'The customer is not fraud'
    
def main():
    st.title("Fraud Detection using Self Organized Map")
    st.header('Enter the following parameter:')
    
    A1 = st.selectbox('Select A1', (0,1))
    if A1 == '0':
        A1 = 0
    else:
        A1 = 1
    A2 = st.number_input('Enter A2')
    A3 = st.number_input('Enter A3')
    A4 = st.selectbox('Select A4', (1,2,3))
    if A4 =='1':
        A4 = [1,0,0]
    elif A4 == '2':
        A4 = [0,1,0]
    else:
        A4 = [0,0,1]
    A5 = st.selectbox('Select A5', (1,2,3,4,5,6,7,8,9,10,11,12,13,14))
    if A5 == '1':
        A5 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif A5 =='2':
        A5 = [0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif A5 =='3':
        A5 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif A5 =='4':
        A5 = [0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif A5 =='5':
        A5 = [0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif A5 =='6':
        A5 = [0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif A5 =='7':
        A5 = [0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif A5 =='8':
        A5 = [0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif A5 =='9':
        A5 = [0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif A5 =='10':
        A5 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    elif A5 =='11':
        A5 = [0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif A5 =='12':
        A5 = [0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif A5 =='13':
        A5 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    else:
        A5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    A6 = st.selectbox('Select A6', (1,2,3,4,5,7,8,9))
    if A6 == '1':
        A6 = [1,0,0,0,0,0,0,0]
    elif A6 =='2':
        A6 = [0,1,0,0,0,0,0,0]
    elif A6 =='3':
        A6 = [0,0,1,0,0,0,0,0]
    elif A6 =='4':
        A6 = [0,0,0,1,0,0,0,0]
    elif A6 =='5':
        A6 = [0,0,0,0,1,0,0,0]
    elif A6 =='7':
        A6 = [0,0,0,0,0,1,0,0]
    elif A6 =='8':
        A6 = [0,0,0,0,0,0,1,0]
    else:
        A6 = [0,0,0,0,0,0,0,1]
    A7 = st.number_input('Enter A7')
    A8 = st.selectbox('Select A8', (0,1))
    if A8 == '0':
        A8 = 0
    else:
        A8 = 1
    A9 = st.selectbox('Select A9', (0,1))
    if A9 == '0':
        A9 = 0
    else:
        A9 = 1
    A10 = st.number_input('Enter A10')
    A11 = st.selectbox('Select A11', (0,1))
    if A11 == '0':
        A11 = 0
    else:
        A11 = 1
    A12 = st.selectbox('Select A12', (1,2,3))
    if A12 =='1':
        A12 = [1,0,0]
    elif A12 == '2':
        A12 = [0,1,0]
    else:
        A12 = [0,0,1]
    A13 = st.number_input('Enter A13')
    A14 = st.number_input('Enter A14')
    
    
    pred = ' '
    if st.button("Predict"):
        pred = pred_fraud([A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14])
    st.success(pred)
    
if __name__=='__main__':
    main()