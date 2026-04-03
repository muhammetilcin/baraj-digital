import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tahtalı Barajı Dijital İkiz", layout="wide")

st.title("🌊 Tahtalı Barajı Dijital Su İkizi")
st.markdown("### *Zaman Serisi Analiz Paneli*")

# --- VERİ SETİ (GEE'den Düzeltilmiş Veriler) ---
zaman_verisi = pd.DataFrame({
    'Tarih': ['05 Ocak', '25 Ocak', '15 Şubat', '05 Mart', '03 Nisan'],
    'Alan_km2': [6.50, 7.20, 8.80, 10.15, 12.08]
})

alan_bugun = 12.08
alan_gecen_yil = 6.81
yagis_toplam = 184.10

# --- KPI PANELİ ---
c1, c2, c3 = st.columns(3)
c1.metric("Mevcut Alan", f"{alan_bugun} km²", "+77%")
c2.metric("Toplam Yağış (2 Ay)", f"{yagis_toplam} mm")
c3.metric("Yıllık Artış", f"{(alan_bugun - alan_gecen_yil):.2f} km²")

st.divider()

# --- GRAFİK VE HARİTA ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("📈 2026 Doluluk Serüveni (Ocak - Nisan)")
    # Çizgi grafik oluşturuyoruz
    st.line_chart(data=zaman_verisi.set_index('Tarih'), color="#0077b6")
    st.write("**Analiz:** Şubat ayındaki ekstrem yağışların ardından baraj yüzey alanında lineer bir artış gözlenmiştir.")

with col_right:
    st.subheader("🛰️ Güncel Uydu Analizi")
    st.image("analiz.jpg", use_container_width=True)

# --- ALT BİLGİ ---
st.info("Bu panel Sentinel-2 uydusundan haftalık olarak çekilen NDWI (Normalleştirilmiş Fark Su Endeksi) verileriyle güncellenmektedir.")
