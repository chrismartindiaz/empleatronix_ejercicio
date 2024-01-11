import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('EMPLEATRONIX')

st.write('Todos los datos sobre los empleados en una aplicación.')

data = pd.read_csv('data/employees.csv')

st.write(data)

st.divider()
# Establecemos las columnas para los selectores
col1, col2, col3 = st.columns(3)
with col1:
    color = st.color_picker('Elige un color para las barras', '#3475B3')

with col2:
    names = st.toggle('Mostrar el nombre', value=True)

with col3:
    salaries = st.toggle('Mostrar sueldo en la barra')

# Creamos la figura y sus respectivos ejes
fig, ax = plt.subplots(figsize=(8, 6))

# Continuamos con la gráfica que en este caso es de Barras Horizontales
bars = ax.barh(data['full name'], data['salary'], color=color)
plt.xticks(rotation=90)
ax.set_xlim(0, 4500)

# Establecemos los parámetros de condición para los toggle
if not names:
    ax.set_yticks([])  # Anulamos las etiquetas

ax.yaxis.grid(False) 
ax.xaxis.grid(False) 

if salaries:
    plt.bar_label(bars, fmt='%d€', padding=4)

# Mostrar el gráfico
st.pyplot(fig)

st.write('Autor original: © Luis José Sánchez - CPIFP Alan Turing')
