import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images (2)/picture.png")

with col2:
    st.title("Varun Palanisamy")
    content = """
    
    INSERT BIO
    
    """
    st.write(content)
