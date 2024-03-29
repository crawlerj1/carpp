import streamlit as st
import pickle
import path
import sys
import numpy as np
import pandas as pd
import sklearn
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# load model
path_to_model = 'carmodel1.pkl'
model2='carinfo1.pkl'
model = pickle.load(open(path_to_model,'rb'))

car_list = pickle.load(open(model2, 'rb'))
car_list2= pd.DataFrame(car_list)


st.title('Car Price Predictor')
st.sidebar.header('Cars Data')
def filter_models(selected_company):
    if selected_company:
        models = car_list2[car_list2['CN'] == selected_company]['N'].unique().tolist()
        return models
    return []
def filter_year(N):
    if N:
        year = car_list2[car_list2['N'] == N]['Y'].unique().tolist()
        return year
    return []
def filter_fuel(N):
    if N:
        fueltype = car_list2[car_list2['N'] == N]['FT'].unique().tolist()
        return fueltype
    return []


def cardata():
    selected_company = st.sidebar.selectbox('Select CompanyName', car_list2['CN'].unique())
    N = st.sidebar.selectbox('Select The Car Model', filter_models(selected_company))

    FT = st.sidebar.selectbox('Fuel Type', filter_fuel(N))

    Y = st.sidebar.selectbox('Year Model', filter_year(N))

    KMD = st.sidebar.slider('Kilometres Driven', 10000, 400000, 10000)

    datafromuser={
    'N': N,
    'CN': selected_company,
    'Y': Y,
    'KMD': KMD,
    'FT': FT,
    }
    got_data = pd.DataFrame(datafromuser, index=[1])
    return got_data


car_data = cardata()
st.header('Used Car Data')
st.write(car_data)
price = model.predict(car_data)

if st.button('Click Here To See The Price'):
    if price>=0:
      st.header('Rs.'+str(price)[1:10])
    else:
      st.header("Not Available")
