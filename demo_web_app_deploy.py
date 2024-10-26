import pandas as pd
import numpy as np
from PIL import Image
import pickle
import streamlit as st

# from modelo_regressao_linear_brasil import RegressaoLinearBRC

#Indicando sidebar
st.markdown('*__Observação: para mais informações acerca do projeto, clique na seta no canto esquerdo superior da tela__* ')

#Indicando do que se trata a web app
# foto = Image.open('bruno.carloto (2).png')
# st.sidebar.image(foto, use_column_width=True)
st.sidebar.subheader('Bruno Rodrigues Carloto')
st.sidebar.markdown('Profissional de Analytics')
st.sidebar.markdown('#### Desenvolvimento de Algoritmo de Regressão Linear')
st.sidebar.markdown('''Leia o [notebook de validação do algoritmo](https://github.com/bruno-rodrigues-carloto/Regressao-Linear-Brasil/blob/main/Valida%C3%A7%C3%A3o%20do%20algoritmo%20RegressaoLinearBRC.ipynb).''')
# pag = st.sidebar.selectbox('Selecione a página', ['Interagir com a inteligência', 'Dashboard da base de dados do projeto'])

st.sidebar.markdown('Feito por : Bruno Rodrigues Carloto')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://medium.com/@brc-deep-analytics)")
st.sidebar.markdown("- [Mercadados](https://brunnocarlotosjob.wixsite.com/mercadados)")
    
st.header('Regressão Linear BRC')
st.subheader('Olá! Eu sou um algoritmo de regressão liinear desenvolvido em língua portuguesa')
st.markdown(' ')
usuario =  st.text_input('Gostaria de saber seu nome.')
st.markdown(' ')
st.markdown('Aqui temos um experimento em que presumo o preço do arroz com base no preço do feijão.')

preco_feijao = st.number_input(f'{usuario}, defina o preço do feijão para que eu estime o preço do arroz.')

# RegressãoLinear
# with open('Modelo_RegressaoLinearBRC.pkl', 'rb') as f:
  #  modelo_carregado = pickle.load(f)
        
X = preco_feijao
y = 5.564934583749978 + 0.9174417727028592 * X
# y = modelo_carregado.predizer(X)
y_ajustado = float(np.round(y, 2))

#Aplicando a inteligência
st.subheader('Resultado')
st.markdown(f'{usuario}, a {preco_feijao} reais, o preço do arroz é estimado em {y_ajustado} reais.')
