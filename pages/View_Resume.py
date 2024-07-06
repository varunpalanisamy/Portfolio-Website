import base64
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


st.markdown("<h1 style='text-align: center; color: White;'>View Resume</h1>", unsafe_allow_html=True)

emptyCol1, middle, emptyCol2 = st.columns([0.25,1,0.25])

pdf_path = 'Varun Palanisamy - Resume (1).pdf'

with middle:
    pdf_viewer(input=pdf_path, width=900, height=1000)









#PREVIOUS ATTEMPT ON PDF VIEWING:

# st.markdown("<h1 style='text-align: center; color: White;'>View Resume</h1>", unsafe_allow_html=True)
#
#
# def displayPDF(file):
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#
#     pdf_display = f'''
#         <div style="display: flex; justify-content: center;">
#             <iframe src="data:application/pdf;base64, {base64_pdf}" width="960" height="1000" type="application/pdf"></iframe>
#         </div>
#     '''
#     st.markdown(pdf_display, unsafe_allow_html=True)
#
# displayPDF('Varun Palanisamy - Resume (1).pdf')
