import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
sns.set_style('darkgrid')


st.set_page_config(page_title = 'Big Data Inmobiliario', page_icon = 'Favicom BDI.png', layout = 'wide')

st.title('TOTAL_BILL @ US RESTAURANTS')


#INPUT

df = sns.load_dataset('tips')

with st.sidebar:
    

	st.image('BIG DATA Inmobiliario Logo white HR.png') 

	seleccion_sexo = st.selectbox('Elige sexo:',['Male','Female'])

	seleccion_fumador = st.radio('Elige fumador:',['Yes','No'])

	slider_total_cuenta = st.slider('Cuenta mayor que: ', 	df.total_bill.min(), df.total_bill.max())


#CALCULOS

datos = df.loc[(df.sex == seleccion_sexo) & 
                      (df.smoker == seleccion_fumador) & 
                      (df.total_bill > slider_total_cuenta)].copy()

ticket_medio = round(datos.total_bill.mean(),2)


#OUTPUT

fig, ax = plt.subplots()

ax = sns.histplot(data = datos, x = 'total_bill', alpha = 0.3)

col1,col2 = st.columns(2)

col1.metric('Ticket Medio',ticket_medio)

col2.pyplot(fig)
