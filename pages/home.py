import streamlit as st
import os
from config import get_colors
from components import render_skills_chart

def render_home():
    c = get_colors()

    # ===== DETECÇÃO DA FOTO =====
    foto_caminhos = [
        "rapha.jpeg", "rapha.jpg",
        "assets/rapha.jpeg", "assets/rapha.jpg",
        "foto.jpeg", "foto.jpg"
    ]
    foto = None
    for caminho in foto_caminhos:
        if os.path.exists(caminho):
            foto = caminho
            break
    if foto is None:
        foto = "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff"

    # ===== HERO =====
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:2rem; padding:2rem 0; flex-wrap:wrap;">
        <img src="{foto}" style="width:180px; height:180px; border-radius:50%; object-fit:cover; border:4px solid {c['primary']}; box-shadow:0 10px 30px rgba(0,0,0,0.2);">
        <div style="flex:1;">
            <h1 style="font-size:2.8rem; font-weight:800; margin:0;">Raphael <span style="color:{c['primary']};">Pires</span></h1>
            <p style="font-size:1.2rem; color:{c['text_muted']};">Analista de Dados &bull; Business Intelligence</p>
            <p style="font-size:1rem; color:{c['text']}; max-width:600px;">Transformando dados em decisões estratégicas com Python, SQL, Power BI, AWS e IA.</p>
            <div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:1rem;">
                <span style="background:{c['tag_bg']}; border:1px solid {c['tag_border']}; padding:0.3rem 1rem; border-radius:999px;">Python</span>
                <span style="background:{c['tag_bg']}; border:1px solid {c['tag_border']}; padding:0.3rem 1rem; border-radius:999px;">SQL</span>
                <span style="background:{c['tag_bg']}; border:1px solid {c['tag_border']}; padding:0.3rem 1rem; border-radius:999px;">Power BI</span>
                <span style="background:{c['tag_bg']}; border:1px solid {c['tag_border']}; padding:0.3rem 1rem; border-radius:999px;">AWS</span>
                <span style="background:{c['tag_bg']}; border:1px solid {c['tag_border']}; padding:0.3rem 1rem; border-radius:999px;">IA Generativa</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ===== KPIs =====
    st.markdown("## 📈 Indicadores")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Experiência", "17+ anos")
    col2.metric("Redução", "70%")
    col3.metric("Registros", "213 mil")
    col4.metric("Dashboards", "15+")
    col5.metric("Análises", "2h → 15min")
    col6.metric("Dados", "R$ 50 bi")

    st.divider()

    # ===== EXPERIÊNCIA =====
    st.header("💼 Experiência profissional")
    with st.container():
        experiences = [
            {"periodo": "2014 – Presente", "cargo": "Analista de Dados & BI", "empresa": "NSM Comércio", "desc": "Centralização de dados, indicadores estratégicos e automação. Redução de 70% do tempo operacional.", "tags": ["Dados","Governança","Indicadores","Automação"], "badge": "Atual"},
            {"periodo": "2012 – Presente", "cargo": "Fundador & Analista de Dados", "empresa": "Jardim do Éden", "desc": "Dashboards com Python, SQL, Power BI e Looker Studio. Redução de 2h para 15 min por análise.", "tags": ["Power BI","Python","SQL","IA Generativa"], "badge": ""},
            {"periodo": "2010 – 2014", "cargo": "Fundador & Analista de KPIs", "empresa": "J Sintonía", "desc": "KPIs de vendas, margem e rentabilidade. Análise de viabilidade econômica.", "tags": ["BI","KPIs","Dashboards"], "badge": ""},
            {"periodo": "2009 – 2010", "cargo": "Estagiário de Automação e Dados", "empresa": "Banco do Brasil", "desc": "Desenvolvimento de macros VBA em 20 agências, reduzindo 70% do tempo operacional.", "tags": ["VBA","Automação","Eficiência"], "badge": ""}
        ]
        for exp in experiences:
            with st.expander(f"{exp['periodo']} – {exp['cargo']} @ {exp['empresa']}"):
                st.write(exp['desc'])
                if exp['badge']:
                    st.caption(f"🏷️ {exp['badge']}")
                st.caption(" ".join([f"`{t}`" for t in exp['tags']]))

    st.divider()

    # ===== PROJETOS =====
    st.header("🚀 Projetos de Analytics")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🇧🇷 Desenrola Brasil")
        st.write("Painel analítico com dados do Banco Central, KPIs e séries temporais.")
        st.link_button("Ver App", "https://desenrolabrasil.streamlit.app")
        st.markdown("#### 🔬 CNPq Analytics")
        st.write("ETL e análise de 213 mil bolsas e R$ 1,2 bi em investimentos.")
        st.link_button("Ver App", "https://cnpa-analytics.streamlit.app")
    with col2:
        st.markdown("#### ⛽ Análise ANP")
        st.write("Dashboard interativo de preços de combustíveis com dados oficiais.")
        st.link_button("Ver Projeto", "https://github.com/raphaelcaxias")
        st.markdown("#### 💎 Portfólio Premium")
        st.write("Este portfólio em Streamlit com design premium e glassmorphism.")
        st.link_button("Ver Código", "https://github.com/raphaelcaxias")

    st.divider()

    # ===== CERTIFICAÇÕES =====
    st.header("📜 Certificações e Formação")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**📘 Hashtag Treinamentos**")
        st.write("SQL Avançado, Power BI, Python para Dados, IA Aplicada")
    with cols[1]:
        st.markdown("**☁️ AWS Educate**")
        st.write("8 módulos: Cloud Computing, Console, Storage, ML, Sustainability")
        st.progress(40, text="Progresso")
    with cols[2]:
        st.markdown("**🎯 Meta 2026**")
        st.write("Certificação AWS Cloud Practitioner – em preparação")

    st.divider()

    # ===== AWS JOURNEY =====
    st.header("☁️ Jornada AWS")
    st.write("Atualmente em trilha de certificação com foco em arquitetura de dados e ML na nuvem.")
    st.progress(40, text="Progresso atual")
    st.caption("🎯 Meta: AWS Cloud Practitioner (Dez/2026)")

    st.divider()

    # ===== SKILLS (gráfico) =====
    st.header("🛠 Competências")
    render_skills_chart()
