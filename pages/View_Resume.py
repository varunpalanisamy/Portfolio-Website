import base64
import streamlit as st

st.markdown("<h1 style='text-align: center; color: White;'>View Resume</h1>", unsafe_allow_html=True)

r
def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'''
        <div style="display: flex; justify-content: center;">
            <iframe src="data:application/pdf;base64,{base64_pdf}" width="960" height="1000" type="application/pdf"></iframe>
        </div>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)

displayPDF('Varun Palanisamy - Resume (1).pdf')
