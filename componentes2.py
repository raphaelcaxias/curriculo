"""
componentes2.py - Todos os componentes visuais e funções de renderização
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import base64
from datetime import datetime, timedelta
from config2 import (
    FOTO_CANDIDATOS, PDF_CANDIDATOS, FOTO_FALLBACK,
    DADOS_PESSOAIS, PERFIL_PROFISSIONAL, CITACAO_PESSOAL, KPIS, TECH_STACK,
    CERTIFICACOES, FORMACAO, IDIOMAS, PROJETOS, EXPERIENCIAS,
    LINKS_SOCIAIS, MODOS_VISUALIZACAO, SOBRE_MIM, get_colors
)

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================
def get_foto_path():
    for caminho in FOTO_CANDIDATOS:
        if os.path.exists(caminho):
            return caminho
    return None

def get_foto_base64(foto_path):
    if foto_path and os.path.exists(foto_path):
        with open(foto_path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()
            ext = foto_path.split('.')[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            return f"data:{mime};base64,{encoded}"
    return None

def get_pdf_path():
    for caminho in PDF_CANDIDATOS:
        if os.path.exists(caminho):
            return caminho
    return None

def get_pdf_base64(pdf_path):
    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()
            return f"data:application/pdf;base64,{encoded}"
    return None

# ============================================================================
# NAVBAR
# ============================================================================
def render_navbar(page_atual):
    theme_label = "☀️" if st.session_state.theme == "dark" else "🌙"
    nome_parts = DADOS_PESSOAIS['nome'].split()
    primeiro = nome_parts[0]
    ultimo = nome_parts[-1]
    
    st.markdown(f"""
    <nav class="navbar">
        <a href="/?page=home" class="navbar-brand">
            <span class="brand-dot"></span>
            {primeiro} <span>{ultimo}</span>
        </a>
        <div class="navbar-links">
            <a href="/?page=home" class="nav-link {'active' if page_atual == 'home' else ''}">Início</a>
            <a href="/?page=curriculo" class="nav-link {'active' if page_atual == 'curriculo' else ''}">Currículo</a>
            <a href="/?page=projetos" class="nav-link {'active' if page_atual == 'projetos' else ''}">Projetos</a>
            <a href="/?page=analytics" class="nav-link {'active' if page_atual == 'analytics' else ''}">Analytics</a>
            <a href="#contato" class="nav-link">Contato</a>
            <div class="theme-toggle" onclick="window.location.href='?theme_toggle=1&page={page_atual}'" title="Alternar tema">
                {theme_label}
            </div>
        </div>
    </nav>
    """, unsafe_allow_html=True)

# ============================================================================
# MODE SELECTOR
# ============================================================================
def render_mode_selector():
    if "modo" not in st.session_state:
        st.session_state.modo = "Dados & BI"
    
    st.markdown("""
    <div style="padding:3rem 2rem 0;text-align:center;">
        <div style="font-size:0.78rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--primary);margin-bottom:1rem;">
            🎯 Como você quer me conhecer?
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    modos = list(MODOS_VISUALIZACAO.keys())
    cols = st.columns(len(modos))
    
    for i, modo in enumerate(modos):
        with cols[i]:
            ativo = st.session_state.modo == modo
            if st.button(
                modo,
                key=f"modo_{i}",
                use_container_width=True,
                type="primary" if ativo else "secondary"
            ):
                st.session_state.modo = modo
                st.rerun()
    
    modo_atual = st.session_state.modo
    st.markdown(f"""
    <div style="text-align:center;margin-top:1rem;color:var(--text-muted);font-size:0.9rem;">
        {MODOS_VISUALIZACAO[modo_atual]['descricao']}
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# HERO
# ============================================================================
def render_hero():
    foto_path = get_foto_path()
    foto_b64 = get_foto_base64(foto_path)
    foto_url = foto_b64 if foto_b64 else FOTO_FALLBACK
    pdf_path = get_pdf_path()
    pdf_b64 = get_pdf_base64(pdf_path)
    
    modo_atual = st.session_state.get("modo", "Dados & BI")
    cor_destaque = MODOS_VISUALIZACAO[modo_atual]["cor_destaque"]
    
    nome_parts = DADOS_PESSOAIS['nome'].split()
    primeiro = nome_parts[0]
    ultimo = nome_parts[-1]
    
    botao_cv = ""
    if pdf_b64:
        botao_cv = f'<a href="{pdf_b64}" download="Curriculo_Raphael.pdf" class="btn-secondary">📄 Baixar CV</a>'
    
    st.markdown(f"""
    <section class="hero-full" id="topo">
        <div class="hero-grid-bg"></div>
        <div class="hero-content">
            <div class="hero-photo-wrapper">
                <div class="hero-photo-ring"></div>
                <img src="{foto_url}" alt="{DADOS_PESSOAIS['nome']}" class="hero-photo">
                <div class="hero-status-badge" title="Disponível"></div>
            </div>
            <div class="hero-text">
                <div class="role-tag">
                    <span style="width:6px;height:6px;border-radius:50%;background:{cor_destaque};"></span>
                    {DADOS_PESSOAIS['titulo']}
                </div>
                <h1>{primeiro} <span class="gradient-name">{ultimo}</span></h1>
                <p class="subtitle">{PERFIL_PROFISSIONAL.strip()}</p>
                <div class="hero-quote">{CITACAO_PESSOAL.strip()}</div>
                <div class="badge-group">
                    <span class="badge">📍 {DADOS_PESSOAIS['localizacao']}</span>
                    <span class="badge">🏠 {DADOS_PESSOAIS['modalidades'][0]}</span>
                    <span class="badge">✈️ {DADOS_PESSOAIS['modalidades'][1]}</span>
                </div>
                <div class="cta-group">
                    <a href="#experiencia" class="btn-primary">💼 Conhecer minha trajetória</a>
                    {botao_cv}
                    <a href="{LINKS_SOCIAIS['linkedin']}" target="_blank" class="btn-secondary">💼 LinkedIn</a>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# ============================================================================
# SOBRE MIM
# ============================================================================
def render_sobre_mim():
    st.markdown(f"""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">👤 Quem sou eu</span>
                <h2>{SOBRE_MIM['titulo']}</h2>
            </div>
            <div class="sobre-section">
                <p class="sobre-text">{SOBRE_MIM['texto'].strip()}</p>
                <div class="valores-grid">
    """, unsafe_allow_html=True)
    
    for valor in SOBRE_MIM['valores']:
        st.markdown(f"""
                <div class="valor-card">
                    <div class="valor-icon">{valor['icone']}</div>
                    <div class="valor-title">{valor['titulo']}</div>
                    <div class="valor-desc">{valor['desc']}</div>
                </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# KPIs
# ============================================================================
def render_kpis():
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">📈 Números que contam histórias</span>
                <h2>Impacto real, não apenas métricas</h2>
                <p>Cada número aqui representa um problema que resolvi</p>
            </div>
            <div class="kpi-grid">
    """, unsafe_allow_html=True)
    
    cols = st.columns(len(KPIS))
    for i, kpi in enumerate(KPIS):
        with cols[i]:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon">{kpi['icone']}</div>
                <div class="kpi-value">{kpi['valor']}</div>
                <div class="kpi-label">{kpi['label']}</div>
                <div class="kpi-context">{kpi['contexto']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# TECH STACK
# ============================================================================
def render_tech_stack():
    modo_atual = st.session_state.get("modo", "Dados & BI")
    destaques = MODOS_VISUALIZACAO[modo_atual]["destaques"]
    
    st.markdown("""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">⚡ Ferramentas que uso</span>
                <h2>Stack tecnológica</h2>
                <p>Tecnologias que domino no dia a dia</p>
            </div>
            <div class="tech-grid">
    """, unsafe_allow_html=True)
    
    techs_ordenadas = []
    for destaque in destaques:
        if destaque in TECH_STACK:
            techs_ordenadas.append((destaque, TECH_STACK[destaque]))
    for tech, dados in TECH_STACK.items():
        if tech not in destaques:
            techs_ordenadas.append((tech, dados))
    
    for tech, dados in techs_ordenadas:
        nivel_class = dados['nivel'].lower().replace('í', 'i').replace('á', 'a')
        itens_html = "".join([f'<span class="tech-item">{item}</span>' for item in dados['itens']])
        destaque_badge = "⭐ " if tech in destaques else ""
        
        st.markdown(f"""
        <div class="tech-card">
            <div class="tech-card-header">
                <div class="tech-icon">{dados['icone']}</div>
                <div>
                    <div class="tech-name">{destaque_badge}{tech}</div>
                    <span class="tech-level {nivel_class}">{dados['nivel']}</span>
                </div>
            </div>
            <div class="tech-items">{itens_html}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# SKILLS CHART
# ============================================================================
def render_skills_chart():
    colors = get_colors()
    
    df = pd.DataFrame({
        "Tecnologia": list(TECH_STACK.keys()),
        "Proficiência": [95 if d['nivel'] == 'Expert' else (82 if d['nivel'] == 'Avançado' else 60) for d in TECH_STACK.values()],
        "Nível": [d['nivel'] for d in TECH_STACK.values()]
    })
    
    fig = px.bar(
        df, x="Proficiência", y="Tecnologia", color="Nível",
        orientation="h", color_discrete_sequence=colors["chart_colors"],
        template=colors["plotly_template"], text="Proficiência"
    )
    
    fig.update_layout(
        height=420, margin=dict(l=20, r=60, t=20, b=40),
        xaxis=dict(range=[0, 110], showgrid=True, gridcolor="rgba(148,163,184,0.12)", zeroline=False),
        yaxis=dict(showgrid=False, categoryorder='total ascending'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter", color=colors["text"], size=12),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=True
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color=colors["text"], size=12, family="Inter"),
        marker=dict(cornerradius=6)
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# EXPERIÊNCIAS
# ============================================================================
def render_experiencias():
    modo_atual = st.session_state.get("modo", "Dados & BI")
    ordem = MODOS_VISUALIZACAO[modo_atual]["ordem_experiencias"]
    
    st.markdown("""
    <div class="section-glass" id="experiencia">
        <div class="container">
            <div class="section-header">
                <span class="label">💼 Minha trajetória</span>
                <h2>Experiência profissional</h2>
                <p>Cada experiência me trouxe algo único</p>
            </div>
            <div class="timeline">
    """, unsafe_allow_html=True)
    
    for idx in ordem:
        exp = EXPERIENCIAS[idx]
        badge_html = f'<span class="timeline-badge">{exp["status"]}</span>' if exp.get("status") else ""
        tags_html = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp['periodo']}</span> {badge_html}
                <div class="timeline-role">{exp['cargo']}</div>
                <div class="timeline-company">{exp['empresa']} · {exp['tipo']}</div>
                <div class="timeline-historia">{exp['historia']}</div>
                <div>{tags_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# PROJETOS
# ============================================================================
def render_projetos():
    st.markdown("""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">🚀 Projetos que construí</span>
                <h2>Analytics na prática</h2>
                <p>Projetos reais com dados reais</p>
            </div>
            <div class="project-grid">
    """, unsafe_allow_html=True)
    
    for projeto in PROJETOS:
        desc_html = "<br>".join([f"• {d}" for d in projeto["descricao"]])
        techs_html = "".join([f'<span class="project-tag">{t}</span>' for t in projeto["tecnologias"]])
        
        if projeto.get("url"):
            link_btn = f'<a href="{projeto["url"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver projeto</a>'
        else:
            link_btn = f'<a href="{LINKS_SOCIAIS["github"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">💻 Ver no GitHub</a>'
        
        st.markdown(f"""
        <div class="project-card">
            <div class="project-icon">{projeto['icone']}</div>
            <h3>{projeto['nome']}</h3>
            <div class="project-subtitle">{projeto['subtitulo']}</div>
            <p>{desc_html}</p>
            <div class="project-context">💡 {projeto['contexto']}</div>
            <div class="project-tech">{techs_html}</div>
            {link_btn}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# CERTIFICAÇÕES
# ============================================================================
def render_certificacoes():
    colors = get_colors()
    
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">🎓 Aprendizado contínuo</span>
                <h2>Certificações</h2>
                <p>Nunca parei de estudar</p>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
    """, unsafe_allow_html=True)
    
    for cert in CERTIFICACOES:
        cursos_html = " · ".join(cert["cursos"])
        
        if "Em andamento" in cert["status"]:
            status_badge = f'<div style="display:inline-block;background:{colors["warning"]};color:white;padding:0.25rem 0.9rem;border-radius:999px;font-size:0.75rem;font-weight:700;">🔄 {cert["status"]}</div>'
            if "modulos_concluidos" in cert:
                status_badge += f'<div class="progress-bar"><div class="progress-fill" style="width:40%;"></div></div>'
                status_badge += f'<div style="font-size:0.78rem;color:{colors["text_muted"]};margin-top:0.5rem;font-weight:600;">{cert["modulos_concluidos"]} módulos concluídos</div>'
        else:
            status_badge = f'<div style="display:inline-block;background:{colors["success"]};color:white;padding:0.25rem 0.9rem;border-radius:999px;font-size:0.75rem;font-weight:700;">✓ {cert["status"]}</div>'
        
        st.markdown(f"""
        <div class="glass-card" style="text-align:center;">
            <div style="font-size:3rem;margin-bottom:1rem;">{cert['icone']}</div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:0.75rem;">{cert['instituicao']}</h3>
            <p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;margin-bottom:1rem;">{cursos_html}</p>
            {status_badge}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# FORMAÇÃO
# ============================================================================
def render_formacao():
    st.markdown("""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">🎓 Base acadêmica</span>
                <h2>Formação</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
    """, unsafe_allow_html=True)
    
    for form in FORMACAO:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;">
                <div style="width:56px;height:56px;border-radius:16px;background:var(--primary-light);display:flex;align-items:center;justify-content:center;font-size:1.8rem;">🎓</div>
                <div>
                    <h4 style="font-size:1.1rem;font-weight:700;margin:0;">{form['curso']}</h4>
                    <div style="color:var(--text-muted);font-size:0.9rem;">{form['instituicao']}</div>
                </div>
            </div>
            <div style="display:inline-block;background:var(--primary-light);border:1px solid var(--tag-border);padding:0.25rem 0.9rem;border-radius:999px;font-size:0.78rem;font-weight:600;color:var(--primary);">Concluído em {form['ano']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# IDIOMAS
# ============================================================================
def render_idiomas():
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">🌐 Idiomas</span>
                <h2>Competências linguísticas</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;max-width:600px;margin:0 auto;">
    """, unsafe_allow_html=True)
    
    for idioma in IDIOMAS:
        bandeira = '🇷' if 'Português' in idioma['idioma'] else '🇺'
        st.markdown(f"""
        <div class="glass-card" style="text-align:center;">
            <div style="font-size:2.5rem;margin-bottom:0.5rem;">{bandeira}</div>
            <h4 style="font-size:1.1rem;font-weight:700;margin-bottom:0.5rem;">{idioma['idioma']}</h4>
            <div style="display:inline-block;background:var(--primary-light);border:1px solid var(--tag-border);padding:0.25rem 0.9rem;border-radius:999px;font-size:0.78rem;font-weight:600;color:var(--primary);">{idioma['nivel']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
def render_footer():
    tel_limpo = DADOS_PESSOAIS['telefone1'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    footer_html = f"""
    <div class="footer" id="contato">
        <div style="display:inline-flex;align-items:center;gap:0.6rem;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.25);padding:0.4rem 1.2rem;border-radius:999px;font-size:0.82rem;font-weight:600;color:var(--success);margin-bottom:1.5rem;">
            <span style="width:8px;height:8px;border-radius:50%;background:var(--success);box-shadow:0 0 12px var(--success);animation:pulse 2s infinite;"></span>
            Disponível para novas oportunidades
        </div>
        <h3>Vamos conversar?</h3>
        <p style="color:var(--text-muted);font-size:1.05rem;margin-bottom:2rem;">Se você busca alguém que entende de negócio E de dados, vamos tomar um café.</p>
        
        <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:2rem;">
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;font-weight:500;">📍 {DADOS_PESSOAIS['localizacao']}</span>
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;font-weight:500;">🏠 {DADOS_PESSOAIS['modalidades'][0]}</span>
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;font-weight:500;">✈️ {DADOS_PESSOAIS['modalidades'][1]}</span>
        </div>
        
        <div class="footer-links">
            <a href="{LINKS_SOCIAIS['linkedin']}" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="{LINKS_SOCIAIS['github']}" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="{LINKS_SOCIAIS['email']}" class="footer-link">✉️ E-mail</a>
            <a href="{LINKS_SOCIAIS['whatsapp']}" target="_blank" class="footer-link">📱 WhatsApp</a>
            <a href="tel:{tel_limpo}" class="footer-link">📞 {DADOS_PESSOAIS['telefone1']}</a>
        </div>
        
        <p class="footer-copy">© 2026 {DADOS_PESSOAIS['nome']} · Feito com ❤️ e muito café ☕</p>
    </div>
    <a href="#topo" class="scroll-top" title="Voltar ao topo">↑</a>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)

# ============================================================================
# PÁGINAS
# ============================================================================
def render_pagina_home():
    render_hero()
    render_sobre_mim()
    render_mode_selector()
    render_kpis()
    render_tech_stack()
    render_experiencias()
    render_projetos()
    
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">📊 Visualização de skills</span>
                <h2>Nível de domínio</h2>
            </div>
    """, unsafe_allow_html=True)
    render_skills_chart()
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    render_certificacoes()
    render_formacao()
    render_idiomas()

def render_pagina_curriculo():
    st.markdown("""
    <div class="page-header">
        <h1>📄 Currículo Completo</h1>
        <p>Toda minha trajetória organizada</p>
    </div>
    """, unsafe_allow_html=True)
    
    render_sobre_mim()
    render_mode_selector()
    render_kpis()
    render_tech_stack()
    render_experiencias()
    render_certificacoes()
    render_formacao()
    render_idiomas()

def render_pagina_projetos():
    st.markdown("""
    <div class="page-header">
        <h1> Projetos de Analytics</h1>
        <p>Construídos com Python, Streamlit e dados reais</p>
    </div>
    """, unsafe_allow_html=True)
    
    render_projetos()
    
    colors = get_colors()
    
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">📊 Tecnologias mais usadas</span>
                <h2>Stack dos projetos</h2>
            </div>
    """, unsafe_allow_html=True)
    
    tech_count = {}
    for projeto in PROJETOS:
        for tech in projeto["tecnologias"]:
            tech_count[tech] = tech_count.get(tech, 0) + 1
    
    df_tech = pd.DataFrame({
        "Tecnologia": list(tech_count.keys()),
        "Projetos": list(tech_count.values())
    }).sort_values("Projetos", ascending=True)
    
    fig = px.bar(
        df_tech, x="Projetos", y="Tecnologia", orientation="h",
        color_discrete_sequence=[colors["primary"]],
        template=colors["plotly_template"], text="Projetos"
    )
    fig.update_layout(
        height=350, margin=dict(l=20, r=40, t=20, b=40),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=False),
        font=dict(family="Inter", color=colors["text"]),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(textposition="outside")
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

def render_pagina_analytics():
    colors = get_colors()
    
    st.markdown("""
    <div class="page-header">
        <h1>📊 Analytics Interativo</h1>
        <p>Dashboards construídos em Streamlit + Plotly</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="padding:2rem;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)
    
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ ANP Combustíveis", "📈 Impacto Operacional"])
    
    with tabs[0]:
        np.random.seed(42)
        regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
        status_opts = ["Renegociado", "Em Negociação", "Inadimplente"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[.45, .28, .15, .07, .05]),
            "Valor": np.random.lognormal(8.5, 1.2, 400),
            "Status": np.random.choice(status_opts, 400, p=[.65, .25, .10])
        })
        
        col1, col2 = st.columns(2)
        reg = col1.multiselect("Região", regioes, default=regioes)
        stat = col2.multiselect("Status", status_opts, default=status_opts)
        filtro = df[df["Região"].isin(reg) & df["Status"].isin(stat)]
        
        if filtro.empty:
            st.info("Nenhum registro encontrado.")
        else:
            k1, k2, k3 = st.columns(3)
            k1.metric("Contratos", f"{len(filtro):,}")
            k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f} M")
            k3.metric("Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            
            a, b = st.columns(2)
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=.6,
                         template=colors["plotly_template"],
                         color_discrete_sequence=colors["chart_colors"])
            fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font=dict(color=colors["text"]), height=380)
            fig2 = px.histogram(filtro, x="Status", color="Status",
                               template=colors["plotly_template"],
                               color_discrete_sequence=colors["chart_colors"])
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font=dict(color=colors["text"]), height=380, showlegend=False)
            a.plotly_chart(fig1, use_container_width=True)
            b.plotly_chart(fig2, use_container_width=True)
    
    with tabs[1]:
        estados = ["SP", "RJ", "MG", "PR"]
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
        dados = []
        np.random.seed(1)
        for e in estados:
            preco = 5.4
            for m in meses:
                preco += np.random.normal(0, .10)
                dados.append([e, m, preco])
        df = pd.DataFrame(dados, columns=["Estado", "Mês", "Preço"])
        estado = st.selectbox("Estado", estados)
        f = df[df["Estado"] == estado]
        
        st.metric("Preço Médio", f"R$ {f['Preço'].mean():.2f}")
        fig = px.line(f, x="Mês", y="Preço", markers=True,
                     template=colors["plotly_template"],
                     color_discrete_sequence=[colors["chart_colors"][0]])
        fig.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                         font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
    
    with tabs[2]:
        antes = [120, 125, 118, 130, 122, 128, 126, 124, 129, 127, 125, 130]
        depois = [95, 70, 55, 45, 38, 35, 33, 32, 30, 29, 28, 27]
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        df = pd.DataFrame({
            "Mês": meses * 2,
            "Horas": antes + depois,
            "Período": ["Antes"] * 12 + ["Depois"] * 12
        })
        fig = px.area(df, x="Mês", y="Horas", color="Período",
                     template=colors["plotly_template"],
                     color_discrete_sequence=[colors["chart_colors"][0], colors["chart_colors"][3]])
        fig.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                         font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
        
        k1, k2, k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93%")
        k2.metric("Custo Evitado", "R$ 185 mil", "+185 mil")
        k3.metric("Projetos", "24", "+60%")
    
    st.markdown('</div>', unsafe_allow_html=True)
