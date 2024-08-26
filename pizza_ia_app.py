# Inicio

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Calculando o valor da Pizza")
st.divider()

diametro = st.number_input("Escolha o tamanho da Pizza: ")

if diametro:
    preco_precisto = modelo.predict([[diametro]])[0][0]
    st.write(f"Ovalor da pizza comm diametro de {diametro:.2f} cm é de R$ {preco_precisto:.2f}")
    
    st.balloons()

# Fim