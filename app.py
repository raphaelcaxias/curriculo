import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Aprimorado
def load_custom_css():
    st.markdown("""
    <style>
        /* Importar fonte moderna */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Timeline Vertical Melhorada */
        .timeline-container {
            position: relative;
            padding: 2rem 0;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .timeline-line {
            position: absolute;
            left: 30px;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, #3B82F6 0%, #0EA5E9 50%, transparent 100%);
            border-radius: 3px;
        }
        
        .timeline-item {
            position: relative;
            padding-left: 80px;
            margin-bottom: 2.5rem;
            animation: fadeInUp 0.6s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .timeline-dot {
            position: absolute;
            left: 22px;
            top: 5px;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: linear-gradient(135deg, #3B82F6, #0EA5E9);
            border: 4px solid #0B1120;
            box-shadow: 0 0 0 3px #3B82F6, 0 4px 12px rgba(59, 130, 246, 0.4);
            z-index: 10;
            transition: transform 0.3s ease;
        }
        
        .timeline-item:hover .timeline-dot {
            transform: scale(1.2);
        }
        
        /* Card Profissional */
        .experience-card {
            background: linear-gradient(135deg, rgba(59,130,246,0.08) 0%, rgba(14,165,233,0.05) 100%);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 16px;
            padding: 1.8rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            backdrop-filter: blur(10px);
        }
        
        .experience-card:hover {
            transform: translateY(-4px) translateX(5px);
            border-color: rgba(59, 130, 246, 0.5);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.1), 
                        0 0 30px rgba(59, 130, 246, 0.2);
        }
        
        .timeline-badge {
            display: inline-block;
            background: linear-gradient(135deg, #3B82F6, #0EA5E9);
            color: white;
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
            box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
        }
        
        .timeline-role {
            font-size: 1.4rem;
            font-weight: 700;
            color: #E5E7EB;
            margin: 0.5rem 0;
            letter-spacing: -0.02em;
        }
        
        .timeline-company {
            font-size: 1rem;
            color: #0EA5E9;
            font-weight: 600;
            margin-bottom: 0.8rem;
        }
        
        .timeline-desc {
            color: #94A3B8;
            line-height: 1.7;
            margin-bottom: 1rem;
        }
        
        .timeline-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .tag {
            background: rgba(59, 130, 246, 0.15);
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 0.35rem 0.9rem;
            border-radius: 8px;
            font-size: 0.8rem;
            color: #DBEAFE;
            font-weight: 500;
            transition: all 0.2s ease;
        }
        
        .tag:hover {
            background: rgba(59, 130, 246, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(59, 130, 246, 0.2);
        }
        
        /* Seção Header */
        .section-header {
            text-align: center;
            margin: 3rem 0 2.5rem;
        }
        
        .section-label {
            display: inline-block;
            background: linear-gradient(135deg, rgba(59,130,246,0.2), rgba(14,165,233,0.15));
            padding: 0.4rem 1.2rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #3B82F6;
            border: 1px solid rgba(59, 130, 246, 0.3);
            margin-bottom: 0.8rem;
        }
        
        .section-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #E5E7EB;
            letter-spacing: -0.03em;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .timeline-item {
                padding-left: 60px;
            }
            .timeline-line {
                left: 20px;
            }
            .timeline-dot {
                left: 12px;
                width: 14px;
                height: 14px;
            }
            .section-title {
                font-size: 1.6rem;
            }
            .experience-card {
                padding: 1.2rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

load_custom_css()

# Sidebar
with st.sidebar:
    st.image("https://ui-avatars.com/api/?name=Raphael+Pires&size=150&background=3B82F6&color=fff", width=120)
    st.markdown("### Raphael Pires")
    st.markdown("Analista de Dados & BI")
    st.markdown("---")
    page = st.radio("Navegação", ["🏠 Início", "📈 Análises", "📊 Dashboard"], index=0, label_visibility="collapsed")

# Função para renderizar experiência
def render_experience_item(date, role, company, desc, tags, badge=""):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
    badge_html = f'<span class="timeline-badge">{badge}</span>' if badge else ""
    
    html = f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="experience-card">
            {badge_html}
            <div style="color: #60A5FA; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.3rem;">{date}</div>
            <h3 class="timeline-role">{role}</h3>
            <div class="timeline-company">{company}</div>
            <p class="timeline-desc">{desc}</p>
            <div class="timeline-tags">{tags_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)  # ✅ CORREÇÃO AQUI

# Página Principal
if "Início" in page:
    # Header da Seção
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Trajetória Profissional</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline Container
    st.markdown('<div class="timeline-container"><div class="timeline-line"></div>', unsafe_allow_html=True)
    
    # Experiências
    experiences = [
        {
            "date": "2014 – Presente · 10+ anos",
            "role": "Analista de Dados & BI",
            "company": "NSM",
            "desc": "Centralização de dados, construção de indicadores estratégicos, automação de relatórios e governança de dados. Redução de 70% do tempo operacional.",
            "tags": ["Dados", "Governança", "Indicadores", "Automação"],
            "badge": "Atual"
        },
        {
            "date": "2012 – Presente · 12+ anos",
            "role": "Fundador & Analista de Dados",
            "company": "Jardim do Éden",
            "desc": "Desenvolvimento de dashboards em Power BI, automações com Python e SQL, uso de IA Generativa para análises preditivas. Redução de 2h para 15min por análise.",
            "tags": ["Power BI", "Python", "SQL", "IA Generativa"],
            "badge": ""
        },
        {
            "date": "2010 – 2014 · 4 anos",
            "role": "Gestão Comercial & BI",
            "company": "J Sintonía",
            "desc": "Implementação de Business Intelligence, criação de KPIs, dashboards gerenciais e análise de viabilidade econômica.",
            "tags": ["BI", "KPIs", "Dashboards"],
            "badge": ""
        },
        {
            "date": "2009 – 2010 · 1 ano",
            "role": "Automação de Processos",
            "company": "Banco do Brasil",
            "desc": "Desenvolvimento de automações em VBA que reduziram o tempo operacional em 70%.",
            "tags": ["VBA", "Automação", "Eficiência"],
            "badge": ""
        }
    ]
    
    for exp in experiences:
        render_experience_item(**exp)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Melhorias adicionais recomendadas:
# 1. Use st.html() para HTML puro (Streamlit 1.39+) [[44]]
# 2. Considere streamlit-card para cards interativos [[61]]
# 3. Use st.key- para CSS seletivo (novo recurso) [[25]][[27]]
# 4. Implemente streamlit-timeline para timeline interativa [[50]][[51]]
