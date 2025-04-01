import streamlit as st

# Personalización del Streamlit
st.set_page_config(
    page_title="Skell's Tecnologys - Dashboard",
    layout="wide"
)

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem /* Reduce Espacio Superior
        }
    </style>
    """,unsafe_allow_html=True)

# Visualización / Esquematización de GUI (Colocar en orden según lo deseado)
# Titulo del Dashboard
st.markdown("# Skell's - Dashboard")

# Creación de Ventanas con nombres
pestaña1, pestaña2, pestaña3 = st.tabs(["Gestión de Clientes", "Horario de Actividad", "Gráficas de Datos"])

#Contenido de Cada Pestaña
with pestaña1:
    st.header("Gestion de Clientes")
    st.write("Registro de un nuevo cliente:")

with pestaña2:
    st.header("Horario de Actividad")
    st.write("Estadísticas de flujo de actividad según el horario:")

with pestaña3:
    st.header("Análsis Visual")
    st.write("Gráficas con todos los datos manejados")

