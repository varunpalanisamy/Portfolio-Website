import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images (2)/IMG_3838.jpg")

with col2:

    st.title("Varun Palanisamy")
    content = """
    
    Hi, my name is Varun Palanisamy and I am a third-year at UC Santa Cruz majoring in Computer Science: Game Design, and minoring in Computer Science and Statistics. My educational background has equipped me with a robust foundation in programming languages such as Python, C++, Java, and SQL, as well as a strong understanding of data structures, algorithms, and data analytics.

My goal is to contribute to innovative tech solutions and to continuously grow as a software engineer. I am eager to connect with other technology professionals and explore new opportunities for growth and development. Let's connect!
    
    """
    st.info(content)


st.divider()

st.markdown("<h3 style='text-align: center; color: white;'>Check out the apps I have built bellow!</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: white;'>Feel free to contact me!</h2>", unsafe_allow_html=True)

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
