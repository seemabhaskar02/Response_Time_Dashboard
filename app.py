import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px       
#import seaborn as sns
import numpy as np    

st.set_page_config(layout="wide")

#st.title("Event Response time Analysis")
st.markdown("<h1 style='text-align: center; color: white;'>Event Response time Analysis</h1>", unsafe_allow_html=True)
st.sidebar.title("Event Response time Analysis")
df1=pd.read_csv("response_sep.csv")
df2=pd.read_csv("response_oct.csv")
df3=pd.read_csv("response_nov.csv")
df4=pd.read_csv("response_dec.csv")
@st.cache_data(persist=True)
def load_data():
    data = read_csv(df1)
    #data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data()        

#col1, col2 = st.columns(2)
col1, padding, col2 = st.columns((10,2,10))  



st.sidebar.markdown("### Select  Month to Display")     
select = st.sidebar.selectbox('Months', ['September', 'October', 'November', 'December'], key='1')


if select=="September":      #selection of september
    with col1:
    	df1.rename(columns = {'RT_of_112_Sytem_(sec)':'RT_of_112_Sytem_sec'}, inplace=True)
    	fig = px.histogram(df1, x="RT of 112 Sytem(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df1, x="RT of Vehicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df1, x="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig)
                     
    with col2:
    	df1.rename(columns = {'RT_of_112_Sytem_(sec)':'RT_of_112_Sytem_sec'}, inplace=True)
    	fig = px.box(df1, x="RT of 112 Sytem(sec)", height=400, width=500)
    	st.plotly_chart(fig) 
    	fig = px.box(df1, y="RT of Vehicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.box(df1, y="RT of CO(sec)",height=400, width=500)
    	st.plotly_chart(fig)     

    		 
    
elif select=="October":      #selection of october
    with col1:
    	df2=df2.dropna()  
    	fig = px.histogram(df2, x="RT of 112 Sytem (sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df2, y="RT of Veicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df2, y="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig)

    with col2:
    	fig = px.box(df2, y="RT of 112 Sytem (sec)", height=400, width=500)
    	st.plotly_chart(fig) 
    	fig = px.box(df2, y="RT of Veicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.box(df2, y="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig)  
     
elif select=="November":      #selection of november
    with col1:
    	df3=df3.dropna()  
    	fig = px.histogram(df3, y="RT of 112 Sytem (sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df3, y="RT of Vehicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df3, y="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig)

    with col2:
    	fig = px.box(df3,y="RT of 112 Sytem (sec)", height=400, width=500)
    	st.plotly_chart(fig) 
    	fig = px.box(df3, y="RT of Vehicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.box(df3, y="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig) 

     
else:
    with col1:      #selection of december
    	df4=df4.dropna()  
    	fig = px.histogram(df4, y="RT of 112 Sytem(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df4,y="RT of Vehicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.histogram(df4,  y="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig)

    with col2:
    	fig = px.box(df4,y="RT of 112 Sytem(sec)", height=400, width=500)
    	st.plotly_chart(fig) 
    	fig = px.box(df4, y="RT of Vehicle(sec)", height=400, width=500)
    	st.plotly_chart(fig)
    	fig = px.box(df4, y="RT of CO(sec)", height=400, width=500)
    	st.plotly_chart(fig) 
	   














