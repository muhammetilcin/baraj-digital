import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tahtalı Barajı Dijital İkiz", layout="wide")

st.title("🌊 Tahtalı Barajı Dijital Su İkizi")
st.info("Veri Kaynağı: Sentinel-2 & CHIRPS (3 Nisan 2026)")

# Verilerimiz
alan_2026 = 12087740.41
alan_2025 = 6814537.04
yagis_mm = 184.10
sicaklik = 16.26

c1, c2, c3 = st.columns(3)
c1.metric("Mevcut Su Alanı", f"{alan_2026/1e6:.2f} km²", "+77%")
c2.metric("2 Aylık Yağış", f"{yagis_mm:.1f} mm")
c3.metric("Su Sıcaklığı", f"{sicaklik:.1f} °C")

st.divider()

col_left, col_right = st.columns([2, 1])
with col_left:
    st.subheader("🛰️ Uydu Analizi")
    st.image("analiz.jpg", use_container_width=True)
with col_right:
    st.subheader("📊 Alan Kıyaslaması (km²)")
    df = pd.DataFrame({'Yıl': ['2025', '2026'], 'Alan': [alan_2025/1e6, alan_2026/1e6]})
    st.bar_chart(data=df, x='Yıl', y='Alan')
