import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from datetime import datetime, timedelta
import base64

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires · Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# TEMA (DARK / LIGHT)
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_colors():
    dark = st.session_state.theme == "dark"
    if dark:
        return {
            "primary": "#3B82F6",
            "primary_hover": "#2563EB",
            "secondary": "#0EA5E9",
            "accent": "#8B5CF6",
            "success": "#22C55E",
            "warning": "#F59E0B",
            "bg": "#0B0F1A",
            "bg_elevated": "#111827",
            "text": "#F1F5F9",
            "text_muted": "#94A3B8",
            "text_subtle": "#64748B",
            "card_bg": "rgba(255,255,255,0.04)",
            "card_bg_hover": "rgba(255,255,255,0.07)",
            "border": "rgba(255,255,255,0.08)",
            "border_hover": "rgba(59,130,246,0.4)",
            "tag_bg": "rgba(59,130,246,0.12)",
            "tag_border": "rgba(59,130,246,0.25)",
            "primary_light": "rgba(59,130,246,0.15)",
            "navbar_bg": "rgba(11,15,26,0.85)",
            "navbar_border": "rgba(255,255,255,0.06)",
            "nav_hover": "rgba(255,255,255,0.06)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.1) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(59,130,246,0.18) 0%, transparent 60%)",
            "section_bg": "rgba(11,15,26,0.6)",
            "section_alt_bg": "rgba(255,255,255,0.02)",
            "shadow": "0 8px 32px rgba(0,0,0,0.4)",
            "shadow_hover": "0 16px 48px rgba(59,130,246,0.25)",
            "shadow_glow": "0 0 40px rgba(59,130,246,0.15)",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#8B5CF6","#22C55E","#F59E0B"],
            "gradient_primary": "linear-gradient(135deg, #3B82F6 0%, #0EA5E9 100%)",
            "gradient_accent": "linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%)",
            "gradient_text": "linear-gradient(135deg, #3B82F6 0%, #0EA5E9 50%, #8B5CF6 100%)"
        }
    else:
        return {
            "primary": "#1D4ED8",
            "primary_hover": "#1E40AF",
            "secondary": "#0EA5E9",
            "accent": "#7C3AED",
            "success": "#16A34A",
            "warning": "#D97706",
            "bg": "#F8FAFC",
            "bg_elevated": "#FFFFFF",
            "text": "#0F172A",
            "text_muted": "#475569",
            "text_subtle": "#94A3B8",
            "card_bg": "rgba(255,255,255,0.8)",
            "card_bg_hover": "rgba(255,255,255,0.95)",
            "border": "rgba(0,0,0,0.06)",
            "border_hover": "rgba(29,78,216,0.3)",
            "tag_bg": "#DBEAFE",
            "tag_border": "#93C5FD",
            "primary_light": "#DBEAFE",
            "navbar_bg": "rgba(248,250,252,0.9)",
            "navbar_border": "rgba(0,0,0,0.06)",
            "nav_hover": "rgba(0,0,0,0.04)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.06) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(29,78,216,0.1) 0%, transparent 60%)",
            "section_bg": "rgba(255,255,255,0.6)",
            "section_alt_bg": "rgba(0,0,0,0.01)",
            "shadow": "0 8px 32px rgba(0,0,0,0.08)",
            "shadow_hover": "0 16px 48px rgba(29,78,216,0.12)",
            "shadow_glow": "0 0 40px rgba(29,78,216,0.08)",
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8","#0EA5E9","#7C3AED","#16A34A","#D97706"],
            "gradient_primary": "linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 100%)",
            "gradient_accent": "linear-gradient(135deg, #7C3AED 0%, #1D4ED8 100%)",
            "gradient_text": "linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 50%, #7C3AED 100%)"
        }

# ============================================================================
# FUNÇÕES AUXILIARES (FOTO, PDF)
# ============================================================================
def get_foto_path():
    candidatos = [
        "assets/rapha.jpeg", "assets/rapha.jpg",
        "rapha.jpeg", "rapha.jpg",
        "foto.jpeg", "foto.jpg",
        "perfil.jpeg", "perfil.jpg"
    ]
    for caminho in candidatos:
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
    candidatos = [
        "Curriculo_Raphael_v2.pdf",
        "Curriculo_Raphael.pdf",
        "cv.pdf",
        "assets/Curriculo_Raphael_v2.pdf",
        "assets/Curriculo_Raphael.pdf",
    ]
    for caminho in candidatos:
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
# CSS PROFISSIONAL
# ============================================================================
def load_css():
    colors = get_colors()
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800;14..32,900&family=JetBrains+Mono:wght@400;500;600&display=swap');

        :root {{
            --primary: {colors['primary']};
            --primary-hover: {colors['primary_hover']};
            --secondary: {colors['secondary']};
            --accent: {colors['accent']};
            --success: {colors['success']};
            --warning: {colors['warning']};
            --bg: {colors['bg']};
            --bg-elevated: {colors['bg_elevated']};
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
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg);
            color: var(--text);
        }}
        
        /* Esconder elementos padrão Streamlit */
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: var(--bg); }}
        .block-container {{ padding: 0 !important; max-width: 100%; }}
        
        /* Esconder botões do Streamlit que interferem */
        .stButton > button {{ 
            background: transparent !important; 
            border: none !important; 
            color: inherit !important;
            padding: 0 !important;
            font-size: inherit !important;
        }}
        .stButton > button:hover {{ background: transparent !important; }}
        .stButton > button:focus {{ outline: none !important; box-shadow: none !important; }}

        /* ============ NAVBAR PREMIUM ============ */
        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
            background: var(--navbar-bg);
            backdrop-filter: blur(20px) saturate(200%);
            -webkit-backdrop-filter: blur(20px) saturate(200%);
            border-bottom: 1px solid var(--navbar-border);
            padding: 0.875rem 2.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.3s ease;
        }}
        .navbar-brand {{ 
            font-weight: 800; font-size: 1.3rem; 
            letter-spacing: -0.03em; 
            color: var(--text); 
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
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
        .navbar-links {{ 
            display: flex; gap: 0.5rem; align-items: center; 
        }}
        .nav-link {{
            padding: 0.5rem 1.1rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.25s ease;
            color: var(--text-muted); background: transparent;
            cursor: pointer; position: relative;
        }}
        .nav-link:hover {{ 
            background: var(--nav-hover); 
            color: var(--text);
            transform: translateY(-1px);
        }}
        .nav-link.active {{
            background: var(--gradient-primary); 
            color: white !important;
            box-shadow: 0 4px 16px rgba(59,130,246,0.35);
        }}
        .theme-toggle {{
            width: 40px; height: 40px; border-radius: 50%;
            background: var(--card-bg); border: 1px solid var(--border);
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: all 0.25s ease;
            font-size: 1.1rem; margin-left: 0.5rem;
        }}
        .theme-toggle:hover {{
            background: var(--nav-hover);
            border-color: var(--primary);
            transform: rotate(15deg) scale(1.05);
            box-shadow: var(--shadow-glow);
        }}

        /* ============ HERO SECTION ============ */
        .hero-full {{
            min-height: 85vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 7rem 2rem 3rem;
            background: var(--hero-bg);
            position: relative;
            overflow: hidden;
        }}
        .hero-full::before {{
            content: ''; position: absolute; inset: 0;
            background: var(--hero-glow);
            opacity: 0.5; pointer-events: none;
        }}
        .hero-full::after {{
            content: ''; position: absolute; inset: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(139,92,246,0.08) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(14,165,233,0.06) 0%, transparent 50%);
            pointer-events: none;
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
            gap: 4rem;
            align-items: center;
            position: relative; z-index: 2;
        }}
        @media (max-width: 900px) {{
            .hero-content {{ grid-template-columns: 1fr; text-align: center; gap: 2rem; }}
            .hero-photo-wrapper {{ margin: 0 auto; }}
        }}
        
        .hero-photo-wrapper {{
            position: relative;
            width: 260px; height: 260px;
        }}
        .hero-photo-ring {{
            position: absolute; inset: -12px;
            border-radius: 50%;
            background: conic-gradient(from 0deg, var(--primary), var(--secondary), var(--accent), var(--primary));
            animation: rotate-ring 8s linear infinite;
            opacity: 0.6;
        }}
        .hero-photo-ring::after {{
            content: ''; position: absolute; inset: 4px;
            border-radius: 50%;
            background: var(--bg);
        }}
        @keyframes rotate-ring {{
            to {{ transform: rotate(360deg); }}
        }}
        .hero-photo {{
            position: relative; z-index: 2;
            width: 260px; height: 260px; border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--bg);
            box-shadow: 0 25px 80px rgba(59,130,246,0.3);
        }}
        .hero-status-badge {{
            position: absolute; bottom: 10px; right: 10px; z-index: 3;
            background: var(--success);
            width: 28px; height: 28px; border-radius: 50%;
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
            letter-spacing: -0.04em; line-height: 1.05; 
            color: var(--text); 
            margin-bottom: 0.5rem;
        }}
        .hero-text h1 .gradient-name {{ 
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .hero-text .role-tag {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--primary-light);
            border: 1px solid var(--tag-border);
            padding: 0.35rem 1rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--primary);
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .hero-text .role-tag .dot {{
            width: 6px; height: 6px; border-radius: 50%;
            background: var(--primary);
        }}
        .hero-text .subtitle {{ 
            font-size: 1.15rem; 
            color: var(--text-muted); 
            margin: 0.5rem 0 1.5rem; 
            line-height: 1.7; 
            max-width: 540px;
        }}
        .hero-text .badge-group {{ 
            display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; 
        }}
        @media (max-width: 900px) {{
            .hero-text .badge-group {{ justify-content: center; }}
            .hero-text .subtitle {{ margin-left: auto; margin-right: auto; }}
        }}
        .hero-text .badge {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            padding: 0.4rem 0.9rem; border-radius: 10px;
            font-size: 0.78rem; font-weight: 500; color: var(--text);
            transition: all 0.2s ease;
            backdrop-filter: blur(8px);
        }}
        .hero-text .badge:hover {{
            border-color: var(--primary);
            background: var(--primary-light);
            transform: translateY(-2px);
        }}
        .hero-text .cta-group {{ 
            display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 2rem; 
        }}
        @media (max-width: 900px) {{
            .hero-text .cta-group {{ justify-content: center; }}
        }}
        .btn-primary {{
            background: var(--gradient-primary); 
            color: white !important;
            padding: 0.75rem 1.75rem; border-radius: 12px;
            font-weight: 600; text-decoration: none; transition: all 0.25s ease;
            display: inline-flex; align-items: center; gap: 0.5rem;
            border: none; cursor: pointer; font-size: 0.9rem;
            box-shadow: 0 4px 16px rgba(59,130,246,0.3);
        }}
        .btn-primary:hover {{ 
            transform: translateY(-2px); 
            box-shadow: 0 8px 28px rgba(59,130,246,0.45);
        }}
        .btn-secondary {{
            background: var(--card-bg); 
            border: 1px solid var(--border);
            padding: 0.75rem 1.75rem; border-radius: 12px;
            font-weight: 600; color: var(--text) !important; 
            text-decoration: none; transition: all 0.25s ease; 
            display: inline-flex; align-items: center; gap: 0.5rem;
            backdrop-filter: blur(8px);
            font-size: 0.9rem;
        }}
        .btn-secondary:hover {{ 
            background: var(--card-bg-hover);
            border-color: var(--primary);
            transform: translateY(-2px);
        }}

        /* ============ SEÇÕES ============ */
        .section-glass {{
            padding: 5rem 2rem;
            background: var(--section-bg);
            backdrop-filter: blur(8px);
            border-top: 1px solid var(--border);
            position: relative;
        }}
        .section-glass.alt {{
            background: var(--section-alt-bg);
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{ text-align: center; margin-bottom: 3.5rem; }}
        .section-header .label {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--primary-light);
            border: 1px solid var(--tag-border);
            padding: 0.35rem 1.1rem; border-radius: 999px;
            font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.1em; color: var(--primary);
            margin-bottom: 1rem;
        }}
        .section-header h2 {{ 
            font-size: 2.5rem; font-weight: 800; 
            margin-top: 0.5rem; color: var(--text); 
            letter-spacing: -0.03em; 
            line-height: 1.15;
        }}
        .section-header p {{ 
            color: var(--text-muted); 
            max-width: 600px; 
            margin: 1rem auto 0; 
            font-size: 1.05rem;
            line-height: 1.6;
        }}

        /* ============ KPI CARDS ============ */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1.25rem;
        }}
        @media (max-width: 1024px) {{ .kpi-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
        @media (max-width: 640px) {{ .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        
        .kpi-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 1.75rem 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .kpi-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: var(--gradient-primary);
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        .kpi-card:hover {{
            transform: translateY(-6px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .kpi-card:hover::before {{ opacity: 1; }}
        .kpi-icon {{
            width: 48px; height: 48px;
            border-radius: 14px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 1rem;
            font-size: 1.4rem;
        }}
        .kpi-value {{
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
            margin-bottom: 0.35rem;
        }}
        .kpi-label {{
            font-size: 0.82rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        /* ============ GLASS CARDS ============ */
        .glass-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 1.75rem;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }}
        .glass-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: var(--gradient-primary);
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        .glass-card:hover {{ 
            transform: translateY(-8px); 
            border-color: var(--border-hover); 
            box-shadow: var(--shadow-hover);
        }}
        .glass-card:hover::before {{ opacity: 1; }}
        
        .glass-card h3 {{
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            color: var(--text);
            letter-spacing: -0.01em;
        }}
        .glass-card p {{
            color: var(--text-muted);
            line-height: 1.65;
            font-size: 0.92rem;
        }}
        .glass-card .card-icon {{
            width: 56px; height: 56px;
            border-radius: 16px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.6rem;
            margin-bottom: 1rem;
        }}

        /* ============ PROJECT GRID ============ */
        .project-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
        }}
        @media (max-width: 768px) {{ .project-grid {{ grid-template-columns: 1fr; }} }}
        
        .project-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .project-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: var(--gradient-primary);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }}
        .project-card:hover {{
            transform: translateY(-8px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .project-card:hover::before {{ transform: scaleX(1); }}
        .project-card .project-icon {{
            width: 64px; height: 64px;
            border-radius: 18px;
            background: var(--gradient-primary);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 8px 24px rgba(59,130,246,0.25);
        }}
        .project-card h3 {{
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            color: var(--text);
        }}
        .project-card p {{
            color: var(--text-muted);
            line-height: 1.65;
            font-size: 0.92rem;
            margin-bottom: 1.25rem;
        }}
        .project-card .project-tags {{
            display: flex; flex-wrap: wrap; gap: 0.4rem;
            margin-bottom: 1.25rem;
        }}
        .project-card .project-tag {{
            font-size: 0.7rem;
            background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            color: var(--primary);
            font-weight: 600;
        }}

        /* ============ TIMELINE ============ */
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
        .timeline-item:nth-child(1) {{ animation-delay: 0.1s; }}
        .timeline-item:nth-child(2) {{ animation-delay: 0.2s; }}
        .timeline-item:nth-child(3) {{ animation-delay: 0.3s; }}
        .timeline-item:nth-child(4) {{ animation-delay: 0.4s; }}
        
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .timeline-dot {{
            position: absolute; left: 20px; top: 8px; width: 18px; height: 18px;
            border-radius: 50%; 
            background: var(--gradient-primary);
            border: 3px solid var(--bg); 
            box-shadow: 0 0 0 4px var(--primary), 0 0 20px rgba(59,130,246,0.4);
            z-index: 2;
        }}
        .timeline-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 20px; padding: 1.75rem;
            transition: all 0.3s ease;
        }}
        .timeline-card:hover {{ 
            border-color: var(--border-hover); 
            transform: translateX(8px); 
            box-shadow: var(--shadow-hover);
        }}
        .timeline-date {{
            display: inline-block; font-size: 0.72rem; font-weight: 700;
            background: var(--primary-light); color: var(--primary);
            padding: 0.25rem 0.9rem; border-radius: 999px;
            letter-spacing: 0.02em;
        }}
        .timeline-badge {{
            background: var(--gradient-primary); color: white;
            font-size: 0.62rem; font-weight: 800; padding: 0.2rem 0.7rem;
            border-radius: 999px; margin-left: 0.5rem; display: inline-block;
            text-transform: uppercase; letter-spacing: 0.05em;
            box-shadow: 0 2px 8px rgba(59,130,246,0.3);
            animation: pulse-badge 2s infinite;
        }}
        @keyframes pulse-badge {{
            0%, 100% {{ box-shadow: 0 2px 8px rgba(59,130,246,0.3); }}
            50% {{ box-shadow: 0 2px 16px rgba(59,130,246,0.5); }}
        }}
        .timeline-role {{ 
            font-size: 1.2rem; font-weight: 700; margin: 0.5rem 0 0.2rem; 
            letter-spacing: -0.01em;
        }}
        .timeline-company {{ 
            color: var(--secondary); font-weight: 600; font-size: 0.95rem;
            margin-bottom: 0.75rem;
        }}
        .timeline-desc {{ 
            color: var(--text-muted); line-height: 1.7; font-size: 0.92rem;
            margin-bottom: 0.75rem;
        }}
        .timeline-tag {{
            font-size: 0.72rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border); padding: 0.25rem 0.7rem;
            border-radius: 8px; display: inline-block; margin: 0.2rem;
            color: var(--primary); font-weight: 600;
        }}

        /* ============ CERTIFICAÇÕES ============ */
        .cert-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
        }}
        @media (max-width: 768px) {{ .cert-grid {{ grid-template-columns: 1fr; }} }}
        
        .cert-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }}
        .cert-card:hover {{
            transform: translateY(-6px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .cert-icon {{
            width: 72px; height: 72px;
            border-radius: 20px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 1.25rem;
            font-size: 2rem;
        }}
        .cert-card h4 {{
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: var(--text);
        }}
        .cert-card p {{
            color: var(--text-muted);
            font-size: 0.88rem;
            line-height: 1.6;
            margin-bottom: 1rem;
        }}
        .progress-bar {{
            width: 100%;
            height: 8px;
            background: var(--border);
            border-radius: 999px;
            overflow: hidden;
            margin-top: 0.75rem;
        }}
        .progress-fill {{
            height: 100%;
            background: var(--gradient-primary);
            border-radius: 999px;
            transition: width 1s ease;
            box-shadow: 0 0 12px var(--primary);
        }}

        /* ============ AWS JOURNEY ============ */
        .aws-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            text-align: center;
        }}
        .aws-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 1.5rem 1rem;
            transition: all 0.3s ease;
        }}
        .aws-card:hover {{
            transform: translateY(-4px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .aws-card .aws-icon {{
            font-size: 2.2rem;
            margin-bottom: 0.75rem;
        }}
        .aws-card .aws-label {{
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text);
        }}
        .aws-card .aws-status {{
            font-size: 0.7rem;
            color: var(--success);
            font-weight: 600;
            margin-top: 0.35rem;
        }}

        /* ============ TESTIMONIALS ============ */
        .testimonial-grid {{ 
            display: grid; 
            grid-template-columns: repeat(3, 1fr); 
            gap: 1.5rem; 
        }}
        @media (max-width: 768px) {{ .testimonial-grid {{ grid-template-columns: 1fr; }} }}
        
        .testimonial-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
        }}
        .testimonial-card::before {{
            content: '"';
            position: absolute;
            top: 1rem; right: 1.5rem;
            font-size: 4rem;
            font-weight: 900;
            color: var(--primary);
            opacity: 0.15;
            line-height: 1;
            font-family: Georgia, serif;
        }}
        .testimonial-card:hover {{
            transform: translateY(-6px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .testimonial-text {{
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.7;
            font-style: italic;
            margin-bottom: 1.25rem;
        }}
        .testimonial-author {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .testimonial-avatar {{
            width: 44px; height: 44px;
            border-radius: 50%;
            background: var(--gradient-primary);
            display: flex; align-items: center; justify-content: center;
            color: white; font-weight: 700; font-size: 1rem;
        }}
        .testimonial-name {{
            font-weight: 700;
            font-size: 0.92rem;
            color: var(--text);
        }}
        .testimonial-role {{
            font-size: 0.78rem;
            color: var(--text-subtle);
        }}

        /* ============ FOOTER ============ */
        .footer {{
            padding: 4rem 2rem 2.5rem; 
            text-align: center;
            border-top: 1px solid var(--border);
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            position: relative;
        }}
        .footer::before {{
            content: '';
            position: absolute;
            top: 0; left: 50%;
            transform: translateX(-50%);
            width: 200px; height: 1px;
            background: var(--gradient-primary);
        }}
        .footer .status {{
            display: inline-flex; align-items: center; gap: 0.6rem;
            background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.25);
            padding: 0.4rem 1.2rem; border-radius: 999px;
            font-size: 0.82rem; font-weight: 600; color: var(--success);
            margin-bottom: 1.5rem;
        }}
        .footer .status-dot {{
            width: 8px; height: 8px; border-radius: 50%;
            background: var(--success); 
            box-shadow: 0 0 12px var(--success);
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} }}
        
        .footer h3 {{
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
            background: var(--gradient-text);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .footer .footer-subtitle {{
            color: var(--text-muted);
            font-size: 1.05rem;
            margin-bottom: 2rem;
        }}
        .footer-modes {{
            display: flex; justify-content: center; flex-wrap: wrap; 
            gap: 0.5rem; margin-bottom: 2rem;
        }}
        .footer-mode {{
            background: var(--tag-bg); border: 1px solid var(--tag-border);
            padding: 0.4rem 1rem; border-radius: 999px;
            font-size: 0.82rem; font-weight: 500;
            color: var(--text);
            transition: all 0.2s ease;
        }}
        .footer-mode:hover {{
            background: var(--primary-light);
            border-color: var(--primary);
        }}
        .footer-links {{ 
            display: flex; justify-content: center; flex-wrap: wrap; 
            gap: 0.6rem; margin: 2rem 0 1.5rem; 
        }}
        .footer-link {{
            background: var(--card-bg); 
            border: 1px solid var(--border);
            padding: 0.6rem 1.25rem; border-radius: 12px;
            color: var(--text) !important; text-decoration: none;
            font-size: 0.88rem; font-weight: 500;
            transition: all 0.25s ease;
            display: inline-flex; align-items: center; gap: 0.4rem;
        }}
        .footer-link:hover {{ 
            background: var(--gradient-primary); 
            color: white !important;
            border-color: transparent;
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(59,130,246,0.3);
        }}
        .footer-copy {{ 
            color: var(--text-subtle); 
            font-size: 0.8rem; 
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border);
        }}

        /* ============ ANÁLISES / DASHBOARD ============ */
        .page-header {{
            padding: 7rem 2rem 2rem;
            text-align: center;
            background: var(--hero-bg);
            position: relative;
            overflow: hidden;
        }}
        .page-header::before {{
            content: ''; position: absolute; inset: 0;
            background: var(--hero-glow);
            opacity: 0.4; pointer-events: none;
        }}
        .page-header h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
            position: relative; z-index: 2;
        }}
        .page-header p {{
            color: var(--text-muted);
            font-size: 1.05rem;
            position: relative; z-index: 2;
        }}
        .analytics-container {{
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        /* Tabs customizados */
        .custom-tabs {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 2rem;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 0.5rem;
            backdrop-filter: blur(12px);
            flex-wrap: wrap;
        }}
        .custom-tab {{
            padding: 0.65rem 1.25rem;
            border-radius: 12px;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.25s ease;
            border: none;
            background: transparent;
        }}
        .custom-tab:hover {{
            color: var(--text);
            background: var(--nav-hover);
        }}
        .custom-tab.active {{
            background: var(--gradient-primary);
            color: white;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
        }}

        /* Metric cards customizados */
        .metric-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }}
        .metric-card:hover {{
            transform: translateY(-4px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .metric-label {{
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }}
        .metric-value {{
            font-size: 1.75rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--text);
            line-height: 1.1;
        }}
        .metric-delta {{
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--success);
            margin-top: 0.35rem;
        }}

        /* Chart containers */
        .chart-container {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 1.75rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }}
        .chart-container:hover {{
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}
        .chart-title {{
            font-size: 1rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        /* ============ SCROLL TO TOP ============ */
        .scroll-top {{
            position: fixed;
            bottom: 2rem; right: 2rem;
            width: 48px; height: 48px;
            border-radius: 50%;
            background: var(--gradient-primary);
            color: white;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(59,130,246,0.35);
            transition: all 0.25s ease;
            z-index: 999;
            text-decoration: none;
        }}
        .scroll-top:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(59,130,246,0.5);
        }}

        /* ============ ANIMAÇÕES GLOBAIS ============ */
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .fade-in {{ animation: fadeIn 0.6s ease backwards; }}
        .slide-up {{ animation: slideUp 0.6s ease backwards; }}

        /* ============ RESPONSIVIDADE ============ */
        @media (max-width: 768px) {{
            .navbar {{ padding: 0.75rem 1rem; }}
            .navbar-brand {{ font-size: 1.1rem; }}
            .navbar-links {{ gap: 0.25rem; }}
            .nav-link {{ padding: 0.4rem 0.75rem; font-size: 0.8rem; }}
            .theme-toggle {{ width: 36px; height: 36px; font-size: 1rem; }}
            .hero-full {{ padding: 6rem 1rem 2rem; min-height: auto; }}
            .hero-text h1 {{ font-size: 2.2rem; }}
            .hero-photo-wrapper {{ width: 200px; height: 200px; }}
            .hero-photo {{ width: 200px; height: 200px; }}
            .section-glass {{ padding: 3rem 1rem; }}
            .section-header h2 {{ font-size: 1.8rem; }}
            .kpi-value {{ font-size: 1.5rem; }}
            .footer h3 {{ font-size: 1.5rem; }}
        }}

        /* ============ CUSTOMIZAÇÃO STREAMLIT ============ */
        .stSelectbox > div > div {{
            background: var(--card-bg) !important;
            border: 1px solid var(--border) !important;
            border-radius: 12px !important;
            color: var(--text) !important;
        }}
        .stMultiSelect > div > div {{
            background: var(--card-bg) !important;
            border: 1px solid var(--border) !important;
            border-radius: 12px !important;
        }}
        .stDataFrame {{
            border: 1px solid var(--border) !important;
            border-radius: 16px !important;
            overflow: hidden !important;
        }}
        .stExpander {{
            background: var(--card-bg) !important;
            border: 1px solid var(--border) !important;
            border-radius: 16px !important;
        }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# RENDERIZAÇÃO DAS PÁGINAS
# ============================================================================

def render_home():
    colors = get_colors()
    foto_path = get_foto_path()
    foto_b64 = get_foto_base64(foto_path)
    foto_url = foto_b64 if foto_b64 else "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff&bold=true"
    pdf_path = get_pdf_path()
    pdf_b64 = get_pdf_base64(pdf_path)

    # HERO
    st.markdown(f"""
    <section class="hero-full" id="topo">
        <div class="hero-grid-bg"></div>
        <div class="hero-content">
            <div class="hero-photo-wrapper">
                <div class="hero-photo-ring"></div>
                <img src="{foto_url}" alt="Raphael Pires" class="hero-photo">
                <div class="hero-status-badge" title="Disponível"></div>
            </div>
            <div class="hero-text">
                <div class="role-tag"><span class="dot"></span> Analista de Dados & BI</div>
                <h1>Raphael <span class="gradient-name">Pires</span></h1>
                <p class="subtitle">
                    Mais de <strong>16 anos</strong> transformando dados brutos em decisões estratégicas. 
                    Especialista em <strong>Power BI, Python e Cloud</strong>, com foco em automação, 
                    governança de dados e dashboards que geram impacto real no negócio.
                </p>
                <div class="badge-group">
                    <span class="badge">📊 Power BI</span>
                    <span class="badge">🐍 Python</span>
                    <span class="badge">🗄️ SQL</span>
                    <span class="badge">☁️ AWS</span>
                    <span class="badge">🤖 IA Generativa</span>
                    <span class="badge">📈 Dashboards</span>
                    <span class="badge">🔄 ETL</span>
                </div>
                <div class="cta-group">
                    <a href="#experiencia" class="btn-primary">Ver trajetória ↓</a>
                    {'<a href="' + pdf_b64 + '" download="Curriculo_Raphael_Pires.pdf" class="btn-secondary">📄 Baixar CV</a>' if pdf_b64 else ''}
                    <a href="#contato" class="btn-secondary">💬 Contato</a>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    # KPIs
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">📈 Impacto Mensurável</span>
                <h2>Números que contam histórias</h2>
                <p>Resultados concretos de mais de uma década transformando dados em valor</p>
            </div>
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-icon">⏱️</div>
                    <div class="kpi-value">16+</div>
                    <div class="kpi-label">Anos de experiência</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">⚡</div>
                    <div class="kpi-value">70%</div>
                    <div class="kpi-label">Redução operacional</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">📊</div>
                    <div class="kpi-value">213k</div>
                    <div class="kpi-label">Registros processados</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">🚀</div>
                    <div class="kpi-value">2h→15m</div>
                    <div class="kpi-label">Tempo de análise</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">💰</div>
                    <div class="kpi-value">R$50bi</div>
                    <div class="kpi-label">Dados analisados</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Experiência
    st.markdown("""
    <div class="section-glass alt" id="experiencia">
        <div class="container">
            <div class="section-header">
                <span class="label">💼 Trajetória</span>
                <h2>Experiência profissional</h2>
                <p>Uma jornada de evolução contínua em dados, BI e automação</p>
            </div>
            <div class="timeline">
    """, unsafe_allow_html=True)

    experiences = [
        {"date":"2014 – Presente · 10+ anos","role":"Analista de Dados & BI","company":"NSM Comércio","desc":"Centralização de dados, construção de indicadores estratégicos, automação de relatórios e governança. Redução de 70% do tempo operacional com implementação de pipelines automatizados.","tags":["Dados","Governança","Indicadores","Automação","Power BI"],"badge":"Atual"},
        {"date":"2012 – Presente · 12+ anos","role":"Fundador & Analista de Dados","company":"Jardim do Éden (Varejo de Moda)","desc":"Estruturação da base de dados, modelagem, limpeza, integração e desenvolvimento de dashboards gerenciais com SQL, Python, Power BI e Looker Studio — reduzindo ciclo de análise de 2h para 15 min.","tags":["Power BI","Python","SQL","IA Generativa","Looker"],"badge":""},
        {"date":"2010 – 2014 · 4 anos","role":"Fundador & Analista de KPIs","company":"J Sintonía (Varejo Especializado)","desc":"Monitoramento de KPIs de vendas, margem e rentabilidade com relatórios automatizados. Análise de viabilidade econômica que fundamentou encerramento estratégico planejado em 2026, evitando prejuízo.","tags":["BI","KPIs","Dashboards","SQL"],"badge":""},
        {"date":"2009 – 2010 · 1 ano","role":"Estagiário de Automação e Dados","company":"Banco do Brasil S.A.","desc":"Desenvolvimento de macros VBA em 20 agências, reduzindo 70% do tempo operacional. Saneou e padronizou bases de dados gerenciais internas.","tags":["VBA","Automação","Eficiência","SQL"],"badge":""}
    ]

    for exp in experiences:
        tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        badge = f'<span class="timeline-badge">{exp["badge"]}</span>' if exp["badge"] else ""
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span> {badge}
                <div class="timeline-role">{exp["role"]}</div>
                <div class="timeline-company">{exp["company"]}</div>
                <div class="timeline-desc">{exp["desc"]}</div>
                <div>{tags}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div></div>", unsafe_allow_html=True)

    # Projetos
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">🚀 Portfólio</span>
                <h2>Projetos de Analytics</h2>
                <p>Aplicações reais construídas com Python, Streamlit e visualizações interativas</p>
            </div>
            <div class="project-grid">
                <div class="project-card">
                    <div class="project-icon">🇧🇷</div>
                    <h3>Desenrola Brasil</h3>
                    <p>Painel analítico executivo com Python, Pandas, Plotly e Streamlit. Processamento de dados oficiais do Banco Central com KPIs, séries temporais e análise de concentração de mercado (HHI).</p>
                    <div class="project-tags">
                        <span class="project-tag">Python</span>
                        <span class="project-tag">Pandas</span>
                        <span class="project-tag">Plotly</span>
                        <span class="project-tag">Streamlit</span>
                    </div>
                    <a href="https://desenrolabrasil.streamlit.app" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver App</a>
                </div>
                <div class="project-card">
                    <div class="project-icon">🔬</div>
                    <h3>CNPq Analytics</h3>
                    <p>ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos, evidenciando desigualdades regionais. Dashboard interativo com filtros dinâmicos.</p>
                    <div class="project-tags">
                        <span class="project-tag">ETL</span>
                        <span class="project-tag">Python</span>
                        <span class="project-tag">Dashboards</span>
                        <span class="project-tag">BI</span>
                    </div>
                    <a href="https://cnpa-analytics.streamlit.app" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver App</a>
                </div>
                <div class="project-card">
                    <div class="project-icon">⛽</div>
                    <h3>Análise de Combustíveis (ANP)</h3>
                    <p>Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da Agência Nacional do Petróleo. Monitoramento de preços em tempo real.</p>
                    <div class="project-tags">
                        <span class="project-tag">ANP</span>
                        <span class="project-tag">Plotly</span>
                        <span class="project-tag">Time Series</span>
                    </div>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">📊 Ver Projeto</a>
                </div>
                <div class="project-card">
                    <div class="project-icon">💎</div>
                    <h3>Portfólio Premium</h3>
                    <p>Este portfólio construído em Streamlit com design premium, glassmorphism, dark/light mode e navegação fixa. Código aberto no GitHub.</p>
                    <div class="project-tags">
                        <span class="project-tag">Streamlit</span>
                        <span class="project-tag">CSS</span>
                        <span class="project-tag">Design</span>
                        <span class="project-tag">UX</span>
                    </div>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">💻 Ver Código</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Certificações
    st.markdown(f"""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">🎓 Certificações</span>
                <h2>Formação contínua</h2>
                <p>Aprendizado constante em tecnologias de ponta</p>
            </div>
            <div class="cert-grid">
                <div class="cert-card">
                    <div class="cert-icon">📘</div>
                    <h4>Hashtag Treinamentos</h4>
                    <p>SQL Avançado · Power BI · Python para Análise de Dados · Algoritmos e IA Aplicada</p>
                    <div style="display:inline-block;background:{colors['success']};color:white;padding:0.25rem 0.9rem;border-radius:999px;font-size:0.75rem;font-weight:700;">✓ Concluído</div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">☁️</div>
                    <h4>AWS Educate</h4>
                    <p>8 módulos: Cloud Computing, Console, Storage, ML Foundations, Sustainability, Cloud Support</p>
                    <div class="progress-bar"><div class="progress-fill" style="width:40%;"></div></div>
                    <div style="font-size:0.78rem;color:{colors['text_muted']};margin-top:0.5rem;font-weight:600;">40% concluído</div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">🎯</div>
                    <h4>Meta 2026</h4>
                    <p>Certificação AWS Cloud Practitioner — em preparação ativa com foco em arquitetura de dados</p>
                    <div style="display:inline-block;background:{colors['warning']};color:white;padding:0.25rem 0.9rem;border-radius:999px;font-size:0.75rem;font-weight:700;">🔄 Em progresso</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # AWS Journey
    st.markdown(f"""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">☁️ Cloud Journey</span>
                <h2>AWS em progresso</h2>
                <p>Atualmente em trilha de certificação, com foco em arquitetura de dados e machine learning na nuvem</p>
            </div>
            <div class="aws-grid">
                <div class="aws-card">
                    <div class="aws-icon">📘</div>
                    <div class="aws-label">Cloud 101</div>
                    <div class="aws-status">✓ Completo</div>
                </div>
                <div class="aws-card">
                    <div class="aws-icon">🖥️</div>
                    <div class="aws-label">AWS Console</div>
                    <div class="aws-status">✓ Completo</div>
                </div>
                <div class="aws-card">
                    <div class="aws-icon">💾</div>
                    <div class="aws-label">Storage</div>
                    <div class="aws-status">✓ Completo</div>
                </div>
                <div class="aws-card">
                    <div class="aws-icon">🤖</div>
                    <div class="aws-label">ML Foundations</div>
                    <div class="aws-status">✓ Completo</div>
                </div>
                <div class="aws-card">
                    <div class="aws-icon">🌱</div>
                    <div class="aws-label">Sustainability</div>
                    <div class="aws-status">✓ Completo</div>
                </div>
                <div class="aws-card">
                    <div class="aws-icon">🛡️</div>
                    <div class="aws-label">Cloud Support</div>
                    <div class="aws-status">✓ Completo</div>
                </div>
            </div>
            <div style="text-align:center;margin-top:2rem;">
                <span style="background:{colors['primary_light']};color:{colors['primary']};padding:0.4rem 1.4rem;border-radius:999px;font-size:0.85rem;font-weight:700;border:1px solid {colors['tag_border']};">🎯 Meta 2026: AWS Cloud Practitioner</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Testimonials
    st.markdown("""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">💬 Recomendações</span>
                <h2>O que dizem sobre meu trabalho</h2>
                <p>Feedback de colegas e líderes com quem tive o prazer de colaborar</p>
            </div>
            <div class="testimonial-grid">
                <div class="testimonial-card">
                    <p class="testimonial-text">Raphael transformou completamente nossa forma de analisar dados. Os dashboards que ele criou reduziram drasticamente o tempo de tomada de decisão.</p>
                    <div class="testimonial-author">
                        <div class="testimonial-avatar">GM</div>
                        <div>
                            <div class="testimonial-name">Gestor de Operações</div>
                            <div class="testimonial-role">NSM Comércio</div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <p class="testimonial-text">Profissional excepcional com capacidade única de traduzir necessidades de negócio em soluções técnicas elegantes. Sua automação VBA economizou centenas de horas.</p>
                    <div class="testimonial-author">
                        <div class="testimonial-avatar">CB</div>
                        <div>
                            <div class="testimonial-name">Coordenador Bancário</div>
                            <div class="testimonial-role">Banco do Brasil</div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <p class="testimonial-text">A visão estratégica do Raphael sobre dados é impressionante. Ele não apenas constrói relatórios, mas conta histórias que orientam decisões importantes.</p>
                    <div class="testimonial-author">
                        <div class="testimonial-avatar">DV</div>
                        <div>
                            <div class="testimonial-name">Diretor de Varejo</div>
                            <div class="testimonial-role">Jardim do Éden</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Skills
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">⚡ Competências</span>
                <h2>Domínio tecnológico</h2>
                <p>Stack tecnológica refinada ao longo de 16+ anos de atuação</p>
            </div>
    """, unsafe_allow_html=True)
    render_skills_chart()
    st.markdown("</div></div>", unsafe_allow_html=True)


def render_skills_chart():
    colors = get_colors()
    df = pd.DataFrame({
        "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "Plotly", "AWS"],
        "Proficiência": [95, 92, 88, 95, 85, 82, 60],
        "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "BI", "Cloud"]
    })
    fig = px.bar(
        df,
        x="Proficiência",
        y="Tecnologia",
        color="Categoria",
        orientation="h",
        color_discrete_sequence=colors["chart_colors"],
        template=colors["plotly_template"],
        text="Proficiência"
    )
    fig.update_layout(
        height=420,
        margin=dict(l=20, r=60, t=20, b=40),
        xaxis=dict(range=[0, 110], showgrid=True, gridcolor="rgba(148,163,184,0.12)", zeroline=False),
        yaxis=dict(showgrid=False, categoryorder='total ascending'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter", color=colors["text"], size=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=True
    )
    fig.update_traces(
        textposition="outside", 
        textfont=dict(color=colors["text"], size=12, family="Inter"),
        marker=dict(cornerradius=6)
    )
    st.plotly_chart(fig, use_container_width=True)


def render_analytics():
    colors = get_colors()
    
    st.markdown(f"""
    <div class="page-header">
        <h1>📊 Analytics Interativo</h1>
        <p>Demonstrações construídas em Streamlit + Plotly com dados simulados</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="analytics-container">', unsafe_allow_html=True)
    
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ ANP Combustíveis", "📈 Impacto Operacional"])

    with tabs[0]:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">🇧🇷 Análise de Renegociação de Dívidas</div>
        </div>
        """, unsafe_allow_html=True)
        
        np.random.seed(42)
        regioes = ["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
        status = ["Renegociado","Em Negociação","Inadimplente"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[.45,.28,.15,.07,.05]),
            "Valor": np.random.lognormal(8.5, 1.2, 400),
            "Status": np.random.choice(status, 400, p=[.65,.25,.10])
        })
        
        col1, col2 = st.columns(2)
        reg = col1.multiselect("Região", regioes, default=regioes)
        stat = col2.multiselect("Status", status, default=status)
        filtro = df[df["Região"].isin(reg) & df["Status"].isin(stat)]
        
        if filtro.empty:
            st.info("Nenhum registro encontrado.")
        else:
            st.markdown(f"""
            <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.5rem 0;">
                <div class="metric-card">
                    <div class="metric-label">Contratos</div>
                    <div class="metric-value">{len(filtro):,}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Valor Total</div>
                    <div class="metric-value">R$ {filtro['Valor'].sum()/1e6:.1f}M</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Taxa de Sucesso</div>
                    <div class="metric-value">{(filtro['Status']=='Renegociado').mean()*100:.1f}%</div>
                    <div class="metric-delta">↑ Acima da meta</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            a, b = st.columns(2)
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=.6, 
                         template=colors["plotly_template"],
                         color_discrete_sequence=colors["chart_colors"])
            fig1.update_layout(margin=dict(l=20,r=20,t=20,b=20), height=380,
                              paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font=dict(color=colors["text"]))
            fig2 = px.histogram(filtro, x="Status", color="Status", 
                               template=colors["plotly_template"],
                               color_discrete_sequence=colors["chart_colors"])
            fig2.update_layout(margin=dict(l=20,r=20,t=20,b=20), height=380,
                              paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              font=dict(color=colors["text"]), showlegend=False)
            a.plotly_chart(fig1, use_container_width=True)
            b.plotly_chart(fig2, use_container_width=True)

    with tabs[1]:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">⛽ Evolução de Preços de Combustíveis</div>
        </div>
        """, unsafe_allow_html=True)
        
        estados = ["SP","RJ","MG","PR"]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
        dados = []
        np.random.seed(1)
        for e in estados:
            preco = 5.4
            for m in meses:
                preco += np.random.normal(0, .10)
                dados.append([e, m, preco])
        df = pd.DataFrame(dados, columns=["Estado","Mês","Preço"])
        estado = st.selectbox("Estado", estados)
        f = df[df["Estado"] == estado]
        
        st.markdown(f"""
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.5rem 0;">
            <div class="metric-card">
                <div class="metric-label">Preço Médio</div>
                <div class="metric-value">R$ {f['Preço'].mean():.2f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Preço Mínimo</div>
                <div class="metric-value">R$ {f['Preço'].min():.2f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Preço Máximo</div>
                <div class="metric-value">R$ {f['Preço'].max():.2f}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        fig = px.line(f, x="Mês", y="Preço", markers=True, 
                     template=colors["plotly_template"],
                     color_discrete_sequence=[colors["chart_colors"][0]])
        fig.update_layout(height=400, margin=dict(l=20,r=20,t=20,b=20),
                         paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                         font=dict(color=colors["text"]))
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">📈 Impacto da Automação em Horas Operacionais</div>
        </div>
        """, unsafe_allow_html=True)
        
        antes = [120,125,118,130,122,128,126,124,129,127,125,130]
        depois = [95,70,55,45,38,35,33,32,30,29,28,27]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        df = pd.DataFrame({
            "Mês": meses*2,
            "Horas": antes + depois,
            "Período": ["Antes"]*12 + ["Depois"]*12
        })
        fig = px.area(df, x="Mês", y="Horas", color="Período", 
                     template=colors["plotly_template"],
                     color_discrete_sequence=[colors["chart_colors"][0], colors["chart_colors"][3]])
        fig.update_layout(height=400, margin=dict(l=20,r=20,t=20,b=20),
                         paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                         font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.5rem 0;">
            <div class="metric-card">
                <div class="metric-label">Horas Economizadas</div>
                <div class="metric-value">1.108 h</div>
                <div class="metric-delta">↑ 93% de eficiência</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Custo Evitado</div>
                <div class="metric-value">R$ 185 mil</div>
                <div class="metric-delta">↑ Economia anual</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Projetos Entregues</div>
                <div class="metric-value">24</div>
                <div class="metric-delta">↑ 60% vs. ano anterior</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_dashboard():
    colors = get_colors()
    
    st.markdown(f"""
    <div class="page-header">
        <h1>📊 Dashboard Executivo</h1>
        <p>Simulação de indicadores de negócio com dados aleatórios</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="analytics-container">', unsafe_allow_html=True)

    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    projetos = ["Análise de Churn","Dashboard de Vendas","Otimização de Preços","Segmentação de Clientes","Previsão de Demanda","Análise de Sentimento","Modelo de Propensão","Automação de Relatórios","Análise de ROI","Monitoramento de KPIs"]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status_opts = ["Concluído","Em Andamento","Planejado"]
    data=[]
    for i in range(150):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status_opts, p=[0.55,0.30,0.15]),
            "Valor": round(np.random.lognormal(9,0.8),2),
            "Horas": np.random.randint(20,400),
            "Satisfacao": np.random.randint(60,100),
            "Complexidade": np.random.choice(["Baixa","Média","Alta"], p=[0.2,0.5,0.3])
        })
    df = pd.DataFrame(data)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.strftime("%Y-%m")

    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">🔍 Filtros</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        periodo = st.selectbox("Período", ["Últimos 6 meses","Últimos 12 meses","Últimos 24 meses"], index=1)
    with col2:
        regiao = st.selectbox("Região", ["Todas"] + sorted(df["Região"].unique().tolist()), index=0)
    with col3:
        status_filtro = st.selectbox("Status", ["Todos"] + sorted(df["Status"].unique().tolist()), index=0)

    df_filtrado = df.copy()
    ultima_data = df["Data"].max()
    if periodo == "Últimos 6 meses":
        data_corte = ultima_data - timedelta(days=180)
    elif periodo == "Últimos 12 meses":
        data_corte = ultima_data - timedelta(days=365)
    else:
        data_corte = ultima_data - timedelta(days=730)
    df_filtrado = df_filtrado[df_filtrado["Data"] >= data_corte]
    if regiao != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Região"] == regiao]
    if status_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"] == status_filtro]

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin:1.5rem 0;">
        <div class="metric-card">
            <div class="metric-label">Total de Projetos</div>
            <div class="metric-value">{len(df_filtrado):,}</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Receita Total</div>
            <div class="metric-value">R$ {df_filtrado['Valor'].sum()/1e6:.1f}M</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Ticket Médio</div>
            <div class="metric-value">R$ {df_filtrado['Valor'].mean():,.0f}</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Satisfação Média</div>
            <div class="metric-value">{df_filtrado['Satisfacao'].mean():.1f}%</div>
            <div class="metric-delta">↑ Excelente</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    fig1 = px.bar(df_filtrado.groupby("Mes").size().reset_index(name="Quantidade").sort_values("Mes"), 
                 x="Mes", y="Quantidade", title="Projetos por Mês", 
                 color_discrete_sequence=[colors["chart_colors"][0]], 
                 template=colors["plotly_template"])
    fig1.update_layout(height=380, margin=dict(l=20,r=20,t=40,b=40), 
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=colors["text"], family="Inter"))
    
    fig2 = px.pie(df_filtrado.groupby("Região")["Valor"].sum().reset_index(), 
                 names="Região", values="Valor", title="Receita por Região", hole=0.4, 
                 color_discrete_sequence=colors["chart_colors"], 
                 template=colors["plotly_template"])
    fig2.update_layout(height=380, margin=dict(l=10,r=10,t=40,b=20), 
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=colors["text"], family="Inter"))
    
    fig3 = px.line(df_filtrado.groupby("Mes")["Valor"].sum().reset_index().sort_values("Mes"), 
                  x="Mes", y="Valor", title="Evolução da Receita", markers=True, 
                  color_discrete_sequence=[colors["chart_colors"][1]], 
                  template=colors["plotly_template"])
    fig3.update_layout(height=380, margin=dict(l=20,r=20,t=40,b=40), 
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=colors["text"], family="Inter"))
    fig3.update_traces(line=dict(width=3))
    
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade", 
                     size="Satisfacao", title="Esforço vs. Retorno", 
                     color_discrete_sequence=colors["chart_colors"], 
                     template=colors["plotly_template"])
    fig4.update_layout(height=380, margin=dict(l=20,r=20,t=40,b=40), 
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=colors["text"], family="Inter"))
    
    fig5 = px.bar(df_filtrado["Status"].value_counts().reset_index(), 
                 x="count", y="Status", orientation="h", title="Status dos Projetos", 
                 color="Status", color_discrete_sequence=colors["chart_colors"][2:], 
                 template=colors["plotly_template"])
    fig5.update_layout(height=320, margin=dict(l=20,r=20,t=40,b=20), showlegend=False, 
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=colors["text"], family="Inter"))

    c1, c2 = st.columns(2)
    c1.plotly_chart(fig1, use_container_width=True)
    c2.plotly_chart(fig2, use_container_width=True)
    c1, c2 = st.columns(2)
    c1.plotly_chart(fig3, use_container_width=True)
    c2.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer" id="contato">
        <div class="status">
            <span class="status-dot"></span>
            Disponível para novas oportunidades
        </div>
        <h3>Vamos conversar sobre dados?</h3>
        <p class="footer-subtitle">Aberto a projetos em Dados, BI e Cloud Computing</p>
        <div class="footer-modes">
            <span class="footer-mode">🏠 Remoto</span>
            <span class="footer-mode">🏢 Híbrido</span>
            <span class="footer-mode">📍 Presencial</span>
            <span class="footer-mode">✈️ Viagens</span>
        </div>
        <div class="footer-links">
            <a href="https://www.linkedin.com/in/raphaelpires" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="https://github.com/raphaelcaxias" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="mailto:contato@raphaelpires.com" class="footer-link">✉️ E-mail</a>
            <a href="tel:+5511999999999" class="footer-link">📱 Telefone</a>
        </div>
        <p class="footer-copy">© 2026 Raphael Fernando da Silva Pires · Construído com ❤️ usando Streamlit</p>
    </div>
    <a href="#topo" class="scroll-top" title="Voltar ao topo">↑</a>
    """, unsafe_allow_html=True)


# ============================================================================
# MAIN
# ============================================================================
def main():
    load_css()

    # Navbar com botão de tema integrado
    page = st.query_params.get("page", "home")
    theme_label = "☀️" if st.session_state.theme == "dark" else "🌙"
    
    st.markdown(f"""
    <nav class="navbar">
        <a href="/?page=home" class="navbar-brand">
            <span class="brand-dot"></span>
            Raphael <span>Pires</span>
        </a>
        <div class="navbar-links">
            <a href="/?page=home" class="nav-link {'active' if page == 'home' else ''}">Início</a>
            <a href="/?page=analytics" class="nav-link {'active' if page == 'analytics' else ''}">Análises</a>
            <a href="/?page=dashboard" class="nav-link {'active' if page == 'dashboard' else ''}">Dashboard</a>
            <a href="#contato" class="nav-link">Contato</a>
            <div class="theme-toggle" onclick="window.location.href='?theme_toggle=1&page={page}'" title="Alternar tema">
                {theme_label}
            </div>
        </div>
    </nav>
    """, unsafe_allow_html=True)

    # Handle theme toggle via query params
    if "theme_toggle" in st.query_params:
        toggle_theme()
        # Remove the param to avoid re-toggling
        params = dict(st.query_params)
        params.pop("theme_toggle", None)
        st.query_params.clear()
        st.query_params.update(params)
        st.rerun()

    # Conteúdo
    if page == "home":
        render_home()
    elif page == "analytics":
        render_analytics()
    elif page == "dashboard":
        render_dashboard()
    else:
        render_home()

    render_footer()

if __name__ == "__main__":
    main()
