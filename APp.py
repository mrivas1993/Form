import streamlit as st

st.title("Formulario de Estimación de Fruta")

st.subheader("Datos del lote")
lote = st.text_input("Nombre del lote")
area = st.number_input("Área del lote (hectáreas)", min_value=0.0)

st.subheader("Datos del árbol")
cantidad_arboles = st.number_input("Cantidad total de árboles", min_value=0)
categoria = st.selectbox("Categoría predominante", ["A", "B", "C"])

st.subheader("Muestreo")
arboles_muesteados = st.slider("Árboles muestreados", min_value=5, max_value=100, value=30)
frutas_promedio = st.number_input("Frutas promedio por árbol muestreado", min_value=0)
peso_promedio = st.number_input("Peso promedio por fruta (kg)", min_value=0.0)

if st.button("Calcular estimación"):
    total_frutas_estimadas = frutas_promedio * cantidad_arboles
    total_kg_estimados = total_frutas_estimadas * peso_promedio
    st.success(f"Estimación total de frutas: {total_frutas_estimadas:,.0f}")
    st.success(f"Producción estimada: {total_kg_estimados:,.2f} kg")
