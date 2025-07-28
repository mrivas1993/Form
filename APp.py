import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Planificación Semanal", layout="wide")

st.title("📅 Planificación Semanal de Labores Agrícolas")

# Diccionario de lotes y áreas
lotes_areas = {
    'B10': 27.0, 'B11': 13.6, 'B12': 13.9, 'B13': 15.3, 'B8': 35.2, 'B9': 40.1,
    'C10': 26.1, 'C11': 23.0, 'C12': 17.7, 'C5': 7.3, 'C6': 4.8, 'C7': 6.2, 'C8': 24.5, 'C9': 19.3,
    'D10': 25.4, 'D11': 14.0, 'D5': 18.8, 'D6': 16.8, 'D7': 11.1, 'D7A': 9.5, 'D8': 26.1, 'D9': 20.0,
    'E10': 3.9, 'E5': 29.1, 'E6': 23.9, 'E7': 27.4, 'E8': 21.8, 'E9': 18.9, 'E9A': 5.6,
    'F10': 1.8, 'F5': 23.6, 'F6': 25.9, 'F7': 16.2, 'F7A': 13.0, 'F8': 26.6, 'F9': 27.3,
    'G10': 7.9, 'G16': 3.1, 'G17': 1.9, 'G18': 1.3, 'G5': 33.5, 'G6': 25.4, 'G7': 23.4, 'G8': 3.7, 'G8A': 7.6, 'G9': 7.5,
    'H10': 9.4, 'H11': 12.0, 'H12': 15.4, 'H13': 3.7, 'H14': 12.6, 'H15': 24.7, 'H16': 22.8, 'H17': 20.2, 'H18': 19.8, 'H19': 6.8,
    'H4': 0.0, 'H5': 14.4, 'H6': 22.3, 'H7': 31.0, 'H8': 12.5, 'H9': 9.6,
    'I10': 20.8, 'I11': 30.0, 'I12': 29.3, 'I13': 23.2, 'I14': 25.0, 'I15': 24.6, 'I16': 25.1, 'I17': 24.7, 'I18': 22.2, 'I19': 23.8,
    'I20': 12.7, 'I21': 10.9, 'I7': 8.8, 'I8': 22.6, 'I9': 17.7,
    'J11': 6.4, 'J12': 26.7, 'J13': 15.2, 'J14': 15.6, 'J15': 13.1, 'J16': 8.6, 'J17': 13.5, 'J18': 13.2, 'J19': 24.5, 'J20': 20.1, 'J21': 21.5, 'J22': 10.4,
    'K11': 4.8, 'K12': 13.9, 'K13': 19.9, 'K14': 10.9, 'K18': 0.0, 'K19': 11.0, 'K20': 3.1, 'K21': 7.6, 'K22': 3.1,
    'L10': 16.4, 'L11': 18.9, 'L12': 23.6, 'L13': 24.8, 'L14': 22.3,
    'M13': 6.7, 'M14': 12.2,
    'MEL-001': 12.9, 'MEL-002': 12.1, 'MEL-003': 22.4, 'MEL-004': 7.1,
    'MEL-050': 17.7, 'MEL-055': 9.2, 'MEL-056': 22.1,
    'MEL-070': 23.8, 'MEL-070A': 17.0, 'MEL-072': 35.8, 'MEL-073': 34.8, 'MEL-074': 28.2, 'MEL-075': 16.3, 'MEL-080': 16.9, 'MEL-081': 20.0, 'MEL-082': 18.3, 'MEL-083': 15.4, 'MEL-084': 25.8,
    'SNP-001': 26.0, 'SNP-002': 19.3, 'SNP-003': 12.1, 'SNP-004': 7.5, 'SNP-005': 32.4, 'SNP-006': 2.9, 'SNP-007': 18.8, 'SNP-008': 15.7, 'SNP-009': 27.6, 'SNP-010': 13.4, 'SNP-011': 31.6, 'SNP-012': 22.3, 'SNP-013': 9.8, 'SNP-014': 5.6, 'SNP-015': 20.5, 'SNP-016': 12.1, 'SNP-017': 20.0, 'SNP-018': 31.1, 'SNP-019': 31.2, 'SNP-020': 30.5, 'SNP-021': 26.7, 'SNP-022': 15.3, 'SNP-023': 40.5, 'SNP-024': 18.4, 'SNP-025': 43.3, 'SNP-026': 22.1, 'SNP-027': 34.5, 'SNP-028': 32.1, 'SNP-029': 23.4, 'SNP-030': 25.1, 'SNP-031': 6.6, 'SNP-032': 24.9, 'SNP-033': 17.3, 'SNP-034': 22.6, 'SNP-035': 33.1, 'SNP-036': 36.2, 'SNP-037': 53.8, 'SNP-038': 26.3, 'SNP-039': 36.5, 'SNP-040': 33.1, 'SNP-041': 27.9, 'SNP-042': 13.3, 'SNP-043': 24.9, 'SNP-044': 20.4, 'SNP-045': 12.2,
    'NIC-001': 16.1, 'NIC-002': 16.5, 'NIC-003': 12.2, 'NIC-004': 15.4, 'NIC-005': 12.7, 'NIC-006': 8.5, 'NIC-007': 6.6, 'NIC-008': 24.4, 'NIC-009': 9.9, 'NIC-010': 18.1, 'NIC-011': 14.7, 'NIC-012': 13.0, 'NIC-013': 4.6, 'NIC-014': 23.4, 'NIC-015': 24.6, 'NIC-016': 15.4, 'NIC-017': 11.8, 'NIC-018': 17.1, 'NIC-019': 23.9, 'NIC-020': 6.8
}

# Fincas asignadas por prefijo de lote para ejemplo (ajusta según corresponda)
def asignar_finca(lote):
    if lote.startswith('MEL'):
        return 'MELCHORA'
    elif lote.startswith('SNP'):
        return 'SAN PANCHO'
    elif lote.startswith('NIC'):
        return 'NICAFRUT'
    elif lote.startswith(('B','C','D','E','F','G','H','I','J','K','L','M')):
        return 'PALO DE ARCO'
    else:
        return 'ISLA GRANDE'

fincas = {lote: asignar_finca(lote) for lote in lotes_areas.keys()}

# Selección y visualización
st.sidebar.header("📋 Datos Generales")
usuario = st.sidebar.text_input("Usuario")
semana = st.sidebar.number_input("Semana", min_value=1, max_value=52, value=datetime.now().isocalendar()[1])

lote = st.selectbox("Seleccionar lote", sorted(lotes_areas.keys()))
area = lotes_areas[lote]
finca = fincas[lote]

st.markdown(f"**Área del lote seleccionado:** {area} ha")
st.markdown(f"**Finca:** {finca}")

# Días y labores para el ingreso
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
labores = [
    "Chapia Mecánica", "Herbicida Mecánico", "Herbicida Manual", "Fertilización Mecánica",
    "Atomizo", "Monitoreo Plataforma", "Inspección de Plagas", "Riego", "Bejuco y Matapalo",
    "Banda Manual", "Control de Zompopa", "Conteo de Árboles", "Reparación de Tractores",
    "Mantenimientos", "Reparación de Implementos"
]

# Formulario ingreso labores
st.subheader("✍️ Ingreso de labores por día y hectáreas")

with st.form("form_labores"):
    datos_labores = []
    for labor in labores:
        hectareas_por_dia = {}
        cols = st.columns(7)
        for i, dia in enumerate(dias_semana):
            hect = cols[i].number_input(f"{labor} - {dia}", min_value=0.0, step=0.1, key=f"{labor}_{dia}")
            hectareas_por_dia[dia] = hect
        datos_labores.append({
            "finca": finca,
            "lote": lote,
            "area": area,
            "usuario": usuario,
            "semana": semana,
            "labor": labor,
            **hectareas_por_dia
        })
    enviado = st.form_submit_button("Guardar planificación")

if enviado:
    df = pd.DataFrame(datos_labores)
    df_melt = df.melt(
        id_vars=["finca","lote","area","usuario","semana","labor"],
        value_vars=dias_semana,
        var_name="día",
        value_name="hectareas"
    )
    df_melt = df_melt[df_melt["hectareas"] > 0]
    df_melt["día"] = pd.Categorical(df_melt["día"], categories=dias_semana, ordered=True)

    tabla_resumen = pd.pivot_table(
        df_melt,
        values="hectareas",
        index="labor",
        columns="día",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total"
    )

    st.subheader("📊 Resumen semanal por labor y día")
    st.dataframe(tabla_resumen.style.background_gradient(cmap="YlOrBr").format("{:.1f}"), use_container_width=True)

