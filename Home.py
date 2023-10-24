import streamlit as st
from pathlib import Path
from PIL import Image
import itertools
import datetime
import qrcode
import io


# Opções do menu da barra lateral
menu = ['Página Inicial', "Me", "Qualifications", "Hard Skills", "Soft Skills", "Work History","Certifications", "Projects", "Contato"]

select_menu = st.sidebar.radio("Menu", menu)


# Remover o menu do streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Conteúdo principal da página
if select_menu == "Página Inicial":


    ####  -------------------- PATH SETTINGS --------------------

    current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
    css_file = current_dir / 'styles' / 'main.css'
    resume_file = current_dir / 'assets' / 'cv.pdf'
    profile_pic = current_dir / 'assets' / 'minhafoto.png'

    ####  -------------------- General SETTINGS --------------------

    Page_title = 'Digital cv | Reinaldo Black'
    Page_icon = ':wave:'
    name = 'Reinaldo Black'
    Description = 'Data Analytics. With Business Experience'

    email = 'reialvesilva@gmail.com'

    social_media = {
        'Youtube': 'https://www.youtube.com/channel/UCELBXwJnsu9QlTSONJy6w8w',
        'linkedin': 'https://www.linkedin.com/in/-reinaldosilva/',
        'GitHub': 'https://github.com/ReinaldoASilva',
        'Medium': 'https://medium.com/@reinaldo.silva'
    }
    

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
            data=PDFbyte,
            file_name='Resume.pdf',
            mime='application/octet-stream'
        )
    st.write(email)

    ####  -------------------- SOCIAL LINKS --------------------

    st.markdown('#')
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].markdown(f'[{platform}]({link})')
    

    # Função para ler e atualizar o contador de visitas
    def update_visit_count():
        try:
            with open("visit_count.txt", "r+") as file:
                count = int(file.read())
                count += 1
                file.seek(0)
                file.write(str(count))
        except FileNotFoundError:
            with open("visit_count.txt", "w") as file:
                count = 1
                file.write(str(count))
        return count

    # Obtém o número de visitas
    visit_count = update_visit_count()

    # Exibe o contador de visitas
    st.sidebar.info(f"Número de Visitas: {visit_count}")
    
    
    
    
    st.write("")
    st.write("")
    st.write(" Seja bem vindo ao nosso espaço.")
    st.write("Reservei esse espaço para contar um pouco sobre minha história, minhas habilidaes e experiêcnias.")
    st.write("Acima você pode baixar uma versão resumida do CV, fique à vontade para fazer o download")
    st.write("Acima você também encontra minhas redes sociais, é sempre bom ver como nos comportamos por lá, não é verdade? ")

elif select_menu == "Me":
    st.write("Tome um ☕ e vamos lá")
    st.write(" Nascido no interior da Bahia, crescido no interior do Rio, filho de pais separados e que sempre sonhou em ganhar o mundo")
    st.write("Aos 20 anos fui morar em atibaia-Sp para dedicar parte da minha vida em uma Organização Norte Americana sem fins lucrativos\
        trabalhando com a realização de projetos sociais, auxiliava na organização de todo o projeto. Realizávamos\
        entraga de cestas básicas,atendimento médico e entrega de refeições. Logo após esse período fui presidente de uma ONG por um ano\
        o que me ajudou a desenvolver um forte papel de liderança.")
    st.write("Nessa jornada da minha vida que foi de 2003 a 2010 conheci 11 estados e morei em 5 cidades diferentes. Essa jornada\
        enriqueceu demais a minha vida em fatores culturais, e valorizando demais a riqueza de nosso país")
    st.write(" Logo após essa jornada fui morar em Sp capital. Essa fase da minha vida com projetos sociais foi fundamental demais\
        para moldar o líder que me tornaria em seguida. Em Sp iniciei a vida de empreendedor quando adquiri uma franquia de agência\
        de turismo, durou apenas dois anos. Mas que tive muitos aprendizados principalmente na questão de parcerias confiáveis.\
        pois com a agência de turismo mantive parceria com uma empresa que prometia passagens com valores mais em conta,\
        o que não levou muito tempo, até que vários clientes ligaram dizendo que não havia passagens, a empresa sumiu e eu tive que\
        arcar com todo o prejuízo. Daí o maior aprendizado, não existe nada fácil, quando for fácil desconfie. Agora imagine\
        todo esse transtorno com 1 mês de casado.")
    st.write(" Já imaginou com 1 mês de casado estar sem trabalho, não é uma situação muito fácil. Mas nesse momento eu precisava\
        agir de forma rápida,pois precisava que dinheiro entrasse de forma mais rápida, foi ai que tive a ideia de trabalhar com lavagem a seco automotiva. \
        Você pode se perguntar porque eu não fui procurar um emprego né, mas muita das vezes os processos seletivos são demorados\
        e as contas não esperam. Como nesse momento estou trabalhando meio período para ajudar nas contas e o outro período estudo\
        porque meu objetivo é poder atuar na área de Dados. Nessa época era bem escasso esse tipo de lavagem\
        e todos cobravam para dar curso, foi aí que encontrei um rapaz que fornecia os produtos e disse que me ensinaria a lavar,\
        comprei os produtos dele e ele me ensinou no estacionamento do shopping central plaza na Vila Prudente. ")
    st.write(" Essa foi uma das fases mais longas, consistente e de intenso aprendizado. Iniciei a empresa Mais Eco Mais Vida,\
        com o foco de quanto mais economia o cliente tivesse de tempo ele teria mais vida. A lavagem a seco proporcionou atender o\
        cliente onde ele estava, uma empresa que iniciou antendendo clintes com uma bicicleta em 6 meses já tínhamos umcarro e atendendo\
        clientes como: Eletropaulo, Zascar, Polícia Cívil, Claro, além de escritórios comerciais. Funcionando com três funcionários\
        atendendo delivery, me senti totalmente realizado. Mas faltava algo, foi ai que juntamente com minha esposa decidimos criar um\
        projeto de ressocialização, onde criamos parceria com um projeto que abrigava os dependentes químicos pra voltar a sociedade.\
        Nunca fui dependente químico mas aprendi desde pequeno a ajudar o próximo, na minha vida em sp, quando dividia a casa com mais\
        dois amigos, dentre eles um Moçambicano chegamos a levar moradores de rua para nossa casa. O mesmo fato aconteceu em campinas na época." )
    st.write(" Os quase 10 anos trabalhando com essa assossiação Norte Americana me forjou e muito para essa fase empreendedor. Pois\
        colocou a empatia no meu processo de liderança. Tudo que precisa ser feito, sempre tem que ser pensado no bem comum de todos.\
        Nessa jornada precisei fazer o que sempre gostei: Estudar. Desenvolvi muitas habilidades voltadas para marketing, gestão de equipe,\
        , gestão de negócios, plano de negócios, pensamento analítico, dentre outros.")
    st.write(" Depois de estar com a vida confortável em Sp veio a nossa filha Nina em 11/2016, que mudou completamente nossos planos,\
        nascida de parto domiciliar planejado, ela veio para trazer mudança em todos os sentidos. Decidimos nos mudar para\
        Astorga interior do Paraná onde a família da minha esposa mora. Lá fomos buscar a paz e tranquilidade para criá-la, pois\
        nessa altura com toda a violência era impossível se ver continar morando em SP. ")
    st.write(" Nessa jornada da vida as coisas sempre vão mudando, e em 2018 depois de tantas conversas em casal\
        decidimos nos mudar para Portugal. Final de 2018 fiquei 30 dias lá realizando uma pesquisa de mercado para abrir um negócio,\
        e foi uma viagem de muito aprendizado, pois havia ido com a ideia de abrir uma estética automotiva inicialmente, mas conversando\
        com os locais descobri que a maior necessidade deles era a prestação de serviçõs de manutenção residencial. Então retornei\
        criamos um projeto e aplicamos ao visto D2 que foi aprovado em maço seguinte. E lá vamos nós novamente agora em terras lusitanas\
        Iniciamos bem a empresa mas nem tudo sai como o planejado pois a pandemia dificultou demais as coisas por lá,\
        pois o lockdown foi longo. Em janeiro de 2021 minha esposa retorna com nossa filha e eu fiquei para poder levantar um dinheiro.\
        Em Março deste ano consegui um emprego de técnico de energia eólica, sendo que o serviço era prestado na frança,\
        seis semanas em parque e uma em casa. Como novato na área, decidi ficar seis meses em parque para aprender logo a profissão.\
        Esse sou eu, sempre dou tudo para aprender. Nessa parte me inspiro muito em Michael Jordan, Koby, são atletas que sempre deram\
        de tudo para ser o melhor.")
    st.write(" O retorno pra casa, em maio de 2022 retorno ao brasil para enfim estar em família, essa foi a pior distância da minha vida,\
        nesse perído tive até crise de ansiedade por estar longe delas. Mas o oceano azul na minha vida aconteceu quando eu fui convidado\
        por um amigo para faze um bootcamp de 8 horas em Análise de Dados com duração de 2 meses na Ironhack, uma escola internacional de\
        tecnologia. Acredito que em dados a fusão da minha vida aconteceu, pois fundiu a ajuda ao próximo e o empreendedorismo.\
        Essa é a profissão que mais tem haver com minha personalidade, pois ajudar empresas e negócios através dos dados a descobrirem padrões,\
        que levam a uma tomada de decisão muito mais acertiva me motiva demais. Atualmente existe uma dificuldade quanto as empresas\
        contratarem juniors na área, mas estou firme aqui estudando e desenvolvendo projetos por conta própria. Sigo minha rotina acordando\
        as 4 da manhã pra estudar antes de sair de casa. Sou incansável para alcançar meus objetivos, sou disciplinado para estudar e \
        autodidatismo para aprender sozinho. Tenho facilidade de aprender qualquer coisa. Já trabalhei como: Mecânico, Segurança, Marido de alugue\
        Empresario de lavagem automotiva, Empresário de Agência de Turismo, além de tantas outras coisas que ocuparia muito espaço.\
        Porque escrevi tudo isso? É sempre importante conhecer quem será a pessoa que estará conosco por um tempo. Uma coisa é certa,\
        posso não possuir todas as qualificações que você precisa mas farei qualquer coisa para conseguir.")
    st.write("Essa é uma parte da minha história, nem mencionei a perda do meu pai quando estava em Portugal, que dor. Mas agradeço se você\
        chegou até aqui? Muito obrigado por ter parado o dia para ler um pouco sobre mim. Me mande uma mensagem no linkedin pra seu saber o que você achou.\
        E não poderia deixar de agradecer a Deus, porque somente\ Ele para me dar forças nos momentos mais difíceis e complexos da minha vida!")
    st.write("Vejo você! Até Breve!")
    
    
    
    # Adicione aqui o conteúdo que deseja exibir na página "Projects"

elif select_menu == "Qualifications":
        st.write('#')
        st.subheader('Experience & Qualifications')

        st.markdown("1. **Empreendedor (11 anos)**:")
        st.markdown("- Fundei e gerenciei meu próprio negócio por 11 anos, demonstrando habilidades empreendedoras e capacidade de assumir riscos.")
        st.markdown("- Desenvolvi estratégias de negócios, gerenciamento financeiro, marketing e liderança de equipe.")

        st.markdown("2. **Pesquisa de Mercado e Abertura de Empresa em Portugal**:")
        st.markdown("- Realizei pesquisas de mercado abrangentes para identificar oportunidades de negócios em Portugal.")
        st.markdown("- Utilizei as informações obtidas para o planejamento e a abertura bem-sucedida de uma empresa no país.")

        st.markdown("3. **Assossiação Norte Americana**:")
        st.markdown(" Atividades Realizadas")
        st.markdown("- Organização e realização de eventos sociais")
        st.markdown("- Entrega de refeições para pessoas em situação de vulnerabilidade")
        st.markdown("- Visita aos lares")

        st.markdown(" Habilidades Desenvolvidas")
        st.markdown("- Trabalho em equipe: Colaborei com pessoas de diferentes origens e habilidades para alcançar objetivos comuns em projetos sociais.")
        st.markdown("- Comunicação efetiva: Aprimorei minhas habilidades de comunicação ao interagir com indivíduos de diversas comunidades e ao transmitir informações de forma clara e acessível.")
        st.markdown("- Empatia: Desenvolvi a capacidade de compreender as necessidades e perspectivas dos outros, demonstrando sensibilidade e cuidado durante as interações com as pessoas atendidas pelos projetos sociais.")
        st.markdown("- Liderança: Assumi responsabilidades de liderança em projetos sociais, coordenando equipes, tomando decisões e motivando membros da equipe para alcançar os objetivos estabelecidos.")
        st.markdown("- Resolução de problemas: Enfrentei desafios complexos em projetos sociais e desenvolvi habilidades para identificar soluções criativas e eficazes.")

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

elif select_menu == "Hard Skills":
        st.write('#')
        st.subheader('Hard Skills')

        # Cria as duas colunas
        col1, col2 = st.columns(2)

        # Dados das habilidades
        dados = {
            'Python': 'Intermediário',
            'SQL': 'Iniciante',
            'Tableau': 'Avançado',
            'Machine_Learning': 'Intermediário',
            'Trading_Quant': 'Intermediário',
            'Pacote_Office': 'Intermediário',
            'Git': 'Intermediário',
            'Inglês': 'Intermediário',
            'Habilidades_em_marketing': 'Intermediário',
            'Habilidades_de_design': 'Intermediário',
            'Google_Analytics': 'Intermediário',
            'Google_Adsense': 'Iniciante',
            'Wordpress': 'Iniciante',
            'Google_Trends': 'Iniciante',
            'Google_Meu_negócio': 'Intermediário',
            'Google_Workspace': 'Iniciante',
            'ChatGpt': 'Intermediário'
        }

        # Divide os dados em duas listas
        habilidades = list(dados.keys())
        niveis = list(dados.values())

        # Adiciona as linhas nas colunas
        for habilidade1, habilidade2, nivel1, nivel2 in zip(habilidades[:10], habilidades[10:], niveis[:10], niveis[10:]):
            col1.write(f"- *{habilidade1} - {nivel1}*")
            col2.write(f"- *{habilidade2} - {nivel2}*")

elif select_menu == "Soft Skills":
        st.write('#')
        st.subheader('Soft Skills')

        # Criar colunas
        col1, col2 = st.columns(2)

        dados = {
            'Inglês' : "Intermediário",
            'Empatia': 'Alto',
            'Responsabilidade': 'Alta',
            'Comunicativo': 'Médio',
            'Trabalho em equipe': 'Alto',
            'Liderança': 'Alto',
            'Criatividade': 'Alta',
            'Gestão de projetos': 'Média',
            'Perseverança': 'Alta',
            'Atitude positiva em relação aos desafios': 'Alta',
            'Pensamento crítico com foco em buscar soluções': 'Alta',
            'Inteligência emocional para lidar com frustrações': 'Alta',
            'Saber ouvir as pessoas':'Alta',
            'Resiliência':'Alta',
            'Princípios éticos':'Alta',
            'Capacidade de trabalhar sob pressão':'Alta',
            'Motivação':'Alta',
            'Autodidata':'Alta',
            'Proatividade':'Alta',
            'Resolução de conflitos':'Alta',
            'Atendimento ao Cliente': 'Alta'
        }
        habilidades = list(dados.keys())
        niveis = list(dados.values())

        for habilidade1, habilidade2, nivel1, nivel2 in zip(habilidades[:10], habilidades[:10], niveis[:10], niveis[:10]):
            col1.write(f"- *{habilidade1} - {nivel1}*")
            col2.write(f"- *{habilidade2} - {nivel2}*")

elif select_menu == "Work History":
        st.write('#')
        st.subheader("Work History")

# Dados da experiência profissional
        experiencia_profissional = [
            {
                'empresa': 'Anywind, França',
                    'cargo': 'Técnico de manutenção em Torres Eólicas - Experiência Internacional',
                    'periodo': 'Mar-2021 - Maio-2022',
                    'descricao': [
                        'Realizei a manutenção corretiva das torres eólicas',
                        'Sugeri melhorias em segurança e o dia a dia do trabalho'
                ],
                    'habilidades': [
                        'Trabalho em equipe',
                        'Gestão de Tempo',
                        'Adaptabilidade',
                        'Solução de Problemas',
                        'Habilidade para lidar com mudanças'
                ]
            },
            {
                'empresa': 'Pratik Serviços, Porto - Portugal',
                'cargo': 'Empresário - Experiência Internacional',
                'periodo': 'Mar-2019 - Fev-2021',
                'descricao' : [
                    'Identifiquei oportunidades e melhorias na empresa, desde o trato com cliente até a compra de ferramentas\
                        para melhoria da prestação de serviço'
                ],
                'habilidades': [
                    'Visão Estratégica',
                    'Proatividade',
                    'Habilidade para resolver problemas',
                    'Orientação a Resultados',
                    'Habilidade para lidar com diferenças culturais',
                    'Prospecção de Clientes'
                ]
            },
            {
                'empresa': 'Mais Eco Mais Vida - São Paulo - São Paulo',
                'cargo': 'Empresário',
                'periodo': 'Jan-2012 - Jan-2019',
                'descricao' : [ "Realizava o contato com o cliente e a prestação do serviço, mas contando com mais 2 funcionários.\
                    realizei diversos cursos na área de estética automotiva e apresentação do projeto para empresas.\
                        Ministrei curso na área de estética e lavagem a seco."
                ],
                'habilidades': [
                    'Flexibilidade',
                    'Comunicação Efetiva',
                    'Capacidade de aprendizado rápido',
                    'Resiliência',
                    'Habilidade de Negociação'
                ]
            }

        ]

        # Exibe a experiência profissional em duas colunas
        col1, col2 = st.columns(2)

        for experiencia in experiencia_profissional:
            col1.markdown(f"**{experiencia['empresa']}**\n*{experiencia['cargo']}*\n{experiencia['periodo']}")
            for descricao in experiencia['descricao']:
                col1.write(f"- {descricao}")
            for habilidade in experiencia['habilidades']:
                col1.write(f"- {habilidade}")


# Exibe a mensagem de última atualização na barra lateral
last_update = datetime.datetime(2023, 10, 24)  # Substitua pela data da última atualização
certifications = "Redes Neurais Artificiais"  # Substitua pelo nome do último projeto
st.sidebar.info(f"Last Update: {last_update.strftime('%d/%m/%Y')}, Certifications: {certifications}")

if select_menu == "Certifications":
        st.write('#')
        st.subheader('Certifications')


        # Dados dos cursos complementares
        cursos_complementares = [
            {
                'curso': 'CPA-20 Anbima',
                'instituicao': 'Anbima',
                'periodo': 'Fev - 2023',
                'habilidades': [
                    'Fundos de Investimentos',
                    'Complice',
                    'Mensuração e Gestão de Performance e Riscos',
                    'Economia e Finanças',
                    'Instrumentos de Renda Variável, Renda Fixa e Derivativos',
                     "----------------------------------------"

                ]
 
            },
            {
                'curso': 'Fundamentos da Gestão de Projetos',
                'instituicao': 'FM2S',
                'periodo': 'Dez-2022',
                'habilidades': [
                    'PMI',
                    'PMBoK',
                    'Riscos',
                    'Monitoramento e Controle',
                    "----------------------------------------"
                ]
            },
            {
                'curso': 'MASP - Metodologia de Análise e Solução de Problemas',
                'instituicao': 'Voitto',
                'periodo': 'Dez-2022',
                'habilidades': [
                    'Tomada de Decisão',
                    'Melhoria Contínua',
                    'Aumento da Eficiência',
                    'Processos Produtivos',
                    "----------------------------------------"
                ]
            },
            {
                'curso': 'Data Analytics Bootcamp Full-Time',
                'instituicao': 'Ironhack',
                'periodo': 'Out-2022 - Dez-2022',
                'habilidades': [
                    'Python',
                    'SQL',
                    'Business Inteligent',
                    'Machine Learning',
                    'Git',
                    'Statistics',
                    "----------------------------------------"
                ]
            },
            {
                'curso': 'Big Data Fundamentos 3.0',
                'instituicao': 'Data Science Academy',
                'periodo': 'Nov-2022',
                'habilidades': [
                    'O Que é Big Data',
                    'Sistemas de Armazenamento de Dados',
                    'Armazenamento e Processamento Paralelo',
                    'Cloud Computing',
                    'MLOps e DataOps',
                    'Dados Como Serviço',
                    'ETL - Extração, Transformação e Carga de Dados',
                    'Como Iniciar um Projeto de Big Data?',
                    "----------------------------------------"
                ]
            },
            {
                'curso': 'Resolução de Problemas e Tomada de Decisão',
                'instituicao': 'Fecap',
                'periodo': 'Nov-2022',
                'habilidades': [
                    'Tomada de Decisão',
                    'Resolução de Problemas',
                    'Melhoria Contínua',
                    'Análise de Dados',
                    'Gestão de Riscos',
                    'Pensamento Crítico',
                    "----------------------------------------"
                ]
            },
            {
                'curso': 'Resolução de Problemas e Tomada de Decisão',
                'instituicao': 'Voitto',
                'periodo': 'Dez-2022',
                'habilidades': [
                    'Tomada de Decisão',
                    'Resolução de Problemas',
                    'Melhoria Contínua',
                    'Análise de Dados',
                    'Gestão de Riscos',
                    'Pensamento Crítico',
                    "----------------------------------------"
                ]
            },
        {
                'curso': 'Act Commands - Seu ChatGPT como Assistente Virtual',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'Act Commands que todo dev deveria conhecer',
                    'Elevando o nível dos Act Commands',
                    "----------------------------------------"
                ]
            },
        
        {
                'curso': 'Como Ingressar no Futuro Agora Mesmo com ChatGPT',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'O código Davinci',
                    'Criando conta na Openai',
                    "----------------------------------------"
                ]
            },
        {
                'curso': 'Como Utilizar o ChatGPT como Copiloto de Programação',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'Pair Programming with GPT',
                    'Documentações Profissionais e Instântaneas',
                    'ChatGpt como Mentor',
                    "----------------------------------------"
                ]
            },
        
          {
                'curso': 'Como Utilizar o ChatGPT para Refatorar Códigos',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'Códigos Eficientes',
                    'Simplificação de Códigos',
                    'Modularizando o Código',
                    'Refatorando a estrutura de pastas e combinando técnicas',
                    "----------------------------------------"
                ]
            },
        
        {
                'curso': 'Como Utilizar o ChatGPT para Simular Entrevistas Técnicas',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'GPT como entrevistador',
                    'Entre no DNA técnico da empresa desejada',
                    'Entre no DNA de soft skills da empresa desejada',
                    'GPT como Entrevistador',
                    "----------------------------------------"
                ]
            },
        
        {
                'curso': 'Introdução ao Machine Learning',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'Métodos de Machine Learning e suas aplicações',
                    'Machine Learning aplicados em sistemas reais',
                    'Modelos de Machine Learning para Visão Computaciona',
                    "----------------------------------------"
                ]
            },

        {
                'curso': 'Métodos de Machine Learning Bioinspirados',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'Métodos de Machine Learning bioinspirados',
                    'Algoritmos Heurísticos x Determinísticos',
                    "----------------------------------------"
                ]
            },

        {
                'curso': 'Redes Neurais Artificiais',
                'instituicao': 'Dio',
                'periodo': 'Out-2023',
                'habilidades': [
                    'Redes Neurais Artificiais',
                    'Treinamento de uma Rede Neural Artificial',
                    'Classificação: Execução da Rede Neural Artificial',
                    "----------------------------------------"
                ]
            }
        
        
        
        ]

        # Exibe os cursos complementares em duas colunas
        col1, col2 = st.columns(2)

        # Exibe os primeiros 4 cursos na primeira coluna
        for i, curso in enumerate(cursos_complementares):
            if i < 7:
                col1.markdown(f"**{curso['curso']}**\n*{curso['instituicao']}*\n{curso['periodo']}")
                for habilidade in curso['habilidades']:
                    col1.write(f"- {habilidade}")
            else:
                col2.markdown(f"**{curso['curso']}**\n*{curso['instituicao']}*\n{curso['periodo']}")
                for habilidade in curso['habilidades']:
                    col2.write(f"- {habilidade}")
        

# Exibe a mensagem de última atualização na barra lateral
last_update = datetime.datetime(2023, 10, 24)  # Substitua pela data da última atualização
project_name = "Employee_Turnover_Predicition"  # Substitua pelo nome do último projeto
st.sidebar.info(f"Last Update: {last_update.strftime('%d/%m/%Y')}, \n  Project_Name: {project_name}")  

if select_menu == "Projects":

    st.write('#')
    st.subheader('Projects')

    st.markdown("")
    projects1 = [
        ('🏆 Calculadora', 'https://github.com/ReinaldoASilva/Calculadora'),
        ('🏆 Simulador de Caos na Academia', 'https://github.com/ReinaldoASilva/simulador-de-caos-academia'),
        ('🏆 Pedra Papel Tesoura', 'https://github.com/ReinaldoASilva/Pedra---Papel---Tesoura'),
        ('🏆 Calcular-IMC', 'https://github.com/ReinaldoASilva/Calcular-IMC'),
        ('🏆 Calcular a Média de um Aluno', 'https://github.com/ReinaldoASilva/Calcular-a-media-de-um-aluno'),
        ('🏆 Locadora de carros', 'https://github.com/ReinaldoASilva/Locadora-de-carros'),
        ('🏆 Simulador da Mega Sena', 'https://github.com/ReinaldoASilva/Simulador-da-Mega-Sena')
    ]

    st.markdown("")
    projects2 = [
        ('🏆 Previsao_max_min_fechamento_eurusd', 'https://github.com/ReinaldoASilva/Previsao_max_min_fechamento_eurusd'),
        ('🏆 Prever Movimento BVBMF', 'https://github.com/ReinaldoASilva/Prever_movimento_BVBMF'),
        ('🏆 Previsão Índice Brasil', 'https://github.com/ReinaldoASilva/Previsao_indice_Brasil'),
        ('🏆 Monte Carlo', 'https://github.com/ReinaldoASilva/Monte_Carlo'),
        ('🏆 Análise de acoe', 'https://github.com/ReinaldoASilva/Analise-de-acoes'),
    ]

    st.markdown("")
    projects3 = [
        ('🏆 Obesidade Infantil', 'https://github.com/ReinaldoASilva/Obesidade-Infantil'),
        ('🏆 Shark Attack', 'https://github.com/ReinaldoASilva/Shark-Attack'),
        ('🏆 Amazon Top Books', 'https://github.com/ReinaldoASilva/Amazon-top-books')
    ]

    st.markdown("")
    projects4 = [
        ('🏆 IBGE', 'https://github.com/ReinaldoASilva/IBGE'),
    ]

    st.markdown("")
    projects5 = [
        ('🏆 Previsão Cão ou Porco', 'https://github.com/ReinaldoASilva/Previsao-cao-ou-porco'),
        ('🏆 Diamante Rick', 'https://github.com/ReinaldoASilva/Diamante-Rick'),
        ('🏆 Credit-score-classification', 'https://github.com/ReinaldoASilva/Credit-score-classification'),
        ('🏆 Employee_Turnover_Predicition', 'https://github.com/ReinaldoASilva/Employee_Turnover_Predicition'),
    ]

    # Exibe os projetos e links
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Aleatórios")
        for project_name, project_link in projects1:
            st.markdown(f"[{project_name}]({project_link})")

        st.markdown("#### Data Visualization")
        for project_name, project_link in projects3:
            st.markdown(f"[{project_name}]({project_link})")

        st.markdown("#### Aprendizagem de Máquina")
        for project_name, project_link in projects5:
            st.markdown(f"[{project_name}]({project_link})")

    with col2:
        st.markdown("#### Mercado Financeiro")
        for project_name, project_link in projects2:
            st.markdown(f"[{project_name}]({project_link})")

        st.markdown("#### Web Scraping")
        for project_name, project_link in projects4:
            st.markdown(f"[{project_name}]({project_link})")

elif select_menu == "Contato":

    # Função para gerar o QR Code
    def generate_qr_code(data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        return qr_img

    # Configurações do WhatsApp
    whatsapp_number = "+5544991653088"

    # Configurações do Streamlit
    st.subheader("Gostaria de tirar alguma dúvida ou entrar em contato?")
    st.markdown("É só scannear o qrcode abaixo e enviar uma mensagem diretamente pro meu whatsapp")

    # Gerando o QR Code com o redirecionamento para o WhatsApp
    qr_code_data = f"https://api.whatsapp.com/send?phone={whatsapp_number}"
    qr_code_img = generate_qr_code(qr_code_data)

    # Convertendo a imagem em bytes
    img_byte_arr = io.BytesIO()
    qr_code_img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Exibindo o QR Code na página
    st.image(img_byte_arr)