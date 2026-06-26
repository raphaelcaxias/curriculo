import streamlit as st

def init_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

def get_colors():
    dark = st.session_state.theme == "dark"
    if dark:
        return {
            "primary": "#3B82F6",
            "secondary": "#0EA5E9",
            "bg": "#0B0F1A",
            "text": "#F1F5F9",
            "text_muted": "#94A3B8",
            "card_bg": "rgba(255,255,255,0.04)",
            "border": "rgba(255,255,255,0.08)",
            "tag_bg": "rgba(59,130,246,0.15)",
            "tag_border": "rgba(59,130,246,0.25)",
            "primary_light": "rgba(59,130,246,0.2)",
            "navbar_bg": "rgba(11,15,26,0.75)",
            "navbar_border": "rgba(255,255,255,0.06)",
            "nav_hover": "rgba(255,255,255,0.06)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.08) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(59,130,246,0.15) 0%, transparent 60%)",
            "section_bg": "rgba(11,15,26,0.5)",
            "section_alt_bg": "rgba(255,255,255,0.02)",
            "shadow": "0 8px 32px rgba(0,0,0,0.4)",
            "shadow_hover": "0 12px 40px rgba(59,130,246,0.2)",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#60A5FA","#2563EB","#0284C7"]
        }
    else:
        return {
            "primary": "#1D4ED8",
            "secondary": "#0EA5E9",
            "bg": "#F8FAFC",
            "text": "#0F172A",
            "text_muted": "#475569",
            "card_bg": "rgba(255,255,255,0.7)",
            "border": "rgba(0,0,0,0.06)",
            "tag_bg": "#DBEAFE",
            "tag_border": "#93C5FD",
            "primary_light": "#DBEAFE",
            "navbar_bg": "rgba(248,250,252,0.8)",
            "navbar_border": "rgba(0,0,0,0.04)",
            "nav_hover": "rgba(0,0,0,0.04)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.04) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(29,78,216,0.08) 0%, transparent 60%)",
            "section_bg": "rgba(255,255,255,0.5)",
            "section_alt_bg": "rgba(0,0,0,0.01)",
            "shadow": "0 8px 32px rgba(0,0,0,0.06)",
            "shadow_hover": "0 12px 40px rgba(29,78,216,0.1)",
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8","#0EA5E9","#3B82F6","#2563EB","#0284C7"]
        }
