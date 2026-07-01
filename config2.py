"""
config2.py - Todas as configurações, cores, CSS e constantes
"""
import streamlit as st

# ============================================================================
# CAMINHOS DOS ARQUIVOS
# ============================================================================
FOTO_CANDIDATOS = [
    "assets/rapha.jpeg", "assets/rapha.jpg",
    "rapha.jpeg", "rapha.jpg",
    "foto.jpeg", "foto.jpg",
    "perfil.jpeg", "perfil.jpg"
]

PDF_CANDIDATOS = [
    "Curriculo_Raphael_v2.pdf",
    "Curriculo_Raphael.pdf",
    "cv.pdf",
    "assets/Curriculo_Raphael_v2.pdf",
    "assets/Curriculo_Raphael.pdf",
]

FOTO_FALLBACK = "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff&bold=true"

# ============================================================================
# DADOS DO CURRÍCULO
# ============================================================================
DADOS_PESSOAIS = {
    "nome": "Raphael Fernando S. Pires",
    "titulo": "Analista de Dados & Business Intelligence",
    "localizacao": "Volta Redonda — RJ",
    "modalidades": ["Remoto", "Disponível para viagens"],
    "telefone1": "(24) 3018-1303",
    "telefone2": "(24) 99278-9637",
    "email": "raphael_caxias@hotmail.com",
    "linkedin": "linkedin.com/in/raphael-pires-caxias",
    "github": "github.com/raphaelcaxias"
}

PERFIL_PROFISSIONAL = """
Não cheguei aos dados por acaso. Cheguei porque vivi o negócio por anos — estoque, vendas, margem, fluxo de caixa, operação. Quando aprendi Power BI, Python e SQL, não foi para seguir tendência. Foi porque finalmente tinha as ferramentas para resolver os problemas que eu já conhecia de perto.

Sou Analista de Dados e BI com formação em Sistemas de Informação, mas minha verdadeira escola foi o chão de loja, o balcão do banco, a gestão de empresas próprias. Hoje transformo essa experiência em dashboards, automações e indicadores que fazem diferença real.
"""

CITACAO_PESSOAL = """
"Não estou entrando em tecnologia. Estou mostrando que, durante anos, já resolvi problemas com dados — mesmo quando meu cargo não tinha 'Analista' no nome."
"""

KPIS = [
    {"valor": "70%", "label": "Redução no tempo operacional", "contexto": "Banco do Brasil", "icone": "⚡"},
    {"valor": "2h→15min", "label": "Ciclo de análise", "contexto": "Relatórios comerciais", "icone": "⏱️"},
    {"valor": "213 mil+", "label": "Registros analisados", "contexto": "Projeto CNPq", "icone": "📊"},
    {"valor": "16 anos", "label": "De experiência real", "contexto": "Vivendo o negócio", "icone": "🏆"}
]

TECH_STACK = {
    "POWER BI": {"itens": ["Dashboards", "KPIs", "DAX", "Power Query"], "icone": "📊", "nivel": "Expert"},
    "SQL": {"itens": ["PostgreSQL", "Consultas", "Modelagem"], "icone": "🗄️", "nivel": "Expert"},
    "PYTHON": {"itens": ["Pandas", "NumPy", "Scikit-learn", "Statsmodels"], "icone": "🐍", "nivel": "Avançado"},
    "VISUALIZAÇÃO": {"itens": ["Plotly", "Streamlit", "Looker Studio"], "icone": "📈", "nivel": "Avançado"},
    "ETL": {"itens": ["Coleta", "Limpeza", "Transformação", "Carga"], "icone": "🔄", "nivel": "Expert"},
    "CLOUD": {"itens": ["AWS Educate", "Fundamentos Cloud"], "icone": "☁️", "nivel": "Intermediário"},
    "FERRAMENTAS": {"itens": ["Excel/VBA", "Git", "IA Generativa"], "icone": "🛠️", "nivel": "Expert"}
}

CERTIFICACOES = [
    {
        "instituicao": "Hashtag Treinamentos",
        "cursos": ["SQL Avançado", "Power BI", "Python para Análise de Dados", "Algoritmos e IA Aplicada"],
        "status": "Concluído",
        "icone": "📘"
    },
    {
        "instituicao": "AWS Educate",
        "cursos": ["Cloud Computing", "Introdução ao Cloud 101", "Console de Gerenciamento da AWS",
                   "Introdução a Armazenamento", "Machine Learning Foundations", "AWS Sustainability",
                   "Cloud and Sustainability", "Cloud Support Associate Day in the Life"],
        "status": "Em andamento (40%)",
        "icone": "☁️",
        "modulos_concluidos": 8
    }
]

FORMACAO = [
    {"curso": "Sistemas de Informação", "instituicao": "UniFOA", "ano": "2010"},
    {"curso": "Técnico em Informática", "instituicao": "CIBA", "ano": "2005"}
]

IDIOMAS = [
    {"idioma": "Português", "nivel": "Nativo"},
    {"idioma": "Inglês", "nivel": "Leitura técnica"}
]

PROJETOS = [
    {
        "nome": "Desenrola Brasil",
        "subtitulo": "Painel Analítico Executivo",
        "tecnologias": ["Python", "Pandas", "Scikit-learn", "Statsmodels", "Plotly", "Streamlit"],
        "url": "https://desenrolabrasil.streamlit.app",
        "descricao": [
            "Dados oficiais do Banco Central transformados em insights reais: KPIs, séries temporais e análise de concentração de mercado (HHI).",
            "Segmentação de perfis de renegociação via clusterização — porque números sem contexto não ajudam ninguém."
        ],
        "icone": "🇧🇷",
        "contexto": "Entender o impacto real do programa no Brasil"
    },
    {
        "nome": "CNPq Analytics",
        "subtitulo": "Investimentos em Pesquisa",
        "tecnologias": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "url": "https://cnpq-analytics.streamlit.app",
        "descricao": [
            "213 mil bolsas e R$ 1,2 bilhão em investimentos públicos analisados. Um dos projetos que mais me orgulho.",
            "Dashboard interativo que evidencia desigualdades regionais na distribuição de recursos."
        ],
        "icone": "🔬",
        "contexto": "Mostrar para onde vai o dinheiro da pesquisa no Brasil"
    },
    {
        "nome": "Dashboard ANP",
        "subtitulo": "Preços de Combustíveis",
        "tecnologias": ["Python", "Pandas", "Plotly", "Streamlit"],
        "url": None,
        "descricao": [
            "Dados oficiais da Agência Nacional do Petróleo com filtros temporais e regionais.",
            "Porque todo cidadão merece entender o que paga no posto."
        ],
        "icone": "⛽",
        "contexto": "Transparência em dados públicos"
    }
]

EXPERIENCIAS = [
    {
        "cargo": "Fundador & Analista de Dados",
        "empresa": "Jardim do Éden — Varejo de Moda",
        "tipo": "Empresa Própria",
        "periodo": "2009 — Atual",
        "status": "Consultiva",
        "historia": "Muita gente vê 'dono de loja'. Mas o que eu fiz foi muito além. Estruturei a base de dados do zero, criei dashboards gerenciais, automatizei processos. Reduzi análises que levavam 2 horas para 15 minutos. Foi aqui que desenvolvi meu pensamento de BI de verdade — usando SQL, Python, Power BI, Looker Studio e IA Generativa no dia a dia.",
        "tags": ["SQL", "Python", "Power BI", "Looker Studio", "IA Generativa", "Empreendedorismo"]
    },
    {
        "cargo": "Fundador & Analista de KPIs",
        "empresa": "J Sintonía — Varejo Especializado",
        "tipo": "Empresa Própria",
        "periodo": "2014 — maio 2026",
        "status": "Encerrado",
        "historia": "Outra empresa própria, outra escola. Trabalhei com indicadores, KPIs, viabilidade econômica, planejamento financeiro. O encerramento do negócio em maio/2026 não foi por impulso — foi baseado em análise de dados, projeções e cenários. Maturidade de quem decide com evidência, não com emoção.",
        "tags": ["KPIs", "Dashboards", "Análise Econômica", "Empreendedorismo"]
    },
    {
        "cargo": "Estagiário de Automação e Dados",
        "empresa": "Banco do Brasil S.A.",
        "tipo": "Estágio",
        "periodo": "2008 — 2010",
        "status": None,
        "historia": "Uma das experiências mais fortes da minha carreira. Desenvolvi macros VBA que chegaram a 20 agências, reduzindo 70% do tempo operacional. Saneei e padronizei bases de dados gerenciais. Aqui aprendi o que é automação de verdade em ambiente corporativo.",
        "tags": ["VBA", "Automação", "SQL", "Ambiente Corporativo"]
    },
    {
        "cargo": "Auxiliar de Dados & Operações",
        "empresa": "NSM Comércio",
        "tipo": "CLT",
        "periodo": "2002 — 2009",
        "status": None,
        "historia": "Meu primeiro contato sério com tecnologia aplicada ao negócio. Centralizei registros de estoque de 7 unidades, eliminando inconsistências de inventário. Aqui desenvolvi minha visão operacional que carrego até hoje.",
        "tags": ["Operações", "Estoque", "Dados", "Visão Operacional"]
    },
    {
        "cargo": "Instrutor de Informática",
        "empresa": "UniFOA — Projeto de Extensão",
        "tipo": "Projeto",
        "periodo": "Jan 2006 — Dez 2007",
        "status": None,
        "historia": "Ensinar é uma das melhores formas de aprender. Capacitei jovens em Excel avançado (tabelas dinâmicas, PROCV, automações) e lógica de programação. Descobri aqui que tenho facilidade para transmitir conhecimento — algo que uso até hoje.",
        "tags": ["Excel", "Programação", "Ensino", "Comunicação"]
    }
]

LINKS_SOCIAIS = {
    "linkedin": "https://www.linkedin.com/in/raphael-pires-caxias",
    "github": "https://github.com/raphaelcaxias",
    "email": "mailto:raphael_caxias@hotmail.com",
    "whatsapp": "https://wa.me/5524992789637"
}

SOBRE_MIM = {
    "titulo": "Minha História",
    "texto": """
Sou de Volta Redonda, RJ. Casado com Daiane, pai da Melina (nossa Mel). 

Minha trajetória não é linear — e isso é minha maior força. Comecei na operação, passei pelo banco, empreendi, ensinei, e agora estou reorganizando tudo isso sob a ótica de Dados e BI.

Não sou aquele profissional que fez curso e saiu procurando emprego. Sou alguém que viveu o negócio por anos e agora tem as ferramentas para transformar essa experiência em valor.

Sou curioso por natureza. Quando aprendo algo, quero entender tudo. Não gosto apenas de consumir conhecimento — gosto de construir, publicar, melhorar. Meu currículo passou por dezenas de revisões. Meu portfólio também. Busco excelência, às vezes até demais.

Hoje meu foco é claro: Analista de Dados, Business Intelligence, Planejamento, Indicadores, Power BI. Abandonei a imagem de "empresário" para mostrar minha experiência através da ótica de dados — e essa foi a melhor decisão que tomei.
    """,
    "valores": [
        {"icone": "🎯", "titulo": "Resolução de Problemas", "desc": "Quando aprendo uma tecnologia, penso: como isso resolve um problema real?"},
        {"icone": "🔍", "titulo": "Curiosidade", "desc": "Quero entender tudo. Não aceito a primeira versão."},
        {"icone": "🛠️", "titulo": "Construção", "desc": "Não consumo conhecimento passivamente. Construo, publico, melhoro."},
        {"icone": "📊", "titulo": "Decisão por Dados", "desc": "Encerrei um negócio baseado em análise, não em impulso."}
    ]
}

MODOS_VISUALIZACAO = {
    "Dados & BI": {
        "descricao": "Foco em análise de dados, BI, dashboards e modelagem",
        "destaques": ["POWER BI", "SQL", "PYTHON", "ETL", "VISUALIZAÇÃO"],
        "ordem_experiencias": [0, 1, 2, 3, 4],
        "cor_destaque": "#3B82F6"
    },
    "Desenvolvimento": {
        "descricao": "Foco em programação, automação e soluções técnicas",
        "destaques": ["PYTHON", "SQL", "ETL", "CLOUD", "FERRAMENTAS"],
        "ordem_experiencias": [0, 1, 2, 3, 4],
        "cor_destaque": "#8B5CF6"
    },
    "Indústria & Gestão": {
        "descricao": "Foco em operações, gestão e processos industriais",
        "destaques": ["POWER BI", "SQL", "ETL", "FERRAMENTAS"],
        "ordem_experiencias": [3, 2, 0, 1, 4],
        "cor_destaque": "#10B981"
    },
    "Empreendedorismo": {
        "descricao": "Foco em fundação de empresas e gestão de negócios",
        "destaques": ["POWER BI", "SQL", "PYTHON", "FERRAMENTAS"],
        "ordem_experiencias": [0, 1, 2, 3, 4],
        "cor_destaque": "#F59E0B"
    }
}

TEMA_DARK = {
    "primary": "#3B82F6", "primary_hover": "#2563EB", "secondary": "#0EA5E9",
    "accent": "#8B5CF6", "success": "#22C55E", "warning": "#F59E0B",
    "bg": "#0B0F1A", "bg_elevated": "#111827",
    "text": "#F1F5F9", "text_muted": "#94A3B8", "text_subtle": "#64748B",
    "card_bg": "rgba(255,255,255,0.04)", "card_bg_hover": "rgba(255,255,255,0.07)",
    "border": "rgba(255,255,255,0.08)", "border_hover": "rgba(59,130,246,0.4)",
    "tag_bg": "rgba(59,130,246,0.12)", "tag_border": "rgba(59,130,246,0.25)",
    "primary_light": "rgba(59,130,246,0.15)",
    "navbar_bg": "rgba(11,15,26,0.85)", "navbar_border": "rgba(255,255,255,0.06)",
    "nav_hover": "rgba(255,255,255,0.06)",
    "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.1) 0%, transparent 70%)",
    "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(59,130,246,0.18) 0%, transparent 60%)",
    "section_bg": "rgba(11,15,26,0.6)", "section_alt_bg": "rgba(255,255,255,0.02)",
    "shadow": "0 8px 32px rgba(0,0,0,0.4)", "shadow_hover": "0 16px 48px rgba(59,130,246,0.25)",
    "shadow_glow": "0 0 40px rgba(59,130,246,0.15)",
    "plotly_template": "plotly_dark",
    "chart_colors": ["#3B82F6", "#0EA5E9", "#8B5CF6", "#22C55E", "#F59E0B"],
    "gradient_primary": "linear-gradient(135deg, #3B82F6 0%, #0EA5E9 100%)",
    "gradient_accent": "linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%)",
    "gradient_text": "linear-gradient(135deg, #3B82F6 0%, #0EA5E9 50%, #8B5CF6 100%)"
}

TEMA_LIGHT = {
    "primary": "#1D4ED8", "primary_hover": "#1E40AF", "secondary": "#0EA5E9",
    "accent": "#7C3AED", "success": "#16A34A", "warning": "#D97706",
    "bg": "#F8FAFC", "bg_elevated": "#FFFFFF",
    "text": "#0F172A", "text_muted": "#475569", "text_subtle": "#94A3B8",
    "card_bg": "rgba(255,255,255,0.8)", "card_bg_hover": "rgba(255,255,255,0.95)",
    "border": "rgba(0,0,0,0.06)", "border_hover": "rgba(29,78,216,0.3)",
    "tag_bg": "#DBEAFE", "tag_border": "#93C5FD",
    "primary_light": "#DBEAFE",
    "navbar_bg": "rgba(248,250,252,0.9)", "navbar_border": "rgba(0,0,0,0.06)",
    "nav_hover": "rgba(0,0,0,0.04)",
    "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.06) 0%, transparent 70%)",
    "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(29,78,216,0.1) 0%, transparent 60%)",
    "section_bg": "rgba(255,255,255,0.6)", "section_alt_bg": "rgba(0,0,0,0.01)",
    "shadow": "0 8px 32px rgba(0,0,0,0.08)", "shadow_hover": "0 16px 48px rgba(29,78,216,0.12)",
    "shadow_glow": "0 0 40px rgba(29,78,216,0.08)",
    "plotly_template": "plotly_white",
    "chart_colors": ["#1D4ED8", "#0EA5E9", "#7C3AED", "#16A34A", "#D97706"],
    "gradient_primary": "linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 100%)",
    "gradient_accent": "linear-gradient(135deg, #7C3AED 0%, #1D4ED8 100%)",
    "gradient_text": "linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 50%, #7C3AED 100%)"
}

def get_colors():
    if st.session_state.get("theme", "dark") == "dark":
        return TEMA_DARK
    return TEMA_LIGHT

def toggle_theme():
    if st.session_state.theme == "dark":
        st.session_state.theme = "light"
    else:
        st.session_state.theme = "dark"

def get_css(colors):
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800;14..32,900&display=swap');

        :root {{
            --primary: {colors['primary']};
            --primary-hover: {colors['primary_hover']};
            --secondary: {colors['secondary']};
            --accent: {colors['accent']};
            --success: {colors['success']};
            --warning: {colors['warning']};
            --bg: {colors['bg']};
            --text: {colors['text']};
            --text-muted: {colors['text_muted']};
            --text-subtle: {colors['text_subtle']};
            --card-bg: {colors['card_bg']};
            --card-bg-hover: {colors['card_bg_hover']};
            --border: {colors['border']};
            --border-hover: {colors['border_hover']};
            --tag-bg: {colors['tag_bg']};
            --tag-border: {colors['tag_border']};
            --primary-light: {colors['primary_light']};
            --navbar-bg: {colors['navbar_bg']};
            --navbar-border: {colors['navbar_border']};
            --nav-hover: {colors['nav_hover']};
            --shadow: {colors['shadow']};
            --shadow-hover: {colors['shadow_hover']};
            --shadow-glow: {colors['shadow_glow']};
            --gradient-primary: {colors['gradient_primary']};
            --gradient-accent: {colors['gradient_accent']};
            --gradient-text: {colors['gradient_text']};
            --section-bg: {colors['section_bg']};
            --section-alt-bg: {colors['section_alt_bg']};
            --hero-bg: {colors['hero_bg']};
            --hero-glow: {colors['hero_glow']};
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg);
            color: var(--text);
        }}
        
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: var(--bg); }}
        .block-container {{ padding: 0 !important; max-width: 100%; }}

        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
            background: var(--navbar-bg);
            backdrop-filter: blur(20px) saturate(200%);
            -webkit-backdrop-filter: blur(20px) saturate(200%);
            border-bottom: 1px solid var(--navbar-border);
            padding: 0.875rem 2.5rem;
            display: flex; align-items: center; justify-content: space-between;
        }}
        .navbar-brand {{ 
            font-weight: 800; font-size: 1.3rem; color: var(--text); 
            text-decoration: none; display: flex; align-items: center; gap: 0.5rem;
        }}
        .navbar-brand .brand-dot {{
            width: 10px; height: 10px; border-radius: 50%;
            background: var(--gradient-primary);
            box-shadow: 0 0 12px var(--primary);
            animation: pulse-dot 2s infinite;
        }}
        @keyframes pulse-dot {{
            0%, 100% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.2); opacity: 0.7; }}
        }}
        .navbar-brand span {{ 
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .navbar-links {{ display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; }}
        .nav-link {{
            padding: 0.5rem 1.1rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.25s ease;
            color: var(--text-muted); background: transparent; cursor: pointer;
        }}
        .nav-link:hover {{ background: var(--nav-hover); color: var(--text); transform: translateY(-1px); }}
        .nav-link.active {{
            background: var(--gradient-primary); color: white !important;
            box-shadow: 0 4px 16px rgba(59,130,246,0.35);
        }}
        .theme-toggle {{
            width: 44px; height: 44px; border-radius: 50%;
            background: var(--card-bg); border: 1px solid var(--border);
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: all 0.4s ease;
            font-size: 1.2rem; margin-left: 0.5rem;
        }}
        .theme-toggle:hover {{
            background: var(--nav-hover); border-color: var(--primary);
            transform: rotate(360deg) scale(1.1);
        }}

        .hero-full {{
            min-height: 85vh; display: flex; align-items: center; justify-content: center;
            padding: 7rem 2rem 3rem; background: var(--hero-bg);
            position: relative; overflow: hidden;
        }}
        .hero-full::before {{
            content: ''; position: absolute; inset: 0;
            background: var(--hero-glow); opacity: 0.5; pointer-events: none;
        }}
        .hero-grid-bg {{
            position: absolute; inset: 0;
            background-image: 
                linear-gradient(rgba(59,130,246,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(59,130,246,0.03) 1px, transparent 1px);
            background-size: 60px 60px;
            mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
            -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
            pointer-events: none;
        }}
        .hero-content {{
            max-width: 1200px; width: 100%;
            display: grid; grid-template-columns: auto 1fr;
            gap: 4rem; align-items: center; position: relative; z-index: 2;
        }}
        @media (max-width: 900px) {{
            .hero-content {{ grid-template-columns: 1fr; text-align: center; gap: 2rem; }}
            .hero-photo-wrapper {{ margin: 0 auto; }}
        }}
        .hero-photo-wrapper {{ position: relative; width: 260px; height: 260px; }}
        .hero-photo-ring {{
            position: absolute; inset: -12px; border-radius: 50%;
            background: conic-gradient(from 0deg, var(--primary), var(--secondary), var(--accent), var(--primary));
            animation: rotate-ring 8s linear infinite; opacity: 0.6;
        }}
        .hero-photo-ring::after {{
            content: ''; position: absolute; inset: 4px;
            border-radius: 50%; background: var(--bg);
        }}
        @keyframes rotate-ring {{ to {{ transform: rotate(360deg); }} }}
        .hero-photo {{
            position: relative; z-index: 2;
            width: 260px; height: 260px; border-radius: 50%;
            object-fit: cover; border: 4px solid var(--bg);
            box-shadow: 0 25px 80px rgba(59,130,246,0.3);
        }}
        .hero-status-badge {{
            position: absolute; bottom: 10px; right: 10px; z-index: 3;
            background: var(--success); width: 28px; height: 28px; border-radius: 50%;
            border: 4px solid var(--bg);
            box-shadow: 0 0 0 3px var(--success), 0 0 20px var(--success);
            animation: pulse-status 2s infinite;
        }}
        @keyframes pulse-status {{
            0%, 100% {{ box-shadow: 0 0 0 3px var(--success), 0 0 20px var(--success); }}
            50% {{ box-shadow: 0 0 0 6px rgba(34,197,94,0.3), 0 0 30px var(--success); }}
        }}
        .hero-text h1 {{ 
            font-size: 3.5rem; font-weight: 900; 
            letter-spacing: -0.04em; line-height: 1.05; margin-bottom: 0.5rem;
        }}
        .hero-text h1 .gradient-name {{ 
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .hero-text .role-tag {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: var(--primary-light); border: 1px solid var(--tag-border);
            padding: 0.35rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 600; color: var(--primary);
            margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;
        }}
        .hero-text .subtitle {{ 
            font-size: 1.1rem; color: var(--text-muted); 
            margin: 0.5rem 0 1.5rem; line-height: 1.7; max-width: 600px;
            white-space: pre-line;
        }}
        .hero-quote {{
            font-style: italic; color: var(--text-subtle);
            font-size: 0.95rem; margin: 1.5rem 0;
            padding-left: 1.5rem; border-left: 3px solid var(--primary);
            max-width: 500px; line-height: 1.6;
            white-space: pre-line;
        }}
        @media (max-width: 900px) {{ .hero-quote {{ margin-left: auto; margin-right: auto; }} }}
        .badge-group {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; }}
        @media (max-width: 900px) {{ .badge-group {{ justify-content: center; }} }}
        .badge {{
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 0.4rem 0.9rem; border-radius: 10px;
            font-size: 0.78rem; font-weight: 500;
            transition: all 0.2s ease; backdrop-filter: blur(8px);
        }}
        .badge:hover {{
            border-color: var(--primary); background: var(--primary-light);
            transform: translateY(-2px);
        }}
        .cta-group {{ display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 2rem; }}
        @media (max-width: 900px) {{ .cta-group {{ justify-content: center; }} }}
        .btn-primary {{
            background: var(--gradient-primary); color: white !important;
            padding: 0.75rem 1.75rem; border-radius: 12px;
            font-weight: 600; text-decoration: none;
            display: inline-flex; align-items: center; gap: 0.5rem;
            box-shadow: 0 4px 16px rgba(59,130,246,0.3);
            transition: all 0.25s ease; border: none; cursor: pointer;
        }}
        .btn-primary:hover {{ 
            transform: translateY(-2px);
            box-shadow: 0 8px 28px rgba(59,130,246,0.45);
        }}
        .btn-secondary {{
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 0.75rem 1.75rem; border-radius: 12px;
            font-weight: 600; color: var(--text) !important;
            text-decoration: none; display: inline-flex;
            align-items: center; gap: 0.5rem; backdrop-filter: blur(8px);
            transition: all 0.25s ease;
        }}
        .btn-secondary:hover {{ 
            background: var(--card-bg-hover); border-color: var(--primary);
            transform: translateY(-2px);
        }}

        .section-glass {{
            padding: 5rem 2rem; background: var(--section-bg);
            backdrop-filter: blur(8px); border-top: 1px solid var(--border);
        }}
        .section-glass.alt {{ background: var(--section-alt-bg); }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{ text-align: center; margin-bottom: 3.5rem; }}
        .section-header .label {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: var(--primary-light); border: 1px solid var(--tag-border);
            padding: 0.35rem 1.1rem; border-radius: 999px;
            font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.1em; color: var(--primary); margin-bottom: 1rem;
        }}
        .section-header h2 {{ 
            font-size: 2.5rem; font-weight: 800;
            margin-top: 0.5rem; letter-spacing: -0.03em; line-height: 1.15;
        }}
        .section-header p {{ 
            color: var(--text-muted); max-width: 600px;
            margin: 1rem auto 0; font-size: 1.05rem; line-height: 1.6;
        }}

        .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }}
        @media (max-width: 1024px) {{ .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (max-width: 640px) {{ .kpi-grid {{ grid-template-columns: 1fr; }} }}
        .kpi-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 20px;
            padding: 1.75rem 1.5rem; text-align: center;
            transition: all 0.3s ease; position: relative; overflow: hidden;
        }}
        .kpi-card::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0;
            height: 3px; background: var(--gradient-primary);
            opacity: 0; transition: opacity 0.3s ease;
        }}
        .kpi-card:hover {{
            transform: translateY(-6px); border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .kpi-card:hover::before {{ opacity: 1; }}
        .kpi-icon {{
            width: 48px; height: 48px; border-radius: 14px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 1rem; font-size: 1.4rem;
        }}
        .kpi-value {{
            font-size: 2rem; font-weight: 800; letter-spacing: -0.03em;
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1; margin-bottom: 0.35rem;
        }}
        .kpi-label {{ font-size: 0.82rem; color: var(--text-muted); font-weight: 500; }}
        .kpi-context {{ font-size: 0.75rem; color: var(--text-subtle); margin-top: 0.25rem; }}

        .tech-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }}
        .tech-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 20px;
            padding: 1.75rem; transition: all 0.3s ease;
        }}
        .tech-card:hover {{
            transform: translateY(-4px); border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .tech-card-header {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }}
        .tech-icon {{
            width: 56px; height: 56px; border-radius: 16px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem;
        }}
        .tech-name {{ font-size: 1.1rem; font-weight: 700; }}
        .tech-level {{
            font-size: 0.72rem; font-weight: 600;
            padding: 0.2rem 0.6rem; border-radius: 999px;
            display: inline-block; margin-top: 0.25rem;
        }}
        .tech-level.expert {{ background: rgba(34,197,94,0.15); color: var(--success); }}
        .tech-level.avancado {{ background: rgba(59,130,246,0.15); color: var(--primary); }}
        .tech-level.intermediario {{ background: rgba(245,158,11,0.15); color: var(--warning); }}
        .tech-items {{ display: flex; flex-wrap: wrap; gap: 0.4rem; }}
        .tech-item {{
            font-size: 0.78rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.25rem 0.7rem; border-radius: 8px;
            color: var(--primary); font-weight: 500;
        }}

        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, var(--primary), var(--secondary), var(--accent), transparent);
        }}
        .timeline-item {{ 
            position: relative; padding-left: 80px; margin-bottom: 2.5rem;
            animation: fadeInUp 0.6s ease backwards;
        }}
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .timeline-dot {{
            position: absolute; left: 20px; top: 8px; width: 18px; height: 18px;
            border-radius: 50%; background: var(--gradient-primary);
            border: 3px solid var(--bg);
            box-shadow: 0 0 0 4px var(--primary), 0 0 20px rgba(59,130,246,0.4);
            z-index: 2;
        }}
        .timeline-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 20px;
            padding: 1.75rem; transition: all 0.3s ease;
        }}
        .timeline-card:hover {{ 
            border-color: var(--border-hover); transform: translateX(8px);
            box-shadow: var(--shadow-hover);
        }}
        .timeline-date {{
            display: inline-block; font-size: 0.72rem; font-weight: 700;
            background: var(--primary-light); color: var(--primary);
            padding: 0.25rem 0.9rem; border-radius: 999px;
        }}
        .timeline-badge {{
            background: var(--gradient-primary); color: white;
            font-size: 0.62rem; font-weight: 800; padding: 0.2rem 0.7rem;
            border-radius: 999px; margin-left: 0.5rem;
            text-transform: uppercase; letter-spacing: 0.05em;
        }}
        .timeline-role {{ font-size: 1.2rem; font-weight: 700; margin: 0.5rem 0 0.2rem; }}
        .timeline-company {{ 
            color: var(--secondary); font-weight: 600; font-size: 0.95rem;
            margin-bottom: 0.75rem;
        }}
        .timeline-historia {{ 
            color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;
            margin-bottom: 0.75rem;
        }}
        .timeline-tag {{
            font-size: 0.72rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.25rem 0.7rem; border-radius: 8px;
            display: inline-block; margin: 0.2rem;
            color: var(--primary); font-weight: 600;
        }}

        .project-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
        }}
        .project-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 24px;
            padding: 2rem; transition: all 0.3s ease;
            position: relative; overflow: hidden;
        }}
        .project-card::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0;
            height: 3px; background: var(--gradient-primary);
            transform: scaleX(0); transform-origin: left;
            transition: transform 0.4s ease;
        }}
        .project-card:hover {{
            transform: translateY(-8px); border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .project-card:hover::before {{ transform: scaleX(1); }}
        .project-icon {{
            width: 64px; height: 64px; border-radius: 18px;
            background: var(--gradient-primary);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem; margin-bottom: 1.25rem;
            box-shadow: 0 8px 24px rgba(59,130,246,0.25);
        }}
        .project-card h3 {{ font-size: 1.25rem; font-weight: 700; margin-bottom: 0.25rem; }}
        .project-card .project-subtitle {{ 
            font-size: 0.9rem; color: var(--text-subtle); 
            margin-bottom: 0.75rem; font-style: italic;
        }}
        .project-card p {{ color: var(--text-muted); line-height: 1.65; font-size: 0.92rem; margin-bottom: 0.5rem; }}
        .project-card .project-context {{
            font-size: 0.85rem; color: var(--primary);
            font-style: italic; margin-bottom: 1rem;
            padding-left: 1rem; border-left: 2px solid var(--primary);
        }}
        .project-tech {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.25rem; }}
        .project-tag {{
            font-size: 0.7rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.2rem 0.6rem; border-radius: 6px;
            color: var(--primary); font-weight: 600;
        }}

        .glass-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 24px;
            padding: 2rem; transition: all 0.3s ease;
        }}
        .glass-card:hover {{
            transform: translateY(-6px); border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}

        .progress-bar {{
            width: 100%; height: 8px;
            background: var(--border); border-radius: 999px;
            overflow: hidden; margin-top: 0.75rem;
        }}
        .progress-fill {{
            height: 100%; background: var(--gradient-primary);
            border-radius: 999px; transition: width 1s ease;
            box-shadow: 0 0 12px var(--primary);
        }}

        .sobre-section {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 2.5rem;
            margin: 2rem 0;
        }}
        .sobre-text {{
            font-size: 1.05rem;
            line-height: 1.8;
            color: var(--text-muted);
            white-space: pre-line;
            margin-bottom: 2rem;
        }}
        .valores-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        .valor-card {{
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }}
        .valor-card:hover {{
            transform: translateY(-4px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .valor-icon {{
            font-size: 2.5rem;
            margin-bottom: 0.75rem;
        }}
        .valor-title {{
            font-size: 1rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 0.5rem;
        }}
        .valor-desc {{
            font-size: 0.85rem;
            color: var(--text-muted);
            line-height: 1.5;
        }}

        .footer {{
            padding: 4rem 2rem 2.5rem; text-align: center;
            border-top: 1px solid var(--border);
            background: var(--card-bg); backdrop-filter: blur(12px);
            position: relative;
        }}
        .footer::before {{
            content: ''; position: absolute; top: 0; left: 50%;
            transform: translateX(-50%); width: 200px; height: 1px;
            background: var(--gradient-primary);
        }}
        .footer h3 {{
            font-size: 2rem; font-weight: 800;
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }}
        .footer-links {{
            display: flex; justify-content: center; flex-wrap: wrap;
            gap: 0.6rem; margin: 2rem 0 1.5rem;
        }}
        .footer-link {{
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 0.6rem 1.25rem; border-radius: 12px;
            color: var(--text) !important; text-decoration: none;
            font-size: 0.88rem; font-weight: 500;
            display: inline-flex; align-items: center; gap: 0.4rem;
            transition: all 0.25s ease;
        }}
        .footer-link:hover {{
            background: var(--gradient-primary); color: white !important;
            border-color: transparent; transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(59,130,246,0.3);
        }}
        .footer-copy {{ 
            color: var(--text-subtle); font-size: 0.8rem;
            margin-top: 1.5rem; padding-top: 1.5rem;
            border-top: 1px solid var(--border);
        }}

        .page-header {{
            padding: 7rem 2rem 2rem; text-align: center;
            background: var(--hero-bg); position: relative; overflow: hidden;
        }}
        .page-header::before {{
            content: ''; position: absolute; inset: 0;
            background: var(--hero-glow); opacity: 0.4; pointer-events: none;
        }}
        .page-header h1 {{
            font-size: 2.5rem; font-weight: 800;
            letter-spacing: -0.03em; margin-bottom: 0.5rem;
            position: relative; z-index: 2;
        }}
        .page-header p {{
            color: var(--text-muted); font-size: 1.05rem;
            position: relative; z-index: 2;
        }}

        .scroll-top {{
            position: fixed; bottom: 2rem; right: 2rem;
            width: 48px; height: 48px; border-radius: 50%;
            background: var(--gradient-primary); color: white;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.2rem; cursor: pointer;
            box-shadow: 0 8px 24px rgba(59,130,246,0.35);
            transition: all 0.25s ease; z-index: 999;
            text-decoration: none;
        }}
        .scroll-top:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(59,130,246,0.5);
        }}

        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} }}

        @media (max-width: 768px) {{
            .navbar {{ padding: 0.75rem 1rem; }}
            .hero-full {{ padding: 6rem 1rem 2rem; min-height: auto; }}
            .hero-text h1 {{ font-size: 2.2rem; }}
            .hero-photo-wrapper {{ width: 200px; height: 200px; }}
            .hero-photo {{ width: 200px; height: 200px; }}
            .section-glass {{ padding: 3rem 1rem; }}
            .section-header h2 {{ font-size: 1.8rem; }}
        }}
    </style>
    """
