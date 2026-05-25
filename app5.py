# -*- coding: utf-8 -*-
"""
🎯 Portfólio Profissional - Raphael Pires
Analista de Dados & Business Intelligence
GitHub: github.com/raphaelcaxias/curriculo
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import os
import requests
from io import BytesIO

# =============================================================================
# CONFIGURAÇÃO DA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CSS PERSONALIZADO
# =============================================================================
def inject_custom_css():
    st.markdown("""
    <style>
        :root {
            --primary: #1e3a5f;
            --secondary: #2c5282;
            --accent: #3182ce;
            --bg-light: #f8fafc;
            --text-dark: #1a202c;
            --text-gray: #4a5568;
            --border: #e2e8f0;
        }
        
        .stApp { background: var(--bg-light); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        
        .hero-section {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            padding: 2.5rem;
            border-radius: 16px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(30, 58, 95, 0.2);
        }
        .hero-name { font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: -0.5px; }
        .hero-title { font-size: 1.4rem; color: #cbd5e1; margin-bottom: 1rem; font-weight: 500; }
        .hero-location { font-size: 1rem; color: #a0aec0; margin-bottom: 1.5rem; }
        
        .stButton > button {
            background: white; color: var(--secondary); border: 2px solid var(--secondary);
            border-radius: 8px; font-weight: 600; padding: 0.5rem 1.5rem; transition: all 0.3s;
        }
        .stButton > button:hover {
            background: var(--secondary); color: white; transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(44, 82, 130, 0.4);
        }
        
        .metric-card {
            background: white; padding: 1.5rem; border-radius: 12px; border-left: 5px solid var(--accent);
            box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center; height: 100%; transition: transform 0.2s;
        }
        .metric-card:hover { transform: translateY(-5px); box-shadow: 0 8px 20px rgba(0,0,0,0.12); }
        .metric-value { font-size: 1.8rem; font-weight: 700; color: var(--primary); display: block; }
        .metric-label { font-size: 0.9rem; color: var(--text-gray); margin-top: 0.5rem; display: block; }
        
        .project-card {
            background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;
            border: 1px solid var(--border); transition: all 0.3s;
        }
        .project-card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.15); border-color: var(--accent); }
        .project-title { font-size: 1.3rem; font-weight: 700; color: var(--text-dark); margin-bottom: 0.8rem; }
        .project-stack { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.8rem 0; }
        .stack-tag {
            background: #ebf4ff; color: var(--secondary); padding: 0.3rem 0.8rem; border-radius: 20px;
            font-size: 0.8rem; font-weight: 600;
        }
        
        .exp-item {
            position: relative; padding-left: 2rem; margin-bottom: 1.5rem; border-left: 4px solid var(--accent); padding-bottom: 1rem;
        }
        .exp-item::before {
            content: ''; position: absolute; left: -11px; top: 4px; width: 18px; height: 18px;
            background: var(--secondary); border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        .exp-header { display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem; }
        .exp-company { font-weight: 700; color: var(--text-dark); font-size: 1.1rem; }
        .exp-role { color: var(--accent); font-weight: 500; }
        .exp-period { background: #ebf8ff; color: var(--secondary); padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600; }
        
        .tech-category { margin-bottom: 1rem; padding: 1rem; background: white; border-radius: 8px; border: 1px solid var(--border); }
        .tech-category strong { color: var(--primary); margin-right: 0.5rem; font-size: 0.95rem; }
        .tech-badge {
            display: inline-block; background: white; border: 1px solid var(--border); padding: 0.4rem 0.8rem;
            border-radius: 6px; margin: 0.2rem; font-size: 0.85rem; color: var(--text-gray); transition: all 0.2s;
        }
        .tech-badge:hover { background: var(--secondary); color: white; border-color: var(--secondary); }
        
        a { color: var(--accent); text-decoration: none; font-weight: 600; }
        a:hover { text-decoration: underline; }
        
        @media (max-width: 768px) {
            .hero-name { font-size: 2rem; }
            .hero-title { font-size: 1.2rem; }
            .exp-header { flex-direction: column; }
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# =============================================================================
# CARREGAMENTO DE ARQUIVOS
# =============================================================================
@st.cache_data
def load_image():
    """Carrega a imagem do perfil com fallback"""
    try:
        img_url = "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg"
        response = requests.get(img_url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
    except Exception:
        pass
    
    if os.path.exists("rapha.jpeg"):
        return Image.open("rapha.jpeg")
    elif os.path.exists("assets/rapha.jpeg"):
        return Image.open("assets/rapha.jpeg")
    return None

@st.cache_data
def load_cv():
    """Carrega o currículo PDF com fallback"""
    try:
        pdf_url = "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/Curriculo_Raphael_Premium_Final.pdf"
        response = requests.get(pdf_url)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass
    
    if os.path.exists("Curriculo_Raphael_Premium_Final.pdf"):
        with open("Curriculo_Raphael_Premium_Final.pdf", "rb") as f:
            return f.read()
    elif os.path.exists("assets/Curriculo_Raphael_Premium_Final.pdf"):
        with open("assets/Curriculo_Raphael_Premium_Final.pdf", "rb") as f:
            return f.read()
    return None

profile_image = load_image()
cv_pdf = load_cv()

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
    if profile_image:
        st.image(profile_image, width=150, use_column_width=True)
    else:
        st.image("https://via.placeholder.com/150x150/1e3a5f/ffffff?text=RP", width=150)
    
    st.markdown("###  Navegação Rápida")
    st.markdown("""
    - [🏠 Início](#topo)
    - [📁 Projetos](#projetos)
    - [ Experiência](#experiencia)
    - [🎓 Formação](#formacao)
    - [📬 Contato](#contato)
    """)
    
    st.markdown("---")
    st.markdown("### 📥 Download")
    
    if cv_pdf:
        st.download_button(
            label="📄 Baixar CV (PDF)",
            data=cv_pdf,
            file_name="Curriculo_Raphael_Premium_Final.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("📁 PDF não encontrado. Verifique o nome do arquivo.")
    
    st.markdown("---")
    st.markdown("### 🔗 Conecte-se")
    st.markdown("""
    [🔗 LinkedIn](https://linkedin.com/in/raphael-pires-caxias)  
    [💻 GitHub](https://github.com/raphaelcaxias)  
    [📧 Email](mailto:raphael_caxias@hotmail.com)
    """)
    
    st.markdown("---")
    st.markdown("*Portfolio atualizado em 2026*")

# =============================================================================
# CONTEÚDO PRINCIPAL
# =============================================================================

# 1. HERO
st.markdown('<a id="topo"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-section">
    <div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px;">
            <div class="hero-name">Raphael Fernando da Silva Pires</div>
            <div class="hero-title">Analista de Dados & Business Intelligence</div>
            <div class="hero-location">📍 Volta Redonda – RJ | 💻 Trabalho Remoto</div>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
                <a href="https://linkedin.com/in/raphael-pires-caxias" target="_blank" style="background: white; color: #1e3a5f; padding: 0.7rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">🔗 LinkedIn</a>
                <a href="https://github.com/raphaelcaxias" target="_blank" style="background: rgba(255,255,255,0.15); color: white; padding: 0.7rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; border: 2px solid white;">💻 GitHub</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. PERFIL
st.markdown("### 👤 Sobre Mim")
st.markdown("""
<div style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #2c5282; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
> Analista de Dados com experiência em operações comerciais reais, atuando na construção de aplicações analíticas, automação de processos e exploração de dados para tomada de decisão. Experiência prática com SQL, Python/Pandas, Power BI e dashboards publicados em nuvem.
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# 3. MÉTRICAS
st.markdown("###  Impacto e Resultados")
col1, col2, col3, col4 = st.columns(4)

metrics = [
    {"value": "70%", "label": "Redução operacional<br><small>(Banco do Brasil)</small>"},
    {"value": "2h → 15min", "label": "Redução no ciclo<br>de análise"},
    {"value": "3", "label": "Aplicações analíticas<br>publicadas"},
    {"value": "213K+", "label": "Registros<br>processados"}
]

for i, metric in enumerate(metrics):
    with [col1, col2, col3, col4][i]:
        st.markdown(f"""
        <div class="metric-card">
            <span class="metric-value">{metric['value']}</span>
            <span class="metric-label">{metric['label']}</span>
        </div>
        """, unsafe_allow_html=True)
st.markdown("---")

# 4. TECH STACK
st.markdown("### ️ Competências Técnicas")
col_tech1, col_tech2 = st.columns(2)

with col_tech1:
    st.markdown("""
    <div class="tech-category">
        <strong>📊 BANCO DE DADOS & ETL</strong><br>
        <span class="tech-badge">SQL</span> <span class="tech-badge">PostgreSQL</span> <span class="tech-badge">Pandas</span> <span class="tech-badge">NumPy</span> <span class="tech-badge">ETL</span>
    </div>
    <div class="tech-category">
        <strong>📈 BI & VISUALIZAÇÃO</strong><br>
        <span class="tech-badge">Power BI</span> <span class="tech-badge">Looker Studio</span> <span class="tech-badge">Plotly</span> <span class="tech-badge">Streamlit</span>
    </div>
    """, unsafe_allow_html=True)

with col_tech2:
    st.markdown("""
    <div class="tech-category">
        <strong>🔍 ANÁLISE & ESTATÍSTICA</strong><br>
        <span class="tech-badge">KPIs</span> <span class="tech-badge">Statsmodels</span> <span class="tech-badge">Análise Exploratória</span>
    </div>
    <div class="tech-category">
        <strong>⚙️ FERRAMENTAS</strong><br>
        <span class="tech-badge">Excel/VBA</span> <span class="tech-badge">Git</span> <span class="tech-badge">IA Generativa</span> <span class="tech-badge">Automação</span>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

# 5. PROJETOS
st.markdown('<a id="projetos"></a>', unsafe_allow_html=True)
st.markdown("### 🚀 Projetos em Destaque")

projects = [
    {
        "title": "🇧🇷 Desenrola Brasil - Dashboard Executivo",
        "stack": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "desc": "Dashboard interativo com dados oficiais do Banco Central sobre o programa Desenrola Brasil. Inclui KPIs, segmentação analítica por região/valor, identificação de padrões em renegociação de dívidas e visualizações interativas para tomada de decisão.",
        "app": "https://desenrolabrasil.streamlit.app",
        "github": "https://github.com/raphaelcaxias/DESENROLA_BRASIL"
    },
    {
        "title": "🔬 CNPq Analytics - Análise de Investimentos",
        "stack": ["Python", "PostgreSQL", "Plotly", "Streamlit", "ETL"],
        "desc": "Pipeline ETL completo e análise exploratória de 213 mil registros públicos do CNPq. Mapeamento de investimentos em pesquisa científica, identificação de desigualdades regionais e padrões de financiamento no Brasil.",
        "app": None,
        "github": "https://github.com/raphaelcaxias/cnpq-analytics"
    },
    {
        "title": "⛽ Dashboard ANP - Preços de Combustíveis",
        "stack": ["Python", "Pandas", "Plotly", "Streamlit"],
        "desc": "Dashboard com dados públicos da ANP (Agência Nacional do Petróleo). Filtros regionais dinâmicos, análise temporal de preços de combustíveis no varejo brasileiro e comparações entre estados e municípios.",
        "app": None,
        "github": "https://github.com/raphaelcaxias/anp-combustiveis-dashboard"
    }
]

for proj in projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{proj['title']}</div>
        <div class="project-stack">
            {''.join([f'<span class="stack-tag">{t}</span>' for t in proj['stack']])}
        </div>
        <p style="color: var(--text-gray); margin: 1rem 0; line-height: 1.6;">{proj['desc']}</p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
            <a href="{proj['github']}" target="_blank" style="background: #f0f9ff; color: var(--secondary); padding: 0.6rem 1.2rem; border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem;">💻 Ver Código</a>
            {f'<a href="{proj["app"]}" target="_blank" style="background: var(--secondary); color: white; padding: 0.6rem 1.2rem; border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem;">🌐 Acessar App</a>' if proj['app'] else ''}
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

# 6. EXPERIÊNCIA
st.markdown('<a id="experiencia"></a>', unsafe_allow_html=True)
st.markdown("### 💼 Trajetória Profissional")

exp_items = [
    {
        "empresa": "Jardim do Éden", "cargo": "Gestão Comercial & Dados", "periodo": "2009 – Atual",
        "bullets": [
            "Estruturação de fluxo analítico comercial com dashboards que reduziram tempo de análise de 2 horas para 15 minutos",
            "Desenvolvimento de consultas SQL e automação de processos para suporte a faturamento, margem de lucro e controle de estoque",
            "Implementação de IA generativa para automação de tarefas operacionais repetitivas"
        ]
    },
    {
        "empresa": "J Sintonía", "cargo": "Analista de KPIs & Operações", "periodo": "2014 – 2026",
        "bullets": [
            "Monitoramento contínuo de KPIs de vendas, margem de contribuição e giro de estoque",
            "Desenvolvimento de relatórios automatizados para gestão estratégica"
        ]
    },
    {
        "empresa": "Banco do Brasil", "cargo": "Automação & Dados", "periodo": "2008 – 2010",
        "bullets": [
            "Automação de processos em 20 agências utilizando VBA/Excel",
            "Redução de 70% no tempo operacional com implementação de macros e planilhas inteligentes"
        ]
    }
]

for exp in exp_items:
    st.markdown(f"""
    <div class="exp-item">
        <div class="exp-header">
            <div>
                <div class="exp-company">{exp['empresa']}</div>
                <div class="exp-role">{exp['cargo']}</div>
            </div>
            <div class="exp-period">{exp['periodo']}</div>
        </div>
        <ul style="padding-left: 1.2rem; color: var(--text-gray); line-height: 1.8;">
            {''.join([f'<li>{b}</li>' for b in exp['bullets']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

# 7. FORMAÇÃO
st.markdown('<a id="formacao"></a>', unsafe_allow_html=True)
col_form1, col_form2 = st.columns(2)

with col_form1:
    st.markdown("#### 🎓 Formação Acadêmica")
    st.markdown("""
    **Sistemas de Informação**  
    UniFOA - Centro Universitário de Volta Redonda
    
    **Técnico em Informática**  
    CIBA - Centro de Informática e Business Administration
    """)

with col_form2:
    st.markdown("#### 📚 Cursos & Certificações")
    st.markdown("""
    **Hashtag Treinamentos:**
    - ✅ SQL para Análise de Dados
    - ✅ Power BI Completo (Básico ao Avançado)
    - ✅ Python para Análise de Dados (Pandas)
    - ✅ Algoritmos e Lógica de Programação
    - ✅ IA Aplicada a Negócios
    """)
st.markdown("---")

# 8. CONTATO & RODAPÉ
st.markdown('<a id="contato"></a>', unsafe_allow_html=True)
st.markdown("### 📬 Vamos Trabalhar Juntos?")

col_contact1, col_contact2 = st.columns([2, 1])

with col_contact1:
    st.markdown("""
    Estou aberto a oportunidades como **Analista de Dados**, **Analista de BI** ou projetos freelance de análise e automação.
    
    Se você busca um profissional com experiência prática em transformar dados em insights acionáveis, vamos conversar!
    
    **📧 Email:** [raphael_caxias@hotmail.com](mailto:raphael_caxias@hotmail.com)  
    **📱 WhatsApp:** [(24) 99227-5226](https://wa.me/5524992275226)  
    **📍 Localização:** Volta Redonda – RJ | Disponível para trabalho remoto
    """)

with col_contact2:
    st.markdown("### 🔗 Links Importantes")
    st.markdown("""
    [🔗 LinkedIn](https://linkedin.com/in/raphael-pires-caxias)  
    [💻 GitHub](https://github.com/raphaelcaxias)  
    
    **Repositórios:**
    - [Desenrola Brasil](https://github.com/raphaelcaxias/DESENROLA_BRASIL)
    - [CNPq Analytics](https://github.com/raphaelcaxias/cnpq-analytics)
    - [Dashboard ANP](https://github.com/raphaelcaxias/anp-combustiveis-dashboard)
    """)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #718096; font-size: 0.9rem; padding: 2rem; background: white; border-radius: 12px; margin-top: 2rem;">
    <strong style="color: var(--primary); font-size: 1.1rem;">Raphael Fernando da Silva Pires</strong><br>
    Analista de Dados & Business Intelligence<br>
    <small style="margin-top: 0.5rem; display: block;">
        Portfolio desenvolvido com Streamlit • GitHub: 
        <a href="https://github.com/raphaelcaxias/curriculo" target="_blank">github.com/raphaelcaxias/curriculo</a><br>
        © 2026 - Todos os direitos reservados
    </small>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# DEMONSTRAÇÃO INTERATIVA (OPCIONAL)
# =============================================================================
with st.expander("📊 Ver Demonstração de Análise Interativa", expanded=False):
    st.markdown("Exemplo de dashboard interativo com Plotly:")
    
    df_demo = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Vendas': [120, 145, 132, 168, 189, 201],
        'Meta': [130, 140, 145, 160, 180, 200]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_demo['Mês'], y=df_demo['Vendas'], name='Vendas Realizadas', mode='lines+markers', line=dict(color='#2c5282', width=3), marker=dict(size=8)))
    fig.add_trace(go.Scatter(x=df_demo['Mês'], y=df_demo['Meta'], name='Meta', mode='lines', line=dict(color='#38a169', width=2, dash='dash')))
    fig.update_layout(title='Acompanhamento de Vendas vs Meta', height=350, margin=dict(t=60, b=0, l=0, r=0), hovermode='x unified', legend=dict(orientation='h', y=1.05))
    st.plotly_chart(fig, use_container_width=True)
    
    col_a, col_b = st.columns(2)
    with col_a: st.metric("Crescimento Acumulado", "+67.5%", "+12.3%")
    with col_b: st.metric("Atingimento da Meta", "100.5%", "+0.5%")
