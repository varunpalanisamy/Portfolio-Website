import streamlit as st
import pandas


st.markdown("<h1 style='text-align: center; color: White;'>Personal Projects</h1>", unsafe_allow_html=True)


st.divider()

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])


df = pandas.read_csv("data (1).csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images (2)/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images (2)/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
