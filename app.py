
import streamlit as st
import math

# KONFIGURASI
st.set_page_config(page_title="GPS Distance Calculator", layout="centered")
st.title("GPS Distance Calculator")
st.caption("Perhitungan Jarak Geografis Menggunakan Formula Haversine")

st.divider()

# INPUT
st.subheader("Koordinat GPS")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Titik Pertama**")
    lat1 = st.number_input("Latitude 1", -90.0, 90.0, 5.5483, format="%.6f")
    lon1 = st.number_input("Longitude 1", -180.0, 180.0, 95.3238, format="%.6f")

with col2:
    st.markdown("**Titik Kedua**")
    lat2 = st.number_input("Latitude 2", -90.0, 90.0, 5.2030, format="%.6f")
    lon2 = st.number_input("Longitude 2", -180.0, 180.0, 96.7000, format="%.6f")

# PERHITUNGAN
if st.button("Hitung Jarak", type="primary", use_container_width=True):

    R = 6371

    # Konversi derajat ke radian
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Menghitung nilai a
    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2)
        * math.sin(delta_lambda / 2) ** 2
    )

    # Menghitung nilai c
    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    # Menghitung jarak akhir
    distance = R * c

    # HASIL
    st.divider()
    st.subheader("Hasil Perhitungan")

    st.success("Perhitungan berhasil dilakukan!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Jarak (Kilometer)", f"{distance:.2f} km")

    with col2:
        st.metric("Jarak (Meter)", f"{distance * 1000:.2f} m")

    # PROSES PERHITUNGAN
    st.divider()
    st.subheader("Proses Perhitungan")

    with st.expander("Lihat Tahapan Perhitungan", expanded=True):

        st.markdown("**1. Konversi Koordinat ke Radian**")

        st.latex(r"\varphi_1 = \text{radians}(\text{Latitude}_1)")
        st.write(f"φ₁ = {phi1:.6f} rad")

        st.latex(r"\varphi_2 = \text{radians}(\text{Latitude}_2)")
        st.write(f"φ₂ = {phi2:.6f} rad")

        st.write(f"Δφ = {delta_phi:.6f} rad")
        st.write(f"Δλ = {delta_lambda:.6f} rad")

        st.markdown("**2. Menghitung Nilai a**")

        st.latex(
            r"a = \sin^2\left(\frac{\Delta\varphi}{2}\right)"
            r"+ \cos(\varphi_1)\cos(\varphi_2)"
            r"\sin^2\left(\frac{\Delta\lambda}{2}\right)"
        )

        st.write(f"a = {a:.10f}")

        st.markdown("**3. Menghitung Nilai c**")

        st.latex(
            r"c = 2 \times \operatorname{atan2}"
            r"(\sqrt{a},\sqrt{1-a})"
        )

        st.write(f"c = {c:.10f}")

        st.markdown("**4. Menghitung Jarak Geografis**")

        st.latex(r"d = R \times c")

        st.write(f"d = 6371 × {c:.10f}")

        st.success(f"Jarak akhir = {distance:.4f} km")