import streamlit as st
import pandas as pd
import datetime

# Simula una base de datos en memoria con pandas
if 'db' not in st.session_state:
    st.session_state.db = pd.DataFrame(columns=["Fecha", "Nombre", "Edad", "Diagnóstico", "Cirugía", "Cirujano", "Sala", "Tipo", "Material Extra", "Material Disponible"])

# Título y logos
col1, col2 = st.columns([0.5, 2])
col1.image("https://github.com/PercyCruzMD/pruebas/blob/main/images/Gea2.png")  # Asegúrate de que la ruta a la imagen es correcta
col2.title("Programación quirúrgica - GEA")

# Mostrar la tabla de pacientes
st.write("Programación de cirugías")
st.dataframe(st.session_state.db.reset_index(drop=True))

# Función para agregar pacientes a la "base de datos"

def add_patient(nombre, edad, diagnostico, cirugia, fecha, cirujano, sala, tipo, material_extra, disp_material):
    # Crear un nuevo DataFrame con los datos del paciente
    new_patient = pd.DataFrame({
        'Nombre': [nombre],
        'Edad': [edad],
        'Diagnóstico': [diagnostico],
        'Cirugía programada': [cirugia],
        'Fecha de la cirugía': [fecha],
        'Cirujano': [cirujano],
        'Sala': [sala],
        'Tipo de paciente': [tipo],
        '¿Requiere material adicional?': [material_extra],
        'Material adicional disponible?': [disp_material]
    })

    # Añadir el nuevo paciente a la base de datos
    st.session_state.db = pd.concat([st.session_state.db, new_patient], ignore_index=True)

# Formulario para añadir pacientes

with st.expander("Añadir Paciente"):
    with st.form("my_form", clear_on_submit=True):
        nombre = st.text_input("Nombre del paciente")
        edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
        diagnostico = st.text_input("Diagnóstico")
        cirugia = st.text_input("Cirugía programada")
        fecha = st.date_input("Fecha de la cirugía")
        cirujano = st.text_input("Cirujano")
        sala = st.text_input("Sala")

        col1, col2, col3 = st.columns(3)
        tipo = col1.radio("Tipo de paciente", ("Hospitalizado", "Ambulatorio"))
        material_extra = col2.radio("¿Requiere material adicional?", ("Sí", "No"))
        disp_material = col3.radio("Material adicional disponible?", ("Sí", "No"))

        # Botón de envío
        submitted = st.form_submit_button("Añadir Paciente")

        if submitted:
            add_patient(nombre, edad, diagnostico, cirugia, fecha, cirujano, sala, tipo, material_extra == 'Sí', disp_material == 'Sí')
