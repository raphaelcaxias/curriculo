import streamlit as st

# ============================================================================
# CONFIGURAÇÕES DE TEMA
# ============================================================================
def init_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_theme():
    return st.session_state.theme

# ============================================================================
# CORES POR TEMA
# ============================================================================
def get_colors():
    is_dark = st.session_state.theme == "dark"
    
    if is_dark:
        return {
            "primary": "#3B82F6",
            "secondary": "#0EA5E9",
            "bg": "#0B1120",
            "text": "#E5E7EB",
            "text_muted": "#94A3B8",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6", "#0EA5E9", "#60A5FA", "#2563EB", "#0284C7"],
            "card_bg": "rgba(59, 130, 246, 0.05)",
            "border": "rgba(59, 130, 246, 0.15)",
            "hover_bg": "rgba(59, 130, 246, 0.1)"
        }
    else:
        return {
            "primary": "#2563EB",
            "secondary": "#0284C7",
            "bg": "#F8FAFC",
            "text": "#0F172A",
            "text_muted": "#64748B",
            "plotly_template": "plotly_white",
            "chart_colors": ["#2563EB", "#0284C7", "#3B82F6", "#1D4ED8", "#0369A1"],
            "card_bg": "rgba(59, 130, 246, 0.03)",
            "border": "rgba(59, 130, 246, 0.1)",
            "hover_bg": "rgba(59, 130, 246, 0.06)"
        }

# ============================================================================
# CONSTANTES
# ============================================================================
SOCIAL_LINKS = {
    "linkedin": "https://www.linkedin.com/in/raphaelpires",
    "github": "https://github.com/raphaelcaxias",
    "email": "mailto:contato@raphaelpires.com",
    "phone": "tel:+5511999999999"
}

TECH_STACK = {
    "Dados": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy"],
    "BI": ["Power BI", "Plotly", "Looker Studio", "Streamlit"],
    "Cloud": ["AWS", "Git", "GitHub"],
    "Automação": ["Excel VBA", "IA Generativa"]
}

SKILLS_DATA = {
    "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
    "Proficiência": [95, 92, 88, 95, 85, 60, 82],
    "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
}

EXPERIENCES = [
    {
        "date": "Experiência Corporativa",
        "role": "Automação de Processos com VBA",
        "company": "Banco do Brasil",
        "description": "Desenvolvimento de automações em VBA que resultaram em redução de 70% do tempo operacional.",
        "tags": ["VBA", "Automação", "Eficiência"]
    },
    {
        "date": "Fundador & Analista",
        "role": "Fundador",
        "company": "Jardim do Éden",
        "description": "Dashboards, Power BI, Python, SQL, KPIs e IA Generativa. Redução de 2h para 15min.",
        "tags": ["Power BI", "Python", "SQL", "IA"]
    },
    {
        "date": "Gestão Comercial",
        "role": "Gestão Comercial & BI",
        "company": "J Sintonía",
        "description": "Business Intelligence, indicadores, dashboards e análise de viabilidade econômica.",
        "tags": ["BI", "KPIs", "Dashboards"]
    },
    {
        "date": "Dados & Operação",
        "role": "Analista de Dados",
        "company": "NSM",
        "description": "Centralização de dados e controle operacional com construção de indicadores.",
        "tags": ["Dados", "Governança", "Indicadores"]
    }
]

PROJECTS = [
    {
        "icon": "🇧🇷",
        "title": "Desenrola Brasil",
        "description": "Análise de dados do programa governamental, explorando renegociações e perfis de consumidores.",
        "link": "https://github.com/raphaelcaxias",
        "label": "Acessar Repositório"
    },
    {
        "icon": "🔬",
        "title": "CNPq Analytics",
        "description": "Dashboard analítico sobre bolsas e fomento do CNPq com cruzamento de dados de pesquisa.",
        "link": "https://github.com/raphaelcaxias",
        "label": "Acessar Repositório"
    },
    {
        "icon": "⛽",
        "title": "Dashboard ANP",
        "description": "Inteligência de dados da ANP com análise de preços e produção de combustíveis.",
        "link": "https://github.com/raphaelcaxias",
        "label": "Ver Dashboard"
    },
    {
        "icon": "💎",
        "title": "Portfólio Premium",
        "description": "Este portfólio construído em Streamlit com design premium e visualização de dados.",
        "link": "https://github.com/raphaelcaxias",
        "label": "Ver Código"
    }
]
