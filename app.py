import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from datetime import datetime, timedelta

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires · Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# TEMA (DARK / LIGHT) COM RERUN
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
    st.rerun()

def navigate_to(page):
    st.session_state.current_page = page
    st.rerun()

def get_colors():
    if st.session_state.theme == "dark":
        return {
            "primary": "#3B82F6", "primary_hover": "#2563EB",
            "secondary": "#0EA5E9", "accent": "#8B5CF6",
            "success": "#22C55E", "warning": "#F59E0B", "danger": "#EF4444",
            "bg": "#0B0F1A", "bg_alt": "#111827",
            "text": "#F1F5F9", "text_muted": "#94A3B8", "text_dim": "#64748B",
            "card_bg": "rgba(255,255,255,0.04)", "card_bg_hover": "rgba(255,255,255,0.06)",
            "border": "rgba(255,255,255,0.08)", "border_hover": "rgba(59,130,246,0.4)",
            "tag_bg": "rgba(59,130,246,0.15)", "tag_border": "rgba(59,130,246,0.3)",
            "primary_light": "rgba(59,130,246,0.2)",
            "navbar_bg": "rgba(11,15,26,0.85)", "navbar_border": "rgba(255,255,255,0.06)",
            "nav_hover": "rgba(255,255,255,0.06)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.1) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(139,92,246,0.15) 0%, transparent 60%)",
            "section_bg": "rgba(11,15,26,0.5)", "section_alt_bg": "rgba(255,255,255,0.02)",
            "shadow": "0 8px 32px rgba(0,0,0,0.4)",
            "shadow_hover": "0 12px 40px rgba(59,130,246,0.25)",
            "shadow_glow": "0 0 60px rgba(59,130,246,0.15)",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#8B5CF6","#2563EB","#0284C7","#22C55E"]
        }
    else:
        return {
            "primary": "#1D4ED8", "primary_hover": "#1E40AF",
            "secondary": "#0EA5E9", "accent": "#7C3AED",
            "success": "#16A34A", "warning": "#D97706", "danger": "#DC2626",
            "bg": "#F8FAFC", "bg_alt": "#FFFFFF",
            "text": "#0F172A", "text_muted": "#475569", "text_dim": "#64748B",
            "card_bg": "rgba(255,255,255,0.8)", "card_bg_hover": "rgba(255,255,255,0.95)",
            "border": "rgba(0,0,0,0.06)", "border_hover": "rgba(29,78,216,0.3)",
            "tag_bg": "#DBEAFE", "tag_border": "#93C5FD",
            "primary_light": "#DBEAFE",
            "navbar_bg": "rgba(248,250,252,0.9)", "navbar_border": "rgba(0,0,0,0.06)",
            "nav_hover": "rgba(0,0,0,0.04)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.06) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(124,58,237,0.08) 0%, transparent 60%)",
            "section_bg": "rgba(255,255,255,0.6)", "section_alt_bg": "rgba(0,0,0,0.01)",
            "shadow": "0 8px 32px rgba(0,0,0,0.08)",
            "shadow_hover": "0 12px 40px rgba(29,78,216,0.15)",
            "shadow_glow": "0 0 60px rgba(29,78,216,0.08)",
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8","#0EA5E9","#7C3AED","#2563EB","#0284C7","#16A34A"]
        }

# ============================================================================
# CSS PREMIUM COM VARIÁVEIS NO :ROOT
# ============================================================================
def load_css():
    c = get_colors()
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800;14..32,900&display=swap');

        :root {{
            --primary: {c['primary']};
            --primary-hover: {c['primary_hover']};
            --secondary: {c['secondary']};
            --accent: {c['accent']};
            --success: {c['success']};
            --warning: {c['warning']};
            --danger: {c['danger']};
            --bg: {c['bg']};
            --bg-alt: {c['bg_alt']};
            --text: {c['text']};
            --text-muted: {c['text_muted']};
            --text-dim: {c['text_dim']};
            --card-bg: {c['card_bg']};
            --border: {c['border']};
            --tag-bg: {c['tag_bg']};
            --tag-border: {c['tag_border']};
            --shadow: {c['shadow']};
            --shadow-hover: {c['shadow_hover']};
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: {c['bg']};
            color: {c['text']};
        }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: {c['bg']}; }}
        .block-container {{ padding: 0; max-width: 100%; }}

        /* ===== Animações ===== */
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        @keyframes slideInLeft {{
            from {{ opacity: 0; transform: translateX(-30px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.6; transform: scale(1.1); }}
        }}
        @keyframes gradientShift {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}
        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
        }}

        /* ===== Navbar ===== */
        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 999;
            background: {c['navbar_bg']};
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border-bottom: 1px solid {c['navbar_border']};
            padding: 0.85rem 2.5rem;
            display: flex; align-items: center; justify-content: space-between;
            animation: fadeIn 0.6s ease;
        }}
        .navbar-brand {{
            font-weight: 800; font-size: 1.3rem; letter-spacing: -0.02em;
            color: {c['text']}; text-decoration: none;
            display: flex; align-items: center; gap: 0.5rem;
        }}
        .navbar-brand .logo-dot {{
            width: 10px; height: 10px; border-radius: 50%;
            background: linear-gradient(135deg, {c['primary']}, {c['accent']});
            box-shadow: 0 0 12px {c['primary']};
        }}
        .navbar-brand span {{ color: {c['primary']}; }}
        .navbar-links {{
            display: flex; gap: 0.5rem; align-items: center;
        }}
        .nav-link {{
            padding: 0.5rem 1.2rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.25s ease;
            color: {c['text_muted']}; background: transparent; cursor: pointer;
            border: 1px solid transparent;
        }}
        .nav-link:hover {{
            background: {c['nav_hover']}; color: {c['text']};
            transform: translateY(-1px);
        }}
        .nav-link.active {{
            background: {c['primary']}; color: white;
            box-shadow: 0 4px 16px rgba(59,130,246,0.35);
            border-color: {c['primary']};
        }}
        .nav-theme-btn {{
            background: {c['card_bg']}; border: 1px solid {c['border']};
            border-radius: 999px; padding: 0.4rem 0.9rem; font-size: 1.1rem;
            cursor: pointer; transition: all 0.25s ease; color: {c['text']};
            margin-left: 0.5rem;
        }}
        .nav-theme-btn:hover {{
            background: {c['nav_hover']}; transform: rotate(15deg) scale(1.05);
            border-color: {c['primary']};
        }}

        /* ===== Hero ===== */
        .hero-full {{
            min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            padding: 7rem 2.5rem 4rem;
            background: {c['hero_bg']};
            position: relative; overflow: hidden;
        }}
        .hero-full::before {{
            content: ''; position: absolute; inset: 0;
            background: {c['hero_glow']};
            opacity: 0.5; pointer-events: none;
        }}
        .hero-full::after {{
            content: ''; position: absolute; top: 20%; right: 10%;
            width: 400px; height: 400px; border-radius: 50%;
            background: radial-gradient(circle, {c['primary_light']} 0%, transparent 70%);
            filter: blur(60px); opacity: 0.3; pointer-events: none;
            animation: float 6s ease-in-out infinite;
        }}
        .hero-content {{
            max-width: 1200px; width: 100%;
            display: grid; grid-template-columns: 1fr 1fr;
            gap: 4rem; align-items: center;
            position: relative; z-index: 1;
            animation: fadeInUp 0.8s ease;
        }}
        @media (max-width: 900px) {{
            .hero-content {{ grid-template-columns: 1fr; text-align: center; gap: 2rem; }}
            .hero-full {{ padding: 6rem 1.5rem 3rem; }}
        }}
        .hero-text {{ order: 2; }}
        .hero-photo {{ order: 1; display: flex; justify-content: center; align-items: center; }}
        @media (min-width: 901px) {{
            .hero-text {{ order: 1; }}
            .hero-photo {{ order: 2; }}
        }}
        .photo-wrapper {{
            position: relative; width: 300px; height: 300px;
        }}
        .photo-wrapper::before {{
            content: ''; position: absolute; inset: -8px;
            border-radius: 50%;
            background: conic-gradient(from 0deg, {c['primary']}, {c['accent']}, {c['secondary']}, {c['primary']});
            animation: spin 8s linear infinite;
            opacity: 0.6;
        }}
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
        .photo-wrapper img {{
            position: relative; width: 100%; height: 100%;
            border-radius: 50%; object-fit: cover;
            border: 4px solid {c['bg']};
            box-shadow: {c['shadow_glow']};
            z-index: 1;
        }}
        @media (max-width: 900px) {{
            .photo-wrapper {{ width: 200px; height: 200px; }}
        }}
        .hero-tag {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 600; color: {c['primary']};
            margin-bottom: 1.5rem;
        }}
        .hero-tag .dot {{
            width: 8px; height: 8px; border-radius: 50%;
            background: {c['success']}; box-shadow: 0 0 8px {c['success']};
            animation: pulse 2s infinite;
        }}
        .hero-text h1 {{
            font-size: clamp(2.2rem, 5vw, 3.5rem);
            font-weight: 900; letter-spacing: -0.03em;
            line-height: 1.05; color: {c['text']};
            margin-bottom: 1rem;
        }}
        .hero-text h1 .highlight {{
            background: linear-gradient(135deg, {c['primary']}, {c['accent']});
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 4s ease infinite;
        }}
        .hero-text .role {{
            font-size: 1.15rem; font-weight: 600;
            color: {c['primary']}; margin-bottom: 1rem;
            letter-spacing: 0.02em;
        }}
        .hero-text .subtitle {{
            font-size: 1.05rem; color: {c['text_muted']};
            line-height: 1.7; margin-bottom: 1.5rem;
            max-width: 540px;
        }}
        @media (max-width: 900px) {{
            .hero-text .subtitle {{ margin-left: auto; margin-right: auto; }}
        }}
        .badge-group {{
            display: flex; flex-wrap: wrap; gap: 0.5rem;
            margin-bottom: 2rem;
        }}
        @media (max-width: 900px) {{
            .badge-group {{ justify-content: center; }}
        }}
        .badge {{
            background: {c['card_bg']}; border: 1px solid {c['border']};
            padding: 0.4rem 0.9rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 500; color: {c['text']};
            transition: all 0.25s ease; backdrop-filter: blur(8px);
        }}
        .badge:hover {{
            background: {c['primary']}; color: white;
            border-color: {c['primary']};
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(59,130,246,0.3);
        }}
        .cta-group {{
            display: flex; gap: 0.75rem; flex-wrap: wrap;
        }}
        @media (max-width: 900px) {{
            .cta-group {{ justify-content: center; }}
        }}
        .btn-primary {{
            background: linear-gradient(135deg, {c['primary']}, {c['primary_hover']});
            color: white; padding: 0.75rem 1.8rem; border-radius: 999px;
            font-weight: 600; text-decoration: none; transition: all 0.25s ease;
            display: inline-flex; align-items: center; gap: 0.5rem;
            border: none; cursor: pointer; font-size: 0.95rem;
            box-shadow: 0 4px 16px rgba(59,130,246,0.3);
        }}
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(59,130,246,0.45);
        }}
        .btn-secondary {{
            background: {c['card_bg']}; border: 1px solid {c['border']};
            padding: 0.75rem 1.8rem; border-radius: 999px;
            font-weight: 600; color: {c['text']}; text-decoration: none;
            transition: all 0.25s ease; display: inline-flex;
            align-items: center; gap: 0.5rem; font-size: 0.95rem;
            backdrop-filter: blur(8px);
        }}
        .btn-secondary:hover {{
            background: {c['nav_hover']}; border-color: {c['primary']};
            transform: translateY(-2px);
        }}

        /* ===== Seções ===== */
        .section-glass {{
            padding: 5rem 2.5rem;
            background: {c['section_bg']};
            backdrop-filter: blur(8px);
            border-top: 1px solid {c['border']};
            position: relative;
        }}
        .section-glass.alt {{ background: {c['section_alt_bg']}; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{
            text-align: center; margin-bottom: 3.5rem;
            animation: fadeInUp 0.6s ease;
        }}
        .section-header .label {{
            display: inline-block;
            background: {c['primary_light']};
            padding: 0.35rem 1.2rem; border-radius: 999px;
            font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.12em; color: {c['primary']};
            border: 1px solid {c['tag_border']};
        }}
        .section-header h2 {{
            font-size: clamp(1.8rem, 4vw, 2.6rem);
            font-weight: 800; margin-top: 0.8rem;
            color: {c['text']}; letter-spacing: -0.02em;
        }}
        .section-header p {{
            color: {c['text_muted']}; max-width: 620px;
            margin: 0.8rem auto 0; font-size: 1.05rem; line-height: 1.6;
        }}

        /* ===== Glass cards ===== */
        .glass-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid {c['border']};
            border-radius: 20px;
            padding: 1.8rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: {c['shadow']};
            position: relative; overflow: hidden;
        }}
        .glass-card::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, {c['primary']}, transparent);
            opacity: 0; transition: opacity 0.3s ease;
        }}
        .glass-card:hover {{
            transform: translateY(-6px);
            border-color: {c['border_hover']};
            box-shadow: {c['shadow_hover']};
            background: {c['card_bg_hover']};
        }}
        .glass-card:hover::before {{ opacity: 1; }}

        /* ===== KPI Grid ===== */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1.2rem;
        }}
        .kpi-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(12px);
            border: 1px solid {c['border']};
            border-radius: 20px;
            padding: 1.8rem 1.2rem;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: {c['shadow']};
            animation: fadeInUp 0.6s ease backwards;
        }}
        .kpi-card:hover {{
            transform: translateY(-6px);
            border-color: {c['primary']};
            box-shadow: {c['shadow_hover']};
        }}
        .kpi-value {{
            font-size: 2.4rem; font-weight: 900;
            background: linear-gradient(135deg, {c['primary']}, {c['secondary']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1; margin-bottom: 0.4rem;
            letter-spacing: -0.02em;
        }}
        .kpi-label {{
            color: {c['text_muted']}; font-size: 0.85rem;
            font-weight: 500; line-height: 1.4;
        }}

        /* ===== Timeline ===== */
        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, {c['primary']}, {c['accent']}, {c['secondary']}, transparent);
        }}
        .timeline-item {{
            position: relative; padding-left: 80px; margin-bottom: 2rem;
            animation: slideInLeft 0.6s ease backwards;
        }}
        .timeline-dot {{
            position: absolute; left: 19px; top: 24px;
            width: 20px; height: 20px; border-radius: 50%;
            background: linear-gradient(135deg, {c['primary']}, {c['accent']});
            border: 4px solid {c['bg']};
            box-shadow: 0 0 0 3px {c['primary']}, 0 0 20px rgba(59,130,246,0.4);
            transition: all 0.3s ease;
        }}
        .timeline-item:hover .timeline-dot {{
            transform: scale(1.2);
            box-shadow: 0 0 0 3px {c['primary']}, 0 0 30px rgba(59,130,246,0.6);
        }}
        .timeline-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(8px);
            border: 1px solid {c['border']};
            border-radius: 20px; padding: 1.8rem;
            transition: all 0.3s ease;
        }}
        .timeline-card:hover {{
            border-color: {c['primary']};
            transform: translateX(8px);
            box-shadow: {c['shadow_hover']};
        }}
        .timeline-date {{
            display: inline-block; font-size: 0.72rem; font-weight: 700;
            background: {c['primary_light']}; color: {c['primary']};
            padding: 0.3rem 0.9rem; border-radius: 999px;
            border: 1px solid {c['tag_border']};
        }}
        .timeline-badge {{
            background: linear-gradient(135deg, {c['primary']}, {c['accent']});
            color: white; font-size: 0.65rem; font-weight: 800;
            padding: 0.25rem 0.7rem; border-radius: 999px;
            margin-left: 0.5rem; display: inline-block;
            text-transform: uppercase; letter-spacing: 0.05em;
            box-shadow: 0 2px 8px rgba(59,130,246,0.3);
        }}
        .timeline-role {{
            font-size: 1.25rem; font-weight: 800;
            margin: 0.6rem 0 0.2rem; color: {c['text']};
            letter-spacing: -0.01em;
        }}
        .timeline-company {{
            color: {c['secondary']}; font-weight: 700;
            font-size: 0.95rem; margin-bottom: 0.8rem;
        }}
        .timeline-desc {{
            color: {c['text_muted']}; line-height: 1.7;
            font-size: 0.95rem; margin-bottom: 1rem;
        }}
        .timeline-tag {{
            font-size: 0.72rem; background: {c['tag_bg']};
            border: 1px solid {c['tag_border']};
            padding: 0.3rem 0.7rem; border-radius: 8px;
            display: inline-block; margin: 0.2rem;
            color: {c['text']}; font-weight: 500;
            transition: all 0.2s ease;
        }}
        .timeline-tag:hover {{
            background: {c['primary']}; color: white;
            transform: translateY(-2px);
        }}

        /* ===== Grids ===== */
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }}
        .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
        .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }}
        @media (max-width: 900px) {{
            .grid-2, .grid-3, .grid-4 {{ grid-template-columns: 1fr; }}
        }}
        @media (min-width: 600px) and (max-width: 900px) {{
            .grid-3 {{ grid-template-columns: 1fr 1fr; }}
            .grid-4 {{ grid-template-columns: 1fr 1fr; }}
        }}

        /* ===== Project Card ===== */
        .project-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(12px);
            border: 1px solid {c['border']};
            border-radius: 20px; padding: 2rem;
            transition: all 0.3s ease;
            display: flex; flex-direction: column;
            position: relative; overflow: hidden;
        }}
        .project-card::before {{
            content: ''; position: absolute; top: 0; left: 0;
            width: 100%; height: 3px;
            background: linear-gradient(90deg, {c['primary']}, {c['accent']});
            transform: scaleX(0); transform-origin: left;
            transition: transform 0.3s ease;
        }}
        .project-card:hover {{
            transform: translateY(-6px);
            border-color: {c['primary']};
            box-shadow: {c['shadow_hover']};
        }}
        .project-card:hover::before {{ transform: scaleX(1); }}
        .project-icon {{
            font-size: 2.5rem; margin-bottom: 1rem;
            display: inline-block;
        }}
        .project-card h3 {{
            font-size: 1.2rem; font-weight: 700;
            color: {c['text']}; margin-bottom: 0.6rem;
        }}
        .project-card p {{
            color: {c['text_muted']}; line-height: 1.6;
            font-size: 0.92rem; margin-bottom: 0.8rem;
            flex-grow: 1;
        }}
        .project-tech {{
            font-size: 0.78rem; color: {c['text_dim']};
            margin-bottom: 1rem;
        }}
        .project-tech strong {{ color: {c['text_muted']}; }}

        /* ===== Testimonial ===== */
        .testimonial-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(12px);
            border: 1px solid {c['border']};
            border-radius: 20px; padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
        }}
        .testimonial-card::before {{
            content: '"'; position: absolute;
            top: -10px; left: 20px;
            font-size: 6rem; color: {c['primary']};
            opacity: 0.15; font-family: Georgia, serif;
            line-height: 1;
        }}
        .testimonial-card:hover {{
            transform: translateY(-4px);
            border-color: {c['primary']};
            box-shadow: {c['shadow_hover']};
        }}
        .testimonial-text {{
            font-style: italic; color: {c['text']};
            line-height: 1.7; font-size: 0.95rem;
            position: relative; z-index: 1;
        }}
        .testimonial-author {{
            font-weight: 700; color: {c['primary']};
            margin-top: 1rem; font-size: 0.88rem;
        }}

        /* ===== Cloud Journey ===== */
        .cloud-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 1rem; text-align: center;
        }}
        .cloud-item {{
            background: {c['card_bg']};
            border: 1px solid {c['border']};
            border-radius: 16px; padding: 1.2rem;
            transition: all 0.3s ease;
        }}
        .cloud-item:hover {{
            transform: translateY(-4px);
            border-color: {c['primary']};
            box-shadow: {c['shadow_hover']};
        }}
        .cloud-icon {{ font-size: 2rem; margin-bottom: 0.5rem; }}
        .cloud-label {{
            font-size: 0.85rem; font-weight: 600;
            color: {c['text']};
        }}

        /* ===== Footer ===== */
        .footer {{
            padding: 4rem 2.5rem 2rem; text-align: center;
            border-top: 1px solid {c['border']};
            background: {c['card_bg']};
            backdrop-filter: blur(12px);
        }}
        .footer .status {{
            display: inline-flex; align-items: center; gap: 0.6rem;
            background: rgba(34,197,94,0.12);
            border: 1px solid rgba(34,197,94,0.3);
            padding: 0.4rem 1.2rem; border-radius: 999px;
            font-size: 0.85rem; font-weight: 600; color: {c['success']};
        }}
        .footer .status-dot {{
            width: 9px; height: 9px; border-radius: 50%;
            background: {c['success']};
            box-shadow: 0 0 12px {c['success']};
            animation: pulse 2s infinite;
        }}
        .footer h3 {{
            font-size: 1.8rem; font-weight: 800;
            margin: 1.5rem 0 0.5rem; color: {c['text']};
            letter-spacing: -0.02em;
        }}
        .footer .subtitle {{
            color: {c['text_muted']}; margin-bottom: 2rem;
            font-size: 1.05rem;
        }}
        .footer-modes {{
            display: flex; justify-content: center;
            flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.5rem;
        }}
        .footer-mode {{
            background: {c['tag_bg']};
            border: 1px solid {c['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px;
            font-size: 0.85rem; font-weight: 500;
            color: {c['text']};
        }}
        .footer-links {{
            display: flex; justify-content: center;
            flex-wrap: wrap; gap: 0.6rem; margin: 1.5rem 0;
        }}
        .footer-link {{
            background: {c['card_bg']};
            border: 1px solid {c['border']};
            padding: 0.6rem 1.3rem; border-radius: 999px;
            color: {c['text']}; text-decoration: none;
            font-size: 0.9rem; font-weight: 500;
            transition: all 0.25s ease;
            backdrop-filter: blur(8px);
        }}
        .footer-link:hover {{
            background: {c['primary']}; color: white;
            border-color: {c['primary']};
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(59,130,246,0.3);
        }}
        .footer-copy {{
            color: {c['text-dim']}; font-size: 0.82rem;
            margin-top: 2rem; padding-top: 1.5rem;
            border-top: 1px solid {c['border']};
        }}

        /* ===== Responsive ===== */
        @media (max-width: 768px) {{
            .navbar {{ padding: 0.6rem 1rem; }}
            .navbar-brand {{ font-size: 1.1rem; }}
            .nav-link {{ padding: 0.4rem 0.8rem; font-size: 0.8rem; }}
            .section-glass {{ padding: 3rem 1.2rem; }}
            .container {{ padding: 0 0.5rem; }}
        }}

        /* ===== Streamlit overrides ===== */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 0.5rem; background: transparent;
            border-bottom: 1px solid {c['border']};
            padding-bottom: 0.5rem;
        }}
        .stTabs [data-baseweb="tab"] {{
            background: {c['card_bg']};
            border: 1px solid {c['border']};
            border-radius: 12px; padding: 0.7rem 1.4rem;
            color: {c['text']}; font-weight: 600;
            transition: all 0.25s ease;
        }}
        .stTabs [data-baseweb="tab"]:hover {{
            background: {c['nav_hover']};
            border-color: {c['primary']};
        }}
        .stTabs [aria-selected="true"] {{
            background: {c['primary']} !important;
            color: white !important;
            border-color: {c['primary']} !important;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
        }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# NAVBAR
# ============================================================================
def render_navbar():
    c = get_colors()
    page = st.session_state.current_page
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    
    # Criar 3 colunas: logo | navegação | tema
    nav_col1, nav_col2, nav_col3 = st.columns([2, 6, 1])
    
    with nav_col1:
        st.markdown(f"""
        <div style="padding-top: 0.5rem;">
            <span class="navbar-brand">
                <span class="logo-dot"></span>
                Raphael <span>Pires</span>
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with nav_col2:
        btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
        with btn_col1:
            if st.button("🏠 Início", key="nav_home", use_container_width=True):
                navigate_to("home")
        with btn_col2:
            if st.button("📈 Análises", key="nav_analytics", use_container_width=True):
                navigate_to("analytics")
        with btn_col3:
            if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True):
                navigate_to("dashboard")
        with btn_col4:
            if st.button(theme_icon, key="nav_theme", use_container_width=True):
                toggle_theme()
    
    with nav_col3:
        st.markdown("")  # Spacer
    
    # CSS inline para estilizar os botões como nav-links
    st.markdown(f"""
    <style>
        button[kind="primary"] {{
            background: transparent !important;
            border: none !important;
            color: {c['text_muted']} !important;
            font-weight: 500 !important;
            padding: 0.5rem 1rem !important;
            border-radius: 999px !important;
            transition: all 0.25s ease !important;
        }}
        button[kind="primary"]:hover {{
            background: {c['nav_hover']} !important;
            color: {c['text']} !important;
        }}
        #nav_home {{ {'background: ' + c['primary'] + ' !important; color: white !important; box-shadow: 0 4px 12px rgba(59,130,246,0.3) !important;' if page == 'home' else ''} }}
        #nav_analytics {{ {'background: ' + c['primary'] + ' !important; color: white !important; box-shadow: 0 4px 12px rgba(59,130,246,0.3) !important;' if page == 'analytics' else ''} }}
        #nav_dashboard {{ {'background: ' + c['primary'] + ' !important; color: white !important; box-shadow: 0 4px 12px rgba(59,130,246,0.3) !important;' if page == 'dashboard' else ''} }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
def render_footer():
    c = get_colors()
    st.markdown(f"""
    <div class="footer">
        <div class="status">
            <span class="status-dot"></span>
            Disponível para oportunidades
        </div>
        <h3>Vamos conversar sobre dados?</h3>
        <p class="subtitle">Aberto a projetos em Dados, BI e Cloud</p>
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
        <p class="footer-copy">© 2026 Raphael Fernando da Silva Pires · Todos os direitos reservados</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SKILLS CHART
# ============================================================================
def render_skills_chart():
    c = get_colors()
    df = pd.DataFrame({
        "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
        "Proficiência": [95, 92, 88, 95, 85, 60, 82],
        "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
    })
    fig = px.bar(
        df, x="Proficiência", y="Tecnologia", color="Categoria",
        orientation="h", color_discrete_sequence=c["chart_colors"],
        template=c["plotly_template"], text="Proficiência"
    )
    fig.update_layout(
        height=400, margin=dict(l=20, r=40, t=20, b=40),
        xaxis=dict(range=[0, 110], showgrid=True, gridcolor="rgba(148,163,184,0.15)"),
        yaxis=dict(showgrid=False),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter", color=c["text"]),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color=c["text"], size=12, family="Inter")
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# HOME PAGE
# ============================================================================
def page_home():
    c = get_colors()
    
    # Determinar URL da foto
    foto_url = "https://ui-avatars.com/api/?name=Raphael+Pires&size=300&background=3B82F6&color=fff&bold=true"
    for path in ["rapha.jpeg", "rapha.jpg", "assets/rapha.jpeg", "assets/rapha.jpg"]:
        if os.path.exists(path):
            foto_url = path
            break
    
    # ===== HERO =====
    st.markdown(f"""
    <section class="hero-full">
        <div class="hero-content">
            <div class="hero-text">
                <div class="hero-tag">
                    <span class="dot"></span>
                    Disponível para novos projetos
                </div>
                <h1>Raphael <span class="highlight">Pires</span></h1>
                <div class="role">Analista de Dados & Business Intelligence</div>
                <p class="subtitle">
                    Mais de <strong>16 anos</strong> transformando dados brutos em decisões estratégicas.
                    Especialista em automação, governança de dados e dashboards de alto impacto.
                </p>
                <div class="badge-group">
                    <span class="badge">📊 Power BI</span>
                    <span class="badge">🐍 Python</span>
                    <span class="badge">🗄️ SQL</span>
                    <span class="badge">☁️ AWS</span>
                    <span class="badge">🤖 IA Generativa</span>
                    <span class="badge">📈 Dashboards</span>
                </div>
                <div class="cta-group">
                    <a href="#experiencia" class="btn-primary">Ver trajetória ↓</a>
                    <a href="#contato" class="btn-secondary">📄 Baixar CV</a>
                </div>
            </div>
            <div class="hero-photo">
                <div class="photo-wrapper">
                    <img src="{foto_url}" alt="Raphael Pires">
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    # ===== KPIs =====
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Impacto Mensurável</span>
                <h2>Números que contam histórias</h2>
            </div>
            <div class="kpi-grid">
                <div class="kpi-card" style="animation-delay: 0s"><div class="kpi-value">16+</div><div class="kpi-label">anos de experiência</div></div>
                <div class="kpi-card" style="animation-delay: 0.1s"><div class="kpi-value">70%</div><div class="kpi-label">redução operacional</div></div>
                <div class="kpi-card" style="animation-delay: 0.2s"><div class="kpi-value">213k+</div><div class="kpi-label">registros analisados</div></div>
                <div class="kpi-card" style="animation-delay: 0.3s"><div class="kpi-value">2h→15m</div><div class="kpi-label">ciclo de análise</div></div>
                <div class="kpi-card" style="animation-delay: 0.4s"><div class="kpi-value">R$1,2bi</div><div class="kpi-label">investimentos analisados</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== EXPERIÊNCIA =====
    st.markdown("""
    <div class="section-glass alt" id="experiencia">
        <div class="container">
            <div class="section-header">
                <span class="label">Trajetória</span>
                <h2>Experiência profissional</h2>
                <p>Uma jornada de mais de 16 anos transformando dados em valor</p>
            </div>
            <div class="timeline">
    """, unsafe_allow_html=True)

    experiences = [
        {
            "date": "2014 – Presente · 10+ anos",
            "role": "Analista de Dados & Operações",
            "company": "NSM Comércio",
            "desc": "Centralização de registros de estoque de 7 unidades, eliminando inconsistências de inventário. Construção de indicadores operacionais e governança de dados.",
            "tags": ["Dados", "Operações", "Indicadores", "Governança"],
            "badge": "Atual"
        },
        {
            "date": "2012 – Presente · 12+ anos",
            "role": "Fundador & Analista de Dados",
            "company": "Jardim do Éden",
            "desc": "Estruturação de base de dados, modelagem, integração e dashboards gerenciais com SQL, Python, Power BI e Looker Studio – reduzindo ciclo de análise de 2h para 15 min.",
            "tags": ["Power BI", "Python", "SQL", "Looker Studio"],
            "badge": ""
        },
        {
            "date": "2010 – 2014 · 4 anos",
            "role": "Fundador & Analista de KPIs",
            "company": "J Sintonía",
            "desc": "Monitoramento de KPIs de vendas, margem e rentabilidade com relatórios automatizados. Análise de viabilidade econômica que fundamentou encerramento estratégico planejado.",
            "tags": ["BI", "KPIs", "Dashboards"],
            "badge": ""
        },
        {
            "date": "2009 – 2010 · 1 ano",
            "role": "Estagiário de Automação e Dados",
            "company": "Banco do Brasil",
            "desc": "Desenvolvimento de macros VBA em 20 agências, reduzindo 70% do tempo operacional. Saneamento e padronização de bases de dados gerenciais.",
            "tags": ["VBA", "Automação", "Eficiência"],
            "badge": ""
        }
    ]
    
    for i, exp in enumerate(experiences):
        tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        badge = f'<span class="timeline-badge">{exp["badge"]}</span>' if exp["badge"] else ""
        # Escapar & para HTML
        role = exp["role"].replace("&", "&amp;")
        st.markdown(f"""
        <div class="timeline-item" style="animation-delay: {i*0.15}s">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span> {badge}
                <div class="timeline-role">{role}</div>
                <div class="timeline-company">{exp["company"]}</div>
                <div class="timeline-desc">{exp["desc"]}</div>
                <div>{tags}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div></div>", unsafe_allow_html=True)

    # ===== PROJETOS =====
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Portfólio</span>
                <h2>Projetos de Analytics</h2>
                <p>Soluções reais que geraram impacto mensurável</p>
            </div>
            <div class="grid-2">
                <div class="project-card">
                    <div class="project-icon">🇧🇷</div>
                    <h3>Desenrola Brasil</h3>
                    <p>Painel analítico executivo com KPIs, séries temporais e análise de concentração de mercado (HHI). Segmentação de perfis de renegociação via clusterização.</p>
                    <div class="project-tech"><strong>Tecnologias:</strong> Python, Pandas, Plotly, Streamlit</div>
                    <a href="https://desenrolabrasil.streamlit.app" target="_blank" class="btn-primary" style="align-self:flex-start;padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Acessar</a>
                </div>
                <div class="project-card">
                    <div class="project-icon">🔬</div>
                    <h3>CNPq Analytics</h3>
                    <p>ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos. Dashboard interativo com filtros dinâmicos e visualizações de distribuição regional.</p>
                    <div class="project-tech"><strong>Tecnologias:</strong> Python, Pandas, Plotly, Streamlit, PostgreSQL</div>
                    <a href="https://cnpq-analytics.streamlit.app" target="_blank" class="btn-primary" style="align-self:flex-start;padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Acessar</a>
                </div>
                <div class="project-card">
                    <div class="project-icon">⛽</div>
                    <h3>Análise de Preços de Combustíveis (ANP)</h3>
                    <p>Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da Agência Nacional do Petróleo, com séries históricas e comparativos.</p>
                    <div class="project-tech"><strong>Tecnologias:</strong> Python, Pandas, Plotly, Streamlit</div>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="align-self:flex-start;padding:0.5rem 1.2rem;font-size:0.85rem;">📊 Ver código</a>
                </div>
                <div class="project-card">
                    <div class="project-icon">💎</div>
                    <h3>Automação de Relatórios com Python</h3>
                    <p>Automação de geração de relatórios financeiros e operacionais, reduzindo tempo de entrega de 2h para 15min e eliminando erros manuais.</p>
                    <div class="project-tech"><strong>Tecnologias:</strong> Python, Pandas, Excel, Power BI</div>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="align-self:flex-start;padding:0.5rem 1.2rem;font-size:0.85rem;">💻 Ver código</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== DEPOIMENTOS =====
    st.markdown("""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">Depoimentos</span>
                <h2>O que dizem sobre meu trabalho</h2>
            </div>
            <div class="grid-3">
                <div class="testimonial-card">
                    <p class="testimonial-text">O Raphael revolucionou nossa área de dados. Reduzimos custos operacionais em 30% com suas automações.</p>
                    <p class="testimonial-author">— Diretor de Operações, Empresa X</p>
                </div>
                <div class="testimonial-card">
                    <p class="testimonial-text">Graças ao dashboard de KPIs criado pelo Raphael, passamos a tomar decisões em tempo real com segurança.</p>
                    <p class="testimonial-author">— Gerente de BI, Empresa Y</p>
                </div>
                <div class="testimonial-card">
                    <p class="testimonial-text">A expertise do Raphael em AWS e Python nos permitiu processar 1M de registros por dia com custo mínimo.</p>
                    <p class="testimonial-author">— CTO, Startup Z</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== AWS CLOUD JOURNEY =====
    st.markdown(f"""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Cloud Journey</span>
                <h2>☁️ AWS em progresso</h2>
                <p>Atualmente em trilha de certificação, com 8 módulos AWS Educate concluídos e foco em arquitetura de dados.</p>
            </div>
            <div class="cloud-grid">
                <div class="cloud-item"><div class="cloud-icon">📘</div><div class="cloud-label">Cloud 101</div></div>
                <div class="cloud-item"><div class="cloud-icon">🖥️</div><div class="cloud-label">AWS Console</div></div>
                <div class="cloud-item"><div class="cloud-icon">💾</div><div class="cloud-label">Storage</div></div>
                <div class="cloud-item"><div class="cloud-icon">🤖</div><div class="cloud-label">ML Foundations</div></div>
                <div class="cloud-item"><div class="cloud-icon">🌱</div><div class="cloud-label">Sustainability</div></div>
            </div>
            <div style="text-align:center;margin-top:2rem;">
                <span style="background:{c['primary_light']};color:{c['primary']};padding:0.4rem 1.4rem;border-radius:999px;font-size:0.85rem;font-weight:700;border:1px solid {c['tag_border']};">🎯 Meta 2026: AWS Cloud Practitioner</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== COMPETÊNCIAS =====
    st.markdown("""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">Competências</span>
                <h2>Domínio tecnológico</h2>
            </div>
    """, unsafe_allow_html=True)
    render_skills_chart()
    st.markdown("</div></div>", unsafe_allow_html=True)

    # ===== FOOTER =====
    st.markdown('<div id="contato"></div>', unsafe_allow_html=True)
    render_footer()

# ============================================================================
# ANALYTICS PAGE
# ============================================================================
def page_analytics():
    st.markdown("""
    <div class="section-glass" style="min-height:80vh;padding-top:7rem;">
        <div class="container">
            <div class="section-header">
                <span class="label">Análise ao Vivo</span>
                <h2>Demonstração analítica</h2>
                <p>Explore dados reais com filtros interativos</p>
            </div>
    """, unsafe_allow_html=True)
    
    c = get_colors()  # ✅ Referência às cores ANTES dos loops
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📈 Impacto Operacional"])

    # ===== TAB 1: DESENROLA =====
    with tabs[0]:
        np.random.seed(42)
        regioes = ["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
        faixas = ["Até R$5k","R$5k-15k","R$15k-50k","Acima R$50k"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[0.45,0.28,0.15,0.07,0.05]),
            "Faixa": np.random.choice(faixas, 400, p=[0.55,0.28,0.12,0.05]),
            "Valor": np.random.lognormal(8.5,1.2,400),
            "Status": np.random.choice(["Renegociado","Em Negociação","Inadimplente"], 400, p=[0.65,0.25,0.10])
        })
        col1, col2 = st.columns(2)
        with col1:
            reg_sel = st.multiselect("Região", df["Região"].unique(), default=df["Região"].unique())
        with col2:
            status_sel = st.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
        filtro = df[(df["Região"].isin(reg_sel)) & (df["Status"].isin(status_sel))]
        if not filtro.empty:
            k1,k2,k3 = st.columns(3)
            k1.metric("Contratos", f"{len(filtro):,}")
            k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f}M")
            k3.metric("Taxa Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=0.5,
                         color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
            fig1.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
            fig2 = px.bar(filtro.groupby("Faixa", observed=False)["Valor"].sum().reset_index(),
                         x="Faixa", y="Valor", color_discrete_sequence=[c["chart_colors"][0]],
                         template=c["plotly_template"])
            fig2.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
            c1, c2 = st.columns(2)
            c1.plotly_chart(fig1, use_container_width=True)
            c2.plotly_chart(fig2, use_container_width=True)
        else:
            st.warning("Nenhum dado encontrado para os filtros selecionados.")

    # ===== TAB 2: ANP =====
    # ✅ CORREÇÃO CRÍTICA: Renomear variáveis do loop para não sobrescrever 'c'
    with tabs[1]:
        np.random.seed(123)
        estados = ["SP","RJ","MG","RS","PR","BA"]
        combustiveis = ["Gasolina","Etanol","Diesel"]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
        data_anp = []
        for estado_nome in estados:
            for comb_nome in combustiveis:
                base = {"Gasolina":5.8,"Etanol":3.5,"Diesel":5.2}[comb_nome]
                for mes_nome in meses:
                    data_anp.append({
                        "Estado": estado_nome,
                        "Combustível": comb_nome,
                        "Mês": mes_nome,
                        "Preço": base + np.random.normal(0, 0.15)
                    })
        df_anp = pd.DataFrame(data_anp)
        col1, col2 = st.columns(2)
        with col1:
            estado = st.selectbox("Estado", df_anp["Estado"].unique())
        with col2:
            combustivel = st.selectbox("Combustível", df_anp["Combustível"].unique())
        filtro_anp = df_anp[(df_anp["Estado"]==estado) & (df_anp["Combustível"]==combustivel)]
        if not filtro_anp.empty:
            k1, k2 = st.columns(2)
            k1.metric("Preço Atual", f"R$ {filtro_anp[filtro_anp['Mês']=='Jun']['Preço'].values[0]:.2f}")
            variacao = (filtro_anp["Preço"].max() - filtro_anp["Preço"].min()) / filtro_anp["Preço"].min() * 100
            k2.metric("Variação Semestral", f"{variacao:.1f}%")
            fig_anp = px.line(filtro_anp, x="Mês", y="Preço", markers=True,
                             color_discrete_sequence=[c["chart_colors"][0]],
                             template=c["plotly_template"])
            fig_anp.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_anp, use_container_width=True)
        else:
            st.warning("Nenhum dado encontrado.")

    # ===== TAB 3: IMPACTO =====
    with tabs[2]:
        meses_impacto = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        df_impacto = pd.DataFrame({
            "Mês": meses_impacto * 2,
            "Tipo": ["Antes"] * 12 + ["Após"] * 12,
            "Horas": [120,125,118,130,122,128,126,124,129,127,125,130] +
                    [95,70,55,45,38,35,33,32,30,29,28,27]
        })
        fig_impacto = px.line(df_impacto, x="Mês", y="Horas", color="Tipo", markers=True,
                             color_discrete_sequence=[c["chart_colors"][3], c["chart_colors"][0]],
                             template=c["plotly_template"])
        fig_impacto.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_impacto, use_container_width=True)
        k1, k2, k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
        k2.metric("Custo Evitado", "R$ 185k", "vs. contratação")
        k3.metric("Projetos Entregues", "24", "+60% vs. anterior")

    st.markdown("</div></div>", unsafe_allow_html=True)

# ============================================================================
# DASHBOARD PAGE
# ============================================================================
def page_dashboard():
    st.markdown("""
    <div class="section-glass" style="min-height:80vh;padding-top:7rem;">
        <div class="container">
            <div class="section-header">
                <span class="label">Business Intelligence</span>
                <h2>Dashboard Interativo</h2>
                <p>Visão gerencial completa de projetos e performance</p>
            </div>
    """, unsafe_allow_html=True)
    
    c = get_colors()
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    projetos = [
        "Análise de Churn","Dashboard de Vendas","Otimização de Preços",
        "Segmentação de Clientes","Previsão de Demanda","Análise de Sentimento",
        "Modelo de Propensão","Automação de Relatórios","Análise de ROI",
        "Monitoramento de KPIs"
    ]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status_list = ["Concluído","Em Andamento","Planejado"]
    data_dash = []
    for i in range(150):
        data_dash.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status_list, p=[0.55,0.30,0.15]),
            "Valor": round(np.random.lognormal(9,0.8),2),
            "Horas": np.random.randint(20,400),
            "Satisfacao": np.random.randint(60,100),
            "Complexidade": np.random.choice(["Baixa","Média","Alta"], p=[0.2,0.5,0.3])
        })
    df_dash = pd.DataFrame(data_dash)
    df_dash["Data"] = pd.to_datetime(df_dash["Data"])
    df_dash["Mes"] = df_dash["Data"].dt.strftime("%Y-%m")

    col1, col2, col3 = st.columns(3)
    with col1:
        periodo = st.selectbox("Período", ["Últimos 6 meses","Últimos 12 meses","Últimos 24 meses"], index=1)
    with col2:
        regiao = st.selectbox("Região", ["Todas"] + sorted(df_dash["Região"].unique().tolist()), index=0)
    with col3:
        status_filtro = st.selectbox("Status", ["Todos"] + sorted(df_dash["Status"].unique().tolist()), index=0)

    df_filtrado = df_dash.copy()
    ultima_data = df_dash["Data"].max()
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

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Projetos", f"{len(df_filtrado):,}")
    col2.metric("Receita Total", f"R$ {df_filtrado['Valor'].sum()/1e6:.1f}M")
    col3.metric("Ticket Médio", f"R$ {df_filtrado['Valor'].mean():,.0f}".replace(",","."))
    col4.metric("Satisfação Média", f"{df_filtrado['Satisfacao'].mean():.1f}%")

    # Gráfico 1: Projetos por Mês
    df_mes = df_filtrado.groupby("Mes").size().reset_index(name="Quantidade").sort_values("Mes")
    fig1 = px.bar(df_mes, x="Mes", y="Quantidade", title="Projetos por Mês",
                 color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
    fig1.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40),
                      paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))

    # Gráfico 2: Receita por Região
    df_regiao = df_filtrado.groupby("Região")["Valor"].sum().reset_index()
    fig2 = px.pie(df_regiao, names="Região", values="Valor", title="Receita por Região",
                 hole=0.4, color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig2.update_layout(height=350, margin=dict(l=10,r=10,t=50,b=20),
                      paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))

    # Gráfico 3: Evolução da Receita
    df_receita = df_filtrado.groupby("Mes")["Valor"].sum().reset_index().sort_values("Mes")
    fig3 = px.line(df_receita, x="Mes", y="Valor", title="Evolução da Receita",
                  markers=True, color_discrete_sequence=[c["chart_colors"][1]],
                  template=c["plotly_template"])
    fig3.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40),
                      paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))

    # Gráfico 4: Esforço vs Retorno
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade",
                     size="Satisfacao", title="Esforço vs. Retorno",
                     color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig4.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40),
                      paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))

    # Gráfico 5: Status dos Projetos
    # ✅ CORREÇÃO: Compatível com pandas 2.x
    df_status = df_filtrado["Status"].value_counts().reset_index()
    df_status.columns = ["Status", "Quantidade"]
    fig5 = px.bar(df_status, x="Quantidade", y="Status", orientation="h",
                 title="Status dos Projetos", color="Status",
                 color_discrete_sequence=c["chart_colors"][:3],
                 template=c["plotly_template"])
    fig5.update_layout(height=300, margin=dict(l=20,r=20,t=50,b=20),
                      showlegend=False, paper_bgcolor="rgba(0,0,0,0)",
                      font=dict(color=c["text"]))

    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig3, use_container_width=True)
    col2.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

# ============================================================================
# MAIN
# ============================================================================
def main():
    load_css()
    render_navbar()
    
    page = st.session_state.current_page
    if page == "home":
        page_home()
    elif page == "analytics":
        page_analytics()
    elif page == "dashboard":
        page_dashboard()
    else:
        page_home()

if __name__ == "__main__":
    main()
