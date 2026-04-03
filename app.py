import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tahtalı Barajı Dijital İkiz", layout="wide")

st.title("🌊 Tahtalı Barajı Dijital Su İkizi")
st.markdown("### *Zaman Serisi Analiz Paneli*")

# --- VERİ SETİ (SIRALAMA HATASI DÜZELTİLMİŞ) ---
zaman_verisi = pd.DataFrame({
    'Tarih': pd.to_datetime(['2026-01-05', '2026-01-25', '2026-02-15', '2026-03-05', '2026-04-03']),
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
    st.subheader("📈 2026 Doluluk Serüveni (Kronolojik)")
    # set_index('Tarih') yapınca artık tarihler doğru sıralanacak
    st.line_chart(data=zaman_verisi.set_index('Tarih'), color="#0077b6")
    st.write("**Analiz:** Grafik artık zaman akışına (Ocak -> Nisan) göre doğru sıralanmıştır.")

with col_right:
    st.subheader("🛰️ Güncel Uydu Analizi")
    st.image("analiz.jpg", use_container_width=True)

st.info("Veri Notu: Ocak başından bugüne kadar baraj yüzey alanındaki değişim %85'lik bir artış trendi göstermektedir.")
