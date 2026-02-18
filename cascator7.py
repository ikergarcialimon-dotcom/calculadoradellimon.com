st.title("🛍️ Calculadora Profesional de Rebajas")
st.markdown("Introduce el precio original y el porcentaje de descuento para calcular el precio final.")
st.divider()




st.sidebar.header("📌 Datos del Producto")

precio_original = st.sidebar.number_input(
    "Precio Original (€)",
    min_value=0.0,
    max_value=10000.0,
    value=100.0,
    step=1.0
)

descuento = st.sidebar.slider(
    "Descuento (%)",
    min_value=0,
    max_value=100,
    value=20
)


if st.button("💰 Calcular Precio Final"):

    if precio_original == 0:
        st.error("El precio original debe ser mayor que 0.")
    else:
        # Cálculo correcto
        ahorro = precio_original * (descuento / 100)
        precio_final = precio_original - ahorro

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Precio Final",
                value=f"{precio_final:.2f} €",
                delta=f"-{ahorro:.2f} €"
            )

        with col2:
            if descuento >= 50:
                st.success("🔥 ¡Gran Oferta!")
                st.write("Es un descuento muy alto. Excelente oportunidad.")
            elif 25 <= descuento < 50:
                st.warning("👍 Oferta Razonable")
                st.write("Es una buena rebaja.")
            else:
                st.info("🤔 Descuento Bajo")
                st.write("Quizás puedas esperar una mejor oferta.")

        st.divider()

    
        st.info("Fórmula matemática aplicada:")
        st.latex(r'''
        Precio\ Final = Precio\ Original - (Precio\ Original \times \frac{Descuento}{100})
        ''')

        st.balloons()
