import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tahtalı Barajı Dijital İkiz", layout="wide")

st.title("🌊 Tahtalı Barajı: 2 Yıllık Karşılaştırmalı Analiz")
st.markdown("### *2025 vs 2026 Su Alanı Değişimi (15 Günlük Periyot)*")

# --- VERİ SETİ OLUŞTURMA (15 Günlük Periyotlar) ---
# 2025 Verileri (Geçen Yıl)
data_2025 = pd.DataFrame({
    'Ay-Gün': ['01-01', '01-15', '02-01', '02-15', '03-01', '03-15', '04-01'],
    '2025 Alan (km²)': [5.20, 5.50, 5.90, 6.30, 6.60, 6.81, 6.75]
})

# 2026 Verileri (Bu Yıl - Günümüze Kadar)
data_2026 = pd.DataFrame({
    'Ay-Gün': ['01-01', '01-15', '02-01', '02-15', '03-01', '03-15', '04-01'],
    '2026 Alan (km²)': [6.50, 7.10, 8.20, 9.50, 10.80, 11.50, 12.08]
})

# Verileri birleştirme
df_final = pd.merge(data_2025, data_2026, on='Ay-Gün')

# --- KPI PANELİ ---
c1, c2, c3 = st.columns(3)
c1.metric("Mevcut Durum (2026)", "12.08 km²", "+77% (vs 2025)")
c2.metric("Geçen Yıl Aynı Dönem", "6.81 km²")
c3.metric("Net Artış", "5.27 km²")

st.divider()

# --- GRAFİK BÖLÜMÜ ---
st.subheader("📈 Yıllara Göre Doluluk Kıyaslaması (Ocak - Nisan)")
# Çizgi grafikte iki yılı birden gösteriyoruz
st.line_chart(data=df_final.set_index('Ay-Gün'), color=["#FF4B4B", "#0077b6"]) 

st.write("**Grafik Okuma:** Kırmızı çizgi 2025, Mavi çizgi 2026 trendini göstermektedir. Şubat ayı ortasından itibaren mavi çizginin (2026) dikey yükselişi, havzadaki ekstrem yağış verimliliğini kanıtlar.")

# --- ALT PANEL: HARİTA VE DETAY ---
col_map, col_text = st.columns([1, 1])

with col_map:
    st.image("analiz.jpg", caption="Mevcut Su Maskesi Analizi", use_container_width=True)

with col_text:
    st.info("""
    **Mühendislik Raporu:**
    * **Periyot:** 15 Günlük Uydu Gözlemi (Sentinel-2)
    * **Gözlem:** 2026 yılındaki doluluk oranı, 2025 yılının aynı dönemine göre yaklaşık 2 kat daha hızlı yükselmiştir.
    * **Risk:** Nisan ayı itibariyle yüzey sıcaklığı (16.2°C) düşük seyretmektedir, bu da buharlaşma kaybının minimize olduğu 'altın dolum' döneminde olduğumuzu gösterir.
    """)
