from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd

####  -------------------- PATH SETTINGS --------------------

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir /'styles'/'main.css'
resume_file = current_dir /'assets'/'cv.pdf'
profile_pic = current_dir / 'assets' / 'fotolinkedin.png'

####  -------------------- General SETTINGS --------------------

Page_title = 'Digital cv | Reinaldo Black'
Page_icon = ':wave:'
name = 'Reinaldo Black'
Description = 'Analista de dados voltado para negócios'

email = 'reialvesilva@gmail.com'

social_media = {
   'Youtube': 'https://www.youtube.com/channel/UCELBXwJnsu9QlTSONJy6w8w',
   'linkedin': 'https://www.linkedin.com/in/-reinaldosilva/',
   'GitHub': 'https://github.com/ReinaldoASilva',
   'Medium': 'https://medium.com/@reinaldo.silva'
}

Projects = {
    ' Dashboard - Obesidade Infantil': 'https://github.com/ReinaldoASilva/Obesidade-Infantil',
    ' Diamond - Clausterização': 'https://github.com/ReinaldoASilva/Diamond',
    ' Shark attack': 'https://github.com/ReinaldoASilva/Shark-Attack'
}

st.set_page_config(page_title=Page_title, page_icon=Page_icon)

def main():
    st.markdown("Hey dear")
    # Mais código do Streamlit aqui

if __name__ == "__main__":
    main() 

####  -------------------- LOAD CSS, PDF, PROFILE PICTURE --------------------

with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


####  -------------------- HERO SECTION --------------------

col1, col2 = st.columns(2, gap='small')

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.markdown(name)
    st.markdown(Description)
    st.download_button(
        label="Download Resume", 
        data=PDFbyte , 
        file_name ='Resume.pdf',
        mime='application/octet-stream'
    )
    st.markdown(email)


####  -------------------- SOCIAL LINKS --------------------

st.markdown('#')
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].markdown(f'[{platform}]({link})')



st.write("Olá, mundo!")






