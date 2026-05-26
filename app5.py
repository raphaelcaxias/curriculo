# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Raphael Pires | Dados & BI", page_icon="📊", layout="wide")

# CSS
st.markdown("""
<style>
:root { --primary: #1e3a5f; --secondary: #2c5282; --accent: #3182ce; --bg: #f8fafc; }
.stApp { background: var(--bg); }
.hero { background: linear-gradient(135deg, var(--primary), var(--secondary)); padding: 2rem; border-radius: 12px; color: white; margin-bottom: 2rem; }
.metric-card { background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid var(--accent); text-align: center; }
.metric-value { font-size: 1.8rem; font-weight: 700; color: var(--primary); }
.metric-label { font-size: 0.85rem; color: #64748b; }
.section { background: white; padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
.proj-card { background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 3px solid var(--accent); }
.exp-item { margin: 1rem 0; padding-left: 1rem; border-left: 3px solid var(--secondary); }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x150/1e3a5f/ffffff?text=RP", width=12