import streamlit as st
import sqlite3 as sql
import pandas as pd

# funciones reutilizables
def agregar_cliente(nombre, cedula, email, telefono, ultima_compra):
    consultaSQL.execute('''
        INSERT INTO clientes (nombre, cedula, email, telefono, lastCompra)
        VALUES (?, ?, ?, ?, ?)
    ''', (str(nombre), int(cedula), str(email), int(telefono), str(ultima_compra)))
    conectorSQL.commit()

def consultar_datos():
    consultaSQL.execute("SELECT * FROM clientes")
    return(consultaSQL.fetchall())

def eliminar_registro(id):
    consultaSQL.execute("DELETE FROM clientes WHERE id = ?", (id))
    conectorSQL.commit()

# Herramientas para manejo de SQL
conectorSQL = sql.connect("Python/base_datos.db")
consultaSQL = conectorSQL.cursor()
try:
    consultaSQL.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cedula INTEGER UNSIGNED NOT NULL,
            email TEXT,
            telefono INT UNSIGNED,
            lastCompra DATE NOT NULL
        )
    ''')
    conectorSQL.commit()
except ValueError:
    print(ValueError)

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
pestaña1, pestaña2, pestaña3, pestaña4 = st.tabs(["Agregar Clientes", "Gestión de Clientes", "Horario de Actividad", "Gráficas de Datos"])

#Contenido de Cada Pestaña
with pestaña1:
    st.header("Agregar Clientes")
    with st.form(key="registrar_cliente"):
        nombre = st.text_input("Nombre Completo *", key='nombre')
        cedula = st.text_input("Cédula del Cliente *", key='cedula')
        email = st.text_input("Email del Cliente", key='email')
        telefono = st.text_input("Teléfono del Cliente *", key='telefono')
        compra = st.date_input("Fecha de Ultima compra", key='today')
        submit = st.form_submit_button("Registrar Cliente")
        if submit:
            if not nombre or not cedula or not telefono:
                st.error("Ingrese todos los campos (*).")
            else:
                st.success(f"Cliente {nombre} registrado exitosamente")
                consultar_datos()
                agregar_cliente(nombre, cedula, email, telefono, compra)
                consultar_datos()

with pestaña2:
    # Visualizador de clientes
    listaClientes = pd.DataFrame(
        consultar_datos(),
        columns=["ID", "Nombre", "Cédula", "Email", "Teléfono", "Ultima Compra"]
    )
    # Datos esteticamente mostrados
    st.title("Listado de Clientes Registrados")
    actualizarLista = st.button("Actualizar la Lista")
    listado = st.dataframe(listaClientes, hide_index=True, use_container_width=True)
    st.header("Eliminar Cliente del Registro")
    if actualizarLista:
        st.rerun()
    with st.form("eliminar_registro"):
        id_cliente = st.text_input("ID del Cliente")
        submit_eliminar = st.form_submit_button("Eliminar Registro")
        if submit_eliminar:
            try:
                id_cliente = int(id_cliente)
                if not id_cliente:
                    st.error("Ingrese un ID de Cliente.")
                else:
                    try:
                        eliminar_registro(str(id_cliente))
                        st.success(f"Cliente de ID {id_cliente} Eliminado.")
                    except ValueError:
                        st.write(ValueError)
            except ValueError:
                st.error("Ingrese un ID válido")

with pestaña3:
    st.header("Horario de Actividad")
    st.write("Estadísticas de flujo de actividad según el horario:")

with pestaña4:
    st.header("Análsis Visual")
    st.write("Gráficas con todos los datos manejados")