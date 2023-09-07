import streamlit as st
import pandas as pd
import altair as alt

st.header("Die 5 größten Gesundheitsprobleme im Corona-Jahr - Deutschland")
st.subheader("Welche der unten genannten Leiden stellen Ihrer Meinung nach derzeit in Ihrem Land die größten gesundheitlichen Probleme dar?")

source = pd.DataFrame({
        'Anteil (%)': [69, 32, 25, 17, 16],
        'Krankheit': ['COVID-19', 'Psychische Probleme', 'Krebs', 'Fettleibigkeit', 'Stress']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Krankheit:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: n=1000+; 16-74 Jahren; Deutschland; 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Ipsos")