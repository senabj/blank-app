import streamlit as st

st.title("Selamat Datang di Website SenaBayhaqiJammaz")
st.write(
    "ngodingseru bersama senabayhaqijammaz."
)
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2 ) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
