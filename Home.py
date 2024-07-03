import streamlit as st
import pandas
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import requests
import re
import io
import streamlit.components.v1 as components
#import tensorflow as tf
import webbrowser
# from link_button import link_button





st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: White;'>Varun Palanisamy</h1>", unsafe_allow_html=True)

st.divider()
st.markdown("<h6 style='text-align: center; color: White;'> </h6>", unsafe_allow_html=True)


# st.title("Varun Palanisamy")
col1, col2 = st.columns(2)


with col1:
    # st.title("")
    st.image("images (2)/IMG_3838.jpg")

    url = 'https://www.linkedin.com/in/varun-palanisamy-88190b1a3/'
    colButton1, colButton2 = st.columns(2)
    #
    # with colButton1:
    # # pdfFileObj = open('Varun Palanisamy - Resume (1).pdf', 'rb')
    #     # st.sidebar.download_button('View Resume', pdfFileObj, file_name='Varun Palanisamy - Resume (1).pdf', mime='pdf')
    #
    # with colButton2:
    st.sidebar.link_button(label="Connect with me on LinkedIn", url=url)


with col2:


    # st.markdown("<h1 style='text-align: center; color: White;'>Varun Palanisamy</h1>", unsafe_allow_html=True)

    content = """
    
    Hi, my name is Varun Palanisamy and I am a third-year at UC Santa Cruz majoring in Computer Science: Game Design, and minoring in Computer Science and Statistics. My educational background has equipped me with a robust foundation in programming languages such as Python, C++, Java, and SQL, as well as a strong understanding of data structures, algorithms, and data analytics.

My goal is to contribute to innovative tech solutions and to continuously grow as a software engineer. I am eager to connect with other technology professionals and explore new opportunities for growth and development. Let's connect!
    
    """
    st.info(content)



