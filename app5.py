import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA (Sempre o primeiro comando)
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# 2. DESIGN DO SISTEMA (CSS Moderno e Injeção de Tema Nativo)
# ============================================================================
# Reduzimos o CSS para focar apenas no refinamento estético dos cards e fontes
st.html("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Configurações Globais de Tipografia */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Customização dos Containers Nativos (Cards Premium) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: var(--st-color-background-secondary);
        border: 1px solid rgba(148, 163, 184, 0.12) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 20px -8px rgba(0, 0, 0, 0.15);
        border-color: var(--st-color-primary) !important;
    }
    
    /* Badges de Tecnologia */
    .tech-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.08);
        color: #6366f1;
        border: 1px solid rgba(99, 102, 241, 0.2);
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.2rem;
    }
    
    /* Status Online do Rodapé */
    .status-indicator {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.2);
        padding: 0.4rem 1rem;
        border-radius: 999px;
        color: #10b981;
        font-size: 0.85rem;
        font-weight: 600;
    }
</style>
""")

# ============================================================================
# 3. HERO SECTION (Apresentação Principal)
# ============================================================================
hero_col1, hero_col2 = st.columns([1, 2], gap="large")

with hero_col1:
    # Fallback elegante caso a imagem falhe
    try:
        st.image("rapha.jpeg", use_container_width=True)
    except Exception:
        st.subheader("💡 Raphael Pires")
        st.caption("Falta a foto `rapha.jpeg` no diretório.")

with hero_col2:
    st.title("Raphael Fernando da Silva Pires")
    st.subheader("Analista de Dados & Business Intelligence")
    
    st.markdown("""
    Transformando dados brutos em decisões estratégicas de negócio. São **mais de 16 anos** de experiência construindo soluções de inteligência computacional, automação de processos 
    e governança de dados que geram impacto real e mensurável.
    """)
    
    # Badges dinâmicos usando HTML limpo
    badges = ["📊 Power BI", "🐍 Python", "🗄️ SQL", "☁️ AWS", "🤖 IA Generativa", "📈 Dashboards"]
    badge_html = "".join([f'<span class="tech-badge">{b}</span>' for b in badges])
    st.markdown(badge_html, unsafe_allow_html=True)
    
    st.write("")
    # Botão de Download simplificado e nativo
    try:
        with open("Curriculo_Raphael_v2.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Currículo PDF",
                data=pdf_file.read(),
                file_name="Curriculo_Raphael_v2.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.caption("ℹ️ *O arquivo PDF do currículo pode ser anexado aqui.*")

st.divider()

# ============================================================================
# 4. METRICAS DE IMPACTO (Substituindo a Grid HTML por Linhas Nativas)
# ============================================================================
st.markdown("### ⚡ Impacto em Números")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    with st.container(border=True):
        st.metric(label="Anos de Experiência", value="16+")
with m_col2:
    with st.container(border=True):
        st.metric(label="Redução de Tempo Operacional", value="70%", delta="-2h para 15min")
with m_col3:
    with st.container(border=True):
        st.metric(label="Dados Públicos Analisados", value="R$ 50 Bi")
with m_col4:
    with st.container(border=True):
        st.metric(label="Registros Processados", value="213k+")

st.divider()

# ============================================================================
# 5. PROJETOS EM DESTAQUE (Grid dinâmica e limpa)
# ============================================================================
st.markdown("### 🚀 Projetos em Destaque")
proj_col1, proj_col2 = st.columns(2, gap="medium")

with proj_col1:
    with st.container(border=True):
        st.markdown("#### 🇧🇷 Desenrola Brasil")
        st.write("Análise exploratória avançada de dados do programa governamental, mapeando renegociações e perfis socioeconômicos de consumidores em larga escala.")
        st.page_link("https://github.com", label="Acessar Repositório", icon="🔗")

    st.write("") # Espaçamento
    
    with st.container(border=True):
        st.markdown("#### ⛽ Dashboard ANP")
        st.write("Mapeamento e análise de preços, distribuição e comportamento do mercado de combustíveis nacional utilizando os dados da Agência Nacional do Petróleo.")
        st.page_link("https://github.com", label="Ver Dashboard", icon="📊")

with proj_col2:
    with st.container(border=True):
        st.markdown("#### 🔬 CNPq Analytics")
        st.write("Painel de Business Intelligence focado na distribuição de bolsas e fomento à pesquisa científica, cruzando dados geográficos e áreas do conhecimento.")
        st.page_link("https://github.com", label="Acessar Repositório", icon="🔗")

    st.write("")
    
    with st.container(border=True):
        st.markdown("#### ☁️ AWS Cloud Journey")
        st.write("Documentação técnica e laboratórios práticos focados na preparação para a certificação AWS Certified Cloud Practitioner.")
        st.page_link("https://github.com", label="Acompanhar Estudos", icon="☁️")

st.divider()

# ============================================================================
# 6. EXPERIÊNCIA PROFISSIONAL (Simplificado e Escaneável)
# ============================================================================
st.markdown("### 💼 Trajetória Profissional")

exp_tabs = st.tabs(["Banco do Brasil", "Jardim do Éden", "J Sintonía", "NSM"])

with exp_tabs[0]:
    st.markdown("#### Automação de Processos com VBA | **Banco do Brasil**")
    st.caption("Foco em Eficiência Operacional")
    st.markdown("""
    * Desenvolvimento de automações robustas em VBA que mitigaram falhas operacionais.
    * Redução de **70% do tempo de processamento** de rotinas diárias da equipe.
    * Liberação de força de trabalho para análises puramente estratégicas.
    """)

with exp_tabs[1]:
    st.markdown("#### Fundador & Analista de BI | **Jardim do Éden**")
    st.caption("Inteligência e Modelagem de Dados")
    st.markdown("""
    * Estruturação de arquiteturas de BI ponta a ponta utilizando **Python, SQL e Power BI**.
    * Implementação de rotinas de IA Generativa para auxiliar na catalogação e análise de dados.
    * Otimização de tempos de resposta analíticos de **2 horas para apenas 15 minutos**.
    """)

with exp_tabs[2]:
    st.markdown("#### Gestão Comercial & BI | **J Sintonía**")
    st.markdown("- Construção de dashboards táticos e operacionais para monitoramento de metas comerciais.")
    ("- Realização de análises de viabilidade econômica baseadas em KPIs consolidados.")

with exp_tabs[3]:
    st.markdown("#### Analista de Dados | **NSM**")
    st.markdown("- Centralização de bases descentralizadas e governança de dados operacionais.")

st.divider()

# ============================================================================
# 7. GRÁFICO DE APRESENTAÇÃO DE SKILLS (Demonstração Técnica Real)
# ============================================================================
st.markdown("### 🛠️ Domínio Tecnológico Relativo")

# Dados estruturados reais para gerar o gráfico nativo do Plotly
skills_data = {
    "Tecnologia": ["Power BI", "SQL / Postgres", "Python (Pandas)", "Excel/VBA", "AWS Cloud", "IA Generativa"],
    "Nível de Proeficiência (%)": [95, 90, 85, 95, 60, 75],
    "Categoria": ["BI", "Dados", "Dados", "Automação", "Cloud", "Inovação"]
}
df_skills = pd.DataFrame(skills_data)

fig = px.bar(
    df_skills, 
    x="Nível de Proeficiência (%)", 
    y="Tecnologia", 
    color="Categoria",
    orientation="h",
    color_discrete_sequence=["#6366f1", "#3b82f6", "#10b981", "#f59e0b"],
    template="plotly_white" if st.get_option("theme.base") == "light" else "plotly_dark"
)

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    height=300,
    xaxis=dict(range=[0, 100])
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ============================================================================
# 8. RODAPÉ (FOOTER)
# ============================================================================
foot_col1, foot_col2 = st.columns([2, 1])

with foot_col1:
    st.markdown("© 2026 Raphael Fernando da Silva Pires • Desenvolvido nativamente em Streamlit.")

with foot_col2:
    st.markdown('<div class="status-indicator"><span style="width:8px;height:8px;background:#10b981;border-radius:50%;display:inline-block;"></span>Disponível para novos projetos</div>', unsafe_allow_html=True)
