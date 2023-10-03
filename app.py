from pathlib import Path
import streamlit as st
from PIL import Image

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
    ' 🏆 Dashboard - Obesidade Infantil': 'https://github.com/ReinaldoASilva/Obesidade-Infantil',
    ' 🏆 Clausterização - Diamond': 'https://github.com/ReinaldoASilva/Diamond',
    ' 🏆 Shark attack': 'https://github.com/ReinaldoASilva/Shark-Attack'
}

st.set_page_config(page_title=Page_title, page_icon=Page_icon)


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
    st.title(name)
    st.write(Description)
    st.download_button(
        label="Download Resume CV", 
        data=PDFbyte , 
        file_name ='Resume.pdf',
        mime='application/octet-stream'
    )
    st.write(email)
   


####  -------------------- SOCIAL LINKS --------------------

st.markdown('#')
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].markdown(f'[{platform}]({link})')


####  -------------------- EXPERIENCE & QUALIDICATION --------------------
import streamlit as st

st.write('#')
st.subheader('Experience & Qualifications')

st.markdown("1. **Empreendedor (11 anos)**:")
st.markdown("- Fundei e gerenciei meu próprio negócio por 11 anos, demonstrando habilidades empreendedoras e capacidade de assumir riscos.")
st.markdown("- Desenvolvi estratégias de negócios, gerenciamento financeiro, marketing e liderança de equipe.")

st.markdown("2. **Pesquisa de Mercado e Abertura de Empresa em Portugal**:")
st.markdown("- Realizei pesquisas de mercado abrangentes para identificar oportunidades de negócios em Portugal.")
st.markdown("- Utilizei as informações obtidas para o planejamento e a abertura bem-sucedida de uma empresa no país.")

# Outras experiências e habilidades
st.subheader("Experiência e Habilidades Adicionais")

st.markdown("1. **Instrutor de Cursos e Palestras**:")
st.markdown("- Possuo experiência em ministrar cursos e palestras, transmitindo conhecimento de forma clara e envolvente.")
st.markdown("- Tenho habilidades de comunicação eficaz e capacidade de adaptação às necessidades e níveis de conhecimento dos participantes.")

st.markdown("2. **Disciplinado e Autodidata**:")
st.markdown("- Sou uma pessoa altamente disciplinada e autodidata, capaz de aprender novas habilidades e conhecimentos de forma independente.")
st.markdown("- Demonstro iniciativa e motivação para buscar constantemente oportunidades de crescimento profissional.")

st.markdown("3. **Gestão de Equipe e Liderança**:")
st.markdown("- Possuo experiência em liderar equipes, definindo metas, atribuindo responsabilidades e incentivando o crescimento profissional dos membros da equipe.")
st.markdown("- Demonstro habilidades sólidas de comunicação, resolução de problemas e tomada de decisões.")

####  -------------------- HARD SKILLS --------------------

st.write('#')
st.subheader('Hard Skills')
st.write( 
    """
    
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    
    
""")

####  -------------------- WORK HISTORY --------------------

st.write('#')
st.subheader('Work History')
st.write("---")

####  -------------------- JOB 1 --------------------

st.write ("🚧",' nome do cargo/ empresa')
st.write('ano')
st.write(
    """ 
    Descrever o que era feito
    
    
    
    
    """)

####  -------------------- Projects & Accomplishments --------------------

st.write('#')
st.write(' Projects & Accomplishments')
st.write('---')
for project, link in Projects.items():
    st.write(f'[{project}({link})]')



